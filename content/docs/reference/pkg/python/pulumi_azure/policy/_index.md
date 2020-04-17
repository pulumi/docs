---
title: Module policy
title_tag: Module policy | Package pulumi_azure | Python SDK
linktitle: policy
notitle: true
---

<div class="section" id="policy">
<h1>policy<a class="headerlink" href="#policy" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.policy"></span><dl class="class">
<dt id="pulumi_azure.policy.Assignment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.policy.</code><code class="sig-name descname">Assignment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">not_scopes=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">policy_definition_id=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Assignment" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the specified Policy Definition at the specified Scope. Also, Policy Set Definitions are supported.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description to use for this Policy Assignment. Changing this forces a new resource to be created.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly display name to use for this Policy Assignment. Changing this forces a new resource to be created.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where this policy assignment should exist. This is required when an Identity is assigned. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Policy Assignment. Changing this forces a new resource to be created.</p></li>
<li><p><strong>not_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the Policy Assignment’s excluded scopes. The list must contain Resource IDs (such as Subscriptions e.g. <code class="docutils literal notranslate"><span class="pre">/subscriptions/00000000-0000-0000-000000000000</span></code> or Resource Groups e.g.<code class="docutils literal notranslate"><span class="pre">/subscriptions/00000000-0000-0000-000000000000/resourceGroups/myResourceGroup</span></code>).</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parameters for the policy definition. This field is a JSON object that maps to the Parameters field from the Policy Definition. Changing this forces a new resource to be created.</p></li>
<li><p><strong>policy_definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Policy Definition to be applied at the specified Scope.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID of this Policy Assignment if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID of this Policy Assignment if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Managed Service Identity Type of this Policy Assignment. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), or <code class="docutils literal notranslate"><span class="pre">None</span></code> (no use of a Managed Service Identity).</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description to use for this Policy Assignment. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly display name to use for this Policy Assignment. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Principal ID of this Policy Assignment if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Tenant ID of this Policy Assignment if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Managed Service Identity Type of this Policy Assignment. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), or <code class="docutils literal notranslate"><span class="pre">None</span></code> (no use of a Managed Service Identity).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where this policy assignment should exist. This is required when an Identity is assigned. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Policy Assignment. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.not_scopes">
<code class="sig-name descname">not_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.not_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Policy Assignment’s excluded scopes. The list must contain Resource IDs (such as Subscriptions e.g. <code class="docutils literal notranslate"><span class="pre">/subscriptions/00000000-0000-0000-000000000000</span></code> or Resource Groups e.g.<code class="docutils literal notranslate"><span class="pre">/subscriptions/00000000-0000-0000-000000000000/resourceGroups/myResourceGroup</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters for the policy definition. This field is a JSON object that maps to the Parameters field from the Policy Definition. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.policy_definition_id">
<code class="sig-name descname">policy_definition_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.policy_definition_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Policy Definition to be applied at the specified Scope.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.Assignment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">not_scopes=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">policy_definition_id=None</em>, <em class="sig-param">scope=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Assignment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Assignment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description to use for this Policy Assignment. Changing this forces a new resource to be created.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly display name to use for this Policy Assignment. Changing this forces a new resource to be created.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where this policy assignment should exist. This is required when an Identity is assigned. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Policy Assignment. Changing this forces a new resource to be created.</p></li>
<li><p><strong>not_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the Policy Assignment’s excluded scopes. The list must contain Resource IDs (such as Subscriptions e.g. <code class="docutils literal notranslate"><span class="pre">/subscriptions/00000000-0000-0000-000000000000</span></code> or Resource Groups e.g.<code class="docutils literal notranslate"><span class="pre">/subscriptions/00000000-0000-0000-000000000000/resourceGroups/myResourceGroup</span></code>).</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parameters for the policy definition. This field is a JSON object that maps to the Parameters field from the Policy Definition. Changing this forces a new resource to be created.</p></li>
<li><p><strong>policy_definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Policy Definition to be applied at the specified Scope.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID of this Policy Assignment if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID of this Policy Assignment if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Managed Service Identity Type of this Policy Assignment. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), or <code class="docutils literal notranslate"><span class="pre">None</span></code> (no use of a Managed Service Identity).</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.Assignment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Assignment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.Assignment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Assignment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.AwaitableGetPolicyDefintionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.policy.</code><code class="sig-name descname">AwaitableGetPolicyDefintionResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">management_group_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">policy_rule=None</em>, <em class="sig-param">policy_type=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.AwaitableGetPolicyDefintionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.policy.Definition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.policy.</code><code class="sig-name descname">Definition</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">management_group_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">policy_rule=None</em>, <em class="sig-param">policy_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a policy rule definition on a management group or your provider subscription.</p>
<p>Policy definitions do not take effect until they are assigned to a scope using a Policy Assignment.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the policy definition.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the policy definition.</p></li>
<li><p><strong>management_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metadata for the policy definition. This
is a json object representing additional metadata that should be stored
with the policy definition.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy mode that allows you to specify which resource
types will be evaluated.  The value can be “All”, “Indexed” or
“NotSpecified”. Changing this resource forces a new resource to be
created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy definition. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.</p></li>
<li><p><strong>policy_rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy type.  The value can be “BuiltIn”, “Custom”
or “NotSpecified”. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.management_group_id">
<code class="sig-name descname">management_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.management_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata for the policy definition. This
is a json object representing additional metadata that should be stored
with the policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy mode that allows you to specify which resource
types will be evaluated.  The value can be “All”, “Indexed” or
“NotSpecified”. Changing this resource forces a new resource to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy definition. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.policy_rule">
<code class="sig-name descname">policy_rule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.policy_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.policy_type">
<code class="sig-name descname">policy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy type.  The value can be “BuiltIn”, “Custom”
or “NotSpecified”. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.Definition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">management_group_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">policy_rule=None</em>, <em class="sig-param">policy_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Definition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Definition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the policy definition.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the policy definition.</p></li>
<li><p><strong>management_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metadata for the policy definition. This
is a json object representing additional metadata that should be stored
with the policy definition.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy mode that allows you to specify which resource
types will be evaluated.  The value can be “All”, “Indexed” or
“NotSpecified”. Changing this resource forces a new resource to be
created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy definition. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.</p></li>
<li><p><strong>policy_rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy type.  The value can be “BuiltIn”, “Custom”
or “NotSpecified”. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.Definition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Definition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.Definition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Definition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.GetPolicyDefintionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.policy.</code><code class="sig-name descname">GetPolicyDefintionResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">management_group_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">policy_rule=None</em>, <em class="sig-param">policy_type=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicyDefintion.</p>
<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Description of the Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Any Metadata defined in the Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Policy Definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Any Parameters defined in the Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.policy_rule">
<code class="sig-name descname">policy_rule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.policy_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>The Rule as defined (in JSON) in the Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.policy_type">
<code class="sig-name descname">policy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Type of the Policy, such as <code class="docutils literal notranslate"><span class="pre">Microsoft.Authorization/policyDefinitions</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Type of Policy.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.policy.PolicySetDefinition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.policy.</code><code class="sig-name descname">PolicySetDefinition</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">management_group_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">policy_definitions=None</em>, <em class="sig-param">policy_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a policy set definition.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Policy set definitions (also known as policy initiatives) do not take effect until they are assigned to a scope using a Policy Set Assignment.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the policy set definition.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the policy set definition.</p></li>
<li><p><strong>management_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metadata for the policy set definition. This is a json object representing additional metadata that should be stored with the policy definition.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy set definition. Changing this forces a new resource to be created.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parameters for the policy set definition. This field is a json object that allows you to parameterize your policy definition.</p></li>
<li><p><strong>policy_definitions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy definitions for the policy set definition. This is a json object representing the bundled policy definitions .</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy set type. Possible values are <code class="docutils literal notranslate"><span class="pre">BuiltIn</span></code> or <code class="docutils literal notranslate"><span class="pre">Custom</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the policy set definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the policy set definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.management_group_id">
<code class="sig-name descname">management_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.management_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata for the policy set definition. This is a json object representing additional metadata that should be stored with the policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy set definition. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters for the policy set definition. This field is a json object that allows you to parameterize your policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.policy_definitions">
<code class="sig-name descname">policy_definitions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.policy_definitions" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy definitions for the policy set definition. This is a json object representing the bundled policy definitions .</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.policy_type">
<code class="sig-name descname">policy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy set type. Possible values are <code class="docutils literal notranslate"><span class="pre">BuiltIn</span></code> or <code class="docutils literal notranslate"><span class="pre">Custom</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.PolicySetDefinition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">management_group_id=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">policy_definitions=None</em>, <em class="sig-param">policy_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PolicySetDefinition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the policy set definition.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the policy set definition.</p></li>
<li><p><strong>management_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metadata for the policy set definition. This is a json object representing additional metadata that should be stored with the policy definition.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy set definition. Changing this forces a new resource to be created.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parameters for the policy set definition. This field is a json object that allows you to parameterize your policy definition.</p></li>
<li><p><strong>policy_definitions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy definitions for the policy set definition. This is a json object representing the bundled policy definitions .</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy set type. Possible values are <code class="docutils literal notranslate"><span class="pre">BuiltIn</span></code> or <code class="docutils literal notranslate"><span class="pre">Custom</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.PolicySetDefinition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.PolicySetDefinition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.Remediation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.policy.</code><code class="sig-name descname">Remediation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location_filters=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_assignment_id=None</em>, <em class="sig-param">policy_definition_reference_id=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Remediation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Policy Remediation at the specified Scope.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the resource locations that will be remediated.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Policy Remediation. Changing this forces a new resource to be created.</p></li>
<li><p><strong>policy_assignment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource ID of the policy assignment that should be remediated.</p></li>
<li><p><strong>policy_definition_reference_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Scope at which the Policy Remediation should be applied. Changing this forces a new resource to be created. A scope must be a Resource ID out of one of the following list:</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.policy.Remediation.location_filters">
<code class="sig-name descname">location_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Remediation.location_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the resource locations that will be remediated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Remediation.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Remediation.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Policy Remediation. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Remediation.policy_assignment_id">
<code class="sig-name descname">policy_assignment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Remediation.policy_assignment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource ID of the policy assignment that should be remediated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Remediation.policy_definition_reference_id">
<code class="sig-name descname">policy_definition_reference_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Remediation.policy_definition_reference_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Remediation.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Remediation.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scope at which the Policy Remediation should be applied. Changing this forces a new resource to be created. A scope must be a Resource ID out of one of the following list:</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.Remediation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location_filters=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_assignment_id=None</em>, <em class="sig-param">policy_definition_reference_id=None</em>, <em class="sig-param">scope=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Remediation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Remediation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the resource locations that will be remediated.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Policy Remediation. Changing this forces a new resource to be created.</p></li>
<li><p><strong>policy_assignment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource ID of the policy assignment that should be remediated.</p></li>
<li><p><strong>policy_definition_reference_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Scope at which the Policy Remediation should be applied. Changing this forces a new resource to be created. A scope must be a Resource ID out of one of the following list:</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.Remediation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Remediation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.Remediation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Remediation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.get_policy_defintion">
<code class="sig-prename descclassname">pulumi_azure.policy.</code><code class="sig-name descname">get_policy_defintion</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">management_group_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.get_policy_defintion" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a Policy Definition, both custom and built in. Retrieves Policy Definitions from your current subscription by default.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display_name</strong> (<em>str</em>) – Specifies the name of the Policy Definition.</p></li>
<li><p><strong>management_group_id</strong> (<em>str</em>) – Only retrieve Policy Definitions from this Management Group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
