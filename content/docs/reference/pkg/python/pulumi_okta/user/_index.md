---
title: Module user
title_tag: Module user | Package pulumi_okta | Python SDK
linktitle: user
notitle: true
---

<div class="section" id="user">
<h1>user<a class="headerlink" href="#user" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.user"></span><dl class="class">
<dt id="pulumi_okta.user.AwaitableGetUserProfileMappingSourceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">AwaitableGetUserProfileMappingSourceResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.AwaitableGetUserProfileMappingSourceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.user.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param">admin_roles=None</em>, <em class="sig-param">city=None</em>, <em class="sig-param">cost_center=None</em>, <em class="sig-param">country_code=None</em>, <em class="sig-param">custom_profile_attributes=None</em>, <em class="sig-param">department=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">division=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">employee_number=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">group_memberships=None</em>, <em class="sig-param">honorific_prefix=None</em>, <em class="sig-param">honorific_suffix=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">locale=None</em>, <em class="sig-param">login=None</em>, <em class="sig-param">manager=None</em>, <em class="sig-param">manager_id=None</em>, <em class="sig-param">middle_name=None</em>, <em class="sig-param">mobile_phone=None</em>, <em class="sig-param">nick_name=None</em>, <em class="sig-param">organization=None</em>, <em class="sig-param">postal_address=None</em>, <em class="sig-param">preferred_language=None</em>, <em class="sig-param">primary_phone=None</em>, <em class="sig-param">profile_url=None</em>, <em class="sig-param">searches=None</em>, <em class="sig-param">second_email=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">street_address=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">user_type=None</em>, <em class="sig-param">zip_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.user.AwaitableGetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">AwaitableGetUsersResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">searches=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.AwaitableGetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.user.BaseSchema">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">BaseSchema</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">index=None</em>, <em class="sig-param">master=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">required=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.BaseSchema" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a User Base Schema property.</p>
<p>This resource allows you to configure a base user schema property.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property name.</p></li>
<li><p><strong>master</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p></li>
<li><p><strong>required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the property is required for this application’s users.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property display name.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.user.BaseSchema.index">
<code class="sig-name descname">index</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.BaseSchema.index" title="Permalink to this definition">¶</a></dt>
<dd><p>The property name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.BaseSchema.master">
<code class="sig-name descname">master</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.BaseSchema.master" title="Permalink to this definition">¶</a></dt>
<dd><p>Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.BaseSchema.permissions">
<code class="sig-name descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.BaseSchema.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.BaseSchema.required">
<code class="sig-name descname">required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.BaseSchema.required" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the property is required for this application’s users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.BaseSchema.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.BaseSchema.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The property display name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.BaseSchema.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.BaseSchema.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.user.BaseSchema.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">index=None</em>, <em class="sig-param">master=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">required=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.BaseSchema.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BaseSchema resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property name.</p></li>
<li><p><strong>master</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p></li>
<li><p><strong>required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the property is required for this application’s users.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property display name.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.user.BaseSchema.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.BaseSchema.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.user.BaseSchema.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.BaseSchema.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.user.GetUserProfileMappingSourceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">GetUserProfileMappingSourceResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.GetUserProfileMappingSourceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUserProfileMappingSource.</p>
<dl class="attribute">
<dt id="pulumi_okta.user.GetUserProfileMappingSourceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserProfileMappingSourceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserProfileMappingSourceResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserProfileMappingSourceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserProfileMappingSourceResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserProfileMappingSourceResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>type of source.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.user.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param">admin_roles=None</em>, <em class="sig-param">city=None</em>, <em class="sig-param">cost_center=None</em>, <em class="sig-param">country_code=None</em>, <em class="sig-param">custom_profile_attributes=None</em>, <em class="sig-param">department=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">division=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">employee_number=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">group_memberships=None</em>, <em class="sig-param">honorific_prefix=None</em>, <em class="sig-param">honorific_suffix=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">locale=None</em>, <em class="sig-param">login=None</em>, <em class="sig-param">manager=None</em>, <em class="sig-param">manager_id=None</em>, <em class="sig-param">middle_name=None</em>, <em class="sig-param">mobile_phone=None</em>, <em class="sig-param">nick_name=None</em>, <em class="sig-param">organization=None</em>, <em class="sig-param">postal_address=None</em>, <em class="sig-param">preferred_language=None</em>, <em class="sig-param">primary_phone=None</em>, <em class="sig-param">profile_url=None</em>, <em class="sig-param">searches=None</em>, <em class="sig-param">second_email=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">street_address=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">user_type=None</em>, <em class="sig-param">zip_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.admin_roles">
<code class="sig-name descname">admin_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.admin_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>Administrator roles assigned to user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.city">
<code class="sig-name descname">city</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.city" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.cost_center">
<code class="sig-name descname">cost_center</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.cost_center" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.country_code">
<code class="sig-name descname">country_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.country_code" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.custom_profile_attributes">
<code class="sig-name descname">custom_profile_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.custom_profile_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>raw JSON containing all custom profile attributes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.department">
<code class="sig-name descname">department</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.department" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.division">
<code class="sig-name descname">division</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.division" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.employee_number">
<code class="sig-name descname">employee_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.employee_number" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.first_name">
<code class="sig-name descname">first_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.group_memberships">
<code class="sig-name descname">group_memberships</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.group_memberships" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.honorific_prefix">
<code class="sig-name descname">honorific_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.honorific_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.honorific_suffix">
<code class="sig-name descname">honorific_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.honorific_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.last_name">
<code class="sig-name descname">last_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.locale">
<code class="sig-name descname">locale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.locale" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.login">
<code class="sig-name descname">login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.login" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.manager">
<code class="sig-name descname">manager</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.manager" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.manager_id">
<code class="sig-name descname">manager_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.manager_id" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.middle_name">
<code class="sig-name descname">middle_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.middle_name" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.mobile_phone">
<code class="sig-name descname">mobile_phone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.mobile_phone" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.nick_name">
<code class="sig-name descname">nick_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.nick_name" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.organization">
<code class="sig-name descname">organization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.postal_address">
<code class="sig-name descname">postal_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.postal_address" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.preferred_language">
<code class="sig-name descname">preferred_language</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.preferred_language" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.primary_phone">
<code class="sig-name descname">primary_phone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.primary_phone" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.profile_url">
<code class="sig-name descname">profile_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.profile_url" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.second_email">
<code class="sig-name descname">second_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.second_email" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.street_address">
<code class="sig-name descname">street_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.street_address" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.timezone">
<code class="sig-name descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.title" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.user_type">
<code class="sig-name descname">user_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.user_type" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUserResult.zip_code">
<code class="sig-name descname">zip_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUserResult.zip_code" title="Permalink to this definition">¶</a></dt>
<dd><p>user profile property.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.user.GetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">GetUsersResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">searches=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.GetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUsers.</p>
<dl class="attribute">
<dt id="pulumi_okta.user.GetUsersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.GetUsersResult.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.GetUsersResult.users" title="Permalink to this definition">¶</a></dt>
<dd><p>collection of users retrieved from Okta with the following properties.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.user.Schema">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">Schema</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">array_enums=None</em>, <em class="sig-param">array_one_ofs=None</em>, <em class="sig-param">array_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enums=None</em>, <em class="sig-param">external_name=None</em>, <em class="sig-param">index=None</em>, <em class="sig-param">master=None</em>, <em class="sig-param">max_length=None</em>, <em class="sig-param">min_length=None</em>, <em class="sig-param">one_ofs=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">required=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.Schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a User Schema property.</p>
<p>This resource allows you to create and configure a custom user schema property.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>array_enums</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values that an array property’s items can be set to.</p></li>
<li><p><strong>array_one_ofs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Display name and value an enum array can be set to.</p></li>
<li><p><strong>array_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the array elements if <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the user schema property.</p></li>
<li><p><strong>enums</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values a primitive property can be set to. See <code class="docutils literal notranslate"><span class="pre">array_enum</span></code> for arrays.</p></li>
<li><p><strong>external_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – External name of the user schema property.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property name.</p></li>
<li><p><strong>master</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p></li>
<li><p><strong>max_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p></li>
<li><p><strong>min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p></li>
<li><p><strong>one_ofs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of maps containing a mapping for display name to enum value.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p></li>
<li><p><strong>required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the property is required for this application’s users.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – determines whether an app user attribute can be set at the Individual or Group Level.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – display name for the enum value.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>array_one_ofs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - display name for the enum value.</p></li>
</ul>
<p>The <strong>one_ofs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - display name for the enum value.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_okta.user.Schema.array_enums">
<code class="sig-name descname">array_enums</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.array_enums" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of values that an array property’s items can be set to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.array_one_ofs">
<code class="sig-name descname">array_one_ofs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.array_one_ofs" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name and value an enum array can be set to.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - display name for the enum value.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.array_type">
<code class="sig-name descname">array_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.array_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the array elements if <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the user schema property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.enums">
<code class="sig-name descname">enums</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.enums" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of values a primitive property can be set to. See <code class="docutils literal notranslate"><span class="pre">array_enum</span></code> for arrays.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.external_name">
<code class="sig-name descname">external_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.external_name" title="Permalink to this definition">¶</a></dt>
<dd><p>External name of the user schema property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.index">
<code class="sig-name descname">index</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.index" title="Permalink to this definition">¶</a></dt>
<dd><p>The property name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.master">
<code class="sig-name descname">master</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.master" title="Permalink to this definition">¶</a></dt>
<dd><p>Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.max_length">
<code class="sig-name descname">max_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.max_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.min_length">
<code class="sig-name descname">min_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.min_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.one_ofs">
<code class="sig-name descname">one_ofs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.one_ofs" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of maps containing a mapping for display name to enum value.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - display name for the enum value.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.permissions">
<code class="sig-name descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.required">
<code class="sig-name descname">required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.required" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the property is required for this application’s users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>determines whether an app user attribute can be set at the Individual or Group Level.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.title" title="Permalink to this definition">¶</a></dt>
<dd><p>display name for the enum value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.Schema.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.Schema.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.user.Schema.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">array_enums=None</em>, <em class="sig-param">array_one_ofs=None</em>, <em class="sig-param">array_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enums=None</em>, <em class="sig-param">external_name=None</em>, <em class="sig-param">index=None</em>, <em class="sig-param">master=None</em>, <em class="sig-param">max_length=None</em>, <em class="sig-param">min_length=None</em>, <em class="sig-param">one_ofs=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">required=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.Schema.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Schema resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>array_enums</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values that an array property’s items can be set to.</p></li>
<li><p><strong>array_one_ofs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Display name and value an enum array can be set to.</p></li>
<li><p><strong>array_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the array elements if <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the user schema property.</p></li>
<li><p><strong>enums</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of values a primitive property can be set to. See <code class="docutils literal notranslate"><span class="pre">array_enum</span></code> for arrays.</p></li>
<li><p><strong>external_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – External name of the user schema property.</p></li>
<li><p><strong>index</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property name.</p></li>
<li><p><strong>master</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master priority for the user schema property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;PROFILE_MASTER&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;OKTA&quot;</span></code>.</p></li>
<li><p><strong>max_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p></li>
<li><p><strong>min_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum length of the user property value. Only applies to type <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>.</p></li>
<li><p><strong>one_ofs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of maps containing a mapping for display name to enum value.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access control permissions for the property. It can be set to <code class="docutils literal notranslate"><span class="pre">&quot;READ_WRITE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HIDE&quot;</span></code>.</p></li>
<li><p><strong>required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the property is required for this application’s users.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – determines whether an app user attribute can be set at the Individual or Group Level.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – display name for the enum value.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the schema property. It can be <code class="docutils literal notranslate"><span class="pre">&quot;string&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;boolean&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;number&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;integer&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;array&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;object&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>array_one_ofs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - display name for the enum value.</p></li>
</ul>
<p>The <strong>one_ofs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">const</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - value mapping to member of <code class="docutils literal notranslate"><span class="pre">enum</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - display name for the enum value.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.user.Schema.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.Schema.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.user.Schema.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.Schema.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.user.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_roles=None</em>, <em class="sig-param">city=None</em>, <em class="sig-param">cost_center=None</em>, <em class="sig-param">country_code=None</em>, <em class="sig-param">custom_profile_attributes=None</em>, <em class="sig-param">department=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">division=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">employee_number=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">group_memberships=None</em>, <em class="sig-param">honorific_prefix=None</em>, <em class="sig-param">honorific_suffix=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">locale=None</em>, <em class="sig-param">login=None</em>, <em class="sig-param">manager=None</em>, <em class="sig-param">manager_id=None</em>, <em class="sig-param">middle_name=None</em>, <em class="sig-param">mobile_phone=None</em>, <em class="sig-param">nick_name=None</em>, <em class="sig-param">organization=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">postal_address=None</em>, <em class="sig-param">preferred_language=None</em>, <em class="sig-param">primary_phone=None</em>, <em class="sig-param">profile_url=None</em>, <em class="sig-param">recovery_answer=None</em>, <em class="sig-param">recovery_question=None</em>, <em class="sig-param">second_email=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">street_address=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">user_type=None</em>, <em class="sig-param">zip_code=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Okta User.</p>
<p>This resource allows you to create and configure an Okta User.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Administrator roles assigned to User.</p></li>
<li><p><strong>city</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>cost_center</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>country_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>custom_profile_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – raw JSON containing all custom profile attributes.</p></li>
<li><p><strong>department</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>division</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>employee_number</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>first_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User’s First Name, required by default.</p></li>
<li><p><strong>group_memberships</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>honorific_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>honorific_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>last_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User’s Last Name, required by default.</p></li>
<li><p><strong>locale</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>manager</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>manager_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>middle_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>mobile_phone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>nick_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User password.</p></li>
<li><p><strong>postal_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>preferred_language</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>primary_phone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>profile_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>recovery_answer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User password recovery answer.</p></li>
<li><p><strong>recovery_question</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User password recovery question.</p></li>
<li><p><strong>second_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>street_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>user_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>zip_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.user.User.admin_roles">
<code class="sig-name descname">admin_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.admin_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>Administrator roles assigned to User.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.city">
<code class="sig-name descname">city</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.city" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.cost_center">
<code class="sig-name descname">cost_center</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.cost_center" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.country_code">
<code class="sig-name descname">country_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.country_code" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.custom_profile_attributes">
<code class="sig-name descname">custom_profile_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.custom_profile_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>raw JSON containing all custom profile attributes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.department">
<code class="sig-name descname">department</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.department" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.division">
<code class="sig-name descname">division</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.division" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.employee_number">
<code class="sig-name descname">employee_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.employee_number" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.first_name">
<code class="sig-name descname">first_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User’s First Name, required by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.group_memberships">
<code class="sig-name descname">group_memberships</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.group_memberships" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.honorific_prefix">
<code class="sig-name descname">honorific_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.honorific_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.honorific_suffix">
<code class="sig-name descname">honorific_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.honorific_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.last_name">
<code class="sig-name descname">last_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User’s Last Name, required by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.locale">
<code class="sig-name descname">locale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.locale" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.login">
<code class="sig-name descname">login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.login" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.manager">
<code class="sig-name descname">manager</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.manager" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.manager_id">
<code class="sig-name descname">manager_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.manager_id" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.middle_name">
<code class="sig-name descname">middle_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.middle_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.mobile_phone">
<code class="sig-name descname">mobile_phone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.mobile_phone" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.nick_name">
<code class="sig-name descname">nick_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.nick_name" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.organization">
<code class="sig-name descname">organization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>User password.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.postal_address">
<code class="sig-name descname">postal_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.postal_address" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.preferred_language">
<code class="sig-name descname">preferred_language</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.preferred_language" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.primary_phone">
<code class="sig-name descname">primary_phone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.primary_phone" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.profile_url">
<code class="sig-name descname">profile_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.profile_url" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.raw_status">
<code class="sig-name descname">raw_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.raw_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The raw status of the User in Okta - (status is mapped)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.recovery_answer">
<code class="sig-name descname">recovery_answer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.recovery_answer" title="Permalink to this definition">¶</a></dt>
<dd><p>User password recovery answer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.recovery_question">
<code class="sig-name descname">recovery_question</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.recovery_question" title="Permalink to this definition">¶</a></dt>
<dd><p>User password recovery question.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.second_email">
<code class="sig-name descname">second_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.second_email" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.state" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.status" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.street_address">
<code class="sig-name descname">street_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.street_address" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.timezone">
<code class="sig-name descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.title" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.user_type">
<code class="sig-name descname">user_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.user_type" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.user.User.zip_code">
<code class="sig-name descname">zip_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.user.User.zip_code" title="Permalink to this definition">¶</a></dt>
<dd><p>User profile property.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.user.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_roles=None</em>, <em class="sig-param">city=None</em>, <em class="sig-param">cost_center=None</em>, <em class="sig-param">country_code=None</em>, <em class="sig-param">custom_profile_attributes=None</em>, <em class="sig-param">department=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">division=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">employee_number=None</em>, <em class="sig-param">first_name=None</em>, <em class="sig-param">group_memberships=None</em>, <em class="sig-param">honorific_prefix=None</em>, <em class="sig-param">honorific_suffix=None</em>, <em class="sig-param">last_name=None</em>, <em class="sig-param">locale=None</em>, <em class="sig-param">login=None</em>, <em class="sig-param">manager=None</em>, <em class="sig-param">manager_id=None</em>, <em class="sig-param">middle_name=None</em>, <em class="sig-param">mobile_phone=None</em>, <em class="sig-param">nick_name=None</em>, <em class="sig-param">organization=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">postal_address=None</em>, <em class="sig-param">preferred_language=None</em>, <em class="sig-param">primary_phone=None</em>, <em class="sig-param">profile_url=None</em>, <em class="sig-param">raw_status=None</em>, <em class="sig-param">recovery_answer=None</em>, <em class="sig-param">recovery_question=None</em>, <em class="sig-param">second_email=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">street_address=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">user_type=None</em>, <em class="sig-param">zip_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Administrator roles assigned to User.</p></li>
<li><p><strong>city</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>cost_center</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>country_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>custom_profile_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – raw JSON containing all custom profile attributes.</p></li>
<li><p><strong>department</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>division</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>employee_number</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>first_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User’s First Name, required by default.</p></li>
<li><p><strong>group_memberships</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>honorific_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>honorific_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>last_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User’s Last Name, required by default.</p></li>
<li><p><strong>locale</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>manager</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>manager_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>middle_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>mobile_phone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>nick_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User password.</p></li>
<li><p><strong>postal_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>preferred_language</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>primary_phone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>profile_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>raw_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The raw status of the User in Okta - (status is mapped)</p></li>
<li><p><strong>recovery_answer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User password recovery answer.</p></li>
<li><p><strong>recovery_question</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User password recovery question.</p></li>
<li><p><strong>second_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>street_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>user_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
<li><p><strong>zip_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User profile property.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.user.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.user.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.user.get_user">
<code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param">searches=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve a users from Okta.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>searches</strong> (<em>list</em>) – Map of search criteria. It supports the following properties.</p>
</dd>
</dl>
<p>The <strong>searches</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comparison to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of property to search against.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value to compare with.</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_okta.user.get_user_profile_mapping_source">
<code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">get_user_profile_mapping_source</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.get_user_profile_mapping_source" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve the base user Profile Mapping source or target from Okta.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_okta.user.get_users">
<code class="sig-prename descclassname">pulumi_okta.user.</code><code class="sig-name descname">get_users</code><span class="sig-paren">(</span><em class="sig-param">searches=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.user.get_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve a list of users from Okta.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>searches</strong> (<em>list</em>) – Map of search criteria to use to find users. It supports the following properties.</p></li>
<li><p><strong>users</strong> (<em>list</em>) – collection of users retrieved from Okta with the following properties.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>searches</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comparison to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of property to search against.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value to compare with.</p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_roles</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Administrator roles assigned to user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">city</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cost_center</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country_code</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">custom_profile_attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - raw JSON containing all custom profile attributes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">department</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">division</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">employee_number</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">first_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_memberships</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">honorific_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">honorific_suffix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locale</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">login</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manager</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manager_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">middle_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobile_phone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nick_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organization</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postal_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preferred_language</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary_phone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">profile_url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">second_email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">street_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zip_code</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - user profile property.</p></li>
</ul>
</dd></dl>

</div>
