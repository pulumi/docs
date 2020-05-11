---
title: Module firewall
title_tag: Module firewall | Package pulumi_openstack | Python SDK
linktitle: firewall
notitle: true
---

<div class="section" id="firewall">
<h1>firewall<a class="headerlink" href="#firewall" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.firewall"></span><dl class="py class">
<dt id="pulumi_openstack.firewall.AwaitableGetPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.firewall.</code><code class="sig-name descname">AwaitableGetPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">audited</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.AwaitableGetPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_openstack.firewall.Firewall">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.firewall.</code><code class="sig-name descname">Firewall</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_routers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_routers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_specs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a v1 firewall resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the firewall
(must be “true” or “false” if provided - defaults to “true”).
Changing this updates the <code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing firewall.</p></li>
<li><p><strong>associated_routers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with <code class="docutils literal notranslate"><span class="pre">no_routers</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the firewall. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the firewall. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall.</p></li>
<li><p><strong>no_routers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this firewall not be associated with any routers
(must be “true” or “false” if provide - defaults to “false”).
Conflicts with <code class="docutils literal notranslate"><span class="pre">associated_routers</span></code>.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy resource id for the firewall. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">policy_id</span></code> of an existing firewall.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the floating IP. Required if admin wants
to create a firewall for another tenant. Changing this creates a new
firewall.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Firewall.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>Administrative up/down status for the firewall
(must be “true” or “false” if provided - defaults to “true”).
Changing this updates the <code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing firewall.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Firewall.associated_routers">
<code class="sig-name descname">associated_routers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.associated_routers" title="Permalink to this definition">¶</a></dt>
<dd><p>Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with <code class="docutils literal notranslate"><span class="pre">no_routers</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Firewall.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the firewall. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Firewall.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the firewall. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Firewall.no_routers">
<code class="sig-name descname">no_routers</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.no_routers" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this firewall not be associated with any routers
(must be “true” or “false” if provide - defaults to “false”).
Conflicts with <code class="docutils literal notranslate"><span class="pre">associated_routers</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Firewall.policy_id">
<code class="sig-name descname">policy_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy resource id for the firewall. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">policy_id</span></code> of an existing firewall.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Firewall.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Firewall.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the floating IP. Required if admin wants
to create a firewall for another tenant. Changing this creates a new
firewall.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Firewall.value_specs">
<code class="sig-name descname">value_specs</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.firewall.Firewall.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_routers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_routers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_specs</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Firewall resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the firewall
(must be “true” or “false” if provided - defaults to “true”).
Changing this updates the <code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing firewall.</p></li>
<li><p><strong>associated_routers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Router(s) to associate this firewall instance
with. Must be a list of strings. Changing this updates the associated routers
of an existing firewall. Conflicts with <code class="docutils literal notranslate"><span class="pre">no_routers</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the firewall. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the firewall. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall.</p></li>
<li><p><strong>no_routers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this firewall not be associated with any routers
(must be “true” or “false” if provide - defaults to “false”).
Conflicts with <code class="docutils literal notranslate"><span class="pre">associated_routers</span></code>.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy resource id for the firewall. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">policy_id</span></code> of an existing firewall.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the floating IP. Required if admin wants
to create a firewall for another tenant. Changing this creates a new
firewall.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.firewall.Firewall.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_openstack.firewall.Firewall.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Firewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_openstack.firewall.GetPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.firewall.</code><code class="sig-name descname">GetPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">audited</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicy.</p>
<dl class="py attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.audited">
<code class="sig-name descname">audited</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.audited" title="Permalink to this definition">¶</a></dt>
<dd><p>The audit status of the firewall policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the firewall policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.policy_id">
<code class="sig-name descname">policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The array of one or more firewall rules that comprise the policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.shared">
<code class="sig-name descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>The sharing status of the firewall policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.GetPolicyResult.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.GetPolicyResult.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_openstack.firewall.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.firewall.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audited</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_specs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a v1 firewall policy resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audited</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Audit status of the firewall policy
(must be “true” or “false” if provided - defaults to “false”).
This status is set to “false” whenever the firewall policy or any of its
rules are changed. Changing this updates the <code class="docutils literal notranslate"><span class="pre">audited</span></code> status of an existing
firewall policy.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the firewall policy. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the firewall policy. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall policy.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sharing status of the firewall policy (must be “true”
or “false” if provided). If this is “true” the policy is visible to, and
can be used in, firewalls in other tenants. Changing this updates the
<code class="docutils literal notranslate"><span class="pre">shared</span></code> status of an existing firewall policy. Only administrative users
can specify if the policy should be shared.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Policy.audited">
<code class="sig-name descname">audited</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.audited" title="Permalink to this definition">¶</a></dt>
<dd><p>Audit status of the firewall policy
(must be “true” or “false” if provided - defaults to “false”).
This status is set to “false” whenever the firewall policy or any of its
rules are changed. Changing this updates the <code class="docutils literal notranslate"><span class="pre">audited</span></code> status of an existing
firewall policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Policy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the firewall policy. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Policy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the firewall policy. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Policy.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Policy.rules">
<code class="sig-name descname">rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Policy.shared">
<code class="sig-name descname">shared</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Sharing status of the firewall policy (must be “true”
or “false” if provided). If this is “true” the policy is visible to, and
can be used in, firewalls in other tenants. Changing this updates the
<code class="docutils literal notranslate"><span class="pre">shared</span></code> status of an existing firewall policy. Only administrative users
can specify if the policy should be shared.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Policy.value_specs">
<code class="sig-name descname">value_specs</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Policy.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.firewall.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audited</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_specs</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audited</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Audit status of the firewall policy
(must be “true” or “false” if provided - defaults to “false”).
This status is set to “false” whenever the firewall policy or any of its
rules are changed. Changing this updates the <code class="docutils literal notranslate"><span class="pre">audited</span></code> status of an existing
firewall policy.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the firewall policy. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the firewall policy. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the v1 networking client.
A networking client is needed to create a firewall policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall policy.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more firewall rules that comprise
the policy. Changing this results in adding/removing rules from the
existing firewall policy.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sharing status of the firewall policy (must be “true”
or “false” if provided). If this is “true” the policy is visible to, and
can be used in, firewalls in other tenants. Changing this updates the
<code class="docutils literal notranslate"><span class="pre">shared</span></code> status of an existing firewall policy. Only administrative users
can specify if the policy should be shared.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.firewall.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_openstack.firewall.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_openstack.firewall.Rule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.firewall.</code><code class="sig-name descname">Rule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_specs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a v1 firewall rule resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action to be taken ( must be “allow” or “deny”) when the
firewall rule matches. Changing this updates the <code class="docutils literal notranslate"><span class="pre">action</span></code> of an existing
firewall rule.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the firewall rule. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall rule.</p></li>
<li><p><strong>destination_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination IP address on which the
firewall rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">destination_ip_address</span></code>
of an existing firewall rule.</p></li>
<li><p><strong>destination_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination port on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">destination_port</span></code> of an existing
firewall rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enabled status for the firewall rule (must be “true”
or “false” if provided - defaults to “true”). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">enabled</span></code> status of an existing firewall rule.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – IP version, either 4 (default) or 6. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">ip_version</span></code> of an existing firewall rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the firewall rule. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall rule.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol type on which the firewall rule operates.
Valid values are: <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>, <code class="docutils literal notranslate"><span class="pre">icmp</span></code>, and <code class="docutils literal notranslate"><span class="pre">any</span></code>. Changing this updates the
<code class="docutils literal notranslate"><span class="pre">protocol</span></code> of an existing firewall rule.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall rule.</p></li>
<li><p><strong>source_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source IP address on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">source_ip_address</span></code> of an existing
firewall rule.</p></li>
<li><p><strong>source_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source port on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">source_port</span></code> of an existing
firewall rule.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.action">
<code class="sig-name descname">action</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Action to be taken ( must be “allow” or “deny”) when the
firewall rule matches. Changing this updates the <code class="docutils literal notranslate"><span class="pre">action</span></code> of an existing
firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the firewall rule. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.destination_ip_address">
<code class="sig-name descname">destination_ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.destination_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination IP address on which the
firewall rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">destination_ip_address</span></code>
of an existing firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.destination_port">
<code class="sig-name descname">destination_port</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.destination_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination port on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">destination_port</span></code> of an existing
firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enabled status for the firewall rule (must be “true”
or “false” if provided - defaults to “true”). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">enabled</span></code> status of an existing firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.ip_version">
<code class="sig-name descname">ip_version</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>IP version, either 4 (default) or 6. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">ip_version</span></code> of an existing firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the firewall rule. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol type on which the firewall rule operates.
Valid values are: <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>, <code class="docutils literal notranslate"><span class="pre">icmp</span></code>, and <code class="docutils literal notranslate"><span class="pre">any</span></code>. Changing this updates the
<code class="docutils literal notranslate"><span class="pre">protocol</span></code> of an existing firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.source_ip_address">
<code class="sig-name descname">source_ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.source_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The source IP address on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">source_ip_address</span></code> of an existing
firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.source_port">
<code class="sig-name descname">source_port</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.source_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The source port on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">source_port</span></code> of an existing
firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.firewall.Rule.value_specs">
<code class="sig-name descname">value_specs</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.firewall.Rule.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.firewall.Rule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_specs</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Rule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action to be taken ( must be “allow” or “deny”) when the
firewall rule matches. Changing this updates the <code class="docutils literal notranslate"><span class="pre">action</span></code> of an existing
firewall rule.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the firewall rule. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing firewall rule.</p></li>
<li><p><strong>destination_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination IP address on which the
firewall rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">destination_ip_address</span></code>
of an existing firewall rule.</p></li>
<li><p><strong>destination_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination port on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">destination_port</span></code> of an existing
firewall rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enabled status for the firewall rule (must be “true”
or “false” if provided - defaults to “true”). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">enabled</span></code> status of an existing firewall rule.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – IP version, either 4 (default) or 6. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">ip_version</span></code> of an existing firewall rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the firewall rule. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing firewall rule.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol type on which the firewall rule operates.
Valid values are: <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>, <code class="docutils literal notranslate"><span class="pre">icmp</span></code>, and <code class="docutils literal notranslate"><span class="pre">any</span></code>. Changing this updates the
<code class="docutils literal notranslate"><span class="pre">protocol</span></code> of an existing firewall rule.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the v1 Compute client.
A Compute client is needed to create a firewall rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
firewall rule.</p></li>
<li><p><strong>source_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source IP address on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">source_ip_address</span></code> of an existing
firewall rule.</p></li>
<li><p><strong>source_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source port on which the firewall
rule operates. Changing this updates the <code class="docutils literal notranslate"><span class="pre">source_port</span></code> of an existing
firewall rule.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the firewall rule. Required if admin
wants to create a firewall rule for another tenant. Changing this creates a
new firewall rule.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.firewall.Rule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_openstack.firewall.Rule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_openstack.firewall.get_policy">
<code class="sig-prename descclassname">pulumi_openstack.firewall.</code><code class="sig-name descname">get_policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.firewall.get_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get firewall policy information of an available OpenStack firewall policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the firewall policy.</p></li>
<li><p><strong>policy_id</strong> (<em>str</em>) – The ID of the firewall policy.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve firewall policy ids. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>tenant_id</strong> (<em>str</em>) – The owner of the firewall policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
