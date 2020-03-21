---
title: Module ldap
title_tag: Module ldap | Package pulumi_keycloak | Python SDK
linktitle: ldap
notitle: true
---

<div class="section" id="module-pulumi_keycloak.ldap">
<span id="ldap"></span><h1>ldap<a class="headerlink" href="#module-pulumi_keycloak.ldap" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_keycloak.ldap.FullNameMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.ldap.</code><code class="sig-name descname">FullNameMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ldap_full_name_attribute=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">read_only=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">write_only=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.FullNameMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing full name mappers for Keycloak users federated
via LDAP.</p>
<p>The LDAP full name mapper can map a user’s full name from an LDAP attribute
to the first and last name attributes of a Keycloak user.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm that this LDAP mapper will exist in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ldap_user_federation_id</span></code> - (Required) The ID of the LDAP user federation provider to attach this mapper to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Display name of this mapper when displayed in the console.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ldap_full_name_attribute</span></code> - (Required) The name of the LDAP attribute containing the user’s full name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, updates to a user within Keycloak will not be written back to LDAP. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_only</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, this mapper will only be used to write updates to LDAP. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_full_name_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_full_name_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_keycloak.ldap.FullNameMapper.ldap_user_federation_id">
<code class="sig-name descname">ldap_user_federation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.FullNameMapper.ldap_user_federation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ldap user federation provider to attach this mapper to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.FullNameMapper.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.FullNameMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the mapper when displayed in the console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.FullNameMapper.realm_id">
<code class="sig-name descname">realm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.FullNameMapper.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm in which the ldap user federation provider exists.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.FullNameMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ldap_full_name_attribute=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">read_only=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">write_only=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.FullNameMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FullNameMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.FullNameMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.FullNameMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.FullNameMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.FullNameMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.GroupMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.ldap.</code><code class="sig-name descname">GroupMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">drop_non_existing_groups_during_sync=None</em>, <em class="sig-param">group_name_ldap_attribute=None</em>, <em class="sig-param">group_object_classes=None</em>, <em class="sig-param">groups_ldap_filter=None</em>, <em class="sig-param">ignore_missing_groups=None</em>, <em class="sig-param">ldap_groups_dn=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">mapped_group_attributes=None</em>, <em class="sig-param">memberof_ldap_attribute=None</em>, <em class="sig-param">membership_attribute_type=None</em>, <em class="sig-param">membership_ldap_attribute=None</em>, <em class="sig-param">membership_user_ldap_attribute=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">preserve_group_inheritance=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">user_roles_retrieve_strategy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.GroupMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing group mappers for Keycloak users federated
via LDAP.</p>
<p>The LDAP group mapper can be used to map an LDAP user’s groups from some DN
to Keycloak groups. This group mapper will also create the groups within Keycloak
if they do not already exist.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm that this LDAP mapper will exist in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ldap_user_federation_id</span></code> - (Required) The ID of the LDAP user federation provider to attach this mapper to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Display name of this mapper when displayed in the console.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ldap_groups_dn</span></code> - (Required) The LDAP DN where groups can be found.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_name_ldap_attribute</span></code> - (Required) The name of the LDAP attribute that is used in group objects for the name and RDN of the group. Typically <code class="docutils literal notranslate"><span class="pre">cn</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_object_classes</span></code> - (Required) Array of strings representing the object classes for the group. Must contain at least one.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserve_group_inheritance</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, group inheritance will be propagated from LDAP to Keycloak. When <code class="docutils literal notranslate"><span class="pre">false</span></code>, all LDAP groups will be propagated as top level groups within Keycloak.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ignore_missing_groups</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, missing groups in the hierarchy will be ignored.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">membership_ldap_attribute</span></code> - (Required) The name of the LDAP attribute that is used for membership mappings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">membership_attribute_type</span></code> - (Optional) Can be one of <code class="docutils literal notranslate"><span class="pre">DN</span></code> or <code class="docutils literal notranslate"><span class="pre">UID</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DN</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">membership_user_ldap_attribute</span></code> - (Required) The name of the LDAP attribute on a user that is used for membership mappings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups_ldap_filter</span></code> - (Optional) When specified, adds an additional custom filter to be used when querying for groups. Must start with <code class="docutils literal notranslate"><span class="pre">(</span></code> and end with <code class="docutils literal notranslate"><span class="pre">)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> - (Optional) Can be one of <code class="docutils literal notranslate"><span class="pre">READ_ONLY</span></code> or <code class="docutils literal notranslate"><span class="pre">LDAP_ONLY</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">READ_ONLY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_roles_retrieve_strategy</span></code> - (Optional) Can be one of <code class="docutils literal notranslate"><span class="pre">LOAD_GROUPS_BY_MEMBER_ATTRIBUTE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET_GROUPS_FROM_USER_MEMBEROF_ATTRIBUTE</span></code>, or <code class="docutils literal notranslate"><span class="pre">LOAD_GROUPS_BY_MEMBER_ATTRIBUTE_RECURSIVELY</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">LOAD_GROUPS_BY_MEMBER_ATTRIBUTE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memberof_ldap_attribute</span></code> - (Optional) Specifies the name of the LDAP attribute on the LDAP user that contains the groups the user is a member of. Defaults to <code class="docutils literal notranslate"><span class="pre">memberOf</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mapped_group_attributes</span></code> - (Optional) Array of strings representing attributes on the LDAP group which will be mapped to attributes on the Keycloak group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drop_non_existing_groups_during_sync</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, groups that no longer exist within LDAP will be dropped in Keycloak during sync. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_group_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_group_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_keycloak.ldap.GroupMapper.ldap_user_federation_id">
<code class="sig-name descname">ldap_user_federation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.GroupMapper.ldap_user_federation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ldap user federation provider to attach this mapper to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.GroupMapper.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.GroupMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the mapper when displayed in the console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.GroupMapper.realm_id">
<code class="sig-name descname">realm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.GroupMapper.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm in which the ldap user federation provider exists.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.GroupMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">drop_non_existing_groups_during_sync=None</em>, <em class="sig-param">group_name_ldap_attribute=None</em>, <em class="sig-param">group_object_classes=None</em>, <em class="sig-param">groups_ldap_filter=None</em>, <em class="sig-param">ignore_missing_groups=None</em>, <em class="sig-param">ldap_groups_dn=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">mapped_group_attributes=None</em>, <em class="sig-param">memberof_ldap_attribute=None</em>, <em class="sig-param">membership_attribute_type=None</em>, <em class="sig-param">membership_ldap_attribute=None</em>, <em class="sig-param">membership_user_ldap_attribute=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">preserve_group_inheritance=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">user_roles_retrieve_strategy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.GroupMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.GroupMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.GroupMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.GroupMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.GroupMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.HardcodedRoleMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.ldap.</code><code class="sig-name descname">HardcodedRoleMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.HardcodedRoleMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>This mapper will grant a specified Keycloak role to each Keycloak user linked with LDAP.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm that this LDAP mapper will exist in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ldap_user_federation_id</span></code> - (Required) The ID of the LDAP user federation provider to attach this mapper to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Display name of this mapper when displayed in the console.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role</span></code> - (Required) The role which should be assigned to the users.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_hardcoded_role_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_hardcoded_role_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role to grant to user.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_keycloak.ldap.HardcodedRoleMapper.ldap_user_federation_id">
<code class="sig-name descname">ldap_user_federation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.HardcodedRoleMapper.ldap_user_federation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ldap user federation provider to attach this mapper to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.HardcodedRoleMapper.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.HardcodedRoleMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the mapper when displayed in the console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.HardcodedRoleMapper.realm_id">
<code class="sig-name descname">realm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.HardcodedRoleMapper.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm in which the ldap user federation provider exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.HardcodedRoleMapper.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.HardcodedRoleMapper.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Role to grant to user.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.HardcodedRoleMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.HardcodedRoleMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HardcodedRoleMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role to grant to user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.HardcodedRoleMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.HardcodedRoleMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.HardcodedRoleMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.HardcodedRoleMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.ldap.</code><code class="sig-name descname">MsadLdsUserAccountControlMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a MsadLdsUserAccountControlMapper resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] ldap_user_federation_id: The ldap user federation provider to attach this mapper to.
:param pulumi.Input[str] name: Display name of the mapper when displayed in the console.
:param pulumi.Input[str] realm_id: The realm in which the ldap user federation provider exists.</p>
<dl class="attribute">
<dt id="pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.ldap_user_federation_id">
<code class="sig-name descname">ldap_user_federation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.ldap_user_federation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ldap user federation provider to attach this mapper to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the mapper when displayed in the console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.realm_id">
<code class="sig-name descname">realm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm in which the ldap user federation provider exists.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MsadLdsUserAccountControlMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.MsadLdsUserAccountControlMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.MsadUserAccountControlMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.ldap.</code><code class="sig-name descname">MsadUserAccountControlMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ldap_password_policy_hints_enabled=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.MsadUserAccountControlMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing MSAD user account control mappers for Keycloak
users federated via LDAP.</p>
<p>The MSAD (Microsoft Active Directory) user account control mapper is specific
to LDAP user federation providers that are pulling from AD, and it can propagate
AD user state to Keycloak in order to enforce settings like expired passwords
or disabled accounts.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm that this LDAP mapper will exist in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ldap_user_federation_id</span></code> - (Required) The ID of the LDAP user federation provider to attach this mapper to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Display name of this mapper when displayed in the console.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ldap_password_policy_hints_enabled</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, advanced password policies, such as password hints and previous password history will be used when writing new passwords to AD. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_msad_user_account_control_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_msad_user_account_control_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_keycloak.ldap.MsadUserAccountControlMapper.ldap_user_federation_id">
<code class="sig-name descname">ldap_user_federation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.MsadUserAccountControlMapper.ldap_user_federation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ldap user federation provider to attach this mapper to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.MsadUserAccountControlMapper.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.MsadUserAccountControlMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the mapper when displayed in the console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.MsadUserAccountControlMapper.realm_id">
<code class="sig-name descname">realm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.MsadUserAccountControlMapper.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm in which the ldap user federation provider exists.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.MsadUserAccountControlMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ldap_password_policy_hints_enabled=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">realm_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.MsadUserAccountControlMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MsadUserAccountControlMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.MsadUserAccountControlMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.MsadUserAccountControlMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.MsadUserAccountControlMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.MsadUserAccountControlMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.UserAttributeMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.ldap.</code><code class="sig-name descname">UserAttributeMapper</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">always_read_value_from_ldap=None</em>, <em class="sig-param">is_mandatory_in_ldap=None</em>, <em class="sig-param">ldap_attribute=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">read_only=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">user_model_attribute=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing user attribute mappers for Keycloak users
federated via LDAP.</p>
<p>The LDAP user attribute mapper can be used to map a single LDAP attribute
to an attribute on the Keycloak user model.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm that this LDAP mapper will exist in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ldap_user_federation_id</span></code> - (Required) The ID of the LDAP user federation provider to attach this mapper to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Display name of this mapper when displayed in the console.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_model_attribute</span></code> - (Required) Name of the user property or attribute you want to map the LDAP attribute into.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ldap_attribute</span></code> - (Required) Name of the mapped attribute on the LDAP object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">always_read_value_from_ldap</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the value fetched from LDAP will override the value stored in Keycloak. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">is_mandatory_in_ldap</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, this attribute must exist in LDAP. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_user_attribute_mapper.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_user_attribute_mapper.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>always_read_value_from_ldap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, the value fetched from LDAP will override the value stored in Keycloak.</p></li>
<li><p><strong>is_mandatory_in_ldap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, this attribute must exist in LDAP.</p></li>
<li><p><strong>ldap_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the mapped attribute on LDAP object.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
<li><p><strong>user_model_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the UserModel property or attribute you want to map the LDAP attribute into.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.always_read_value_from_ldap">
<code class="sig-name descname">always_read_value_from_ldap</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.always_read_value_from_ldap" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, the value fetched from LDAP will override the value stored in Keycloak.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.is_mandatory_in_ldap">
<code class="sig-name descname">is_mandatory_in_ldap</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.is_mandatory_in_ldap" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, this attribute must exist in LDAP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.ldap_attribute">
<code class="sig-name descname">ldap_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.ldap_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the mapped attribute on LDAP object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.ldap_user_federation_id">
<code class="sig-name descname">ldap_user_federation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.ldap_user_federation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ldap user federation provider to attach this mapper to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the mapper when displayed in the console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.read_only">
<code class="sig-name descname">read_only</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.realm_id">
<code class="sig-name descname">realm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm in which the ldap user federation provider exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.user_model_attribute">
<code class="sig-name descname">user_model_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.user_model_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the UserModel property or attribute you want to map the LDAP attribute into.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">always_read_value_from_ldap=None</em>, <em class="sig-param">is_mandatory_in_ldap=None</em>, <em class="sig-param">ldap_attribute=None</em>, <em class="sig-param">ldap_user_federation_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">read_only=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">user_model_attribute=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserAttributeMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>always_read_value_from_ldap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, the value fetched from LDAP will override the value stored in Keycloak.</p></li>
<li><p><strong>is_mandatory_in_ldap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, this attribute must exist in LDAP.</p></li>
<li><p><strong>ldap_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the mapped attribute on LDAP object.</p></li>
<li><p><strong>ldap_user_federation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ldap user federation provider to attach this mapper to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the mapper when displayed in the console.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm in which the ldap user federation provider exists.</p></li>
<li><p><strong>user_model_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the UserModel property or attribute you want to map the LDAP attribute into.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.UserAttributeMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.UserAttributeMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.UserFederation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.ldap.</code><code class="sig-name descname">UserFederation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">batch_size_for_sync=None</em>, <em class="sig-param">bind_credential=None</em>, <em class="sig-param">bind_dn=None</em>, <em class="sig-param">cache_policy=None</em>, <em class="sig-param">changed_sync_period=None</em>, <em class="sig-param">connection_timeout=None</em>, <em class="sig-param">connection_url=None</em>, <em class="sig-param">custom_user_search_filter=None</em>, <em class="sig-param">edit_mode=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">full_sync_period=None</em>, <em class="sig-param">import_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pagination=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">rdn_ldap_attribute=None</em>, <em class="sig-param">read_timeout=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">search_scope=None</em>, <em class="sig-param">sync_registrations=None</em>, <em class="sig-param">use_truststore_spi=None</em>, <em class="sig-param">user_object_classes=None</em>, <em class="sig-param">username_ldap_attribute=None</em>, <em class="sig-param">users_dn=None</em>, <em class="sig-param">uuid_ldap_attribute=None</em>, <em class="sig-param">validate_password_policy=None</em>, <em class="sig-param">vendor=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing LDAP user federation providers within Keycloak.</p>
<p>Keycloak can use an LDAP user federation provider to federate users to Keycloak
from a directory system such as LDAP or Active Directory. Federated users
will exist within the realm and will be able to log in to clients. Federated
users can have their attributes defined using mappers.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm that this provider will provide user federation for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Display name of the provider when displayed in the console.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">false</span></code>, this provider will not be used when performing queries for users. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> - (Optional) Priority of this provider when looking up users. Lower values are first. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">import_enabled</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, LDAP users will be imported into the Keycloak database. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edit_mode</span></code> - (Optional) Can be one of <code class="docutils literal notranslate"><span class="pre">READ_ONLY</span></code>, <code class="docutils literal notranslate"><span class="pre">WRITABLE</span></code>, or <code class="docutils literal notranslate"><span class="pre">UNSYNCED</span></code>. <code class="docutils literal notranslate"><span class="pre">UNSYNCED</span></code> allows user data to be imported but not synced back to LDAP. Defaults to <code class="docutils literal notranslate"><span class="pre">READ_ONLY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sync_registrations</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, newly created users will be synced back to LDAP. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vendor</span></code> - (Optional) Can be one of <code class="docutils literal notranslate"><span class="pre">OTHER</span></code>, <code class="docutils literal notranslate"><span class="pre">EDIRECTORY</span></code>, <code class="docutils literal notranslate"><span class="pre">AD</span></code>, <code class="docutils literal notranslate"><span class="pre">RHDS</span></code>, or <code class="docutils literal notranslate"><span class="pre">TIVOLI</span></code>. When this is selected in the GUI, it provides reasonable defaults for other fields. When used with the Keycloak API, this attribute does nothing, but is still required. Defaults to <code class="docutils literal notranslate"><span class="pre">OPTIONAL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username_ldap_attribute</span></code> - (Required) Name of the LDAP attribute to use as the Keycloak username.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rdn_ldap_attribute</span></code> - (Required) Name of the LDAP attribute to use as the relative distinguished name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uuid_ldap_attribute</span></code> - (Required) Name of the LDAP attribute to use as a unique object identifier for objects in LDAP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_object_classes</span></code> - (Required) Array of all values of LDAP objectClass attribute for users in LDAP. Must contain at least one.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_url</span></code> - (Required) Connection URL to the LDAP server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">users_dn</span></code> - (Required) Full DN of LDAP tree where your users are.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bind_dn</span></code> - (Optional) DN of LDAP admin, which will be used by Keycloak to access LDAP server. This attribute must be set if <code class="docutils literal notranslate"><span class="pre">bind_credential</span></code> is set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bind_credential</span></code> - (Optional) Password of LDAP admin. This attribute must be set if <code class="docutils literal notranslate"><span class="pre">bind_dn</span></code> is set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">custom_user_search_filter</span></code> - (Optional) Additional LDAP filter for filtering searched users. Must begin with <code class="docutils literal notranslate"><span class="pre">(</span></code> and end with <code class="docutils literal notranslate"><span class="pre">)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">search_scope</span></code> - (Optional) Can be one of <code class="docutils literal notranslate"><span class="pre">ONE_LEVEL</span></code> or <code class="docutils literal notranslate"><span class="pre">SUBTREE</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ONE_LEVEL</span></code>: Only search for users in the DN specified by <code class="docutils literal notranslate"><span class="pre">user_dn</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">SUBTREE</span></code>: Search entire LDAP subtree.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">validate_password_policy</span></code> - (Optional) When <code class="docutils literal notranslate"><span class="pre">true</span></code>, Keycloak will validate passwords using the realm policy before updating it.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use_truststore_spi</span></code> - (Optional) Can be one of <code class="docutils literal notranslate"><span class="pre">ALWAYS</span></code>, <code class="docutils literal notranslate"><span class="pre">ONLY_FOR_LDAPS</span></code>, or <code class="docutils literal notranslate"><span class="pre">NEVER</span></code>:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ALWAYS</span></code> - Always use the truststore SPI for LDAP connections.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">NEVER</span></code> - Never use the truststore SPI for LDAP connections.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ONLY_FOR_LDAPS</span></code> - Only use the truststore SPI if your LDAP connection uses the ldaps protocol.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_timeout</span></code> - (Optional) LDAP connection timeout in the format of a <a class="reference external" href="https://golang.org/pkg/time/#Duration.String">Go duration string</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_timeout</span></code> - (Optional) LDAP read timeout in the format of a <a class="reference external" href="https://golang.org/pkg/time/#Duration.String">Go duration string</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pagination</span></code> - (Optional) When true, Keycloak assumes the LDAP server supports pagination. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batch_size_for_sync</span></code> - (Optional) The number of users to sync within a single transaction. Defaults to <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">full_sync_period</span></code> - (Optional) How frequently Keycloak should sync all LDAP users, in seconds. Omit this property to disable periodic full sync.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">changed_sync_period</span></code> - (Optional) How frequently Keycloak should sync changed LDAP users, in seconds. Omit this property to disable periodic changed users sync.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cache_policy</span></code> - (Optional) Can be one of <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>, <code class="docutils literal notranslate"><span class="pre">EVICT_DAILY</span></code>, <code class="docutils literal notranslate"><span class="pre">EVICT_WEEKLY</span></code>, <code class="docutils literal notranslate"><span class="pre">MAX_LIFESPAN</span></code>, or <code class="docutils literal notranslate"><span class="pre">NO_CACHE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_user_federation.html.markdown">https://github.com/mrparkers/terraform-provider-keycloak/blob/master/website/docs/r/keycloak_ldap_user_federation.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>batch_size_for_sync</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of users to sync within a single transaction.</p></li>
<li><p><strong>bind_credential</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password of LDAP admin.</p></li>
<li><p><strong>bind_dn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DN of LDAP admin, which will be used by Keycloak to access LDAP server.</p></li>
<li><p><strong>changed_sync_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How frequently Keycloak should sync changed LDAP users, in seconds. Omit this property to disable periodic changed users
sync.</p></li>
<li><p><strong>connection_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – LDAP connection timeout (duration string)</p></li>
<li><p><strong>connection_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Connection URL to the LDAP server.</p></li>
<li><p><strong>custom_user_search_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Additional LDAP filter for filtering searched users. Must begin with ‘(‘ and end with ‘)’.</p></li>
<li><p><strong>edit_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – READ_ONLY and WRITABLE are self-explanatory. UNSYNCED allows user data to be imported but not synced back to LDAP.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When false, this provider will not be used when performing queries for users.</p></li>
<li><p><strong>full_sync_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How frequently Keycloak should sync all LDAP users, in seconds. Omit this property to disable periodic full sync.</p></li>
<li><p><strong>import_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, LDAP users will be imported into the Keycloak database.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the provider when displayed in the console.</p></li>
<li><p><strong>pagination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, Keycloak assumes the LDAP server supports pagination.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of this provider when looking up users. Lower values are first.</p></li>
<li><p><strong>rdn_ldap_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the LDAP attribute to use as the relative distinguished name.</p></li>
<li><p><strong>read_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – LDAP read timeout (duration string)</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this provider will provide user federation for.</p></li>
<li><p><strong>search_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ONE_LEVEL: only search for users in the DN specified by user_dn. SUBTREE: search entire LDAP subtree.</p></li>
<li><p><strong>sync_registrations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, newly created users will be synced back to LDAP.</p></li>
<li><p><strong>user_object_classes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – All values of LDAP objectClass attribute for users in LDAP.</p></li>
<li><p><strong>username_ldap_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the LDAP attribute to use as the Keycloak username.</p></li>
<li><p><strong>users_dn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Full DN of LDAP tree where your users are.</p></li>
<li><p><strong>uuid_ldap_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the LDAP attribute to use as a unique object identifier for objects in LDAP.</p></li>
<li><p><strong>validate_password_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, Keycloak will validate passwords using the realm policy before updating it.</p></li>
<li><p><strong>vendor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – LDAP vendor. I am almost certain this field does nothing, but the UI indicates that it is required.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.batch_size_for_sync">
<code class="sig-name descname">batch_size_for_sync</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.batch_size_for_sync" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of users to sync within a single transaction.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.bind_credential">
<code class="sig-name descname">bind_credential</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.bind_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>Password of LDAP admin.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.bind_dn">
<code class="sig-name descname">bind_dn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.bind_dn" title="Permalink to this definition">¶</a></dt>
<dd><p>DN of LDAP admin, which will be used by Keycloak to access LDAP server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.changed_sync_period">
<code class="sig-name descname">changed_sync_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.changed_sync_period" title="Permalink to this definition">¶</a></dt>
<dd><p>How frequently Keycloak should sync changed LDAP users, in seconds. Omit this property to disable periodic changed users
sync.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.connection_timeout">
<code class="sig-name descname">connection_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.connection_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>LDAP connection timeout (duration string)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.connection_url">
<code class="sig-name descname">connection_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.connection_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Connection URL to the LDAP server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.custom_user_search_filter">
<code class="sig-name descname">custom_user_search_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.custom_user_search_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional LDAP filter for filtering searched users. Must begin with ‘(‘ and end with ‘)’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.edit_mode">
<code class="sig-name descname">edit_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.edit_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>READ_ONLY and WRITABLE are self-explanatory. UNSYNCED allows user data to be imported but not synced back to LDAP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When false, this provider will not be used when performing queries for users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.full_sync_period">
<code class="sig-name descname">full_sync_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.full_sync_period" title="Permalink to this definition">¶</a></dt>
<dd><p>How frequently Keycloak should sync all LDAP users, in seconds. Omit this property to disable periodic full sync.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.import_enabled">
<code class="sig-name descname">import_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.import_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, LDAP users will be imported into the Keycloak database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the provider when displayed in the console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.pagination">
<code class="sig-name descname">pagination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.pagination" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, Keycloak assumes the LDAP server supports pagination.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Priority of this provider when looking up users. Lower values are first.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.rdn_ldap_attribute">
<code class="sig-name descname">rdn_ldap_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.rdn_ldap_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the LDAP attribute to use as the relative distinguished name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.read_timeout">
<code class="sig-name descname">read_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.read_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>LDAP read timeout (duration string)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.realm_id">
<code class="sig-name descname">realm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm this provider will provide user federation for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.search_scope">
<code class="sig-name descname">search_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.search_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>ONE_LEVEL: only search for users in the DN specified by user_dn. SUBTREE: search entire LDAP subtree.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.sync_registrations">
<code class="sig-name descname">sync_registrations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.sync_registrations" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, newly created users will be synced back to LDAP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.user_object_classes">
<code class="sig-name descname">user_object_classes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.user_object_classes" title="Permalink to this definition">¶</a></dt>
<dd><p>All values of LDAP objectClass attribute for users in LDAP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.username_ldap_attribute">
<code class="sig-name descname">username_ldap_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.username_ldap_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the LDAP attribute to use as the Keycloak username.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.users_dn">
<code class="sig-name descname">users_dn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.users_dn" title="Permalink to this definition">¶</a></dt>
<dd><p>Full DN of LDAP tree where your users are.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.uuid_ldap_attribute">
<code class="sig-name descname">uuid_ldap_attribute</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.uuid_ldap_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the LDAP attribute to use as a unique object identifier for objects in LDAP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.validate_password_policy">
<code class="sig-name descname">validate_password_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.validate_password_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, Keycloak will validate passwords using the realm policy before updating it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_keycloak.ldap.UserFederation.vendor">
<code class="sig-name descname">vendor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.vendor" title="Permalink to this definition">¶</a></dt>
<dd><p>LDAP vendor. I am almost certain this field does nothing, but the UI indicates that it is required.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.UserFederation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">batch_size_for_sync=None</em>, <em class="sig-param">bind_credential=None</em>, <em class="sig-param">bind_dn=None</em>, <em class="sig-param">cache_policy=None</em>, <em class="sig-param">changed_sync_period=None</em>, <em class="sig-param">connection_timeout=None</em>, <em class="sig-param">connection_url=None</em>, <em class="sig-param">custom_user_search_filter=None</em>, <em class="sig-param">edit_mode=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">full_sync_period=None</em>, <em class="sig-param">import_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pagination=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">rdn_ldap_attribute=None</em>, <em class="sig-param">read_timeout=None</em>, <em class="sig-param">realm_id=None</em>, <em class="sig-param">search_scope=None</em>, <em class="sig-param">sync_registrations=None</em>, <em class="sig-param">use_truststore_spi=None</em>, <em class="sig-param">user_object_classes=None</em>, <em class="sig-param">username_ldap_attribute=None</em>, <em class="sig-param">users_dn=None</em>, <em class="sig-param">uuid_ldap_attribute=None</em>, <em class="sig-param">validate_password_policy=None</em>, <em class="sig-param">vendor=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserFederation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>batch_size_for_sync</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of users to sync within a single transaction.</p></li>
<li><p><strong>bind_credential</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password of LDAP admin.</p></li>
<li><p><strong>bind_dn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DN of LDAP admin, which will be used by Keycloak to access LDAP server.</p></li>
<li><p><strong>changed_sync_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How frequently Keycloak should sync changed LDAP users, in seconds. Omit this property to disable periodic changed users
sync.</p></li>
<li><p><strong>connection_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – LDAP connection timeout (duration string)</p></li>
<li><p><strong>connection_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Connection URL to the LDAP server.</p></li>
<li><p><strong>custom_user_search_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Additional LDAP filter for filtering searched users. Must begin with ‘(‘ and end with ‘)’.</p></li>
<li><p><strong>edit_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – READ_ONLY and WRITABLE are self-explanatory. UNSYNCED allows user data to be imported but not synced back to LDAP.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When false, this provider will not be used when performing queries for users.</p></li>
<li><p><strong>full_sync_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How frequently Keycloak should sync all LDAP users, in seconds. Omit this property to disable periodic full sync.</p></li>
<li><p><strong>import_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, LDAP users will be imported into the Keycloak database.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the provider when displayed in the console.</p></li>
<li><p><strong>pagination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, Keycloak assumes the LDAP server supports pagination.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of this provider when looking up users. Lower values are first.</p></li>
<li><p><strong>rdn_ldap_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the LDAP attribute to use as the relative distinguished name.</p></li>
<li><p><strong>read_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – LDAP read timeout (duration string)</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this provider will provide user federation for.</p></li>
<li><p><strong>search_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ONE_LEVEL: only search for users in the DN specified by user_dn. SUBTREE: search entire LDAP subtree.</p></li>
<li><p><strong>sync_registrations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, newly created users will be synced back to LDAP.</p></li>
<li><p><strong>user_object_classes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – All values of LDAP objectClass attribute for users in LDAP.</p></li>
<li><p><strong>username_ldap_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the LDAP attribute to use as the Keycloak username.</p></li>
<li><p><strong>users_dn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Full DN of LDAP tree where your users are.</p></li>
<li><p><strong>uuid_ldap_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the LDAP attribute to use as a unique object identifier for objects in LDAP.</p></li>
<li><p><strong>validate_password_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, Keycloak will validate passwords using the realm policy before updating it.</p></li>
<li><p><strong>vendor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – LDAP vendor. I am almost certain this field does nothing, but the UI indicates that it is required.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_keycloak.ldap.UserFederation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.ldap.UserFederation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.ldap.UserFederation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
