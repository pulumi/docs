---
title: Module loadbalancer
title_tag: Module loadbalancer | Package pulumi_openstack | Python SDK
linktitle: loadbalancer
notitle: true
---

<div class="section" id="loadbalancer">
<h1>loadbalancer<a class="headerlink" href="#loadbalancer" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.loadbalancer"></span><dl class="py class">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">L7PolicyV2</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">position</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redirect_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Load Balancer L7 Policy resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The L7 Policy action - can either be REDIRECT_TO_POOL,
REDIRECT_TO_URL or REJECT.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the L7 Policy.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the L7 Policy.</p></li>
<li><p><strong>listener_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Listener on which the L7 Policy will be associated with.
Changing this creates a new L7 Policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the L7 Policy. Does not have
to be unique.</p></li>
<li><p><strong>position</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The position of this policy on the listener. Positions start at 1.</p></li>
<li><p><strong>redirect_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requests matching this policy will be redirected to the
pool with this ID. Only valid if action is REDIRECT_TO_POOL.</p></li>
<li><p><strong>redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requests matching this policy will be redirected to this URL.
Only valid if action is REDIRECT_TO_URL.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
L7 Policy.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the L7 Policy.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new L7 Policy.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.action">
<code class="sig-name descname">action</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The L7 Policy action - can either be REDIRECT_TO_POOL,
REDIRECT_TO_URL or REJECT.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the L7 Policy.
A valid value is true (UP) or false (DOWN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description for the L7 Policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.listener_id">
<code class="sig-name descname">listener_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.listener_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Listener on which the L7 Policy will be associated with.
Changing this creates a new L7 Policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable name for the L7 Policy. Does not have
to be unique.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.position">
<code class="sig-name descname">position</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.position" title="Permalink to this definition">¶</a></dt>
<dd><p>The position of this policy on the listener. Positions start at 1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.redirect_pool_id">
<code class="sig-name descname">redirect_pool_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.redirect_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Requests matching this policy will be redirected to the
pool with this ID. Only valid if action is REDIRECT_TO_POOL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.redirect_url">
<code class="sig-name descname">redirect_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.redirect_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Requests matching this policy will be redirected to this URL.
Only valid if action is REDIRECT_TO_URL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
L7 Policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for admins. The UUID of the tenant who owns
the L7 Policy.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new L7 Policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">position</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redirect_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redirect_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing L7PolicyV2 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The L7 Policy action - can either be REDIRECT_TO_POOL,
REDIRECT_TO_URL or REJECT.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the L7 Policy.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the L7 Policy.</p></li>
<li><p><strong>listener_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Listener on which the L7 Policy will be associated with.
Changing this creates a new L7 Policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the L7 Policy. Does not have
to be unique.</p></li>
<li><p><strong>position</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The position of this policy on the listener. Positions start at 1.</p></li>
<li><p><strong>redirect_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requests matching this policy will be redirected to the
pool with this ID. Only valid if action is REDIRECT_TO_POOL.</p></li>
<li><p><strong>redirect_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Requests matching this policy will be redirected to this URL.
Only valid if action is REDIRECT_TO_URL.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
L7 Policy.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the L7 Policy.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new L7 Policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.L7PolicyV2.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7PolicyV2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.L7RuleV2">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">L7RuleV2</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compare_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">l7policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 L7 Rule resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the L7 Rule.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>compare_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The comparison type for the L7 rule - can either be
CONTAINS, STARTS_WITH, ENDS_WITH, EQUAL_TO or REGEX</p></li>
<li><p><strong>invert</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true the logic of the rule is inverted. For example, with invert
true, equal to would become not equal to. Default is false.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key to use for the comparison. For example, the name of the cookie to
evaluate. Valid when <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to COOKIE or HEADER.</p></li>
<li><p><strong>l7policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the L7 Policy to query. Changing this creates a new
L7 Rule.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
L7 Rule.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the L7 Rule.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new L7 Rule.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The L7 Rule type - can either be COOKIE, FILE_TYPE, HEADER,
HOST_NAME or PATH.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to use for the comparison. For example, the file type to
compare.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the L7 Rule.
A valid value is true (UP) or false (DOWN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.compare_type">
<code class="sig-name descname">compare_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.compare_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The comparison type for the L7 rule - can either be
CONTAINS, STARTS_WITH, ENDS_WITH, EQUAL_TO or REGEX</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.invert">
<code class="sig-name descname">invert</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.invert" title="Permalink to this definition">¶</a></dt>
<dd><p>When true the logic of the rule is inverted. For example, with invert
true, equal to would become not equal to. Default is false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.key">
<code class="sig-name descname">key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The key to use for the comparison. For example, the name of the cookie to
evaluate. Valid when <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to COOKIE or HEADER.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.l7policy_id">
<code class="sig-name descname">l7policy_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.l7policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the L7 Policy to query. Changing this creates a new
L7 Rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.listener_id">
<code class="sig-name descname">listener_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.listener_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Listener owning this resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
L7 Rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for admins. The UUID of the tenant who owns
the L7 Rule.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new L7 Rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The L7 Rule type - can either be COOKIE, FILE_TYPE, HEADER,
HOST_NAME or PATH.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.value">
<code class="sig-name descname">value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value to use for the comparison. For example, the file type to
compare.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compare_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">l7policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing L7RuleV2 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the L7 Rule.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>compare_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The comparison type for the L7 rule - can either be
CONTAINS, STARTS_WITH, ENDS_WITH, EQUAL_TO or REGEX</p></li>
<li><p><strong>invert</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true the logic of the rule is inverted. For example, with invert
true, equal to would become not equal to. Default is false.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key to use for the comparison. For example, the name of the cookie to
evaluate. Valid when <code class="docutils literal notranslate"><span class="pre">type</span></code> is set to COOKIE or HEADER.</p></li>
<li><p><strong>l7policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the L7 Policy to query. Changing this creates a new
L7 Rule.</p></li>
<li><p><strong>listener_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Listener owning this resource.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
L7 Rule.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the L7 Rule.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new L7 Rule.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The L7 Rule type - can either be COOKIE, FILE_TYPE, HEADER,
HOST_NAME or PATH.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value to use for the comparison. For example, the file type to
compare.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.L7RuleV2.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.L7RuleV2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.Listener">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">Listener</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_tls_container_ref</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insert_headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">loadbalancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sni_container_refs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_client_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_member_connect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_member_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_tcp_inspect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 listener resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of connections allowed
for the Listener.</p></li>
<li><p><strong>default_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the default pool with which the
Listener is associated.</p></li>
<li><p><strong>default_tls_container_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is <code class="docutils literal notranslate"><span class="pre">TERMINATED_HTTPS</span></code>. See
<a class="reference external" href="https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer">here</a>
for more information.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the Listener.</p></li>
<li><p><strong>insert_headers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The load balancer on which to provision this
Listener. Changing this creates a new Listener.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the Listener. Does not have
to be unique.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.</p></li>
<li><p><strong>protocol_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which to listen for client traffic.
Changing this creates a new Listener.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
Listener.</p></li>
<li><p><strong>sni_container_refs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of references to Barbican Secrets
containers which store SNI information. See
<a class="reference external" href="https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer">here</a>
for more information.</p>
</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.</p></li>
<li><p><strong>timeout_client_data</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The client inactivity timeout in milliseconds.</p></li>
<li><p><strong>timeout_member_connect</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The member connection timeout in milliseconds.</p></li>
<li><p><strong>timeout_member_data</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The member inactivity timeout in milliseconds.</p></li>
<li><p><strong>timeout_tcp_inspect</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in milliseconds, to wait for additional
TCP packets for content inspection.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.connection_limit">
<code class="sig-name descname">connection_limit</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.connection_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of connections allowed
for the Listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.default_pool_id">
<code class="sig-name descname">default_pool_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.default_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the default pool with which the
Listener is associated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.default_tls_container_ref">
<code class="sig-name descname">default_tls_container_ref</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.default_tls_container_ref" title="Permalink to this definition">¶</a></dt>
<dd><p>A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is <code class="docutils literal notranslate"><span class="pre">TERMINATED_HTTPS</span></code>. See
<a class="reference external" href="https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer">here</a>
for more information.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description for the Listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.insert_headers">
<code class="sig-name descname">insert_headers</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.insert_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.loadbalancer_id">
<code class="sig-name descname">loadbalancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The load balancer on which to provision this
Listener. Changing this creates a new Listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable name for the Listener. Does not have
to be unique.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.protocol_port">
<code class="sig-name descname">protocol_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.protocol_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which to listen for client traffic.
Changing this creates a new Listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
Listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.sni_container_refs">
<code class="sig-name descname">sni_container_refs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.sni_container_refs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of references to Barbican Secrets
containers which store SNI information. See
<a class="reference external" href="https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer">here</a>
for more information.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.timeout_client_data">
<code class="sig-name descname">timeout_client_data</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.timeout_client_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The client inactivity timeout in milliseconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.timeout_member_connect">
<code class="sig-name descname">timeout_member_connect</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.timeout_member_connect" title="Permalink to this definition">¶</a></dt>
<dd><p>The member connection timeout in milliseconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.timeout_member_data">
<code class="sig-name descname">timeout_member_data</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.timeout_member_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The member inactivity timeout in milliseconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Listener.timeout_tcp_inspect">
<code class="sig-name descname">timeout_tcp_inspect</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.timeout_tcp_inspect" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in milliseconds, to wait for additional
TCP packets for content inspection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.Listener.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_tls_container_ref</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insert_headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">loadbalancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sni_container_refs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_client_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_member_connect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_member_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_tcp_inspect</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Listener resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the Listener.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of connections allowed
for the Listener.</p></li>
<li><p><strong>default_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the default pool with which the
Listener is associated.</p></li>
<li><p><strong>default_tls_container_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A reference to a Barbican Secrets
container which stores TLS information. This is required if the protocol
is <code class="docutils literal notranslate"><span class="pre">TERMINATED_HTTPS</span></code>. See
<a class="reference external" href="https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer">here</a>
for more information.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the Listener.</p></li>
<li><p><strong>insert_headers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The list of key value pairs representing headers to insert
into the request before it is sent to the backend members. Changing this updates the headers of the
existing listener.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The load balancer on which to provision this
Listener. Changing this creates a new Listener.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the Listener. Does not have
to be unique.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol - can either be TCP, HTTP, HTTPS,
TERMINATED_HTTPS or UDP (supported only in Octavia). Changing this creates a
new Listener.</p></li>
<li><p><strong>protocol_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which to listen for client traffic.
Changing this creates a new Listener.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
Listener.</p></li>
<li><p><strong>sni_container_refs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of references to Barbican Secrets
containers which store SNI information. See
<a class="reference external" href="https://wiki.openstack.org/wiki/Network/LBaaS/docs/how-to-create-tls-loadbalancer">here</a>
for more information.</p>
</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the Listener.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new Listener.</p></li>
<li><p><strong>timeout_client_data</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The client inactivity timeout in milliseconds.</p></li>
<li><p><strong>timeout_member_connect</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The member connection timeout in milliseconds.</p></li>
<li><p><strong>timeout_member_data</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The member inactivity timeout in milliseconds.</p></li>
<li><p><strong>timeout_tcp_inspect</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in milliseconds, to wait for additional
TCP packets for content inspection.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.Listener.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.Listener.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Listener.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.LoadBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flavor_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">loadbalancer_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vip_subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 loadbalancer resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the Loadbalancer.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the Loadbalancer.</p></li>
<li><p><strong>flavor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of a flavor. Changing this creates a new
loadbalancer.</p></li>
<li><p><strong>loadbalancer_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the provider. Changing this
creates a new loadbalancer.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the Loadbalancer. Does not have
to be unique.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB member.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to apply to the
loadbalancer. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the Loadbalancer.  Only administrative users can specify a tenant UUID
other than their own.  Changing this creates a new loadbalancer.</p></li>
<li><p><strong>vip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ip address of the load balancer.
Changing this creates a new loadbalancer.</p></li>
<li><p><strong>vip_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network on which to allocate the
Loadbalancer’s address. A tenant can only create Loadbalancers on networks
authorized by policy (e.g. networks that belong to them or networks that
are shared).  Changing this creates a new loadbalancer.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the Loadbalancer.
A valid value is true (UP) or false (DOWN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description for the Loadbalancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.flavor_id">
<code class="sig-name descname">flavor_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.flavor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of a flavor. Changing this creates a new
loadbalancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.loadbalancer_provider">
<code class="sig-name descname">loadbalancer_provider</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.loadbalancer_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the provider. Changing this
creates a new loadbalancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable name for the Loadbalancer. Does not have
to be unique.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group IDs to apply to the
loadbalancer. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for admins. The UUID of the tenant who owns
the Loadbalancer.  Only administrative users can specify a tenant UUID
other than their own.  Changing this creates a new loadbalancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.vip_address">
<code class="sig-name descname">vip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.vip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The ip address of the load balancer.
Changing this creates a new loadbalancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.vip_port_id">
<code class="sig-name descname">vip_port_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.vip_port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Port ID of the Load Balancer IP.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.vip_subnet_id">
<code class="sig-name descname">vip_subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.vip_subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The network on which to allocate the
Loadbalancer’s address. A tenant can only create Loadbalancers on networks
authorized by policy (e.g. networks that belong to them or networks that
are shared).  Changing this creates a new loadbalancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flavor_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">loadbalancer_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vip_port_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vip_subnet_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the Loadbalancer.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the Loadbalancer.</p></li>
<li><p><strong>flavor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of a flavor. Changing this creates a new
loadbalancer.</p></li>
<li><p><strong>loadbalancer_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the provider. Changing this
creates a new loadbalancer.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the Loadbalancer. Does not have
to be unique.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB member.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to apply to the
loadbalancer. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the Loadbalancer.  Only administrative users can specify a tenant UUID
other than their own.  Changing this creates a new loadbalancer.</p></li>
<li><p><strong>vip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ip address of the load balancer.
Changing this creates a new loadbalancer.</p></li>
<li><p><strong>vip_port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Port ID of the Load Balancer IP.</p></li>
<li><p><strong>vip_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network on which to allocate the
Loadbalancer’s address. A tenant can only create Loadbalancers on networks
authorized by policy (e.g. networks that belong to them or networks that
are shared).  Changing this creates a new loadbalancer.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.LoadBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.Member">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">Member</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 member resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the member to receive traffic from
the load balancer. Changing this creates a new member.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the member.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the member.</p></li>
<li><p><strong>pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the pool that this member will be
assigned to.</p></li>
<li><p><strong>protocol_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which to listen for client traffic.
Changing this creates a new member.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
member.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subnet in which to access the member</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the member.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new member.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A positive integer value that indicates the relative
portion of traffic that this member should receive from the pool. For
example, a member with a weight of 10 receives five times as much traffic
as a member with a weight of 2.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Member.address">
<code class="sig-name descname">address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the member to receive traffic from
the load balancer. Changing this creates a new member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Member.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the member.
A valid value is true (UP) or false (DOWN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Member.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable name for the member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Member.pool_id">
<code class="sig-name descname">pool_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the pool that this member will be
assigned to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Member.protocol_port">
<code class="sig-name descname">protocol_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.protocol_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which to listen for client traffic.
Changing this creates a new member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Member.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Member.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subnet in which to access the member</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Member.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for admins. The UUID of the tenant who owns
the member.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Member.weight">
<code class="sig-name descname">weight</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>A positive integer value that indicates the relative
portion of traffic that this member should receive from the pool. For
example, a member with a weight of 10 receives five times as much traffic
as a member with a weight of 2.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.Member.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Member resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the member to receive traffic from
the load balancer. Changing this creates a new member.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the member.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the member.</p></li>
<li><p><strong>pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the pool that this member will be
assigned to.</p></li>
<li><p><strong>protocol_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which to listen for client traffic.
Changing this creates a new member.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
member.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subnet in which to access the member</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the member.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new member.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A positive integer value that indicates the relative
portion of traffic that this member should receive from the pool. For
example, a member with a weight of 10 receives five times as much traffic
as a member with a weight of 2.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.Member.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.Member.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Member.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.MemberV1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">MemberV1</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.MemberV1" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 load balancer member resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the member. Changing this creates a
new member.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the member.
Acceptable values are ‘true’ and ‘false’. Changing this value updates the
state of the existing member.</p></li>
<li><p><strong>pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the LB pool. Changing this creates a new
member.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – An integer representing the port on which the member is
hosted. Changing this creates a new member.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB member.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the member. Required if admin wants to
create a member for another tenant. Changing this creates a new member.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MemberV1.address">
<code class="sig-name descname">address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MemberV1.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the member. Changing this creates a
new member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MemberV1.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MemberV1.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the member.
Acceptable values are ‘true’ and ‘false’. Changing this value updates the
state of the existing member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MemberV1.pool_id">
<code class="sig-name descname">pool_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MemberV1.pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the LB pool. Changing this creates a new
member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MemberV1.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MemberV1.port" title="Permalink to this definition">¶</a></dt>
<dd><p>An integer representing the port on which the member is
hosted. Changing this creates a new member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MemberV1.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MemberV1.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MemberV1.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MemberV1.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the member. Required if admin wants to
create a member for another tenant. Changing this creates a new member.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.MemberV1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.MemberV1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MemberV1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the member. Changing this creates a
new member.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the member.
Acceptable values are ‘true’ and ‘false’. Changing this value updates the
state of the existing member.</p></li>
<li><p><strong>pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the LB pool. Changing this creates a new
member.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – An integer representing the port on which the member is
hosted. Changing this creates a new member.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB member. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB member.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the member. Required if admin wants to
create a member for another tenant. Changing this creates a new member.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.MemberV1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.MemberV1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.MemberV1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.MemberV1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.Monitor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">Monitor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries_down</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 monitor resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the monitor.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, between sending probes to members.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
“200”, or a range like “200-202”.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it
defaults to “GET”.</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of permissible ping failures before
changing the member’s status to INACTIVE. Must be a number between 1
and 10.</p></li>
<li><p><strong>max_retries_down</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of permissible ping failures befor changing the member’s
status to ERROR. Must be a number between 1 and 10 (supported only in Octavia).
Changing this updates the max_retries_down of the existing monitor.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Monitor.</p></li>
<li><p><strong>pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the pool that this monitor will be assigned to.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
monitor.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the monitor.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new monitor.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay
value.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of probe, which is PING, TCP, HTTP, HTTPS,
TLS-HELLO or UDP-CONNECT (supported only in Octavia), that is sent by the load
balancer to verify the member state. Changing this creates a new monitor.</p></li>
<li><p><strong>url_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the monitor.
A valid value is true (UP) or false (DOWN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.delay">
<code class="sig-name descname">delay</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.delay" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, between sending probes to members.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.expected_codes">
<code class="sig-name descname">expected_codes</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.expected_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
“200”, or a range like “200-202”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.http_method">
<code class="sig-name descname">http_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it
defaults to “GET”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.max_retries">
<code class="sig-name descname">max_retries</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.max_retries" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of permissible ping failures before
changing the member’s status to INACTIVE. Must be a number between 1
and 10.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.max_retries_down">
<code class="sig-name descname">max_retries_down</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.max_retries_down" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of permissible ping failures befor changing the member’s
status to ERROR. Must be a number between 1 and 10 (supported only in Octavia).
Changing this updates the max_retries_down of the existing monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.pool_id">
<code class="sig-name descname">pool_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the pool that this monitor will be assigned to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for admins. The UUID of the tenant who owns
the monitor.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.timeout">
<code class="sig-name descname">timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay
value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of probe, which is PING, TCP, HTTP, HTTPS,
TLS-HELLO or UDP-CONNECT (supported only in Octavia), that is sent by the load
balancer to verify the member state. Changing this creates a new monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Monitor.url_path">
<code class="sig-name descname">url_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.url_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.Monitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries_down</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_path</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Monitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the monitor.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, between sending probes to members.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
“200”, or a range like “200-202”.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it
defaults to “GET”.</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of permissible ping failures before
changing the member’s status to INACTIVE. Must be a number between 1
and 10.</p></li>
<li><p><strong>max_retries_down</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of permissible ping failures befor changing the member’s
status to ERROR. Must be a number between 1 and 10 (supported only in Octavia).
Changing this updates the max_retries_down of the existing monitor.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Monitor.</p></li>
<li><p><strong>pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the pool that this monitor will be assigned to.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
monitor.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the monitor.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new monitor.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay
value.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of probe, which is PING, TCP, HTTP, HTTPS,
TLS-HELLO or UDP-CONNECT (supported only in Octavia), that is sent by the load
balancer to verify the member state. Changing this creates a new monitor.</p></li>
<li><p><strong>url_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.Monitor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.Monitor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Monitor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.MonitorV1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">MonitorV1</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 load balancer monitor resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The administrative state of the monitor.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing monitor.</p></li>
<li><p><strong>delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, between sending probes to members.
Changing this creates a new monitor.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
“200”, or a range like “200-202”. Changing this updates the expected_codes
of the existing monitor.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to “GET”. Changing this updates the http_method of the existing monitor.</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of permissible ping failures before changing
the member’s status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB monitor.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.</p></li>
<li><p><strong>url_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the monitor.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.delay">
<code class="sig-name descname">delay</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.delay" title="Permalink to this definition">¶</a></dt>
<dd><p>The time, in seconds, between sending probes to members.
Changing this creates a new monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.expected_codes">
<code class="sig-name descname">expected_codes</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.expected_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
“200”, or a range like “200-202”. Changing this updates the expected_codes
of the existing monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.http_method">
<code class="sig-name descname">http_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to “GET”. Changing this updates the http_method of the existing monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.max_retries">
<code class="sig-name descname">max_retries</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.max_retries" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of permissible ping failures before changing
the member’s status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.timeout">
<code class="sig-name descname">timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.url_path">
<code class="sig-name descname">url_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.url_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_codes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url_path</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MonitorV1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The administrative state of the monitor.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing monitor.</p></li>
<li><p><strong>delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time, in seconds, between sending probes to members.
Changing this creates a new monitor.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. Expected HTTP codes
for a passing HTTP(S) monitor. You can either specify a single status like
“200”, or a range like “200-202”. Changing this updates the expected_codes
of the existing monitor.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. The HTTP method used
for requests by the monitor. If this attribute is not specified, it defaults
to “GET”. Changing this updates the http_method of the existing monitor.</p></li>
<li><p><strong>max_retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of permissible ping failures before changing
the member’s status to INACTIVE. Must be a number between 1 and 10. Changing
this updates the max_retries of the existing monitor.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB monitor. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB monitor.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the monitor. Required if admin wants to
create a monitor for another tenant. Changing this creates a new monitor.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of seconds for a monitor to wait for a
ping reply before it times out. The value must be less than the delay value.
Changing this updates the timeout of the existing monitor.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of probe, which is PING, TCP, HTTP, or HTTPS,
that is sent by the monitor to verify the member state. Changing this
creates a new monitor.</p></li>
<li><p><strong>url_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for HTTP(S) types. URI path that will be
accessed if monitor type is HTTP or HTTPS. Changing this updates the
url_path of the existing monitor.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.MonitorV1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.MonitorV1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.MonitorV1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.Pool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">Pool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lb_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">loadbalancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persistence</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 pool resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the pool.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the pool.</p></li>
<li><p><strong>lb_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The load balancing algorithm to
distribute traffic to the pool’s members. Must be one of
ROUND_ROBIN, LEAST_CONNECTIONS, or SOURCE_IP.</p></li>
<li><p><strong>listener_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Listener on which the members of the pool
will be associated with. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The load balancer on which to provision this
pool. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the pool.</p></li>
<li><p><strong>persistence</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Omit this field to prevent session persistence.  Indicates
whether connections in the same session will be processed by the same Pool
member or not. Changing this creates a new pool.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol - can either be TCP, HTTP, HTTPS, PROXY
or UDP (supported only in Octavia). Changing this creates a new pool.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
pool.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the pool.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new pool.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>persistence</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cookie if persistence mode is set
appropriately. Required if <code class="docutils literal notranslate"><span class="pre">type</span> <span class="pre">=</span> <span class="pre">APP_COOKIE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of persistence mode. The current specification
supports SOURCE_IP, HTTP_COOKIE, and APP_COOKIE.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Pool.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the pool.
A valid value is true (UP) or false (DOWN).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Pool.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description for the pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Pool.lb_method">
<code class="sig-name descname">lb_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.lb_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The load balancing algorithm to
distribute traffic to the pool’s members. Must be one of
ROUND_ROBIN, LEAST_CONNECTIONS, or SOURCE_IP.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Pool.listener_id">
<code class="sig-name descname">listener_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.listener_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Listener on which the members of the pool
will be associated with. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Pool.loadbalancer_id">
<code class="sig-name descname">loadbalancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The load balancer on which to provision this
pool. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Pool.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable name for the pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Pool.persistence">
<code class="sig-name descname">persistence</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.persistence" title="Permalink to this definition">¶</a></dt>
<dd><p>Omit this field to prevent session persistence.  Indicates
whether connections in the same session will be processed by the same Pool
member or not. Changing this creates a new pool.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the cookie if persistence mode is set
appropriately. Required if <code class="docutils literal notranslate"><span class="pre">type</span> <span class="pre">=</span> <span class="pre">APP_COOKIE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of persistence mode. The current specification
supports SOURCE_IP, HTTP_COOKIE, and APP_COOKIE.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Pool.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol - can either be TCP, HTTP, HTTPS, PROXY
or UDP (supported only in Octavia). Changing this creates a new pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Pool.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Pool.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required for admins. The UUID of the tenant who owns
the pool.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new pool.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.Pool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lb_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">loadbalancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persistence</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the pool.
A valid value is true (UP) or false (DOWN).</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the pool.</p></li>
<li><p><strong>lb_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The load balancing algorithm to
distribute traffic to the pool’s members. Must be one of
ROUND_ROBIN, LEAST_CONNECTIONS, or SOURCE_IP.</p></li>
<li><p><strong>listener_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Listener on which the members of the pool
will be associated with. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The load balancer on which to provision this
pool. Changing this creates a new pool.
Note:  One of LoadbalancerID or ListenerID must be provided.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable name for the pool.</p></li>
<li><p><strong>persistence</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Omit this field to prevent session persistence.  Indicates
whether connections in the same session will be processed by the same Pool
member or not. Changing this creates a new pool.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol - can either be TCP, HTTP, HTTPS, PROXY
or UDP (supported only in Octavia). Changing this creates a new pool.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an . If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
pool.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required for admins. The UUID of the tenant who owns
the pool.  Only administrative users can specify a tenant UUID
other than their own. Changing this creates a new pool.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>persistence</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cookie if persistence mode is set
appropriately. Required if <code class="docutils literal notranslate"><span class="pre">type</span> <span class="pre">=</span> <span class="pre">APP_COOKIE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of persistence mode. The current specification
supports SOURCE_IP, HTTP_COOKIE, and APP_COOKIE.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.Pool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.Pool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Pool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.PoolV1">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">PoolV1</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lb_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lb_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 load balancer pool resource within OpenStack.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">member</span></code> block is deprecated in favor of the <code class="docutils literal notranslate"><span class="pre">loadbalancer.MemberV1</span></code> resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>lb_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The algorithm used to distribute load between the
members of the pool. The current specification supports ‘ROUND_ROBIN’ and
‘LEAST_CONNECTIONS’ as valid values for this attribute.</p></li>
<li><p><strong>lb_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The backend load balancing provider. For example:
<code class="docutils literal notranslate"><span class="pre">haproxy</span></code>, <code class="docutils literal notranslate"><span class="pre">F5</span></code>, etc.</p></li>
<li><p><strong>monitor_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IDs of monitors to associate with the
pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pool. Changing this updates the name of
the existing pool.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol used by the pool members, you can use
either ‘TCP, ‘HTTP’, or ‘HTTPS’. Changing this creates a new pool.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB pool. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB pool.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network on which the members of the pool will be
located. Only members that are on this network can be added to the pool.
Changing this creates a new pool.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the member. Required if admin wants to
create a pool member for another tenant. Changing this creates a new member.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.PoolV1.lb_method">
<code class="sig-name descname">lb_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.lb_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The algorithm used to distribute load between the
members of the pool. The current specification supports ‘ROUND_ROBIN’ and
‘LEAST_CONNECTIONS’ as valid values for this attribute.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.PoolV1.lb_provider">
<code class="sig-name descname">lb_provider</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.lb_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The backend load balancing provider. For example:
<code class="docutils literal notranslate"><span class="pre">haproxy</span></code>, <code class="docutils literal notranslate"><span class="pre">F5</span></code>, etc.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.PoolV1.monitor_ids">
<code class="sig-name descname">monitor_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.monitor_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IDs of monitors to associate with the
pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.PoolV1.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pool. Changing this updates the name of
the existing pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.PoolV1.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol used by the pool members, you can use
either ‘TCP, ‘HTTP’, or ‘HTTPS’. Changing this creates a new pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.PoolV1.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB pool. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.PoolV1.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The network on which the members of the pool will be
located. Only members that are on this network can be added to the pool.
Changing this creates a new pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.PoolV1.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the member. Required if admin wants to
create a pool member for another tenant. Changing this creates a new member.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.PoolV1.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lb_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lb_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PoolV1 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>lb_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The algorithm used to distribute load between the
members of the pool. The current specification supports ‘ROUND_ROBIN’ and
‘LEAST_CONNECTIONS’ as valid values for this attribute.</p></li>
<li><p><strong>lb_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The backend load balancing provider. For example:
<code class="docutils literal notranslate"><span class="pre">haproxy</span></code>, <code class="docutils literal notranslate"><span class="pre">F5</span></code>, etc.</p></li>
<li><p><strong>monitor_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IDs of monitors to associate with the
pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pool. Changing this updates the name of
the existing pool.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol used by the pool members, you can use
either ‘TCP, ‘HTTP’, or ‘HTTPS’. Changing this creates a new pool.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB pool. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
LB pool.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network on which the members of the pool will be
located. Only members that are on this network can be added to the pool.
Changing this creates a new pool.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the member. Required if admin wants to
create a pool member for another tenant. Changing this creates a new member.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.PoolV1.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.PoolV1.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.PoolV1.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.Vip">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.loadbalancer.</code><code class="sig-name descname">Vip</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conn_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">floating_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persistence</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 load balancer vip resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the vip. Changing this creates a new
vip.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the vip.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing vip.</p></li>
<li><p><strong>conn_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the vip. Changing
this updates the description of the existing vip.</p></li>
<li><p><strong>floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <em>Networking</em> Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vip. Changing this updates the name of
the existing vip.</p></li>
<li><p><strong>persistence</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.</p></li>
<li><p><strong>pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which to listen for client traffic. Changing
this creates a new vip.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol - can be either ‘TCP, ‘HTTP’, or
HTTPS’. Changing this creates a new vip.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
VIP.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network on which to allocate the vip’s address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.address">
<code class="sig-name descname">address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the vip. Changing this creates a new
vip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the vip.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing vip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.conn_limit">
<code class="sig-name descname">conn_limit</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.conn_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description for the vip. Changing
this updates the description of the existing vip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.floating_ip">
<code class="sig-name descname">floating_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>A <em>Networking</em> Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vip. Changing this updates the name of
the existing vip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.persistence">
<code class="sig-name descname">persistence</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.persistence" title="Permalink to this definition">¶</a></dt>
<dd><p>Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.pool_id">
<code class="sig-name descname">pool_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which to listen for client traffic. Changing
this creates a new vip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.port_id">
<code class="sig-name descname">port_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Port UUID for this VIP at associated floating IP (if any).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol - can be either ‘TCP, ‘HTTP’, or
HTTPS’. Changing this creates a new vip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
VIP.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The network on which to allocate the vip’s address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_openstack.loadbalancer.Vip.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.Vip.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_state_up</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conn_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">floating_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">persistence</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Vip resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the vip. Changing this creates a new
vip.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the vip.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing vip.</p></li>
<li><p><strong>conn_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the vip. Changing
this updates the description of the existing vip.</p></li>
<li><p><strong>floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <em>Networking</em> Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vip. Changing this updates the name of
the existing vip.</p></li>
<li><p><strong>persistence</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.</p></li>
<li><p><strong>pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which to listen for client traffic. Changing
this creates a new vip.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Port UUID for this VIP at associated floating IP (if any).</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol - can be either ‘TCP, ‘HTTP’, or
HTTPS’. Changing this creates a new vip.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
VIP.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network on which to allocate the vip’s address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_openstack.loadbalancer.Vip.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.loadbalancer.Vip.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.loadbalancer.Vip.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
