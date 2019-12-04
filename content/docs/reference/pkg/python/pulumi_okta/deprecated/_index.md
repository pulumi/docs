---
title: Module deprecated
linktitle: deprecated
notitle: true
---

<div class="section" id="deprecated">
<h1>deprecated<a class="headerlink" href="#deprecated" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.deprecated"></span><dl class="class">
<dt id="pulumi_okta.deprecated.AuthLoginApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">AuthLoginApp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">credentials_scheme=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">reveal_password=None</em>, <em class="sig-param">shared_password=None</em>, <em class="sig-param">shared_username=None</em>, <em class="sig-param">sign_on_redirect_url=None</em>, <em class="sig-param">sign_on_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AuthLoginApp resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="method">
<dt id="pulumi_okta.deprecated.AuthLoginApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">credentials_scheme=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">reveal_password=None</em>, <em class="sig-param">shared_password=None</em>, <em class="sig-param">shared_username=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">sign_on_redirect_url=None</em>, <em class="sig-param">sign_on_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthLoginApp resource’s state with the given name, id, and optional extra
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
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.AuthLoginApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.AuthLoginApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.AuthLoginApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.AwaitableGetDefaultPoliciesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">AwaitableGetDefaultPoliciesResult</code><span class="sig-paren">(</span><em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.AwaitableGetDefaultPoliciesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.deprecated.BookmarkApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">BookmarkApp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">request_integration=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a BookmarkApp resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="method">
<dt id="pulumi_okta.deprecated.BookmarkApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">request_integration=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BookmarkApp resource’s state with the given name, id, and optional extra
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
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.BookmarkApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.BookmarkApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.BookmarkApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.GetDefaultPoliciesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">GetDefaultPoliciesResult</code><span class="sig-paren">(</span><em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.GetDefaultPoliciesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefaultPolicies.</p>
<dl class="attribute">
<dt id="pulumi_okta.deprecated.GetDefaultPoliciesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.deprecated.GetDefaultPoliciesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.deprecated.Idp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">Idp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">acs_binding=None</em>, <em class="sig-param">acs_type=None</em>, <em class="sig-param">authorization_binding=None</em>, <em class="sig-param">authorization_url=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">issuer_url=None</em>, <em class="sig-param">jwks_binding=None</em>, <em class="sig-param">jwks_url=None</em>, <em class="sig-param">max_clock_skew=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">protocol_type=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">token_binding=None</em>, <em class="sig-param">token_url=None</em>, <em class="sig-param">user_info_binding=None</em>, <em class="sig-param">user_info_url=None</em>, <em class="sig-param">username_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.Idp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Idp resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_okta.deprecated.Idp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">acs_binding=None</em>, <em class="sig-param">acs_type=None</em>, <em class="sig-param">authorization_binding=None</em>, <em class="sig-param">authorization_url=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">issuer_url=None</em>, <em class="sig-param">jwks_binding=None</em>, <em class="sig-param">jwks_url=None</em>, <em class="sig-param">max_clock_skew=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">protocol_type=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">token_binding=None</em>, <em class="sig-param">token_url=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_info_binding=None</em>, <em class="sig-param">user_info_url=None</em>, <em class="sig-param">username_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.Idp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Idp resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.Idp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.Idp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.Idp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.Idp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.MfaPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">MfaPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">duo=None</em>, <em class="sig-param">fido_u2f=None</em>, <em class="sig-param">fido_webauthn=None</em>, <em class="sig-param">google_otp=None</em>, <em class="sig-param">groups_includeds=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">okta_call=None</em>, <em class="sig-param">okta_otp=None</em>, <em class="sig-param">okta_password=None</em>, <em class="sig-param">okta_push=None</em>, <em class="sig-param">okta_question=None</em>, <em class="sig-param">okta_sms=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">rsa_token=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">symantec_vip=None</em>, <em class="sig-param">yubikey_token=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a MfaPolicy resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>duo</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fido_u2f</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fido_webauthn</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>google_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_call</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_password</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_push</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_question</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_sms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rsa_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>symantec_vip</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>yubikey_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="method">
<dt id="pulumi_okta.deprecated.MfaPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">duo=None</em>, <em class="sig-param">fido_u2f=None</em>, <em class="sig-param">fido_webauthn=None</em>, <em class="sig-param">google_otp=None</em>, <em class="sig-param">groups_includeds=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">okta_call=None</em>, <em class="sig-param">okta_otp=None</em>, <em class="sig-param">okta_password=None</em>, <em class="sig-param">okta_push=None</em>, <em class="sig-param">okta_question=None</em>, <em class="sig-param">okta_sms=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">rsa_token=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">symantec_vip=None</em>, <em class="sig-param">yubikey_token=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MfaPolicy resource’s state with the given name, id, and optional extra
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
<p>The <strong>duo</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fido_u2f</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fido_webauthn</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>google_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_call</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_otp</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_password</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_push</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_question</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>okta_sms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rsa_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>symantec_vip</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>yubikey_token</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consent_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enroll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.MfaPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.MfaPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.MfaPolicyRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">MfaPolicyRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enroll=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_connection=None</em>, <em class="sig-param">network_excludes=None</em>, <em class="sig-param">network_includes=None</em>, <em class="sig-param">policyid=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">users_excludeds=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a MfaPolicyRule resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enroll=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_connection=None</em>, <em class="sig-param">network_excludes=None</em>, <em class="sig-param">network_includes=None</em>, <em class="sig-param">policyid=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">users_excludeds=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MfaPolicyRule resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.MfaPolicyRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.MfaPolicyRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.MfaPolicyRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.OauthApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">OauthApp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_key_rotation=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">client_basic_secret=None</em>, <em class="sig-param">client_uri=None</em>, <em class="sig-param">consent_method=None</em>, <em class="sig-param">custom_client_id=None</em>, <em class="sig-param">grant_types=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">login_uri=None</em>, <em class="sig-param">logo_uri=None</em>, <em class="sig-param">omit_secret=None</em>, <em class="sig-param">policy_uri=None</em>, <em class="sig-param">post_logout_redirect_uris=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">redirect_uris=None</em>, <em class="sig-param">response_types=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">token_endpoint_auth_method=None</em>, <em class="sig-param">tos_uri=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a OauthApp resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="method">
<dt id="pulumi_okta.deprecated.OauthApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_key_rotation=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">client_basic_secret=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">client_uri=None</em>, <em class="sig-param">consent_method=None</em>, <em class="sig-param">custom_client_id=None</em>, <em class="sig-param">grant_types=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">login_uri=None</em>, <em class="sig-param">logo_uri=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">omit_secret=None</em>, <em class="sig-param">policy_uri=None</em>, <em class="sig-param">post_logout_redirect_uris=None</em>, <em class="sig-param">profile=None</em>, <em class="sig-param">redirect_uris=None</em>, <em class="sig-param">response_types=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">token_endpoint_auth_method=None</em>, <em class="sig-param">tos_uri=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OauthApp resource’s state with the given name, id, and optional extra
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
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.OauthApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.OauthApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.OauthAppRedirectUri">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">OauthAppRedirectUri</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">uri=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthAppRedirectUri" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a OauthAppRedirectUri resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_okta.deprecated.OauthAppRedirectUri.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthAppRedirectUri.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OauthAppRedirectUri resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.OauthAppRedirectUri.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthAppRedirectUri.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.OauthAppRedirectUri.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.OauthAppRedirectUri.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.PasswordPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">PasswordPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_provider=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">email_recovery=None</em>, <em class="sig-param">groups_includeds=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_auto_unlock_minutes=None</em>, <em class="sig-param">password_dictionary_lookup=None</em>, <em class="sig-param">password_exclude_first_name=None</em>, <em class="sig-param">password_exclude_last_name=None</em>, <em class="sig-param">password_exclude_username=None</em>, <em class="sig-param">password_expire_warn_days=None</em>, <em class="sig-param">password_history_count=None</em>, <em class="sig-param">password_max_age_days=None</em>, <em class="sig-param">password_max_lockout_attempts=None</em>, <em class="sig-param">password_min_age_minutes=None</em>, <em class="sig-param">password_min_length=None</em>, <em class="sig-param">password_min_lowercase=None</em>, <em class="sig-param">password_min_number=None</em>, <em class="sig-param">password_min_symbol=None</em>, <em class="sig-param">password_min_uppercase=None</em>, <em class="sig-param">password_show_lockout_failures=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">question_min_length=None</em>, <em class="sig-param">question_recovery=None</em>, <em class="sig-param">recovery_email_token=None</em>, <em class="sig-param">skip_unlock=None</em>, <em class="sig-param">sms_recovery=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PasswordPolicy resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_okta.deprecated.PasswordPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_provider=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">email_recovery=None</em>, <em class="sig-param">groups_includeds=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_auto_unlock_minutes=None</em>, <em class="sig-param">password_dictionary_lookup=None</em>, <em class="sig-param">password_exclude_first_name=None</em>, <em class="sig-param">password_exclude_last_name=None</em>, <em class="sig-param">password_exclude_username=None</em>, <em class="sig-param">password_expire_warn_days=None</em>, <em class="sig-param">password_history_count=None</em>, <em class="sig-param">password_max_age_days=None</em>, <em class="sig-param">password_max_lockout_attempts=None</em>, <em class="sig-param">password_min_age_minutes=None</em>, <em class="sig-param">password_min_length=None</em>, <em class="sig-param">password_min_lowercase=None</em>, <em class="sig-param">password_min_number=None</em>, <em class="sig-param">password_min_symbol=None</em>, <em class="sig-param">password_min_uppercase=None</em>, <em class="sig-param">password_show_lockout_failures=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">question_min_length=None</em>, <em class="sig-param">question_recovery=None</em>, <em class="sig-param">recovery_email_token=None</em>, <em class="sig-param">skip_unlock=None</em>, <em class="sig-param">sms_recovery=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PasswordPolicy resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.PasswordPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.PasswordPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.PasswordPolicyRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">PasswordPolicyRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_connection=None</em>, <em class="sig-param">network_excludes=None</em>, <em class="sig-param">network_includes=None</em>, <em class="sig-param">password_change=None</em>, <em class="sig-param">password_reset=None</em>, <em class="sig-param">password_unlock=None</em>, <em class="sig-param">policyid=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">users_excludeds=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PasswordPolicyRule resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_connection=None</em>, <em class="sig-param">network_excludes=None</em>, <em class="sig-param">network_includes=None</em>, <em class="sig-param">password_change=None</em>, <em class="sig-param">password_reset=None</em>, <em class="sig-param">password_unlock=None</em>, <em class="sig-param">policyid=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">users_excludeds=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PasswordPolicyRule resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.PasswordPolicyRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.PasswordPolicyRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SamlApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SamlApp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_login_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">app_settings_json=None</em>, <em class="sig-param">assertion_signed=None</em>, <em class="sig-param">attribute_statements=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">authn_context_class_ref=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">default_relay_state=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">digest_algorithm=None</em>, <em class="sig-param">features=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">honor_force_authn=None</em>, <em class="sig-param">idp_issuer=None</em>, <em class="sig-param">key_name=None</em>, <em class="sig-param">key_years_valid=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">recipient=None</em>, <em class="sig-param">request_compressed=None</em>, <em class="sig-param">response_signed=None</em>, <em class="sig-param">signature_algorithm=None</em>, <em class="sig-param">sp_issuer=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_name_id_format=None</em>, <em class="sig-param">subject_name_id_template=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_suffix=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SamlApp resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attribute_statements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filterType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="method">
<dt id="pulumi_okta.deprecated.SamlApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_login_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">app_settings_json=None</em>, <em class="sig-param">assertion_signed=None</em>, <em class="sig-param">attribute_statements=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">authn_context_class_ref=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">default_relay_state=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">digest_algorithm=None</em>, <em class="sig-param">entity_key=None</em>, <em class="sig-param">entity_url=None</em>, <em class="sig-param">features=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">honor_force_authn=None</em>, <em class="sig-param">http_post_binding=None</em>, <em class="sig-param">http_redirect_binding=None</em>, <em class="sig-param">idp_issuer=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">key_name=None</em>, <em class="sig-param">key_years_valid=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">recipient=None</em>, <em class="sig-param">request_compressed=None</em>, <em class="sig-param">response_signed=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">signature_algorithm=None</em>, <em class="sig-param">sp_issuer=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_name_id_format=None</em>, <em class="sig-param">subject_name_id_template=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_suffix=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SamlApp resource’s state with the given name, id, and optional extra
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
<p>The <strong>attribute_statements</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filterType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.SamlApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SamlApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SamlIdp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SamlIdp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">acs_binding=None</em>, <em class="sig-param">acs_type=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_format=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">sso_binding=None</em>, <em class="sig-param">sso_destination=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_filter=None</em>, <em class="sig-param">subject_formats=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">username_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SamlIdp resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_okta.deprecated.SamlIdp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">acs_binding=None</em>, <em class="sig-param">acs_type=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_format=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">sso_binding=None</em>, <em class="sig-param">sso_destination=None</em>, <em class="sig-param">sso_url=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_filter=None</em>, <em class="sig-param">subject_formats=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">username_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SamlIdp resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.SamlIdp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SamlIdp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SamlIdpSigningKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SamlIdpSigningKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">x5cs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdpSigningKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SamlIdpSigningKey resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_okta.deprecated.SamlIdpSigningKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">expires_at=None</em>, <em class="sig-param">kid=None</em>, <em class="sig-param">kty=None</em>, <em class="sig-param">use=None</em>, <em class="sig-param">x5cs=None</em>, <em class="sig-param">x5t_s256=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdpSigningKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SamlIdpSigningKey resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.SamlIdpSigningKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdpSigningKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SamlIdpSigningKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SamlIdpSigningKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SecurePasswordStoreApp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">credentials_scheme=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">optional_field1=None</em>, <em class="sig-param">optional_field1_value=None</em>, <em class="sig-param">optional_field2=None</em>, <em class="sig-param">optional_field2_value=None</em>, <em class="sig-param">optional_field3=None</em>, <em class="sig-param">optional_field3_value=None</em>, <em class="sig-param">password_field=None</em>, <em class="sig-param">reveal_password=None</em>, <em class="sig-param">shared_password=None</em>, <em class="sig-param">shared_username=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">username_field=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecurePasswordStoreApp resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="method">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">credentials_scheme=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">optional_field1=None</em>, <em class="sig-param">optional_field1_value=None</em>, <em class="sig-param">optional_field2=None</em>, <em class="sig-param">optional_field2_value=None</em>, <em class="sig-param">optional_field3=None</em>, <em class="sig-param">optional_field3_value=None</em>, <em class="sig-param">password_field=None</em>, <em class="sig-param">reveal_password=None</em>, <em class="sig-param">shared_password=None</em>, <em class="sig-param">shared_username=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">username_field=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurePasswordStoreApp resource’s state with the given name, id, and optional extra
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
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SecurePasswordStoreApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SecurePasswordStoreApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SignonPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SignonPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">groups_includeds=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SignonPolicy resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_okta.deprecated.SignonPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">groups_includeds=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SignonPolicy resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.SignonPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SignonPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SignonPolicyRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SignonPolicyRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access=None</em>, <em class="sig-param">authtype=None</em>, <em class="sig-param">mfa_lifetime=None</em>, <em class="sig-param">mfa_prompt=None</em>, <em class="sig-param">mfa_remember_device=None</em>, <em class="sig-param">mfa_required=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_connection=None</em>, <em class="sig-param">network_excludes=None</em>, <em class="sig-param">network_includes=None</em>, <em class="sig-param">policyid=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">session_idle=None</em>, <em class="sig-param">session_lifetime=None</em>, <em class="sig-param">session_persistent=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">users_excludeds=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SignonPolicyRule resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access=None</em>, <em class="sig-param">authtype=None</em>, <em class="sig-param">mfa_lifetime=None</em>, <em class="sig-param">mfa_prompt=None</em>, <em class="sig-param">mfa_remember_device=None</em>, <em class="sig-param">mfa_required=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_connection=None</em>, <em class="sig-param">network_excludes=None</em>, <em class="sig-param">network_includes=None</em>, <em class="sig-param">policyid=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">session_idle=None</em>, <em class="sig-param">session_lifetime=None</em>, <em class="sig-param">session_persistent=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">users_excludeds=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SignonPolicyRule resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.SignonPolicyRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SignonPolicyRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SignonPolicyRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SocialIdp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SocialIdp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">match_attribute=None</em>, <em class="sig-param">match_type=None</em>, <em class="sig-param">max_clock_skew=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">protocol_type=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">username_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SocialIdp resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_okta.deprecated.SocialIdp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_link_action=None</em>, <em class="sig-param">account_link_group_includes=None</em>, <em class="sig-param">authorization_binding=None</em>, <em class="sig-param">authorization_url=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">deprovisioned_action=None</em>, <em class="sig-param">groups_action=None</em>, <em class="sig-param">groups_assignments=None</em>, <em class="sig-param">groups_attribute=None</em>, <em class="sig-param">groups_filters=None</em>, <em class="sig-param">issuer_mode=None</em>, <em class="sig-param">match_attribute=None</em>, <em class="sig-param">match_type=None</em>, <em class="sig-param">max_clock_skew=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_master=None</em>, <em class="sig-param">protocol_type=None</em>, <em class="sig-param">provisioning_action=None</em>, <em class="sig-param">request_signature_algorithm=None</em>, <em class="sig-param">request_signature_scope=None</em>, <em class="sig-param">response_signature_algorithm=None</em>, <em class="sig-param">response_signature_scope=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">subject_match_attribute=None</em>, <em class="sig-param">subject_match_type=None</em>, <em class="sig-param">suspended_action=None</em>, <em class="sig-param">token_binding=None</em>, <em class="sig-param">token_url=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">username_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SocialIdp resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.SocialIdp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SocialIdp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SocialIdp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SwaApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">SwaApp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">button_field=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">password_field=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">url_regex=None</em>, <em class="sig-param">username_field=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SwaApp resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="method">
<dt id="pulumi_okta.deprecated.SwaApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">button_field=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_field=None</em>, <em class="sig-param">preconfigured_app=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">url_regex=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">username_field=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SwaApp resource’s state with the given name, id, and optional extra
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
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.SwaApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.SwaApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.SwaApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.ThreeFieldApp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">ThreeFieldApp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">button_selector=None</em>, <em class="sig-param">extra_field_selector=None</em>, <em class="sig-param">extra_field_value=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">password_selector=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">url_regex=None</em>, <em class="sig-param">username_selector=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ThreeFieldApp resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="method">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessibility_error_redirect_url=None</em>, <em class="sig-param">accessibility_self_service=None</em>, <em class="sig-param">auto_submit_toolbar=None</em>, <em class="sig-param">button_selector=None</em>, <em class="sig-param">extra_field_selector=None</em>, <em class="sig-param">extra_field_value=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">hide_ios=None</em>, <em class="sig-param">hide_web=None</em>, <em class="sig-param">label=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password_selector=None</em>, <em class="sig-param">sign_on_mode=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">url_regex=None</em>, <em class="sig-param">user_name_template=None</em>, <em class="sig-param">user_name_template_type=None</em>, <em class="sig-param">username_selector=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ThreeFieldApp resource’s state with the given name, id, and optional extra
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
<p>The <strong>users</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.deprecated.ThreeFieldApp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.ThreeFieldApp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.ThreeFieldApp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.deprecated.get_default_policies">
<code class="sig-prename descclassname">pulumi_okta.deprecated.</code><code class="sig-name descname">get_default_policies</code><span class="sig-paren">(</span><em class="sig-param">type=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.deprecated.get_default_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
