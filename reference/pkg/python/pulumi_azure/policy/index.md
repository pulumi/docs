<div class="section" id="module-pulumi_azure.policy">
<span id="policy"></span><h1>policy<a class="headerlink" href="#module-pulumi_azure.policy" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.policy.Assignment">
<em class="property">class </em><code class="descclassname">pulumi_azure.policy.</code><code class="descname">Assignment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>identity=None</em>, <em>location=None</em>, <em>name=None</em>, <em>not_scopes=None</em>, <em>parameters=None</em>, <em>policy_definition_id=None</em>, <em>scope=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Assignment" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the specified Policy Definition at the specified Scope. Also, Policy Set Definitions are supported.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description to use for this Policy Assignment. Changing this forces a new resource to be created.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly display name to use for this Policy Assignment. Changing this forces a new resource to be created.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where this policy assignment should exist. This is required when an Identity is assigned. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Policy Assignment. Changing this forces a new resource to be created.</li>
<li><strong>not_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the Policy Assignment’s excluded scopes. The list must contain Resource IDs (such as Subscriptions e.g. <code class="docutils literal notranslate"><span class="pre">/subscriptions/00000000-0000-0000-000000000000</span></code> or Resource Groups e.g.<code class="docutils literal notranslate"><span class="pre">/subscriptions/00000000-0000-0000-000000000000/resourceGroups/myResourceGroup</span></code>).</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parameters for the policy definition. This field is a JSON object that maps to the Parameters field from the Policy Definition. Changing this forces a new resource to be created.</li>
<li><strong>policy_definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Policy Definition to be applied at the specified Scope.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] scope</p>
<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description to use for this Policy Assignment. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly display name to use for this Policy Assignment. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where this policy assignment should exist. This is required when an Identity is assigned. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Policy Assignment. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.not_scopes">
<code class="descname">not_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.not_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Policy Assignment’s excluded scopes. The list must contain Resource IDs (such as Subscriptions e.g. <code class="docutils literal notranslate"><span class="pre">/subscriptions/00000000-0000-0000-000000000000</span></code> or Resource Groups e.g.<code class="docutils literal notranslate"><span class="pre">/subscriptions/00000000-0000-0000-000000000000/resourceGroups/myResourceGroup</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters for the policy definition. This field is a JSON object that maps to the Parameters field from the Policy Definition. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Assignment.policy_definition_id">
<code class="descname">policy_definition_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Assignment.policy_definition_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Policy Definition to be applied at the specified Scope.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.Assignment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Assignment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.Assignment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Assignment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.Definition">
<em class="property">class </em><code class="descclassname">pulumi_azure.policy.</code><code class="descname">Definition</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>management_group_id=None</em>, <em>metadata=None</em>, <em>mode=None</em>, <em>name=None</em>, <em>parameters=None</em>, <em>policy_rule=None</em>, <em>policy_type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Definition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a policy rule definition on a management group or your provider subscription.</p>
<p>Policy definitions do not take effect until they are assigned to a scope using a Policy Assignment.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the policy definition.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the policy definition.</li>
<li><strong>management_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.</li>
<li><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metadata for the policy definition. This
is a json object representing additional metadata that should be stored
with the policy definition.</li>
<li><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy mode that allows you to specify which resource
types will be evaluated.  The value can be “All”, “Indexed” or
“NotSpecified”. Changing this resource forces a new resource to be
created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy definition. Changing this forces a
new resource to be created.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.</li>
<li><strong>policy_rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.</li>
<li><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy type.  The value can be “BuiltIn”, “Custom”
or “NotSpecified”. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.management_group_id">
<code class="descname">management_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.management_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata for the policy definition. This
is a json object representing additional metadata that should be stored
with the policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.mode">
<code class="descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy mode that allows you to specify which resource
types will be evaluated.  The value can be “All”, “Indexed” or
“NotSpecified”. Changing this resource forces a new resource to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy definition. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters for the policy definition. This field
is a json object that allows you to parameterize your policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.policy_rule">
<code class="descname">policy_rule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.policy_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy rule for the policy definition. This
is a json object representing the rule that contains an if and
a then block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.Definition.policy_type">
<code class="descname">policy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.Definition.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy type.  The value can be “BuiltIn”, “Custom”
or “NotSpecified”. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.Definition.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Definition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.Definition.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.Definition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.GetPolicyDefintionResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.policy.</code><code class="descname">GetPolicyDefintionResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>metadata=None</em>, <em>name=None</em>, <em>parameters=None</em>, <em>policy_rule=None</em>, <em>policy_type=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicyDefintion.</p>
<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Description of the Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Any Metadata defined in the Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Policy Definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Any Parameters defined in the Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.policy_rule">
<code class="descname">policy_rule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.policy_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>The Rule as defined (in JSON) in the Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.policy_type">
<code class="descname">policy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Type of the Policy, such as <code class="docutils literal notranslate"><span class="pre">Microsoft.Authorization/policyDefinitions</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Type of Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.GetPolicyDefintionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.GetPolicyDefintionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.policy.PolicySetDefinition">
<em class="property">class </em><code class="descclassname">pulumi_azure.policy.</code><code class="descname">PolicySetDefinition</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>display_name=None</em>, <em>management_group_id=None</em>, <em>metadata=None</em>, <em>name=None</em>, <em>parameters=None</em>, <em>policy_definitions=None</em>, <em>policy_type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a policy set definition.</p>
<blockquote>
<div><strong>NOTE:</strong>  Policy set definitions (also known as policy initiatives) do not take effect until they are assigned to a scope using a Policy Set Assignment.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the policy set definition.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of the policy set definition.</li>
<li><strong>management_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.</li>
<li><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metadata for the policy set definition. This is a json object representing additional metadata that should be stored with the policy definition.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy set definition. Changing this forces a new resource to be created.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Parameters for the policy set definition. This field is a json object that allows you to parameterize your policy definition.</li>
<li><strong>policy_definitions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy definitions for the policy set definition. This is a json object representing the bundled policy definitions .</li>
<li><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy set type. Possible values are <code class="docutils literal notranslate"><span class="pre">BuiltIn</span></code> or <code class="docutils literal notranslate"><span class="pre">Custom</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the policy set definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of the policy set definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.management_group_id">
<code class="descname">management_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.management_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Management Group where this policy should be defined. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata for the policy set definition. This is a json object representing additional metadata that should be stored with the policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy set definition. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters for the policy set definition. This field is a json object that allows you to parameterize your policy definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.policy_definitions">
<code class="descname">policy_definitions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.policy_definitions" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy definitions for the policy set definition. This is a json object representing the bundled policy definitions .</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.policy.PolicySetDefinition.policy_type">
<code class="descname">policy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy set type. Possible values are <code class="docutils literal notranslate"><span class="pre">BuiltIn</span></code> or <code class="docutils literal notranslate"><span class="pre">Custom</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.policy.PolicySetDefinition.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.policy.PolicySetDefinition.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.PolicySetDefinition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_azure.policy.get_policy_defintion">
<code class="descclassname">pulumi_azure.policy.</code><code class="descname">get_policy_defintion</code><span class="sig-paren">(</span><em>display_name=None</em>, <em>management_group_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.policy.get_policy_defintion" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a Policy Definition, both custom and built in. Retrieves Policy Definitions from your current subscription by default.</p>
</dd></dl>

</div>
