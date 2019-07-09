---
---

<div class="section" id="module-pulumi_openstack.firewall">
<span id="firewall"></span><h1>firewall<a class="headerlink" href="#module-pulumi_openstack.firewall" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_openstack.firewall.Firewall">
<em class="property">class </em><code class="descclassname">pulumi_openstack.firewall.</code><code class="descname">Firewall</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>admin_state_up=None</em>, <em>associated_routers=None</em>, <em>description=None</em>, <em>name=None</em>, <em>no_routers=None</em>, <em>policy_id=None</em>, <em>region=None</em>, <em>tenant_id=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a v1 firewall resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the firewall
(must be “true” or “false” if provided - defaults to “true”).
Changing this updates the <code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing firewall.</li>
<li><strong>associated_routers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with <code class="docutils literal notranslate"><span class="pre">no_routers</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the firewall. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the firewall. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall.</li>
<li><strong>no_routers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this firewall not be associated with any routers
(must be “true” or “false” if provide - defaults to “false”).
Conflicts with <code class="docutils literal notranslate"><span class="pre">associated_routers</span></code>.</li>
<li><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy resource id for the firewall. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">policy_id</span></code> of an existing firewall.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the floating IP. Required if admin wants
to create a firewall for another tenant. Changing this creates a new
firewall.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/fw_firewall_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/fw_firewall_v1.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.firewall.Firewall.admin_state_up">
<code class="descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>Administrative up/down status for the firewall
(must be “true” or “false” if provided - defaults to “true”).
Changing this updates the <code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing firewall.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Firewall.associated_routers">
<code class="descname">associated_routers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.associated_routers" title="Permalink to this definition">¶</a></dt>
<dd><p>Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with <code class="docutils literal notranslate"><span class="pre">no_routers</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Firewall.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the firewall. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Firewall.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the firewall. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Firewall.no_routers">
<code class="descname">no_routers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.no_routers" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this firewall not be associated with any routers
(must be “true” or “false” if provide - defaults to “false”).
Conflicts with <code class="docutils literal notranslate"><span class="pre">associated_routers</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Firewall.policy_id">
<code class="descname">policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy resource id for the firewall. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">policy_id</span></code> of an existing firewall.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Firewall.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Firewall.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the floating IP. Required if admin wants
to create a firewall for another tenant. Changing this creates a new
firewall.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Firewall.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.firewall.Firewall.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.firewall.Firewall.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.firewall.GetPolicyResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.firewall.</code><code class="descname">GetPolicyResult</code><span class="sig-paren">(</span><em>audited=None</em>, <em>description=None</em>, <em>name=None</em>, <em>policy_id=None</em>, <em>region=None</em>, <em>rules=None</em>, <em>shared=None</em>, <em>tenant_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicy.</p>
<dl class="attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.audited">
<code class="descname">audited</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.audited" title="Permalink to this definition">¶</a></dt>
<dd><p>The audit status of the firewall policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the firewall policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.policy_id">
<code class="descname">policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.rules">
<code class="descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The array of one or more firewall rules that comprise the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.shared">
<code class="descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>The sharing status of the firewall policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.firewall.Policy">
<em class="property">class </em><code class="descclassname">pulumi_openstack.firewall.</code><code class="descname">Policy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>audited=None</em>, <em>description=None</em>, <em>name=None</em>, <em>region=None</em>, <em>rules=None</em>, <em>shared=None</em>, <em>tenant_id=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a v1 firewall policy resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>audited</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Audit status of the firewall policy
(must be “true” or “false” if provided - defaults to “false”).
This status is set to “false” whenever the firewall policy or any of its
rules are changed. Changing this updates the <code class="docutils literal notranslate"><span class="pre">audited</span></code> status of an existing
firewall policy.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the firewall policy. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall policy.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the firewall policy. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall policy.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall policy.</li>
<li><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.</li>
<li><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sharing status of the firewall policy (must be “true”
or “false” if provided). If this is “true” the policy is visible to, and
can be used in, firewalls in other tenants. Changing this updates the
<code class="docutils literal notranslate"><span class="pre">shared</span></code> status of an existing firewall policy. Only administrative users
can specify if the policy should be shared.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/fw_policy_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/fw_policy_v1.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.firewall.Policy.audited">
<code class="descname">audited</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.audited" title="Permalink to this definition">¶</a></dt>
<dd><p>Audit status of the firewall policy
(must be “true” or “false” if provided - defaults to “false”).
This status is set to “false” whenever the firewall policy or any of its
rules are changed. Changing this updates the <code class="docutils literal notranslate"><span class="pre">audited</span></code> status of an existing
firewall policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Policy.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the firewall policy. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Policy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the firewall policy. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Policy.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Policy.rules">
<code class="descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Policy.shared">
<code class="descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Sharing status of the firewall policy (must be “true”
or “false” if provided). If this is “true” the policy is visible to, and
can be used in, firewalls in other tenants. Changing this updates the
<code class="docutils literal notranslate"><span class="pre">shared</span></code> status of an existing firewall policy. Only administrative users
can specify if the policy should be shared.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Policy.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.firewall.Policy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.firewall.Policy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.firewall.Rule">
<em class="property">class </em><code class="descclassname">pulumi_openstack.firewall.</code><code class="descname">Rule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>action=None</em>, <em>description=None</em>, <em>destination_ip_address=None</em>, <em>destination_port=None</em>, <em>enabled=None</em>, <em>ip_version=None</em>, <em>name=None</em>, <em>protocol=None</em>, <em>region=None</em>, <em>source_ip_address=None</em>, <em>source_port=None</em>, <em>tenant_id=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a v1 firewall rule resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action to be taken ( must be “allow” or “deny”) when the
firewall rule matches. Changing this updates the <code class="docutils literal notranslate"><span class="pre">action</span></code> of an existing
firewall rule.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the firewall rule. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall rule.</li>
<li><strong>destination_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination IP address on which the
firewall rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">destination_ip_address</span></code>
of an existing firewall rule.</li>
<li><strong>destination_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination port on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">destination_port</span></code> of an existing
firewall rule.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enabled status for the firewall rule (must be “true”
or “false” if provided - defaults to “true”). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">enabled</span></code> status of an existing firewall rule.</li>
<li><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – IP version, either 4 (default) or 6. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">ip_version</span></code> of an existing firewall rule.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the firewall rule. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall rule.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol type on which the firewall rule operates.
Valid values are: <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>, <code class="docutils literal notranslate"><span class="pre">icmp</span></code>, and <code class="docutils literal notranslate"><span class="pre">any</span></code>. Changing this updates the
<code class="docutils literal notranslate"><span class="pre">protocol</span></code> of an existing firewall rule.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall rule.</li>
<li><strong>source_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source IP address on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">source_ip_address</span></code> of an existing
firewall rule.</li>
<li><strong>source_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source port on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">source_port</span></code> of an existing
firewall rule.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/fw_rule_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/fw_rule_v1.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.action">
<code class="descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Action to be taken ( must be “allow” or “deny”) when the
firewall rule matches. Changing this updates the <code class="docutils literal notranslate"><span class="pre">action</span></code> of an existing
firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the firewall rule. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.destination_ip_address">
<code class="descname">destination_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.destination_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination IP address on which the
firewall rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">destination_ip_address</span></code>
of an existing firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.destination_port">
<code class="descname">destination_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.destination_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination port on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">destination_port</span></code> of an existing
firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enabled status for the firewall rule (must be “true”
or “false” if provided - defaults to “true”). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">enabled</span></code> status of an existing firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.ip_version">
<code class="descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>IP version, either 4 (default) or 6. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">ip_version</span></code> of an existing firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the firewall rule. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol type on which the firewall rule operates.
Valid values are: <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>, <code class="docutils literal notranslate"><span class="pre">icmp</span></code>, and <code class="docutils literal notranslate"><span class="pre">any</span></code>. Changing this updates the
<code class="docutils literal notranslate"><span class="pre">protocol</span></code> of an existing firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.source_ip_address">
<code class="descname">source_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.source_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The source IP address on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">source_ip_address</span></code> of an existing
firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.source_port">
<code class="descname">source_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.source_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The source port on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">source_port</span></code> of an existing
firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.firewall.Rule.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.firewall.Rule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.firewall.Rule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.firewall.get_policy">
<code class="descclassname">pulumi_openstack.firewall.</code><code class="descname">get_policy</code><span class="sig-paren">(</span><em>name=None</em>, <em>policy_id=None</em>, <em>region=None</em>, <em>tenant_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.get_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get firewall policy information of an available OpenStack firewall policy.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/fw_policy_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/fw_policy_v1.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
