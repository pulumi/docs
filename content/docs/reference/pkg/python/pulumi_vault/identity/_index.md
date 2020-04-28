---
title: Module identity
title_tag: Module identity | Package pulumi_vault | Python SDK
linktitle: identity
notitle: true
---

<div class="section" id="identity">
<h1>identity<a class="headerlink" href="#identity" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.identity"></span><dl class="class">
<dt id="pulumi_vault.identity.AwaitableGetEntityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">AwaitableGetEntityResult</code><span class="sig-paren">(</span><em class="sig-param">alias_id=None</em>, <em class="sig-param">alias_mount_accessor=None</em>, <em class="sig-param">alias_name=None</em>, <em class="sig-param">aliases=None</em>, <em class="sig-param">creation_time=None</em>, <em class="sig-param">data_json=None</em>, <em class="sig-param">direct_group_ids=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">entity_id=None</em>, <em class="sig-param">entity_name=None</em>, <em class="sig-param">group_ids=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">inherited_group_ids=None</em>, <em class="sig-param">last_update_time=None</em>, <em class="sig-param">merged_entity_ids=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">namespace_id=None</em>, <em class="sig-param">policies=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.AwaitableGetEntityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_vault.identity.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">alias_canonical_id=None</em>, <em class="sig-param">alias_creation_time=None</em>, <em class="sig-param">alias_id=None</em>, <em class="sig-param">alias_last_update_time=None</em>, <em class="sig-param">alias_merged_from_canonical_ids=None</em>, <em class="sig-param">alias_metadata=None</em>, <em class="sig-param">alias_mount_accessor=None</em>, <em class="sig-param">alias_mount_path=None</em>, <em class="sig-param">alias_mount_type=None</em>, <em class="sig-param">alias_name=None</em>, <em class="sig-param">creation_time=None</em>, <em class="sig-param">data_json=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">last_update_time=None</em>, <em class="sig-param">member_entity_ids=None</em>, <em class="sig-param">member_group_ids=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">modify_index=None</em>, <em class="sig-param">namespace_id=None</em>, <em class="sig-param">parent_group_ids=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_vault.identity.Entity">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">Entity</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">external_policies=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Entity" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Entity resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] disabled: True/false Is this entity currently disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>
:param pulumi.Input[bool] external_policies: <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, this resource will ignore any policies return from Vault or specified in the resource. You can use <code class="docutils literal notranslate"><span class="pre">identity.EntityPolicies</span></code> to manage policies for this entity in a decoupled manner.
:param pulumi.Input[dict] metadata: A Map of additional metadata to associate with the user.
:param pulumi.Input[str] name: Name of the identity entity to create.
:param pulumi.Input[list] policies: A list of policies to apply to the entity.</p>
<dl class="attribute">
<dt id="pulumi_vault.identity.Entity.disabled">
<code class="sig-name descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Entity.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>True/false Is this entity currently disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.Entity.external_policies">
<code class="sig-name descname">external_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Entity.external_policies" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">false</span></code> by default. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, this resource will ignore any policies return from Vault or specified in the resource. You can use <code class="docutils literal notranslate"><span class="pre">identity.EntityPolicies</span></code> to manage policies for this entity in a decoupled manner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.Entity.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Entity.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A Map of additional metadata to associate with the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.Entity.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Entity.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the identity entity to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.Entity.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Entity.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policies to apply to the entity.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.Entity.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">external_policies=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policies=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Entity.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Entity resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True/false Is this entity currently disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>external_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, this resource will ignore any policies return from Vault or specified in the resource. You can use <code class="docutils literal notranslate"><span class="pre">identity.EntityPolicies</span></code> to manage policies for this entity in a decoupled manner.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Map of additional metadata to associate with the user.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the identity entity to create.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of policies to apply to the entity.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.Entity.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Entity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.Entity.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Entity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.EntityAlias">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">EntityAlias</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">canonical_id=None</em>, <em class="sig-param">mount_accessor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.EntityAlias" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a EntityAlias resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] canonical_id: Entity ID to which this alias belongs to.
:param pulumi.Input[str] mount_accessor: Accessor of the mount to which the alias should belong to.
:param pulumi.Input[str] name: Name of the alias. Name should be the identifier of the client in the authentication source. For example, if the alias belongs to userpass backend, the name should be a valid username within userpass backend. If alias belongs to GitHub, it should be the GitHub username.</p>
<dl class="attribute">
<dt id="pulumi_vault.identity.EntityAlias.canonical_id">
<code class="sig-name descname">canonical_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.EntityAlias.canonical_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Entity ID to which this alias belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.EntityAlias.mount_accessor">
<code class="sig-name descname">mount_accessor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.EntityAlias.mount_accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>Accessor of the mount to which the alias should belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.EntityAlias.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.EntityAlias.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the alias. Name should be the identifier of the client in the authentication source. For example, if the alias belongs to userpass backend, the name should be a valid username within userpass backend. If alias belongs to GitHub, it should be the GitHub username.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.EntityAlias.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">canonical_id=None</em>, <em class="sig-param">mount_accessor=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.EntityAlias.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EntityAlias resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>canonical_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entity ID to which this alias belongs to.</p></li>
<li><p><strong>mount_accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Accessor of the mount to which the alias should belong to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the alias. Name should be the identifier of the client in the authentication source. For example, if the alias belongs to userpass backend, the name should be a valid username within userpass backend. If alias belongs to GitHub, it should be the GitHub username.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.EntityAlias.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.EntityAlias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.EntityAlias.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.EntityAlias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.EntityPolicies">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">EntityPolicies</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">entity_id=None</em>, <em class="sig-param">exclusive=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.EntityPolicies" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages policies for an Identity Entity for Vault. The <a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html">Identity secrets engine</a> is the identity management solution for Vault.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entity_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entity ID to assign policies to.</p></li>
<li><p><strong>exclusive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of policies to assign to the entity</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.identity.EntityPolicies.entity_id">
<code class="sig-name descname">entity_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.EntityPolicies.entity_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Entity ID to assign policies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.EntityPolicies.entity_name">
<code class="sig-name descname">entity_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.EntityPolicies.entity_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the entity that are assigned the policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.EntityPolicies.exclusive">
<code class="sig-name descname">exclusive</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.EntityPolicies.exclusive" title="Permalink to this definition">¶</a></dt>
<dd><p>Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.EntityPolicies.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.EntityPolicies.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to assign to the entity</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.EntityPolicies.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">entity_id=None</em>, <em class="sig-param">entity_name=None</em>, <em class="sig-param">exclusive=None</em>, <em class="sig-param">policies=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.EntityPolicies.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EntityPolicies resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>entity_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Entity ID to assign policies to.</p></li>
<li><p><strong>entity_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the entity that are assigned the policies.</p></li>
<li><p><strong>exclusive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of policies to assign to the entity</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.EntityPolicies.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.EntityPolicies.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.EntityPolicies.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.EntityPolicies.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.GetEntityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">GetEntityResult</code><span class="sig-paren">(</span><em class="sig-param">alias_id=None</em>, <em class="sig-param">alias_mount_accessor=None</em>, <em class="sig-param">alias_name=None</em>, <em class="sig-param">aliases=None</em>, <em class="sig-param">creation_time=None</em>, <em class="sig-param">data_json=None</em>, <em class="sig-param">direct_group_ids=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">entity_id=None</em>, <em class="sig-param">entity_name=None</em>, <em class="sig-param">group_ids=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">inherited_group_ids=None</em>, <em class="sig-param">last_update_time=None</em>, <em class="sig-param">merged_entity_ids=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">namespace_id=None</em>, <em class="sig-param">policies=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEntity.</p>
<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.aliases">
<code class="sig-name descname">aliases</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of entity alias. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.creation_time">
<code class="sig-name descname">creation_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Creation time of the Alias</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.data_json">
<code class="sig-name descname">data_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.data_json" title="Permalink to this definition">¶</a></dt>
<dd><p>A string containing the full data payload retrieved from
Vault, serialized in JSON format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.direct_group_ids">
<code class="sig-name descname">direct_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.direct_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Group IDs of which the entity is directly a member of</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.disabled">
<code class="sig-name descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the entity is disabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.group_ids">
<code class="sig-name descname">group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of all Group IDs of which the entity is a member of</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.inherited_group_ids">
<code class="sig-name descname">inherited_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.inherited_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of all Group IDs of which the entity is a member of transitively</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.last_update_time">
<code class="sig-name descname">last_update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.last_update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Last update time of the alias</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.merged_entity_ids">
<code class="sig-name descname">merged_entity_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.merged_entity_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Other entity IDs which is merged with this entity</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary metadata</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.namespace_id">
<code class="sig-name descname">namespace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Namespace of which the entity is part of</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetEntityResult.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetEntityResult.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies attached to the entity</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_vault.identity.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">alias_canonical_id=None</em>, <em class="sig-param">alias_creation_time=None</em>, <em class="sig-param">alias_id=None</em>, <em class="sig-param">alias_last_update_time=None</em>, <em class="sig-param">alias_merged_from_canonical_ids=None</em>, <em class="sig-param">alias_metadata=None</em>, <em class="sig-param">alias_mount_accessor=None</em>, <em class="sig-param">alias_mount_path=None</em>, <em class="sig-param">alias_mount_type=None</em>, <em class="sig-param">alias_name=None</em>, <em class="sig-param">creation_time=None</em>, <em class="sig-param">data_json=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">last_update_time=None</em>, <em class="sig-param">member_entity_ids=None</em>, <em class="sig-param">member_group_ids=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">modify_index=None</em>, <em class="sig-param">namespace_id=None</em>, <em class="sig-param">parent_group_ids=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.alias_canonical_id">
<code class="sig-name descname">alias_canonical_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.alias_canonical_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Canonical ID of the Alias</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.alias_creation_time">
<code class="sig-name descname">alias_creation_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.alias_creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Creation time of the Alias</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.alias_last_update_time">
<code class="sig-name descname">alias_last_update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.alias_last_update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Last update time of the alias</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.alias_merged_from_canonical_ids">
<code class="sig-name descname">alias_merged_from_canonical_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.alias_merged_from_canonical_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of canonical IDs merged with this alias</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.alias_metadata">
<code class="sig-name descname">alias_metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.alias_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary metadata</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.alias_mount_path">
<code class="sig-name descname">alias_mount_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.alias_mount_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Authentication mount path which this alias belongs to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.alias_mount_type">
<code class="sig-name descname">alias_mount_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.alias_mount_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Authentication mount type which this alias belongs to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.creation_time">
<code class="sig-name descname">creation_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.creation_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Creation timestamp of the group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.data_json">
<code class="sig-name descname">data_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.data_json" title="Permalink to this definition">¶</a></dt>
<dd><p>A string containing the full data payload retrieved from
Vault, serialized in JSON format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.last_update_time">
<code class="sig-name descname">last_update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.last_update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Last updated time of the group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.member_entity_ids">
<code class="sig-name descname">member_entity_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.member_entity_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Entity IDs which are members of this group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.member_group_ids">
<code class="sig-name descname">member_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.member_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Group IDs which are members of this group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary metadata</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.modify_index">
<code class="sig-name descname">modify_index</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.modify_index" title="Permalink to this definition">¶</a></dt>
<dd><p>Modify index of the group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.namespace_id">
<code class="sig-name descname">namespace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Namespace of which the group is part of</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.parent_group_ids">
<code class="sig-name descname">parent_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.parent_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Group IDs which are parents of this group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies attached to the group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GetGroupResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GetGroupResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of group</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_vault.identity.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">external_policies=None</em>, <em class="sig-param">member_entity_ids=None</em>, <em class="sig-param">member_group_ids=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Identity Group for Vault. The <a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html">Identity secrets engine</a> is the identity management solution for Vault.</p>
<p>A group can contain multiple entities as its members. A group can also have subgroups. Policies set on the group is granted to all members of the group. During request time, when the token’s entity ID is being evaluated for the policies that it has access to; along with the policies on the entity itself, policies that are inherited due to group memberships are also granted.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>external_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, this resource will ignore any policies return from Vault or specified in the resource. You can use <code class="docutils literal notranslate"><span class="pre">identity.GroupPolicies</span></code> to manage policies for this group in a decoupled manner.</p></li>
<li><p><strong>member_entity_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Entity IDs to be assigned as group members. Not allowed on <code class="docutils literal notranslate"><span class="pre">external</span></code> groups.</p></li>
<li><p><strong>member_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Group IDs to be assigned as group members.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Map of additional metadata to associate with the group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the identity group to create.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of policies to apply to the group.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the group, internal or external. Defaults to <code class="docutils literal notranslate"><span class="pre">internal</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.identity.Group.external_policies">
<code class="sig-name descname">external_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Group.external_policies" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">false</span></code> by default. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, this resource will ignore any policies return from Vault or specified in the resource. You can use <code class="docutils literal notranslate"><span class="pre">identity.GroupPolicies</span></code> to manage policies for this group in a decoupled manner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.Group.member_entity_ids">
<code class="sig-name descname">member_entity_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Group.member_entity_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Entity IDs to be assigned as group members. Not allowed on <code class="docutils literal notranslate"><span class="pre">external</span></code> groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.Group.member_group_ids">
<code class="sig-name descname">member_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Group.member_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Group IDs to be assigned as group members.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.Group.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Group.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A Map of additional metadata to associate with the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the identity group to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.Group.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Group.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policies to apply to the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.Group.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Group.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the group, internal or external. Defaults to <code class="docutils literal notranslate"><span class="pre">internal</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">external_policies=None</em>, <em class="sig-param">member_entity_ids=None</em>, <em class="sig-param">member_group_ids=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>external_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, this resource will ignore any policies return from Vault or specified in the resource. You can use <code class="docutils literal notranslate"><span class="pre">identity.GroupPolicies</span></code> to manage policies for this group in a decoupled manner.</p></li>
<li><p><strong>member_entity_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Entity IDs to be assigned as group members. Not allowed on <code class="docutils literal notranslate"><span class="pre">external</span></code> groups.</p></li>
<li><p><strong>member_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Group IDs to be assigned as group members.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Map of additional metadata to associate with the group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the identity group to create.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of policies to apply to the group.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the group, internal or external. Defaults to <code class="docutils literal notranslate"><span class="pre">internal</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.GroupAlias">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">GroupAlias</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">canonical_id=None</em>, <em class="sig-param">mount_accessor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.GroupAlias" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Identity Group Alias for Vault. The <a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html">Identity secrets engine</a> is the identity management solution for Vault.</p>
<p>Group aliases allows entity membership in external groups to be managed semi-automatically. External group serves as a mapping to a group that is outside of the identity store. External groups can have one (and only one) alias. This alias should map to a notion of group that is outside of the identity store. For example, groups in LDAP, and teams in GitHub. A username in LDAP, belonging to a group in LDAP, can get its entity ID added as a member of a group in Vault automatically during logins and token renewals. This works only if the group in Vault is an external group and has an alias that maps to the group in LDAP. If the user is removed from the group in LDAP, that change gets reflected in Vault only upon the subsequent login or renewal operation.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>canonical_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the group to which this is an alias.</p></li>
<li><p><strong>mount_accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mount accessor of the authentication backend to which this alias belongs to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the group alias to create.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.identity.GroupAlias.canonical_id">
<code class="sig-name descname">canonical_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GroupAlias.canonical_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the group to which this is an alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GroupAlias.mount_accessor">
<code class="sig-name descname">mount_accessor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GroupAlias.mount_accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>Mount accessor of the authentication backend to which this alias belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GroupAlias.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GroupAlias.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the group alias to create.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.GroupAlias.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">canonical_id=None</em>, <em class="sig-param">mount_accessor=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.GroupAlias.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupAlias resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>canonical_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the group to which this is an alias.</p></li>
<li><p><strong>mount_accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mount accessor of the authentication backend to which this alias belongs to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the group alias to create.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.GroupAlias.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.GroupAlias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.GroupAlias.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.GroupAlias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.GroupPolicies">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">GroupPolicies</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">exclusive=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.GroupPolicies" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages policies for an Identity Group for Vault. The <a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html">Identity secrets engine</a> is the identity management solution for Vault.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>exclusive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Group ID to assign policies to.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of policies to assign to the group</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.identity.GroupPolicies.exclusive">
<code class="sig-name descname">exclusive</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GroupPolicies.exclusive" title="Permalink to this definition">¶</a></dt>
<dd><p>Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GroupPolicies.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GroupPolicies.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Group ID to assign policies to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GroupPolicies.group_name">
<code class="sig-name descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GroupPolicies.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the group that are assigned the policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.GroupPolicies.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.GroupPolicies.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to assign to the group</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.GroupPolicies.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">exclusive=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">policies=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.GroupPolicies.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupPolicies resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>exclusive</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Group ID to assign policies to.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group that are assigned the policies.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of policies to assign to the group</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.GroupPolicies.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.GroupPolicies.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.GroupPolicies.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.GroupPolicies.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.Oidc">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">Oidc</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Oidc" title="Permalink to this definition">¶</a></dt>
<dd><p>Configure the <a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html#identity-tokens">Identity Tokens Backend</a>.</p>
<p>The Identity secrets engine is the identity management solution for Vault. It internally maintains
the clients who are recognized by Vault.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Each Vault server may only have one Identity Tokens Backend configuration. Multiple configurations of the resource against the same Vault server will cause a perpetual difference.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Issuer URL to be used in the iss claim of the token. If not set, Vault’s
<code class="docutils literal notranslate"><span class="pre">api_addr</span></code> will be used. The issuer is a case sensitive URL using the https scheme that contains
scheme, host, and optionally, port number and path components, but no query or fragment
components.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.identity.Oidc.issuer">
<code class="sig-name descname">issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.Oidc.issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>Issuer URL to be used in the iss claim of the token. If not set, Vault’s
<code class="docutils literal notranslate"><span class="pre">api_addr</span></code> will be used. The issuer is a case sensitive URL using the https scheme that contains
scheme, host, and optionally, port number and path components, but no query or fragment
components.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.Oidc.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">issuer=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Oidc.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Oidc resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Issuer URL to be used in the iss claim of the token. If not set, Vault’s
<code class="docutils literal notranslate"><span class="pre">api_addr</span></code> will be used. The issuer is a case sensitive URL using the https scheme that contains
scheme, host, and optionally, port number and path components, but no query or fragment
components.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.Oidc.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Oidc.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.Oidc.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.Oidc.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.OidcKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">OidcKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">allowed_client_ids=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rotation_period=None</em>, <em class="sig-param">verification_ttl=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a OidcKey resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] algorithm: Signing algorithm to use. Signing algorithm to use.</p>
<blockquote>
<div><p>Allowed values are: RS256 (default), RS384, RS512, ES256, ES384, ES512, EdDSA.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>allowed_client_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of role client ids allowed to use this key for signing. If empty, no roles are allowed. If “*”, all roles are
allowed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the OIDC Key to create.</p></li>
<li><p><strong>rotation_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often to generate a new signing key in number of seconds</p></li>
<li><p><strong>verification_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – “Controls how long the public portion of a signing key will be
available for verification after being rotated in seconds.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.identity.OidcKey.algorithm">
<code class="sig-name descname">algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcKey.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Signing algorithm to use. Signing algorithm to use.
Allowed values are: RS256 (default), RS384, RS512, ES256, ES384, ES512, EdDSA.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.OidcKey.allowed_client_ids">
<code class="sig-name descname">allowed_client_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcKey.allowed_client_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of role client ids allowed to use this key for signing. If empty, no roles are allowed. If “*”, all roles are
allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.OidcKey.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the OIDC Key to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.OidcKey.rotation_period">
<code class="sig-name descname">rotation_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcKey.rotation_period" title="Permalink to this definition">¶</a></dt>
<dd><p>How often to generate a new signing key in number of seconds</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.OidcKey.verification_ttl">
<code class="sig-name descname">verification_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcKey.verification_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>“Controls how long the public portion of a signing key will be
available for verification after being rotated in seconds.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.OidcKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">algorithm=None</em>, <em class="sig-param">allowed_client_ids=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rotation_period=None</em>, <em class="sig-param">verification_ttl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OidcKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signing algorithm to use. Signing algorithm to use.
Allowed values are: RS256 (default), RS384, RS512, ES256, ES384, ES512, EdDSA.</p></li>
<li><p><strong>allowed_client_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of role client ids allowed to use this key for signing. If empty, no roles are allowed. If “*”, all roles are
allowed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the OIDC Key to create.</p></li>
<li><p><strong>rotation_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often to generate a new signing key in number of seconds</p></li>
<li><p><strong>verification_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – “Controls how long the public portion of a signing key will be
available for verification after being rotated in seconds.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.OidcKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.OidcKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.OidcKeyAllowedClientID">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">OidcKeyAllowedClientID</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_client_id=None</em>, <em class="sig-param">key_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcKeyAllowedClientID" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a OidcKeyAllowedClientID resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] allowed_client_id: Client ID to allow usage with the OIDC named key
:param pulumi.Input[str] key_name: Name of the OIDC Key allow the Client ID.</p>
<dl class="attribute">
<dt id="pulumi_vault.identity.OidcKeyAllowedClientID.allowed_client_id">
<code class="sig-name descname">allowed_client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcKeyAllowedClientID.allowed_client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client ID to allow usage with the OIDC named key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.OidcKeyAllowedClientID.key_name">
<code class="sig-name descname">key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcKeyAllowedClientID.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the OIDC Key allow the Client ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.OidcKeyAllowedClientID.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_client_id=None</em>, <em class="sig-param">key_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcKeyAllowedClientID.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OidcKeyAllowedClientID resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID to allow usage with the OIDC named key</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the OIDC Key allow the Client ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.OidcKeyAllowedClientID.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcKeyAllowedClientID.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.OidcKeyAllowedClientID.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcKeyAllowedClientID.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.OidcRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">OidcRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">template=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a OidcRole resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] key: A configured named key, the key must already exist</p>
<blockquote>
<div><p>before tokens can be issued.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the OIDC Role to create.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The template string to use for generating tokens. This may be in
string-ified JSON or base64 format. See the
<a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html#token-contents-and-templates">documentation</a>
for the template format.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – TTL of the tokens generated against the role in number of seconds.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.identity.OidcRole.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcRole.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The value that will be included in the <code class="docutils literal notranslate"><span class="pre">aud</span></code> field of all the OIDC identity
tokens issued by this role</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.OidcRole.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcRole.key" title="Permalink to this definition">¶</a></dt>
<dd><p>A configured named key, the key must already exist
before tokens can be issued.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.OidcRole.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the OIDC Role to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.OidcRole.template">
<code class="sig-name descname">template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcRole.template" title="Permalink to this definition">¶</a></dt>
<dd><p>The template string to use for generating tokens. This may be in
string-ified JSON or base64 format. See the
<a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html#token-contents-and-templates">documentation</a>
for the template format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.identity.OidcRole.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.identity.OidcRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>TTL of the tokens generated against the role in number of seconds.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.OidcRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">template=None</em>, <em class="sig-param">ttl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OidcRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value that will be included in the <code class="docutils literal notranslate"><span class="pre">aud</span></code> field of all the OIDC identity
tokens issued by this role</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A configured named key, the key must already exist
before tokens can be issued.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the OIDC Role to create.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The template string to use for generating tokens. This may be in
string-ified JSON or base64 format. See the
<a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html#token-contents-and-templates">documentation</a>
for the template format.</p>
</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – TTL of the tokens generated against the role in number of seconds.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.identity.OidcRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.OidcRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.OidcRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.identity.get_entity">
<code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">get_entity</code><span class="sig-paren">(</span><em class="sig-param">alias_id=None</em>, <em class="sig-param">alias_mount_accessor=None</em>, <em class="sig-param">alias_name=None</em>, <em class="sig-param">entity_id=None</em>, <em class="sig-param">entity_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.get_entity" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>alias_id</strong> (<em>str</em>) – ID of the alias.</p></li>
<li><p><strong>alias_mount_accessor</strong> (<em>str</em>) – Accessor of the mount to which the alias belongs to.
This should be supplied in conjunction with <code class="docutils literal notranslate"><span class="pre">alias_name</span></code>.</p></li>
<li><p><strong>alias_name</strong> (<em>str</em>) – Name of the alias. This should be supplied in conjunction with
<code class="docutils literal notranslate"><span class="pre">alias_mount_accessor</span></code>.</p></li>
<li><p><strong>entity_id</strong> (<em>str</em>) – ID of the entity.</p></li>
<li><p><strong>entity_name</strong> (<em>str</em>) – Name of the entity.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_vault.identity.get_group">
<code class="sig-prename descclassname">pulumi_vault.identity.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param">alias_id=None</em>, <em class="sig-param">alias_mount_accessor=None</em>, <em class="sig-param">alias_name=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.identity.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>alias_id</strong> (<em>str</em>) – ID of the alias.</p></li>
<li><p><strong>alias_mount_accessor</strong> (<em>str</em>) – Accessor of the mount to which the alias belongs to.
This should be supplied in conjunction with <code class="docutils literal notranslate"><span class="pre">alias_name</span></code>.</p></li>
<li><p><strong>alias_name</strong> (<em>str</em>) – Name of the alias. This should be supplied in conjunction with
<code class="docutils literal notranslate"><span class="pre">alias_mount_accessor</span></code>.</p></li>
<li><p><strong>group_id</strong> (<em>str</em>) – ID of the group.</p></li>
<li><p><strong>group_name</strong> (<em>str</em>) – Name of the group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
