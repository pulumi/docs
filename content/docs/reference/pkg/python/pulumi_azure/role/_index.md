---
title: Module role
---

<div class="section" id="role">
<h1>role<a class="headerlink" href="#role" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.role"></span><dl class="class">
<dt id="pulumi_azure.role.Assignment">
<em class="property">class </em><code class="descclassname">pulumi_azure.role.</code><code class="descname">Assignment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>principal_id=None</em>, <em>role_definition_id=None</em>, <em>role_definition_name=None</em>, <em>scope=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.Assignment" title="Permalink to this definition">¶</a></dt>
<dd><p>Assigns a given Principal (User or Application) to a given Role.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.</li>
<li><strong>principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Principal (User, Group, Service Principal, or Application) to assign the Role Definition to. Changing this forces a new resource to be created.</li>
<li><strong>role_definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_name</span></code>.</li>
<li><strong>role_definition_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_id</span></code>.</li>
<li><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope at which the Role Assignment applies too, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/role_assignment.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/role_assignment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.role.Assignment.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Assignment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.Assignment.principal_id">
<code class="descname">principal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Assignment.principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Principal (User, Group, Service Principal, or Application) to assign the Role Definition to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.Assignment.role_definition_id">
<code class="descname">role_definition_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Assignment.role_definition_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.Assignment.role_definition_name">
<code class="descname">role_definition_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Assignment.role_definition_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_id</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.Assignment.scope">
<code class="descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Assignment.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The scope at which the Role Assignment applies too, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.role.Assignment.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>name=None</em>, <em>principal_id=None</em>, <em>role_definition_id=None</em>, <em>role_definition_name=None</em>, <em>scope=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.Assignment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Assignment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.
:param pulumi.Input[str] principal_id: The ID of the Principal (User, Group, Service Principal, or Application) to assign the Role Definition to. Changing this forces a new resource to be created. 
:param pulumi.Input[str] role_definition_id: The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_name</span></code>.
:param pulumi.Input[str] role_definition_name: The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_id</span></code>.
:param pulumi.Input[str] scope: The scope at which the Role Assignment applies too, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>. Changing this forces a new resource to be created.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/role_assignment.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/role_assignment.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.role.Assignment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.Assignment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.role.Assignment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.Assignment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.role.AwaitableGetBuiltinRoleDefinitionResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.role.</code><code class="descname">AwaitableGetBuiltinRoleDefinitionResult</code><span class="sig-paren">(</span><em>assignable_scopes=None</em>, <em>description=None</em>, <em>name=None</em>, <em>permissions=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.AwaitableGetBuiltinRoleDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.role.AwaitableGetRoleDefinitionResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.role.</code><code class="descname">AwaitableGetRoleDefinitionResult</code><span class="sig-paren">(</span><em>assignable_scopes=None</em>, <em>description=None</em>, <em>name=None</em>, <em>permissions=None</em>, <em>role_definition_id=None</em>, <em>scope=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.AwaitableGetRoleDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.role.Definition">
<em class="property">class </em><code class="descclassname">pulumi_azure.role.</code><code class="descname">Definition</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>assignable_scopes=None</em>, <em>description=None</em>, <em>name=None</em>, <em>permissions=None</em>, <em>role_definition_id=None</em>, <em>scope=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.Definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a custom Role Definition, used to assign Roles to Users/Principals. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/role-definitions">‘Understand role definitions’</a> in the Azure documentation for more details.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>assignable_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more assignable scopes for this Role Definition, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the Role Definition.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Role Definition. Changing this forces a new resource to be created.</li>
<li><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as defined below.</li>
<li><strong>role_definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.</li>
<li><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope at which the Role Definition applies too, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/role_definition.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/role_definition.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.role.Definition.assignable_scopes">
<code class="descname">assignable_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Definition.assignable_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more assignable scopes for this Role Definition, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.Definition.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Definition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the Role Definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.Definition.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Definition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Role Definition. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.Definition.permissions">
<code class="descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Definition.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.Definition.role_definition_id">
<code class="descname">role_definition_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Definition.role_definition_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.Definition.scope">
<code class="descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.Definition.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The scope at which the Role Definition applies too, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.role.Definition.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>assignable_scopes=None</em>, <em>description=None</em>, <em>name=None</em>, <em>permissions=None</em>, <em>role_definition_id=None</em>, <em>scope=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.Definition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Definition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] assignable_scopes: One or more assignable scopes for this Role Definition, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>.
:param pulumi.Input[str] description: A description of the Role Definition.
:param pulumi.Input[str] name: The name of the Role Definition. Changing this forces a new resource to be created.
:param pulumi.Input[list] permissions: A <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as defined below.
:param pulumi.Input[str] role_definition_id: A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.
:param pulumi.Input[str] scope: The scope at which the Role Definition applies too, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>. Changing this forces a new resource to be created.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/role_definition.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/role_definition.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.role.Definition.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.Definition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.role.Definition.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.Definition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.role.GetBuiltinRoleDefinitionResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.role.</code><code class="descname">GetBuiltinRoleDefinitionResult</code><span class="sig-paren">(</span><em>assignable_scopes=None</em>, <em>description=None</em>, <em>name=None</em>, <em>permissions=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.GetBuiltinRoleDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBuiltinRoleDefinition.</p>
<dl class="attribute">
<dt id="pulumi_azure.role.GetBuiltinRoleDefinitionResult.assignable_scopes">
<code class="descname">assignable_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.GetBuiltinRoleDefinitionResult.assignable_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more assignable scopes for this Role Definition, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.GetBuiltinRoleDefinitionResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.GetBuiltinRoleDefinitionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>the Description of the built-in Role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.GetBuiltinRoleDefinitionResult.permissions">
<code class="descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.GetBuiltinRoleDefinitionResult.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>a <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.GetBuiltinRoleDefinitionResult.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.GetBuiltinRoleDefinitionResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>the Type of the Role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.GetBuiltinRoleDefinitionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.GetBuiltinRoleDefinitionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.role.GetRoleDefinitionResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.role.</code><code class="descname">GetRoleDefinitionResult</code><span class="sig-paren">(</span><em>assignable_scopes=None</em>, <em>description=None</em>, <em>name=None</em>, <em>permissions=None</em>, <em>role_definition_id=None</em>, <em>scope=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.GetRoleDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRoleDefinition.</p>
<dl class="attribute">
<dt id="pulumi_azure.role.GetRoleDefinitionResult.assignable_scopes">
<code class="descname">assignable_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.GetRoleDefinitionResult.assignable_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more assignable scopes for this Role Definition, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.GetRoleDefinitionResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.GetRoleDefinitionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>the Description of the built-in Role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.GetRoleDefinitionResult.permissions">
<code class="descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.GetRoleDefinitionResult.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>a <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.GetRoleDefinitionResult.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.GetRoleDefinitionResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>the Type of the Role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.role.GetRoleDefinitionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.role.GetRoleDefinitionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.role.get_builtin_role_definition">
<code class="descclassname">pulumi_azure.role.</code><code class="descname">get_builtin_role_definition</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.get_builtin_role_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a built-in Role Definition. To access information about a custom Role Definition, please see the <code class="docutils literal notranslate"><span class="pre">role.Definition</span></code> data source instead.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The this datasource has been deprecated in favour of <code class="docutils literal notranslate"><span class="pre">role.Definition</span></code> that now can look up role definitions by name. As such this data source will be removed in version 2.0 of the AzureRM Provider.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/builtin_role_definition.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/builtin_role_definition.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.role.get_role_definition">
<code class="descclassname">pulumi_azure.role.</code><code class="descname">get_role_definition</code><span class="sig-paren">(</span><em>name=None</em>, <em>role_definition_id=None</em>, <em>scope=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.role.get_role_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Role Definition.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/role_definition.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/role_definition.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
