---
title: Module identity
title_tag: Module identity | Package pulumi_openstack | Python SDK
linktitle: identity
notitle: true
---

<div class="section" id="identity">
<h1>identity<a class="headerlink" href="#identity" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.identity"></span><dl class="class">
<dt id="pulumi_openstack.identity.ApplicationCredential">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">ApplicationCredential</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_rules=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expires_at=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">unrestricted=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V3 Application Credential resource within OpenStack Keystone.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the application credential name and secret
will be stored in the raw state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data
in state</a>.</p>
<p><strong>Note:</strong> An Application Credential is created within the authenticated user
project scope and is not visible by an admin or other accounts.
The Application Credential visibility is similar to
<code class="docutils literal notranslate"><span class="pre">compute.Keypair</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the application credential.
Changing this creates a new application credential.</p></li>
<li><p><strong>expires_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expiration time of the application credential
in the RFC3339 timestamp format (e.g. <code class="docutils literal notranslate"><span class="pre">2019-03-09T12:58:49Z</span></code>). If omitted,
an application credential will never expire. Changing this creates a new
application credential.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name of the application credential. Changing this
creates a new application credential.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new application credential.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user’s roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.</p></li>
<li><p><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.</p></li>
<li><p><strong>unrestricted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>access_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_application_credential_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_application_credential_v3.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.identity.ApplicationCredential.access_rules">
<code class="sig-name descname">access_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.access_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ApplicationCredential.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the application credential.
Changing this creates a new application credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ApplicationCredential.expires_at">
<code class="sig-name descname">expires_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The expiration time of the application credential
in the RFC3339 timestamp format (e.g. <code class="docutils literal notranslate"><span class="pre">2019-03-09T12:58:49Z</span></code>). If omitted,
an application credential will never expire. Changing this creates a new
application credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ApplicationCredential.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name of the application credential. Changing this
creates a new application credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ApplicationCredential.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project the application credential was created
for and that authentication requests using this application credential will
be scoped to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ApplicationCredential.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new application credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ApplicationCredential.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user’s roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ApplicationCredential.secret">
<code class="sig-name descname">secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ApplicationCredential.unrestricted">
<code class="sig-name descname">unrestricted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.unrestricted" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.ApplicationCredential.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_rules=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expires_at=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">unrestricted=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationCredential resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of one or more access rules, which
this application credential allows to follow. The structure is described
below. Changing this creates a new application credential.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the application credential.
Changing this creates a new application credential.</p></li>
<li><p><strong>expires_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expiration time of the application credential
in the RFC3339 timestamp format (e.g. <code class="docutils literal notranslate"><span class="pre">2019-03-09T12:58:49Z</span></code>). If omitted,
an application credential will never expire. Changing this creates a new
application credential.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name of the application credential. Changing this
creates a new application credential.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project the application credential was created
for and that authentication requests using this application credential will
be scoped to.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new application credential.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of one or more role names, which this
application credential has to be associated with its project. If omitted,
all the current user’s roles within the scoped project will be inherited by
a new application credential. Changing this creates a new application
credential.</p></li>
<li><p><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret for the application credential. If omitted,
it will be generated by the server. Changing this creates a new application
credential.</p></li>
<li><p><strong>unrestricted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating whether the application
credential may be used for creation or destruction of other application
credentials or trusts. Changing this creates a new application credential.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>access_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_application_credential_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_application_credential_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.ApplicationCredential.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.ApplicationCredential.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.ApplicationCredential.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.AwaitableGetAuthScopeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">AwaitableGetAuthScopeResult</code><span class="sig-paren">(</span><em class="sig-param">domain_id=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_domain_id=None</em>, <em class="sig-param">project_domain_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">user_domain_id=None</em>, <em class="sig-param">user_domain_name=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">user_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.AwaitableGetAuthScopeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.AwaitableGetEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">AwaitableGetEndpointResult</code><span class="sig-paren">(</span><em class="sig-param">endpoint_region=None</em>, <em class="sig-param">interface=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.AwaitableGetEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">is_domain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.AwaitableGetRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">AwaitableGetRoleResult</code><span class="sig-paren">(</span><em class="sig-param">domain_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.AwaitableGetRoleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param">default_project_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_expires_at=None</em>, <em class="sig-param">protocol_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.EndpointV3">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">EndpointV3</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint_region=None</em>, <em class="sig-param">interface=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V3 Endpoint resource within OpenStack Keystone.</p>
<blockquote>
<div><p><strong>Note:</strong> This usually requires admin privileges.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint region. The <code class="docutils literal notranslate"><span class="pre">region</span></code> and
<code class="docutils literal notranslate"><span class="pre">endpoint_region</span></code> can be different.</p></li>
<li><p><strong>interface</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint interface. Valid values are <code class="docutils literal notranslate"><span class="pre">public</span></code>,
<code class="docutils literal notranslate"><span class="pre">internal</span></code> and <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">public</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint name.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint service ID.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint url.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_endpoint_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_endpoint_v3.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.identity.EndpointV3.endpoint_region">
<code class="sig-name descname">endpoint_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.endpoint_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint region. The <code class="docutils literal notranslate"><span class="pre">region</span></code> and
<code class="docutils literal notranslate"><span class="pre">endpoint_region</span></code> can be different.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.EndpointV3.interface">
<code class="sig-name descname">interface</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.interface" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint interface. Valid values are <code class="docutils literal notranslate"><span class="pre">public</span></code>,
<code class="docutils literal notranslate"><span class="pre">internal</span></code> and <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">public</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.EndpointV3.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.EndpointV3.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.EndpointV3.service_id">
<code class="sig-name descname">service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint service ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.EndpointV3.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The service name of the endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.EndpointV3.service_type">
<code class="sig-name descname">service_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The service type of the endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.EndpointV3.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint url.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.EndpointV3.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint_region=None</em>, <em class="sig-param">interface=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EndpointV3 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint region. The <code class="docutils literal notranslate"><span class="pre">region</span></code> and
<code class="docutils literal notranslate"><span class="pre">endpoint_region</span></code> can be different.</p></li>
<li><p><strong>interface</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint interface. Valid values are <code class="docutils literal notranslate"><span class="pre">public</span></code>,
<code class="docutils literal notranslate"><span class="pre">internal</span></code> and <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">public</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint name.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint service ID.</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service name of the endpoint.</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service type of the endpoint.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint url.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_endpoint_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_endpoint_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.EndpointV3.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.EndpointV3.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.EndpointV3.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.GetAuthScopeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">GetAuthScopeResult</code><span class="sig-paren">(</span><em class="sig-param">domain_id=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_domain_id=None</em>, <em class="sig-param">project_domain_name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">user_domain_id=None</em>, <em class="sig-param">user_domain_name=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">user_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuthScope.</p>
<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain ID of the scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name of the scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.project_domain_id">
<code class="sig-name descname">project_domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.project_domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain ID of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.project_domain_name">
<code class="sig-name descname">project_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.project_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID of the scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.project_name">
<code class="sig-name descname">project_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.project_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The project name of the scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of roles in the current scope. See reference below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.user_domain_id">
<code class="sig-name descname">user_domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.user_domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain ID of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.user_domain_name">
<code class="sig-name descname">user_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.user_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.user_id">
<code class="sig-name descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user ID the of the scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.user_name">
<code class="sig-name descname">user_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetAuthScopeResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetAuthScopeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.GetEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">GetEndpointResult</code><span class="sig-paren">(</span><em class="sig-param">endpoint_region=None</em>, <em class="sig-param">interface=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.GetEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEndpoint.</p>
<dl class="attribute">
<dt id="pulumi_openstack.identity.GetEndpointResult.endpoint_region">
<code class="sig-name descname">endpoint_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetEndpointResult.endpoint_region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetEndpointResult.interface">
<code class="sig-name descname">interface</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetEndpointResult.interface" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetEndpointResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetEndpointResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetEndpointResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetEndpointResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetEndpointResult.service_id">
<code class="sig-name descname">service_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetEndpointResult.service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetEndpointResult.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetEndpointResult.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetEndpointResult.service_type">
<code class="sig-name descname">service_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetEndpointResult.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetEndpointResult.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetEndpointResult.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetEndpointResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetEndpointResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_openstack.identity.GetGroupResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetGroupResult.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetGroupResult.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetGroupResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetGroupResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetGroupResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">is_domain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="attribute">
<dt id="pulumi_openstack.identity.GetProjectResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetProjectResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetProjectResult.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetProjectResult.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetProjectResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetProjectResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetProjectResult.is_domain">
<code class="sig-name descname">is_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetProjectResult.is_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetProjectResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetProjectResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetProjectResult.parent_id">
<code class="sig-name descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetProjectResult.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetProjectResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetProjectResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region the project is located in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetProjectResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.GetRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">GetRoleResult</code><span class="sig-paren">(</span><em class="sig-param">domain_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.GetRoleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRole.</p>
<dl class="attribute">
<dt id="pulumi_openstack.identity.GetRoleResult.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetRoleResult.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetRoleResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetRoleResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetRoleResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetRoleResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetRoleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetRoleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="attribute">
<dt id="pulumi_openstack.identity.GetServiceResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetServiceResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The service description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetServiceResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetServiceResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetServiceResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetServiceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetServiceResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetServiceResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetServiceResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetServiceResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param">default_project_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_expires_at=None</em>, <em class="sig-param">protocol_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.default_project_id">
<code class="sig-name descname">default_project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.default_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.idp_id">
<code class="sig-name descname">idp_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.idp_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.password_expires_at">
<code class="sig-name descname">password_expires_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.password_expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.protocol_id">
<code class="sig-name descname">protocol_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.protocol_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region the user is located in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.GetUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.identity.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">is_domain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V3 Project resource within OpenStack Keystone.</p>
<p>Note: You <em>must</em> have admin privileges in your OpenStack cloud to use
this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the project.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain this project belongs to.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the project is enabled or disabled. Valid
values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>is_domain</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this project is a domain. Valid values
are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent of this project.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new User.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_project_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_project_v3.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.identity.Project.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.Project.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.Project.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.Project.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain this project belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.Project.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.Project.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the project is enabled or disabled. Valid
values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.Project.is_domain">
<code class="sig-name descname">is_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.Project.is_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this project is a domain. Valid values
are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.Project.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.Project.parent_id">
<code class="sig-name descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.Project.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The parent of this project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.Project.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.Project.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new User.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">is_domain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the project.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain this project belongs to.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the project is enabled or disabled. Valid
values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>is_domain</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this project is a domain. Valid values
are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent of this project.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new User.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_project_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_project_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V3 Role resource within OpenStack Keystone.</p>
<p>Note: You <em>must</em> have admin privileges in your OpenStack cloud to use
this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain the role belongs to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new Role.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_role_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_role_v3.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.identity.Role.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.Role.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain the role belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.Role.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.Role.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.Role.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new Role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain the role belongs to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new Role.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_role_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_role_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.RoleAssignment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">RoleAssignment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.RoleAssignment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V3 Role assignment within OpenStack Keystone.</p>
<p>Note: You <em>must</em> have admin privileges in your OpenStack cloud to use
this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to assign the role in.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group to assign the role to.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project to assign the role in.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role to assign.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to assign the role to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_role_assignment_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_role_assignment_v3.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.identity.RoleAssignment.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.RoleAssignment.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain to assign the role in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.RoleAssignment.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.RoleAssignment.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The group to assign the role to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.RoleAssignment.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.RoleAssignment.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project to assign the role in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.RoleAssignment.role_id">
<code class="sig-name descname">role_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.RoleAssignment.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The role to assign.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.RoleAssignment.user_id">
<code class="sig-name descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.RoleAssignment.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user to assign the role to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.RoleAssignment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.RoleAssignment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RoleAssignment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to assign the role in.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group to assign the role to.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project to assign the role in.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role to assign.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to assign the role to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_role_assignment_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_role_assignment_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.RoleAssignment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.RoleAssignment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.RoleAssignment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.RoleAssignment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.ServiceV3">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">ServiceV3</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.ServiceV3" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V3 Service resource within OpenStack Keystone.</p>
<blockquote>
<div><p><strong>Note:</strong> This usually requires admin privileges.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The service status. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service name.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service type.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_service_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_service_v3.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.identity.ServiceV3.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ServiceV3.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The service description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ServiceV3.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ServiceV3.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>The service status. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ServiceV3.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ServiceV3.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The service name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ServiceV3.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ServiceV3.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.ServiceV3.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.ServiceV3.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The service type.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.ServiceV3.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.ServiceV3.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceV3 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The service status. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service name.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service type.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_service_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_service_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.ServiceV3.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.ServiceV3.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.ServiceV3.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.ServiceV3.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_project_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extra=None</em>, <em class="sig-param">ignore_change_password_upon_first_use=None</em>, <em class="sig-param">ignore_lockout_failure_attempts=None</em>, <em class="sig-param">ignore_password_expiry=None</em>, <em class="sig-param">multi_factor_auth_enabled=None</em>, <em class="sig-param">multi_factor_auth_rules=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V3 User resource within OpenStack Keystone.</p>
<p>Note: You <em>must</em> have admin privileges in your OpenStack cloud to use
this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default project this user belongs to.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the user.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain this user belongs to.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is enabled or disabled. Valid
values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>extra</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Free-form key/value pairs of extra information.</p></li>
<li><p><strong>ignore_change_password_upon_first_use</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User will not have to
change their password upon first use. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ignore_lockout_failure_attempts</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User will not have a failure
lockout placed on their account. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ignore_password_expiry</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User’s password will not expire.
Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>multi_factor_auth_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable multi-factor
authentication. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>multi_factor_auth_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A multi-factor authentication rule.
The structure is documented below. Please see the
<a class="reference external" href="https://docs.openstack.org/releasenotes/keystone/ocata.html">Ocata release notes</a>
for more information on how to use mulit-factor rules.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the user.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new User.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>multi_factor_auth_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_user_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_user_v3.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.identity.User.default_project_id">
<code class="sig-name descname">default_project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.default_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The default project this user belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain this user belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is enabled or disabled. Valid
values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.extra">
<code class="sig-name descname">extra</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.extra" title="Permalink to this definition">¶</a></dt>
<dd><p>Free-form key/value pairs of extra information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.ignore_change_password_upon_first_use">
<code class="sig-name descname">ignore_change_password_upon_first_use</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.ignore_change_password_upon_first_use" title="Permalink to this definition">¶</a></dt>
<dd><p>User will not have to
change their password upon first use. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.ignore_lockout_failure_attempts">
<code class="sig-name descname">ignore_lockout_failure_attempts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.ignore_lockout_failure_attempts" title="Permalink to this definition">¶</a></dt>
<dd><p>User will not have a failure
lockout placed on their account. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.ignore_password_expiry">
<code class="sig-name descname">ignore_password_expiry</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.ignore_password_expiry" title="Permalink to this definition">¶</a></dt>
<dd><p>User’s password will not expire.
Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.multi_factor_auth_enabled">
<code class="sig-name descname">multi_factor_auth_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.multi_factor_auth_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable multi-factor
authentication. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.multi_factor_auth_rules">
<code class="sig-name descname">multi_factor_auth_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.multi_factor_auth_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A multi-factor authentication rule.
The structure is documented below. Please see the
<a class="reference external" href="https://docs.openstack.org/releasenotes/keystone/ocata.html">Ocata release notes</a>
for more information on how to use mulit-factor rules.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.identity.User.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.identity.User.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new User.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_project_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extra=None</em>, <em class="sig-param">ignore_change_password_upon_first_use=None</em>, <em class="sig-param">ignore_lockout_failure_attempts=None</em>, <em class="sig-param">ignore_password_expiry=None</em>, <em class="sig-param">multi_factor_auth_enabled=None</em>, <em class="sig-param">multi_factor_auth_rules=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default project this user belongs to.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the user.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain this user belongs to.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is enabled or disabled. Valid
values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>extra</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Free-form key/value pairs of extra information.</p></li>
<li><p><strong>ignore_change_password_upon_first_use</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User will not have to
change their password upon first use. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ignore_lockout_failure_attempts</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User will not have a failure
lockout placed on their account. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ignore_password_expiry</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – User’s password will not expire.
Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>multi_factor_auth_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable multi-factor
authentication. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>multi_factor_auth_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A multi-factor authentication rule.
The structure is documented below. Please see the
<a class="reference external" href="https://docs.openstack.org/releasenotes/keystone/ocata.html">Ocata release notes</a>
for more information on how to use mulit-factor rules.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the user.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new User.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>multi_factor_auth_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_user_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_user_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.identity.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.identity.get_auth_scope">
<code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">get_auth_scope</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.get_auth_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get authentication information about the current
auth scope in use. This can be used as self-discovery or introspection of
the username or project name currently in use.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the scope. This is an arbitrary name which is
only used as a unique identifier so an actual token isn’t used as the ID.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V3 Identity client.
A Identity client is needed to retrieve tokens IDs. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_auth_scope_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_auth_scope_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.identity.get_endpoint">
<code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">get_endpoint</code><span class="sig-paren">(</span><em class="sig-param">endpoint_region=None</em>, <em class="sig-param">interface=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">service_id=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.get_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an OpenStack endpoint.</p>
<blockquote>
<div><p><strong>Note:</strong> This usually requires admin privileges.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>endpoint_region</strong> (<em>str</em>) – The region the endpoint is assigned to. The
<code class="docutils literal notranslate"><span class="pre">region</span></code> and <code class="docutils literal notranslate"><span class="pre">endpoint_region</span></code> can be different.</p></li>
<li><p><strong>interface</strong> (<em>str</em>) – The endpoint interface. Valid values are <code class="docutils literal notranslate"><span class="pre">public</span></code>,
<code class="docutils literal notranslate"><span class="pre">internal</span></code>, and <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">public</span></code></p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the endpoint.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>service_id</strong> (<em>str</em>) – The service id this endpoint belongs to.</p></li>
<li><p><strong>service_name</strong> (<em>str</em>) – The service name of the endpoint.</p></li>
<li><p><strong>service_type</strong> (<em>str</em>) – The service type of the endpoint.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_endpoint_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_endpoint_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.identity.get_group">
<code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param">domain_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an OpenStack group.</p>
<p>Note: This usually requires admin privileges.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain_id</strong> (<em>str</em>) – The domain the group belongs to.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the group.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_group_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_group_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.identity.get_project">
<code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param">domain_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">is_domain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an OpenStack project.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain_id</strong> (<em>str</em>) – The domain this project belongs to.</p></li>
<li><p><strong>enabled</strong> (<em>bool</em>) – Whether the project is enabled or disabled. Valid
values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>is_domain</strong> (<em>bool</em>) – Whether this project is a domain. Valid values
are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the project.</p></li>
<li><p><strong>parent_id</strong> (<em>str</em>) – The parent of this project.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_project_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_project_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.identity.get_role">
<code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">get_role</code><span class="sig-paren">(</span><em class="sig-param">domain_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.get_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an OpenStack role.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain_id</strong> (<em>str</em>) – The domain the role belongs to.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the role.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_role_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_role_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.identity.get_service">
<code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an OpenStack service.</p>
<blockquote>
<div><p><strong>Note:</strong> This usually requires admin privileges.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>enabled</strong> (<em>bool</em>) – The service status.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The service name.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V3 Keystone client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – The service type.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_service_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_service_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.identity.get_user">
<code class="sig-prename descclassname">pulumi_openstack.identity.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param">domain_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">idp_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_expires_at=None</em>, <em class="sig-param">protocol_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.identity.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an OpenStack user.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain_id</strong> (<em>str</em>) – The domain this user belongs to.</p></li>
<li><p><strong>enabled</strong> (<em>bool</em>) – Whether the user is enabled or disabled. Valid
values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>idp_id</strong> (<em>str</em>) – The identity provider ID of the user.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the user.</p></li>
<li><p><strong>password_expires_at</strong> (<em>str</em>) – Query for expired passwords. See the <a class="reference external" href="https://developer.openstack.org/api-ref/identity/v3/#list-users">OpenStack API docs</a> for more information on the query format.</p></li>
<li><p><strong>protocol_id</strong> (<em>str</em>) – The protocol ID of the user.</p></li>
<li><p><strong>unique_id</strong> (<em>str</em>) – The unique ID of the user.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_user_v3.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_user_v3.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
