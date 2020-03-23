---
title: Module group
title_tag: Module group | Package pulumi_okta | Python SDK
linktitle: group
notitle: true
---

<div class="section" id="group">
<h1>group<a class="headerlink" href="#group" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-okta/issues">pulumi/pulumi-okta repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-okta/issues">terraform-providers/terraform-provider-okta repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_okta.group"></span><dl class="class">
<dt id="pulumi_okta.group.AwaitableGetEveryoneGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.group.</code><code class="sig-name descname">AwaitableGetEveryoneGroupResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">include_users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.AwaitableGetEveryoneGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.group.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.group.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">include_users=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_okta.group.GetEveryoneGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.group.</code><code class="sig-name descname">GetEveryoneGroupResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">include_users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.GetEveryoneGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEveryoneGroup.</p>
<dl class="attribute">
<dt id="pulumi_okta.group.GetEveryoneGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.GetEveryoneGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.group.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.group.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">include_users=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_okta.group.GetGroupResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.GetGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>description of group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.group.GetGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.group.GetGroupResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.GetGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>name of group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.group.GetGroupResult.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.GetGroupResult.users" title="Permalink to this definition">¶</a></dt>
<dd><p>user ids that are members of this group, only included if <code class="docutils literal notranslate"><span class="pre">include_users</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_okta.group.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.group.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Okta Group.</p>
<p>This resource allows you to create and configure an Okta Group.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/group.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Okta Group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Okta Group.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the group. This can also be done per user.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.group.Group.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Okta Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.group.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Okta Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.group.Group.users">
<code class="sig-name descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.Group.users" title="Permalink to this definition">¶</a></dt>
<dd><p>Users associated with the group. This can also be done per user.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.group.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Okta Group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Okta Group.</p></li>
<li><p><strong>users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Users associated with the group. This can also be done per user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.group.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.group.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.group.Roles">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.group.</code><code class="sig-name descname">Roles</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_roles=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Roles" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates Group level Admin Role Assignments.</p>
<p>This resource allows you to create and configure Group level Admin Role Assignments.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/group_roles.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/group_roles.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Admin roles associated with the group. It can be any of the following values <code class="docutils literal notranslate"><span class="pre">&quot;SUPER_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ORG_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APP_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USER_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HELP_DESK_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MOBILE_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;API_ACCESS_MANAGEMENT_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;REPORT_ADMIN&quot;</span></code>.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of group to attach admin roles to.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.group.Roles.admin_roles">
<code class="sig-name descname">admin_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.Roles.admin_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>Admin roles associated with the group. It can be any of the following values <code class="docutils literal notranslate"><span class="pre">&quot;SUPER_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ORG_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APP_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USER_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HELP_DESK_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MOBILE_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;API_ACCESS_MANAGEMENT_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;REPORT_ADMIN&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.group.Roles.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.Roles.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of group to attach admin roles to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.group.Roles.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_roles=None</em>, <em class="sig-param">group_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Roles.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Roles resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Admin roles associated with the group. It can be any of the following values <code class="docutils literal notranslate"><span class="pre">&quot;SUPER_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ORG_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;APP_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;USER_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;HELP_DESK_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;READ_ONLY_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;MOBILE_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;API_ACCESS_MANAGEMENT_ADMIN&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;REPORT_ADMIN&quot;</span></code>.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of group to attach admin roles to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.group.Roles.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Roles.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.group.Roles.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Roles.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.group.Rule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_okta.group.</code><code class="sig-name descname">Rule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">expression_type=None</em>, <em class="sig-param">expression_value=None</em>, <em class="sig-param">group_assignments=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates an Okta Group Rule.</p>
<p>This resource allows you to create and configure an Okta Group Rule.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/group_rule.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/r/group_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expression_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expression type to use to invoke the rule. The default is <code class="docutils literal notranslate"><span class="pre">&quot;urn:okta:expression:1.0&quot;</span></code>.</p></li>
<li><p><strong>expression_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expression value.</p></li>
<li><p><strong>group_assignments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of group ids to assign the users to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Group Rule.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the group rule.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_okta.group.Rule.expression_type">
<code class="sig-name descname">expression_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.Rule.expression_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The expression type to use to invoke the rule. The default is <code class="docutils literal notranslate"><span class="pre">&quot;urn:okta:expression:1.0&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.group.Rule.expression_value">
<code class="sig-name descname">expression_value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.Rule.expression_value" title="Permalink to this definition">¶</a></dt>
<dd><p>The expression value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.group.Rule.group_assignments">
<code class="sig-name descname">group_assignments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.Rule.group_assignments" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of group ids to assign the users to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.group.Rule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Group Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_okta.group.Rule.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_okta.group.Rule.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the group rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.group.Rule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">expression_type=None</em>, <em class="sig-param">expression_value=None</em>, <em class="sig-param">group_assignments=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Rule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>expression_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expression type to use to invoke the rule. The default is <code class="docutils literal notranslate"><span class="pre">&quot;urn:okta:expression:1.0&quot;</span></code>.</p></li>
<li><p><strong>expression_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expression value.</p></li>
<li><p><strong>group_assignments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of group ids to assign the users to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Group Rule.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the group rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_okta.group.Rule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.group.Rule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_okta.group.get_everyone_group">
<code class="sig-prename descclassname">pulumi_okta.group.</code><code class="sig-name descname">get_everyone_group</code><span class="sig-paren">(</span><em class="sig-param">include_users=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.get_everyone_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve the Everyone group from Okta. The same can be achieved with the <code class="docutils literal notranslate"><span class="pre">group.Group</span></code> data source with <code class="docutils literal notranslate"><span class="pre">name</span> <span class="pre">=</span> <span class="pre">&quot;Everyone&quot;</span></code>. This is simply a shortcut.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/everyone_group.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/everyone_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_okta.group.get_group">
<code class="sig-prename descclassname">pulumi_okta.group.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param">include_users=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_okta.group.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve a group from Okta.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/group.html.markdown">https://github.com/articulate/terraform-provider-okta/blob/master/website/docs/d/group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>include_users</strong> (<em>bool</em>) – whether or not to retrieve all member ids.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – name of group to retrieve.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
