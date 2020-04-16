---
title: Module authorization
title_tag: Module authorization | Package pulumi_azure | Python SDK
linktitle: authorization
notitle: true
---

<div class="section" id="authorization">
<h1>authorization<a class="headerlink" href="#authorization" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.authorization"></span><dl class="class">
<dt id="pulumi_azure.authorization.Assignment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.authorization.</code><code class="sig-name descname">Assignment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">principal_id=None</em>, <em class="sig-param">role_definition_id=None</em>, <em class="sig-param">role_definition_name=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">skip_service_principal_aad_check=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.Assignment" title="Permalink to this definition">¶</a></dt>
<dd><p>Assigns a given Principal (User or Application) to a given Role.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.</p></li>
<li><p><strong>principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Principal (User, Group, Service Principal, or Application) to assign the Role Definition to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>role_definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_name</span></code>.</p></li>
<li><p><strong>role_definition_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_id</span></code>.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope at which the Role Assignment applies to, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>, or <code class="docutils literal notranslate"><span class="pre">/providers/Microsoft.Management/managementGroups/myMG</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>skip_service_principal_aad_check</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the <code class="docutils literal notranslate"><span class="pre">principal_id</span></code> is a newly provisioned <code class="docutils literal notranslate"><span class="pre">Service</span> <span class="pre">Principal</span></code> set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> to skip the <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> check which may fail due to replication lag. This argument is only valid if the <code class="docutils literal notranslate"><span class="pre">principal_id</span></code> is a <code class="docutils literal notranslate"><span class="pre">Service</span> <span class="pre">Principal</span></code> identity. If it is not a <code class="docutils literal notranslate"><span class="pre">Service</span> <span class="pre">Principal</span></code> identity it will cause the role assignment to fail. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.authorization.Assignment.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.Assignment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.Assignment.principal_id">
<code class="sig-name descname">principal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.Assignment.principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Principal (User, Group, Service Principal, or Application) to assign the Role Definition to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.Assignment.principal_type">
<code class="sig-name descname">principal_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.Assignment.principal_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the <code class="docutils literal notranslate"><span class="pre">principal_id</span></code>, e.g. User, Group, Service Principal, Application, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.Assignment.role_definition_id">
<code class="sig-name descname">role_definition_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.Assignment.role_definition_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.Assignment.role_definition_name">
<code class="sig-name descname">role_definition_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.Assignment.role_definition_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_id</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.Assignment.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.Assignment.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The scope at which the Role Assignment applies to, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>, or <code class="docutils literal notranslate"><span class="pre">/providers/Microsoft.Management/managementGroups/myMG</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.Assignment.skip_service_principal_aad_check">
<code class="sig-name descname">skip_service_principal_aad_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.Assignment.skip_service_principal_aad_check" title="Permalink to this definition">¶</a></dt>
<dd><p>If the <code class="docutils literal notranslate"><span class="pre">principal_id</span></code> is a newly provisioned <code class="docutils literal notranslate"><span class="pre">Service</span> <span class="pre">Principal</span></code> set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> to skip the <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> check which may fail due to replication lag. This argument is only valid if the <code class="docutils literal notranslate"><span class="pre">principal_id</span></code> is a <code class="docutils literal notranslate"><span class="pre">Service</span> <span class="pre">Principal</span></code> identity. If it is not a <code class="docutils literal notranslate"><span class="pre">Service</span> <span class="pre">Principal</span></code> identity it will cause the role assignment to fail. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.authorization.Assignment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">principal_id=None</em>, <em class="sig-param">principal_type=None</em>, <em class="sig-param">role_definition_id=None</em>, <em class="sig-param">role_definition_name=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">skip_service_principal_aad_check=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.Assignment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Assignment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.</p></li>
<li><p><strong>principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Principal (User, Group, Service Principal, or Application) to assign the Role Definition to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>principal_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the <code class="docutils literal notranslate"><span class="pre">principal_id</span></code>, e.g. User, Group, Service Principal, Application, etc.</p></li>
<li><p><strong>role_definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_name</span></code>.</p></li>
<li><p><strong>role_definition_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with <code class="docutils literal notranslate"><span class="pre">role_definition_id</span></code>.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope at which the Role Assignment applies to, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>, or <code class="docutils literal notranslate"><span class="pre">/providers/Microsoft.Management/managementGroups/myMG</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>skip_service_principal_aad_check</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the <code class="docutils literal notranslate"><span class="pre">principal_id</span></code> is a newly provisioned <code class="docutils literal notranslate"><span class="pre">Service</span> <span class="pre">Principal</span></code> set this value to <code class="docutils literal notranslate"><span class="pre">true</span></code> to skip the <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span></code> check which may fail due to replication lag. This argument is only valid if the <code class="docutils literal notranslate"><span class="pre">principal_id</span></code> is a <code class="docutils literal notranslate"><span class="pre">Service</span> <span class="pre">Principal</span></code> identity. If it is not a <code class="docutils literal notranslate"><span class="pre">Service</span> <span class="pre">Principal</span></code> identity it will cause the role assignment to fail. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.authorization.Assignment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.Assignment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.authorization.Assignment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.Assignment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.authorization.AwaitableGetRoleDefinitionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.authorization.</code><code class="sig-name descname">AwaitableGetRoleDefinitionResult</code><span class="sig-paren">(</span><em class="sig-param">assignable_scopes=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">role_definition_id=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.AwaitableGetRoleDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.authorization.AwaitableGetUserAssignedIdentityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.authorization.</code><code class="sig-name descname">AwaitableGetUserAssignedIdentityResult</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">principal_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.AwaitableGetUserAssignedIdentityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.authorization.GetRoleDefinitionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.authorization.</code><code class="sig-name descname">GetRoleDefinitionResult</code><span class="sig-paren">(</span><em class="sig-param">assignable_scopes=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">role_definition_id=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.GetRoleDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRoleDefinition.</p>
<dl class="attribute">
<dt id="pulumi_azure.authorization.GetRoleDefinitionResult.assignable_scopes">
<code class="sig-name descname">assignable_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.GetRoleDefinitionResult.assignable_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more assignable scopes for this Role Definition, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.GetRoleDefinitionResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.GetRoleDefinitionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>the Description of the built-in Role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.GetRoleDefinitionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.GetRoleDefinitionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.GetRoleDefinitionResult.permissions">
<code class="sig-name descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.GetRoleDefinitionResult.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>a <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.GetRoleDefinitionResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.GetRoleDefinitionResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>the Type of the Role.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.authorization.GetUserAssignedIdentityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.authorization.</code><code class="sig-name descname">GetUserAssignedIdentityResult</code><span class="sig-paren">(</span><em class="sig-param">client_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">principal_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.GetUserAssignedIdentityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUserAssignedIdentity.</p>
<dl class="attribute">
<dt id="pulumi_azure.authorization.GetUserAssignedIdentityResult.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.GetUserAssignedIdentityResult.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client ID of the User Assigned Identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.GetUserAssignedIdentityResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.GetUserAssignedIdentityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.GetUserAssignedIdentityResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.GetUserAssignedIdentityResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the User Assigned Identity exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.GetUserAssignedIdentityResult.principal_id">
<code class="sig-name descname">principal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.GetUserAssignedIdentityResult.principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Principal ID of the User Assigned Identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.GetUserAssignedIdentityResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.GetUserAssignedIdentityResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the User Assigned Identity.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.authorization.RoleDefinition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.authorization.</code><code class="sig-name descname">RoleDefinition</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">assignable_scopes=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">role_definition_id=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.RoleDefinition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a custom Role Definition, used to assign Roles to Users/Principals. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/role-definitions">‘Understand role definitions’</a> in the Azure documentation for more details.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignable_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more assignable scopes for this Role Definition, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the Role Definition.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Role Definition. Changing this forces a new resource to be created.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as defined below.</p></li>
<li><p><strong>role_definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope at which the Role Definition applies too, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>. It is recommended to use the first entry of the <code class="docutils literal notranslate"><span class="pre">assignable_scopes</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more Allowed Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Resources/subscriptions/resourceGroups/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more Allowed Data Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more Disallowed Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Resources/subscriptions/resourceGroups/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notDataActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more Disallowed Data Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Resources/subscriptions/resourceGroups/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.authorization.RoleDefinition.assignable_scopes">
<code class="sig-name descname">assignable_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.RoleDefinition.assignable_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more assignable scopes for this Role Definition, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.RoleDefinition.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.RoleDefinition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the Role Definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.RoleDefinition.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.RoleDefinition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Role Definition. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.RoleDefinition.permissions">
<code class="sig-name descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.RoleDefinition.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more Allowed Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Resources/subscriptions/resourceGroups/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more Allowed Data Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more Disallowed Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Resources/subscriptions/resourceGroups/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notDataActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more Disallowed Data Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Resources/subscriptions/resourceGroups/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.RoleDefinition.role_definition_id">
<code class="sig-name descname">role_definition_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.RoleDefinition.role_definition_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.RoleDefinition.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.RoleDefinition.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The scope at which the Role Definition applies too, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>. It is recommended to use the first entry of the <code class="docutils literal notranslate"><span class="pre">assignable_scopes</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.authorization.RoleDefinition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">assignable_scopes=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">role_definition_id=None</em>, <em class="sig-param">scope=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.RoleDefinition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RoleDefinition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignable_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more assignable scopes for this Role Definition, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the Role Definition.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Role Definition. Changing this forces a new resource to be created.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">permissions</span></code> block as defined below.</p></li>
<li><p><strong>role_definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope at which the Role Definition applies too, such as <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333</span></code>, <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup</span></code>, or <code class="docutils literal notranslate"><span class="pre">/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM</span></code>. It is recommended to use the first entry of the <code class="docutils literal notranslate"><span class="pre">assignable_scopes</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more Allowed Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Resources/subscriptions/resourceGroups/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more Allowed Data Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more Disallowed Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Resources/subscriptions/resourceGroups/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notDataActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more Disallowed Data Actions, such as <code class="docutils literal notranslate"><span class="pre">*</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Resources/subscriptions/resourceGroups/read</span></code>. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations">‘Azure Resource Manager resource provider operations’</a> for details.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.authorization.RoleDefinition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.RoleDefinition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.authorization.RoleDefinition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.RoleDefinition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.authorization.UserAssignedIdentity">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.authorization.</code><code class="sig-name descname">UserAssignedIdentity</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.UserAssignedIdentity" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a user assigned identity.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the user assigned identity is
created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user assigned identity. Changing this forces a
new identity to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the user assigned identity.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.authorization.UserAssignedIdentity.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.UserAssignedIdentity.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client ID associated with the user assigned identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.UserAssignedIdentity.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.UserAssignedIdentity.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the user assigned identity is
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.UserAssignedIdentity.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.UserAssignedIdentity.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user assigned identity. Changing this forces a
new identity to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.UserAssignedIdentity.principal_id">
<code class="sig-name descname">principal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.UserAssignedIdentity.principal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Service Principal ID associated with the user assigned identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.UserAssignedIdentity.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.UserAssignedIdentity.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the user assigned identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.authorization.UserAssignedIdentity.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.authorization.UserAssignedIdentity.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.authorization.UserAssignedIdentity.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">principal_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.UserAssignedIdentity.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserAssignedIdentity resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client ID associated with the user assigned identity.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the user assigned identity is
created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user assigned identity. Changing this forces a
new identity to be created.</p></li>
<li><p><strong>principal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service Principal ID associated with the user assigned identity.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the user assigned identity.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.authorization.UserAssignedIdentity.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.UserAssignedIdentity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.authorization.UserAssignedIdentity.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.UserAssignedIdentity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.authorization.get_role_definition">
<code class="sig-prename descclassname">pulumi_azure.authorization.</code><code class="sig-name descname">get_role_definition</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">role_definition_id=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.get_role_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Role Definition.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the Name of either a built-in or custom Role Definition.</p></li>
<li><p><strong>role_definition_id</strong> (<em>str</em>) – Specifies the ID of the Role Definition as a UUID/GUID.</p></li>
<li><p><strong>scope</strong> (<em>str</em>) – Specifies the Scope at which the Custom Role Definition exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.authorization.get_user_assigned_identity">
<code class="sig-prename descclassname">pulumi_azure.authorization.</code><code class="sig-name descname">get_user_assigned_identity</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.authorization.get_user_assigned_identity" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing User Assigned Identity.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the User Assigned Identity.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the User Assigned Identity exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
