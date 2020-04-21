---
title: Package pulumi_aiven
title_tag: Package pulumi_aiven | Python SDK
linktitle: pulumi_aiven
notitle: true
---

<div class="section" id="module-pulumi_aiven">
<span id="pulumi-aiven"></span><h1>Pulumi Aiven<a class="headerlink" href="#module-pulumi_aiven" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aiven.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_team_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">update_time=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Account" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account name</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant id</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of last update</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.Account.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Account.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Account.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Account.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of creation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Account.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Account name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Account.owner_team_id">
<code class="sig-name descname">owner_team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Account.owner_team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Owner team id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Account.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Account.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Tenant id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Account.update_time">
<code class="sig-name descname">update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Account.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of last update</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_team_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">update_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account name</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant id</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of last update</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeam">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AccountTeam</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">update_time=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeam" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team name</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of last update</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.AccountTeam.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeam.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeam.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeam.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of creation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeam.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeam.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeam.team_id">
<code class="sig-name descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeam.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeam.update_time">
<code class="sig-name descname">update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeam.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of last update</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.AccountTeam.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">update_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeam.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountTeam resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team name</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team id</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of last update</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.AccountTeam.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeam.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeam.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeam.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AccountTeamMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accepted=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">invited_by_user_email=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">user_email=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>During the creation of <code class="docutils literal notranslate"><span class="pre">.AccountTeamMember</span></code> resource, an email invitation will be sent
to a user using <code class="docutils literal notranslate"><span class="pre">user_email</span></code> address. If the user accepts an invitation, he or she will become a member of the account team. 
The deletion of <code class="docutils literal notranslate"><span class="pre">.AccountTeamMember</span></code> will not only delete invitation if one was sent but not yet accepted by the 
user, and it will also eliminate an account team member if one has accepted an invitation previously.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accepted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Team member invitation status</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>invited_by_user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Team invited by user email</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team id</p></li>
<li><p><strong>user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Team invite user email</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.AccountTeamMember.accepted">
<code class="sig-name descname">accepted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.accepted" title="Permalink to this definition">¶</a></dt>
<dd><p>Team member invitation status</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeamMember.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeamMember.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of creation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeamMember.invited_by_user_email">
<code class="sig-name descname">invited_by_user_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.invited_by_user_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Team invited by user email</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeamMember.team_id">
<code class="sig-name descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeamMember.user_email">
<code class="sig-name descname">user_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.user_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Team invite user email</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.AccountTeamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accepted=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">invited_by_user_email=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">user_email=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountTeamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accepted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Team member invitation status</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>invited_by_user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Team invited by user email</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team id</p></li>
<li><p><strong>user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Team invite user email</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.AccountTeamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeamProject">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AccountTeamProject</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">team_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamProject" title="Permalink to this definition">¶</a></dt>
<dd><p>The account team project is intended to link and existing project to the existing account team. It is important to note 
that the project should have an <code class="docutils literal notranslate"><span class="pre">account_id</span></code> property set and equal to account team you are trying to link this project.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team project name</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team id</p></li>
<li><p><strong>team_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team project type, can one of the following values: admin, developer, operator and read_only</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.AccountTeamProject.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeamProject.project_name">
<code class="sig-name descname">project_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.project_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team project name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeamProject.team_id">
<code class="sig-name descname">team_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team id</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.AccountTeamProject.team_type">
<code class="sig-name descname">team_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.team_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team project type, can one of the following values: admin, developer, operator and read_only</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.AccountTeamProject.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">team_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountTeamProject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team project name</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team id</p></li>
<li><p><strong>team_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team project type, can one of the following values: admin, developer, operator and read_only</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.AccountTeamProject.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeamProject.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_team_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">update_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetAccountTeamMemberResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetAccountTeamMemberResult</code><span class="sig-paren">(</span><em class="sig-param">accepted=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">invited_by_user_email=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">user_email=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetAccountTeamMemberResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetAccountTeamProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetAccountTeamProjectResult</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">team_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetAccountTeamProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetAccountTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetAccountTeamResult</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">update_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetAccountTeamResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetConnectionPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetConnectionPoolResult</code><span class="sig-paren">(</span><em class="sig-param">connection_uri=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">pool_mode=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">pool_size=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetConnectionPoolResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetDatabaseResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetDatabaseResult</code><span class="sig-paren">(</span><em class="sig-param">database_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">lc_collate=None</em>, <em class="sig-param">lc_ctype=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">termination_protection=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetDatabaseResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetElasticSearchAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetElasticSearchAclResult</code><span class="sig-paren">(</span><em class="sig-param">acls=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extended_acl=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetElasticSearchAclResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetKafkaAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaAclResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">permission=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">topic=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaAclResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetKafkaConnectorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaConnectorResult</code><span class="sig-paren">(</span><em class="sig-param">config=None</em>, <em class="sig-param">connector_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">plugin_author=None</em>, <em class="sig-param">plugin_class=None</em>, <em class="sig-param">plugin_doc_url=None</em>, <em class="sig-param">plugin_title=None</em>, <em class="sig-param">plugin_type=None</em>, <em class="sig-param">plugin_version=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">tasks=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaConnectorResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetKafkaSchemaConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaSchemaConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaSchemaConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetKafkaSchemaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaSchemaResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaSchemaResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetKafkaTopicResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaTopicResult</code><span class="sig-paren">(</span><em class="sig-param">cleanup_policy=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">minimum_in_sync_replicas=None</em>, <em class="sig-param">partitions=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">replication=None</em>, <em class="sig-param">retention_bytes=None</em>, <em class="sig-param">retention_hours=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">termination_protection=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaTopicResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">billing_address=None</em>, <em class="sig-param">billing_emails=None</em>, <em class="sig-param">ca_cert=None</em>, <em class="sig-param">card_id=None</em>, <em class="sig-param">copy_from_project=None</em>, <em class="sig-param">country_code=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">technical_emails=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetProjectUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetProjectUserResult</code><span class="sig-paren">(</span><em class="sig-param">accepted=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">member_type=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetProjectUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetProjectVpcResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetProjectVpcResult</code><span class="sig-paren">(</span><em class="sig-param">cloud_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">network_cidr=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">state=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetProjectVpcResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetServiceIntegrationEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetServiceIntegrationEndpointResult</code><span class="sig-paren">(</span><em class="sig-param">datadog_user_config=None</em>, <em class="sig-param">endpoint_config=None</em>, <em class="sig-param">endpoint_name=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">external_elasticsearch_logs_user_config=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">prometheus_user_config=None</em>, <em class="sig-param">rsyslog_user_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetServiceIntegrationEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param">cassandra=None</em>, <em class="sig-param">cassandra_user_config=None</em>, <em class="sig-param">cloud_name=None</em>, <em class="sig-param">components=None</em>, <em class="sig-param">elasticsearch=None</em>, <em class="sig-param">elasticsearch_user_config=None</em>, <em class="sig-param">grafana=None</em>, <em class="sig-param">grafana_user_config=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">influxdb=None</em>, <em class="sig-param">influxdb_user_config=None</em>, <em class="sig-param">kafka=None</em>, <em class="sig-param">kafka_connect=None</em>, <em class="sig-param">kafka_connect_user_config=None</em>, <em class="sig-param">kafka_user_config=None</em>, <em class="sig-param">maintenance_window_dow=None</em>, <em class="sig-param">maintenance_window_time=None</em>, <em class="sig-param">mysql=None</em>, <em class="sig-param">mysql_user_config=None</em>, <em class="sig-param">pg=None</em>, <em class="sig-param">pg_user_config=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">project_vpc_id=None</em>, <em class="sig-param">redis=None</em>, <em class="sig-param">redis_user_config=None</em>, <em class="sig-param">service_host=None</em>, <em class="sig-param">service_integrations=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">service_password=None</em>, <em class="sig-param">service_port=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">service_uri=None</em>, <em class="sig-param">service_username=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">termination_protection=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetServiceUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetServiceUserResult</code><span class="sig-paren">(</span><em class="sig-param">access_cert=None</em>, <em class="sig-param">access_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetServiceUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.AwaitableGetVpcPeeringConnectionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetVpcPeeringConnectionResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">peer_cloud_account=None</em>, <em class="sig-param">peer_region=None</em>, <em class="sig-param">peer_vpc=None</em>, <em class="sig-param">peering_connection_id=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">state_info=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetVpcPeeringConnectionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aiven.ConnectionPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ConnectionPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">pool_mode=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">pool_size=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ConnectionPool" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database the pool connects to</p></li>
<li><p><strong>pool_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mode the pool operates in (session, transaction, statement)</p></li>
<li><p><strong>pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the pool</p></li>
<li><p><strong>pool_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of connections the pool may create towards the backend server</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the connection pool to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the connection pool to</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service user used to connect to the database</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.ConnectionPool.connection_uri">
<code class="sig-name descname">connection_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ConnectionPool.connection_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the pool</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ConnectionPool.database_name">
<code class="sig-name descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ConnectionPool.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the database the pool connects to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ConnectionPool.pool_mode">
<code class="sig-name descname">pool_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ConnectionPool.pool_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Mode the pool operates in (session, transaction, statement)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ConnectionPool.pool_name">
<code class="sig-name descname">pool_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ConnectionPool.pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the pool</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ConnectionPool.pool_size">
<code class="sig-name descname">pool_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ConnectionPool.pool_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of connections the pool may create towards the backend server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ConnectionPool.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ConnectionPool.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the connection pool to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ConnectionPool.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ConnectionPool.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the connection pool to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ConnectionPool.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ConnectionPool.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the service user used to connect to the database</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ConnectionPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_uri=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">pool_mode=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">pool_size=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ConnectionPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConnectionPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the pool</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database the pool connects to</p></li>
<li><p><strong>pool_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mode the pool operates in (session, transaction, statement)</p></li>
<li><p><strong>pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the pool</p></li>
<li><p><strong>pool_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of connections the pool may create towards the backend server</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the connection pool to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the connection pool to</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service user used to connect to the database</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ConnectionPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ConnectionPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ConnectionPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ConnectionPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">lc_collate=None</em>, <em class="sig-param">lc_ctype=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">termination_protection=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Database" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service database name</p></li>
<li><p><strong>lc_collate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default string sort order (LC_COLLATE) of the database. Default value: en_US.UTF-8</p></li>
<li><p><strong>lc_ctype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default character classification (LC_CTYPE) of the database. Default value: en_US.UTF-8</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the database to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the database to</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
recommended to enable this for any production databases containing critical data.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.Database.database_name">
<code class="sig-name descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Database.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service database name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Database.lc_collate">
<code class="sig-name descname">lc_collate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Database.lc_collate" title="Permalink to this definition">¶</a></dt>
<dd><p>Default string sort order (LC_COLLATE) of the database. Default value: en_US.UTF-8</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Database.lc_ctype">
<code class="sig-name descname">lc_ctype</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Database.lc_ctype" title="Permalink to this definition">¶</a></dt>
<dd><p>Default character classification (LC_CTYPE) of the database. Default value: en_US.UTF-8</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Database.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Database.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the database to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Database.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Database.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the database to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Database.termination_protection">
<code class="sig-name descname">termination_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Database.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
recommended to enable this for any production databases containing critical data.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">lc_collate=None</em>, <em class="sig-param">lc_ctype=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">termination_protection=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service database name</p></li>
<li><p><strong>lc_collate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default string sort order (LC_COLLATE) of the database. Default value: en_US.UTF-8</p></li>
<li><p><strong>lc_ctype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default character classification (LC_CTYPE) of the database. Default value: en_US.UTF-8</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the database to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the database to</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
recommended to enable this for any production databases containing critical data.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ElasticSearchAcl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ElasticSearchAcl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acls=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extended_acl=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ElasticSearchAcl resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] acls: List of Elasticsearch ACLs
:param pulumi.Input[bool] enabled: Enable Elasticsearch ACLs. When disabled authenticated service users have unrestricted access
:param pulumi.Input[bool] extended_acl: Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs (and only those) by enabling the</p>
<blockquote>
<div><p>ExtendedAcl option for the service. When it is enabled, users can use these APIs as long as all operations only target
indexes they have been granted access to</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Elasticsearch ACLs to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Elasticsearch ACLs to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permission</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aiven.ElasticSearchAcl.acls">
<code class="sig-name descname">acls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.acls" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Elasticsearch ACLs</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permission</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ElasticSearchAcl.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable Elasticsearch ACLs. When disabled authenticated service users have unrestricted access</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ElasticSearchAcl.extended_acl">
<code class="sig-name descname">extended_acl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.extended_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs (and only those) by enabling the
ExtendedAcl option for the service. When it is enabled, users can use these APIs as long as all operations only target
indexes they have been granted access to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ElasticSearchAcl.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the Elasticsearch ACLs to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ElasticSearchAcl.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the Elasticsearch ACLs to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ElasticSearchAcl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acls=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extended_acl=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ElasticSearchAcl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Elasticsearch ACLs</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Elasticsearch ACLs. When disabled authenticated service users have unrestricted access</p></li>
<li><p><strong>extended_acl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs (and only those) by enabling the
ExtendedAcl option for the service. When it is enabled, users can use these APIs as long as all operations only target
indexes they have been granted access to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Elasticsearch ACLs to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Elasticsearch ACLs to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permission</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ElasticSearchAcl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ElasticSearchAcl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_team_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">update_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetAccountTeamMemberResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetAccountTeamMemberResult</code><span class="sig-paren">(</span><em class="sig-param">accepted=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">invited_by_user_email=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">user_email=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetAccountTeamMemberResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountTeamMember.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetAccountTeamMemberResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetAccountTeamMemberResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetAccountTeamProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetAccountTeamProjectResult</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">team_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetAccountTeamProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountTeamProject.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetAccountTeamProjectResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetAccountTeamProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetAccountTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetAccountTeamResult</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">team_id=None</em>, <em class="sig-param">update_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetAccountTeamResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountTeam.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetAccountTeamResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetAccountTeamResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetConnectionPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetConnectionPoolResult</code><span class="sig-paren">(</span><em class="sig-param">connection_uri=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">pool_mode=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">pool_size=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetConnectionPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getConnectionPool.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetConnectionPoolResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetConnectionPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetDatabaseResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetDatabaseResult</code><span class="sig-paren">(</span><em class="sig-param">database_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">lc_collate=None</em>, <em class="sig-param">lc_ctype=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">termination_protection=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetDatabaseResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatabase.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetDatabaseResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetDatabaseResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetElasticSearchAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetElasticSearchAclResult</code><span class="sig-paren">(</span><em class="sig-param">acls=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extended_acl=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetElasticSearchAclResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getElasticSearchAcl.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetElasticSearchAclResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetElasticSearchAclResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetKafkaAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaAclResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">permission=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">topic=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaAclResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaAcl.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetKafkaAclResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetKafkaAclResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetKafkaConnectorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaConnectorResult</code><span class="sig-paren">(</span><em class="sig-param">config=None</em>, <em class="sig-param">connector_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">plugin_author=None</em>, <em class="sig-param">plugin_class=None</em>, <em class="sig-param">plugin_doc_url=None</em>, <em class="sig-param">plugin_title=None</em>, <em class="sig-param">plugin_type=None</em>, <em class="sig-param">plugin_version=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">tasks=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaConnectorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaConnector.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetKafkaConnectorResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetKafkaConnectorResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetKafkaSchemaConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaSchemaConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaSchemaConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaSchemaConfiguration.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetKafkaSchemaConfigurationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetKafkaSchemaConfigurationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetKafkaSchemaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaSchemaResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaSchemaResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaSchema.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetKafkaSchemaResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetKafkaSchemaResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetKafkaTopicResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaTopicResult</code><span class="sig-paren">(</span><em class="sig-param">cleanup_policy=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">minimum_in_sync_replicas=None</em>, <em class="sig-param">partitions=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">replication=None</em>, <em class="sig-param">retention_bytes=None</em>, <em class="sig-param">retention_hours=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">termination_protection=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaTopicResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaTopic.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetKafkaTopicResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetKafkaTopicResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">billing_address=None</em>, <em class="sig-param">billing_emails=None</em>, <em class="sig-param">ca_cert=None</em>, <em class="sig-param">card_id=None</em>, <em class="sig-param">copy_from_project=None</em>, <em class="sig-param">country_code=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">technical_emails=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetProjectResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetProjectUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetProjectUserResult</code><span class="sig-paren">(</span><em class="sig-param">accepted=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">member_type=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetProjectUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjectUser.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetProjectUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetProjectUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetProjectVpcResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetProjectVpcResult</code><span class="sig-paren">(</span><em class="sig-param">cloud_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">network_cidr=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">state=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetProjectVpcResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjectVpc.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetProjectVpcResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetProjectVpcResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetServiceIntegrationEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetServiceIntegrationEndpointResult</code><span class="sig-paren">(</span><em class="sig-param">datadog_user_config=None</em>, <em class="sig-param">endpoint_config=None</em>, <em class="sig-param">endpoint_name=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">external_elasticsearch_logs_user_config=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">prometheus_user_config=None</em>, <em class="sig-param">rsyslog_user_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetServiceIntegrationEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceIntegrationEndpoint.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetServiceIntegrationEndpointResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetServiceIntegrationEndpointResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param">cassandra=None</em>, <em class="sig-param">cassandra_user_config=None</em>, <em class="sig-param">cloud_name=None</em>, <em class="sig-param">components=None</em>, <em class="sig-param">elasticsearch=None</em>, <em class="sig-param">elasticsearch_user_config=None</em>, <em class="sig-param">grafana=None</em>, <em class="sig-param">grafana_user_config=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">influxdb=None</em>, <em class="sig-param">influxdb_user_config=None</em>, <em class="sig-param">kafka=None</em>, <em class="sig-param">kafka_connect=None</em>, <em class="sig-param">kafka_connect_user_config=None</em>, <em class="sig-param">kafka_user_config=None</em>, <em class="sig-param">maintenance_window_dow=None</em>, <em class="sig-param">maintenance_window_time=None</em>, <em class="sig-param">mysql=None</em>, <em class="sig-param">mysql_user_config=None</em>, <em class="sig-param">pg=None</em>, <em class="sig-param">pg_user_config=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">project_vpc_id=None</em>, <em class="sig-param">redis=None</em>, <em class="sig-param">redis_user_config=None</em>, <em class="sig-param">service_host=None</em>, <em class="sig-param">service_integrations=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">service_password=None</em>, <em class="sig-param">service_port=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">service_uri=None</em>, <em class="sig-param">service_username=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">termination_protection=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetServiceUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetServiceUserResult</code><span class="sig-paren">(</span><em class="sig-param">access_cert=None</em>, <em class="sig-param">access_key=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetServiceUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceUser.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetServiceUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetServiceUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.GetVpcPeeringConnectionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetVpcPeeringConnectionResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">peer_cloud_account=None</em>, <em class="sig-param">peer_region=None</em>, <em class="sig-param">peer_vpc=None</em>, <em class="sig-param">peering_connection_id=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">state_info=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetVpcPeeringConnectionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcPeeringConnection.</p>
<dl class="attribute">
<dt id="pulumi_aiven.GetVpcPeeringConnectionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.GetVpcPeeringConnectionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aiven.KafkaAcl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaAcl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">permission=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">topic=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaAcl" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permission</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka permission to grant (admin, read, readwrite, write)</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Kafka ACL to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Kafka ACL to</p></li>
<li><p><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic name pattern for the ACL entry</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username pattern for the ACL entry</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.KafkaAcl.permission">
<code class="sig-name descname">permission</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaAcl.permission" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka permission to grant (admin, read, readwrite, write)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaAcl.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaAcl.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the Kafka ACL to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaAcl.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaAcl.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the Kafka ACL to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaAcl.topic">
<code class="sig-name descname">topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaAcl.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Topic name pattern for the ACL entry</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaAcl.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaAcl.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username pattern for the ACL entry</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.KafkaAcl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">permission=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">topic=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaAcl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaAcl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permission</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka permission to grant (admin, read, readwrite, write)</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Kafka ACL to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Kafka ACL to</p></li>
<li><p><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic name pattern for the ACL entry</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username pattern for the ACL entry</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.KafkaAcl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaAcl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaConnector">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaConnector</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">config=None</em>, <em class="sig-param">connector_name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaConnector" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KafkaConnector resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] config: Kafka Connector configuration parameters
:param pulumi.Input[str] connector_name: Kafka connector name
:param pulumi.Input[str] project: Project to link the kafka connector to
:param pulumi.Input[str] service_name: Service to link the kafka connector to</p>
<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.config">
<code class="sig-name descname">config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Connector configuration parameters</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.connector_name">
<code class="sig-name descname">connector_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.connector_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.plugin_author">
<code class="sig-name descname">plugin_author</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_author" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector author</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.plugin_class">
<code class="sig-name descname">plugin_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector Java class</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.plugin_doc_url">
<code class="sig-name descname">plugin_doc_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_doc_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector documentation URL</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.plugin_title">
<code class="sig-name descname">plugin_title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_title" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector title</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.plugin_type">
<code class="sig-name descname">plugin_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector type</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.plugin_version">
<code class="sig-name descname">plugin_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector version</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the kafka connector to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the kafka connector to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaConnector.tasks">
<code class="sig-name descname">tasks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaConnector.tasks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tasks of a connector</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">task</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.KafkaConnector.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">config=None</em>, <em class="sig-param">connector_name=None</em>, <em class="sig-param">plugin_author=None</em>, <em class="sig-param">plugin_class=None</em>, <em class="sig-param">plugin_doc_url=None</em>, <em class="sig-param">plugin_title=None</em>, <em class="sig-param">plugin_type=None</em>, <em class="sig-param">plugin_version=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">tasks=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaConnector.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaConnector resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kafka Connector configuration parameters</p></li>
<li><p><strong>connector_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector name</p></li>
<li><p><strong>plugin_author</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector author</p></li>
<li><p><strong>plugin_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector Java class</p></li>
<li><p><strong>plugin_doc_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector documentation URL</p></li>
<li><p><strong>plugin_title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector title</p></li>
<li><p><strong>plugin_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector type</p></li>
<li><p><strong>plugin_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector version</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the kafka connector to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the kafka connector to</p></li>
<li><p><strong>tasks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of tasks of a connector</p></li>
</ul>
</dd>
</dl>
<p>The <strong>tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">task</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.KafkaConnector.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaConnector.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaConnector.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaConnector.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaSchema">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaSchema</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchema" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KafkaSchema resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] project: Project to link the Kafka Schema to
:param pulumi.Input[str] schema: Kafka Schema configuration should be a valid Avro Schema JSON format
:param pulumi.Input[str] service_name: Service to link the Kafka Schema to
:param pulumi.Input[str] subject_name: Kafka Schema Subject name</p>
<dl class="attribute">
<dt id="pulumi_aiven.KafkaSchema.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaSchema.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the Kafka Schema to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaSchema.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaSchema.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Schema configuration should be a valid Avro Schema JSON format</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaSchema.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaSchema.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the Kafka Schema to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaSchema.subject_name">
<code class="sig-name descname">subject_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaSchema.subject_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Schema Subject name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaSchema.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaSchema.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Schema configuration version</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.KafkaSchema.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchema.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaSchema resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Kafka Schema to</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka Schema configuration should be a valid Avro Schema JSON format</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Kafka Schema to</p></li>
<li><p><strong>subject_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka Schema Subject name</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Kafka Schema configuration version</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.KafkaSchema.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchema.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaSchema.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchema.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaSchemaConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaSchemaConfiguration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compatibility_level=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KafkaSchemaConfiguration resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] compatibility_level: Kafka Schemas compatibility level
:param pulumi.Input[str] project: Project to link the Kafka Schemas Configuration to
:param pulumi.Input[str] service_name: Service to link the Kafka Schemas Configuration to</p>
<dl class="attribute">
<dt id="pulumi_aiven.KafkaSchemaConfiguration.compatibility_level">
<code class="sig-name descname">compatibility_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.compatibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Schemas compatibility level</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaSchemaConfiguration.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the Kafka Schemas Configuration to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaSchemaConfiguration.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the Kafka Schemas Configuration to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.KafkaSchemaConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compatibility_level=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaSchemaConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compatibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka Schemas compatibility level</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Kafka Schemas Configuration to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Kafka Schemas Configuration to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.KafkaSchemaConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaSchemaConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaTopic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaTopic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cleanup_policy=None</em>, <em class="sig-param">minimum_in_sync_replicas=None</em>, <em class="sig-param">partitions=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">replication=None</em>, <em class="sig-param">retention_bytes=None</em>, <em class="sig-param">retention_hours=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">termination_protection=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaTopic" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cleanup_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic cleanup policy. Allowed values: delete, compact</p></li>
<li><p><strong>minimum_in_sync_replicas</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum required nodes in-sync replicas (ISR) to produce to a partition</p></li>
<li><p><strong>partitions</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of partitions to create in the topic</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the kafka topic to</p></li>
<li><p><strong>replication</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Replication factor for the topic</p></li>
<li><p><strong>retention_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention bytes</p></li>
<li><p><strong>retention_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention period (hours)</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the kafka topic to</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is a Terraform client-side deletion protection, which prevents a Kafka topic from being deleted. It is recommended to
enable this for any production Kafka topic containing critical data.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic name</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.KafkaTopic.cleanup_policy">
<code class="sig-name descname">cleanup_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaTopic.cleanup_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Topic cleanup policy. Allowed values: delete, compact</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaTopic.minimum_in_sync_replicas">
<code class="sig-name descname">minimum_in_sync_replicas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaTopic.minimum_in_sync_replicas" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum required nodes in-sync replicas (ISR) to produce to a partition</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaTopic.partitions">
<code class="sig-name descname">partitions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaTopic.partitions" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of partitions to create in the topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaTopic.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaTopic.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the kafka topic to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaTopic.replication">
<code class="sig-name descname">replication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaTopic.replication" title="Permalink to this definition">¶</a></dt>
<dd><p>Replication factor for the topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaTopic.retention_bytes">
<code class="sig-name descname">retention_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaTopic.retention_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Retention bytes</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaTopic.retention_hours">
<code class="sig-name descname">retention_hours</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaTopic.retention_hours" title="Permalink to this definition">¶</a></dt>
<dd><p>Retention period (hours)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaTopic.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaTopic.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the kafka topic to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaTopic.termination_protection">
<code class="sig-name descname">termination_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaTopic.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>It is a Terraform client-side deletion protection, which prevents a Kafka topic from being deleted. It is recommended to
enable this for any production Kafka topic containing critical data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.KafkaTopic.topic_name">
<code class="sig-name descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.KafkaTopic.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Topic name</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.KafkaTopic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cleanup_policy=None</em>, <em class="sig-param">minimum_in_sync_replicas=None</em>, <em class="sig-param">partitions=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">replication=None</em>, <em class="sig-param">retention_bytes=None</em>, <em class="sig-param">retention_hours=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">termination_protection=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaTopic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaTopic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cleanup_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic cleanup policy. Allowed values: delete, compact</p></li>
<li><p><strong>minimum_in_sync_replicas</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum required nodes in-sync replicas (ISR) to produce to a partition</p></li>
<li><p><strong>partitions</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of partitions to create in the topic</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the kafka topic to</p></li>
<li><p><strong>replication</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Replication factor for the topic</p></li>
<li><p><strong>retention_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention bytes</p></li>
<li><p><strong>retention_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention period (hours)</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the kafka topic to</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is a Terraform client-side deletion protection, which prevents a Kafka topic from being deleted. It is recommended to
enable this for any production Kafka topic containing critical data.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic name</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.KafkaTopic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaTopic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaTopic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaTopic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">billing_address=None</em>, <em class="sig-param">billing_emails=None</em>, <em class="sig-param">ca_cert=None</em>, <em class="sig-param">card_id=None</em>, <em class="sig-param">copy_from_project=None</em>, <em class="sig-param">country_code=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">technical_emails=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Project" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account ID</p></li>
<li><p><strong>billing_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Billing name and address of the project</p></li>
<li><p><strong>billing_emails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Billing contact emails of the project</p></li>
<li><p><strong>ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project root CA. This is used by some services like Kafka to sign service certificate</p></li>
<li><p><strong>card_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Credit card ID</p></li>
<li><p><strong>copy_from_project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Copy properties from another project. Only has effect when a new project is created.</p></li>
<li><p><strong>country_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Billing country code of the project</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project name</p></li>
<li><p><strong>technical_emails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Technical contact emails of the project</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.Project.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Project.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Project.billing_address">
<code class="sig-name descname">billing_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Project.billing_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Billing name and address of the project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Project.billing_emails">
<code class="sig-name descname">billing_emails</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Project.billing_emails" title="Permalink to this definition">¶</a></dt>
<dd><p>Billing contact emails of the project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Project.ca_cert">
<code class="sig-name descname">ca_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Project.ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>Project root CA. This is used by some services like Kafka to sign service certificate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Project.card_id">
<code class="sig-name descname">card_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Project.card_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Credit card ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Project.copy_from_project">
<code class="sig-name descname">copy_from_project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Project.copy_from_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Copy properties from another project. Only has effect when a new project is created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Project.country_code">
<code class="sig-name descname">country_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Project.country_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Billing country code of the project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Project.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Project.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Project.technical_emails">
<code class="sig-name descname">technical_emails</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Project.technical_emails" title="Permalink to this definition">¶</a></dt>
<dd><p>Technical contact emails of the project</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">billing_address=None</em>, <em class="sig-param">billing_emails=None</em>, <em class="sig-param">ca_cert=None</em>, <em class="sig-param">card_id=None</em>, <em class="sig-param">copy_from_project=None</em>, <em class="sig-param">country_code=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">technical_emails=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account ID</p></li>
<li><p><strong>billing_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Billing name and address of the project</p></li>
<li><p><strong>billing_emails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Billing contact emails of the project</p></li>
<li><p><strong>ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project root CA. This is used by some services like Kafka to sign service certificate</p></li>
<li><p><strong>card_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Credit card ID</p></li>
<li><p><strong>copy_from_project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Copy properties from another project. Only has effect when a new project is created.</p></li>
<li><p><strong>country_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Billing country code of the project</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project name</p></li>
<li><p><strong>technical_emails</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Technical contact emails of the project</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ProjectUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ProjectUser</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">member_type=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectUser" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address of the user</p></li>
<li><p><strong>member_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project membership type. One of: admin, developer, operator</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project the user belongs to</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.ProjectUser.accepted">
<code class="sig-name descname">accepted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ProjectUser.accepted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user has accepted project membership or not</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ProjectUser.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ProjectUser.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address of the user</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ProjectUser.member_type">
<code class="sig-name descname">member_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ProjectUser.member_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Project membership type. One of: admin, developer, operator</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ProjectUser.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ProjectUser.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project the user belongs to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ProjectUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accepted=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">member_type=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accepted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user has accepted project membership or not</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address of the user</p></li>
<li><p><strong>member_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project membership type. One of: admin, developer, operator</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project the user belongs to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ProjectUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ProjectUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ProjectVpc">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ProjectVpc</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloud_name=None</em>, <em class="sig-param">network_cidr=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectVpc" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the VPC is in</p></li>
<li><p><strong>network_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network address range used by the VPC like 192.168.0.0/24</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project the VPC belongs to</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.ProjectVpc.cloud_name">
<code class="sig-name descname">cloud_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ProjectVpc.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the VPC is in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ProjectVpc.network_cidr">
<code class="sig-name descname">network_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ProjectVpc.network_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>Network address range used by the VPC like 192.168.0.0/24</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ProjectVpc.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ProjectVpc.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project the VPC belongs to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ProjectVpc.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ProjectVpc.state" title="Permalink to this definition">¶</a></dt>
<dd><p>State of the VPC (APPROVED, ACTIVE, DELETING, DELETED)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ProjectVpc.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloud_name=None</em>, <em class="sig-param">network_cidr=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">state=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectVpc.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectVpc resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the VPC is in</p></li>
<li><p><strong>network_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network address range used by the VPC like 192.168.0.0/24</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project the VPC belongs to</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – State of the VPC (APPROVED, ACTIVE, DELETING, DELETED)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ProjectVpc.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectVpc.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ProjectVpc.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectVpc.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_token=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the aiven package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven Authentication Token</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_aiven.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cassandra=None</em>, <em class="sig-param">cassandra_user_config=None</em>, <em class="sig-param">cloud_name=None</em>, <em class="sig-param">elasticsearch=None</em>, <em class="sig-param">elasticsearch_user_config=None</em>, <em class="sig-param">grafana=None</em>, <em class="sig-param">grafana_user_config=None</em>, <em class="sig-param">influxdb=None</em>, <em class="sig-param">influxdb_user_config=None</em>, <em class="sig-param">kafka=None</em>, <em class="sig-param">kafka_connect=None</em>, <em class="sig-param">kafka_connect_user_config=None</em>, <em class="sig-param">kafka_user_config=None</em>, <em class="sig-param">maintenance_window_dow=None</em>, <em class="sig-param">maintenance_window_time=None</em>, <em class="sig-param">mysql=None</em>, <em class="sig-param">mysql_user_config=None</em>, <em class="sig-param">pg=None</em>, <em class="sig-param">pg_user_config=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">project_vpc_id=None</em>, <em class="sig-param">redis=None</em>, <em class="sig-param">redis_user_config=None</em>, <em class="sig-param">service_integrations=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">termination_protection=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Service" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cassandra</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Cassandra specific server provided values</p></li>
<li><p><strong>cassandra_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Cassandra specific user configurable settings</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>elasticsearch</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Elasticsearch specific server provided values</p></li>
<li><p><strong>elasticsearch_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Elasticsearch specific user configurable settings</p></li>
<li><p><strong>grafana</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Grafana specific server provided values</p></li>
<li><p><strong>grafana_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Grafana specific user configurable settings</p></li>
<li><p><strong>influxdb</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – InfluxDB specific server provided values</p></li>
<li><p><strong>influxdb_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – InfluxDB specific user configurable settings</p></li>
<li><p><strong>kafka</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kafka specific server provided values</p></li>
<li><p><strong>kafka_connect</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kafka Connect specific server provided values</p></li>
<li><p><strong>kafka_connect_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kafka Connect specific user configurable settings</p></li>
<li><p><strong>kafka_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kafka specific user configurable settings</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>mysql</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – MySQL specific server provided values</p></li>
<li><p><strong>mysql_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – MySQL specific user configurable settings</p></li>
<li><p><strong>pg</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – PostgreSQL specific server provided values</p></li>
<li><p><strong>pg_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – PostgreSQL specific user configurable settings</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>redis</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Redis specific server provided values</p></li>
<li><p><strong>redis_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Redis specific user configurable settings</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service type code</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cassandra_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">migrateSstableloader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>elasticsearch</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kibanaUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>elasticsearch_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableReplicationFactorAdjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionAutoCreateIndexEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">actionDestructiveRequiresName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMaxContentLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesFielddataCacheSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesMemoryIndexBufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesQueriesCacheSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesQueryBoolMaxClauseCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reindexRemoteWhitelists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolAnalyzeQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolAnalyzeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolForceMergeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolGetQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolGetSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolIndexQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolIndexSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchThrottledQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchThrottledSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolWriteQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolWriteSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexPatterns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIndexCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchRequestTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOldSpaceSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIndexCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryBasebackupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>grafana_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alertingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alertingErrorOrTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alertingNodataOrNullvalues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowEmbedding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGenericOauth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrganizations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGithub</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrganizations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGitlab</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGoogle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieSamesite</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dashboardsVersionsToKeep</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproxySendUserHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproxyTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableGravatar</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">editorsCanAdmin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">externalImageStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">googleAnalyticsUaId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">grafana</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">grafana</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fromAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipVerify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAutoAssignOrg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAutoAssignOrgRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewersCanEdit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>influxdb</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>influxdb_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">influxdb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">influxdb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>kafka</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_cert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistryUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>kafka_connect_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerIsolationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerMaxPollRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetFlushIntervalMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>kafka_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoCreateTopicsEnable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectionsMaxIdleMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultReplicationFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupMaxSessionTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupMinSessionTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMaxCompactionLagMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMinCleanableRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMinCompactionLagMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanupPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMessageTimestampDifferenceMaxMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMessageTimestampType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logRetentionBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logRetentionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logSegmentBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionsPerIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numPartitions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetsRetentionMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerPurgatoryPurgeIntervalRequests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaFetchMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaFetchResponseMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">socketRequestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaAuthenticationMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaConnectConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerIsolationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerMaxPollRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetFlushIntervalMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRestConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerEnableAutoCommit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerRequestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerRequestTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerAcks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerLingerMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">simpleconsumerPoolSizeMax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>mysql_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupMinute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultTimeZone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupConcatMaxLen</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">informationSchemaStatsExpiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbFtMinTokenSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbFtServerStopwordTable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbLockWaitTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbOnlineAlterLogMaxSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbRollbackOnTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAllowedPacket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netReadTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netWriteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlRequirePrimaryKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mysqlVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryTargetTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>pg</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dbname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslmode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>pg_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupMinute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumAnalyzeScaleFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumAnalyzeThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumMaxWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumNaptime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumCostDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumCostLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumScaleFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deadlockTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleInTransactionSessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logAutovacuumMinDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logErrorVerbosity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMinDurationStatement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxLocksPerTransaction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxParallelWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxParallelWorkersPerGather</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPredLocksPerTransaction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPreparedTransactions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStackDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStandbyArchiveDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStandbyStreamingDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWorkerProcesses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgStatStatementsTrack</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tempFileLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trackActivityQuerySize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trackFunctions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">walWriterDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgReadReplica</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgServiceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">serverResetQueryAlways</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pglookout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailoverReplicationTimeLag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryTargetTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timescaledb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackgroundWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">variant</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>redis_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">migration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisLfuDecayTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisLfuLogFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisMaxmemoryPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisNotifyKeyspaceEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>service_integrations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">integration_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aiven.Service.cassandra">
<code class="sig-name descname">cassandra</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.cassandra" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra specific server provided values</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.cassandra_user_config">
<code class="sig-name descname">cassandra_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.cassandra_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">migrateSstableloader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.cloud_name">
<code class="sig-name descname">cloud_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.components">
<code class="sig-name descname">components</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">component</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaAuthenticationMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">route</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.elasticsearch">
<code class="sig-name descname">elasticsearch</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.elasticsearch" title="Permalink to this definition">¶</a></dt>
<dd><p>Elasticsearch specific server provided values</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kibanaUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.elasticsearch_user_config">
<code class="sig-name descname">elasticsearch_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.elasticsearch_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Elasticsearch specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableReplicationFactorAdjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionAutoCreateIndexEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">actionDestructiveRequiresName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMaxContentLength</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesFielddataCacheSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesMemoryIndexBufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesQueriesCacheSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesQueryBoolMaxClauseCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reindexRemoteWhitelists</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolAnalyzeQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolAnalyzeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolForceMergeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolGetQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolGetSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolIndexQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolIndexSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchThrottledQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchThrottledSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolWriteQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolWriteSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexPatterns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIndexCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchRequestTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOldSpaceSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIndexCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryBasebackupName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.grafana">
<code class="sig-name descname">grafana</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.grafana" title="Permalink to this definition">¶</a></dt>
<dd><p>Grafana specific server provided values</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.grafana_user_config">
<code class="sig-name descname">grafana_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.grafana_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Grafana specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alertingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alertingErrorOrTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alertingNodataOrNullvalues</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowEmbedding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGenericOauth</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrganizations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGithub</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrganizations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGitlab</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGoogle</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieSamesite</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dashboardsVersionsToKeep</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproxySendUserHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproxyTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableGravatar</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">editorsCanAdmin</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">externalImageStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">googleAnalyticsUaId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">grafana</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">grafana</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpServer</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fromAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipVerify</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAutoAssignOrg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAutoAssignOrgRole</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewersCanEdit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.influxdb">
<code class="sig-name descname">influxdb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.influxdb" title="Permalink to this definition">¶</a></dt>
<dd><p>InfluxDB specific server provided values</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.influxdb_user_config">
<code class="sig-name descname">influxdb_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.influxdb_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>InfluxDB specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">influxdb</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">influxdb</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.kafka">
<code class="sig-name descname">kafka</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.kafka" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka specific server provided values</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_cert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistryUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.kafka_connect">
<code class="sig-name descname">kafka_connect</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.kafka_connect" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Connect specific server provided values</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.kafka_connect_user_config">
<code class="sig-name descname">kafka_connect_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.kafka_connect_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Connect specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerIsolationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerMaxPollRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetFlushIntervalMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.kafka_user_config">
<code class="sig-name descname">kafka_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.kafka_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoCreateTopicsEnable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectionsMaxIdleMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultReplicationFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupMaxSessionTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupMinSessionTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMaxCompactionLagMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMinCleanableRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMinCompactionLagMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanupPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMessageTimestampDifferenceMaxMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMessageTimestampType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logRetentionBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logRetentionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logSegmentBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionsPerIp</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numPartitions</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetsRetentionMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerPurgatoryPurgeIntervalRequests</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaFetchMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaFetchResponseMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">socketRequestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaAuthenticationMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaConnectConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerIsolationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerMaxPollRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetFlushIntervalMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRest</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRestConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerEnableAutoCommit</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerRequestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerRequestTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerAcks</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerLingerMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">simpleconsumerPoolSizeMax</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRest</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistry</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistry</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.maintenance_window_dow">
<code class="sig-name descname">maintenance_window_dow</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.maintenance_window_time">
<code class="sig-name descname">maintenance_window_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.mysql">
<code class="sig-name descname">mysql</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.mysql" title="Permalink to this definition">¶</a></dt>
<dd><p>MySQL specific server provided values</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.mysql_user_config">
<code class="sig-name descname">mysql_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.mysql_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>MySQL specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupHour</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupMinute</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultTimeZone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupConcatMaxLen</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">informationSchemaStatsExpiry</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbFtMinTokenSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbFtServerStopwordTable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbLockWaitTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbOnlineAlterLogMaxSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbRollbackOnTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAllowedPacket</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netReadTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netWriteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlRequirePrimaryKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mysqlVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryTargetTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.pg">
<code class="sig-name descname">pg</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.pg" title="Permalink to this definition">¶</a></dt>
<dd><p>PostgreSQL specific server provided values</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dbname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslmode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.pg_user_config">
<code class="sig-name descname">pg_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.pg_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>PostgreSQL specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupHour</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupMinute</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumAnalyzeScaleFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumAnalyzeThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumMaxWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumNaptime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumCostDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumCostLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumScaleFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deadlockTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleInTransactionSessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logAutovacuumMinDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logErrorVerbosity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMinDurationStatement</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxLocksPerTransaction</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxParallelWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxParallelWorkersPerGather</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPredLocksPerTransaction</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPreparedTransactions</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStackDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStandbyArchiveDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStandbyStreamingDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWorkerProcesses</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgStatStatementsTrack</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tempFileLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trackActivityQuerySize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trackFunctions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">walWriterDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgReadReplica</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgServiceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">serverResetQueryAlways</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pglookout</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailoverReplicationTimeLag</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryTargetTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timescaledb</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackgroundWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">variant</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.project_vpc_id">
<code class="sig-name descname">project_vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.redis">
<code class="sig-name descname">redis</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.redis" title="Permalink to this definition">¶</a></dt>
<dd><p>Redis specific server provided values</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.redis_user_config">
<code class="sig-name descname">redis_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.redis_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Redis specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">migration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redis</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redis</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisLfuDecayTime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisLfuLogFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisMaxmemoryPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisNotifyKeyspaceEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.service_host">
<code class="sig-name descname">service_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.service_integrations">
<code class="sig-name descname">service_integrations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">integration_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.service_password">
<code class="sig-name descname">service_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.service_port">
<code class="sig-name descname">service_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.service_type">
<code class="sig-name descname">service_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Service type code</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.service_uri">
<code class="sig-name descname">service_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.service_username">
<code class="sig-name descname">service_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.Service.termination_protection">
<code class="sig-name descname">termination_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.Service.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cassandra=None</em>, <em class="sig-param">cassandra_user_config=None</em>, <em class="sig-param">cloud_name=None</em>, <em class="sig-param">components=None</em>, <em class="sig-param">elasticsearch=None</em>, <em class="sig-param">elasticsearch_user_config=None</em>, <em class="sig-param">grafana=None</em>, <em class="sig-param">grafana_user_config=None</em>, <em class="sig-param">influxdb=None</em>, <em class="sig-param">influxdb_user_config=None</em>, <em class="sig-param">kafka=None</em>, <em class="sig-param">kafka_connect=None</em>, <em class="sig-param">kafka_connect_user_config=None</em>, <em class="sig-param">kafka_user_config=None</em>, <em class="sig-param">maintenance_window_dow=None</em>, <em class="sig-param">maintenance_window_time=None</em>, <em class="sig-param">mysql=None</em>, <em class="sig-param">mysql_user_config=None</em>, <em class="sig-param">pg=None</em>, <em class="sig-param">pg_user_config=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">project_vpc_id=None</em>, <em class="sig-param">redis=None</em>, <em class="sig-param">redis_user_config=None</em>, <em class="sig-param">service_host=None</em>, <em class="sig-param">service_integrations=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">service_password=None</em>, <em class="sig-param">service_port=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">service_uri=None</em>, <em class="sig-param">service_username=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">termination_protection=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cassandra</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Cassandra specific server provided values</p></li>
<li><p><strong>cassandra_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Cassandra specific user configurable settings</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>elasticsearch</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Elasticsearch specific server provided values</p></li>
<li><p><strong>elasticsearch_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Elasticsearch specific user configurable settings</p></li>
<li><p><strong>grafana</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Grafana specific server provided values</p></li>
<li><p><strong>grafana_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Grafana specific user configurable settings</p></li>
<li><p><strong>influxdb</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – InfluxDB specific server provided values</p></li>
<li><p><strong>influxdb_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – InfluxDB specific user configurable settings</p></li>
<li><p><strong>kafka</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kafka specific server provided values</p></li>
<li><p><strong>kafka_connect</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kafka Connect specific server provided values</p></li>
<li><p><strong>kafka_connect_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kafka Connect specific user configurable settings</p></li>
<li><p><strong>kafka_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kafka specific user configurable settings</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>mysql</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – MySQL specific server provided values</p></li>
<li><p><strong>mysql_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – MySQL specific user configurable settings</p></li>
<li><p><strong>pg</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – PostgreSQL specific server provided values</p></li>
<li><p><strong>pg_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – PostgreSQL specific user configurable settings</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>redis</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Redis specific server provided values</p></li>
<li><p><strong>redis_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Redis specific user configurable settings</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cassandra_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">migrateSstableloader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>components</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">component</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaAuthenticationMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">route</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>elasticsearch</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kibanaUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>elasticsearch_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableReplicationFactorAdjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionAutoCreateIndexEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">actionDestructiveRequiresName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMaxContentLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesFielddataCacheSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesMemoryIndexBufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesQueriesCacheSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesQueryBoolMaxClauseCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reindexRemoteWhitelists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolAnalyzeQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolAnalyzeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolForceMergeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolGetQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolGetSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolIndexQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolIndexSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchThrottledQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchThrottledSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolWriteQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolWriteSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexPatterns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIndexCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchRequestTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOldSpaceSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIndexCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryBasebackupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>grafana_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alertingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alertingErrorOrTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alertingNodataOrNullvalues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowEmbedding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGenericOauth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrganizations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGithub</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrganizations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGitlab</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGoogle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieSamesite</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dashboardsVersionsToKeep</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproxySendUserHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproxyTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableGravatar</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">editorsCanAdmin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">externalImageStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">googleAnalyticsUaId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">grafana</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">grafana</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fromAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipVerify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAutoAssignOrg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAutoAssignOrgRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewersCanEdit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>influxdb</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>influxdb_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">influxdb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">influxdb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>kafka</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_cert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistryUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>kafka_connect_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerIsolationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerMaxPollRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetFlushIntervalMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>kafka_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoCreateTopicsEnable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectionsMaxIdleMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultReplicationFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupMaxSessionTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupMinSessionTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMaxCompactionLagMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMinCleanableRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMinCompactionLagMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanupPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMessageTimestampDifferenceMaxMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMessageTimestampType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logRetentionBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logRetentionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logSegmentBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionsPerIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numPartitions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetsRetentionMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerPurgatoryPurgeIntervalRequests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaFetchMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaFetchResponseMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">socketRequestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaAuthenticationMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaConnectConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerIsolationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerMaxPollRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetFlushIntervalMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRestConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerEnableAutoCommit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerRequestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerRequestTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerAcks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerLingerMs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">simpleconsumerPoolSizeMax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>mysql_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupMinute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultTimeZone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupConcatMaxLen</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">informationSchemaStatsExpiry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbFtMinTokenSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbFtServerStopwordTable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbLockWaitTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbOnlineAlterLogMaxSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbRollbackOnTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAllowedPacket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netReadTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netWriteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlRequirePrimaryKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mysqlVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryTargetTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>pg</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dbname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslmode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>pg_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupMinute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumAnalyzeScaleFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumAnalyzeThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumMaxWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumNaptime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumCostDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumCostLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumScaleFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deadlockTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleInTransactionSessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logAutovacuumMinDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logErrorVerbosity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMinDurationStatement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxLocksPerTransaction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxParallelWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxParallelWorkersPerGather</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPredLocksPerTransaction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPreparedTransactions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStackDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStandbyArchiveDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStandbyStreamingDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWorkerProcesses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgStatStatementsTrack</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tempFileLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trackActivityQuerySize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trackFunctions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">walWriterDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgReadReplica</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgServiceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">serverResetQueryAlways</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pglookout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailoverReplicationTimeLag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryTargetTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timescaledb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackgroundWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">variant</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>redis_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">migration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisLfuDecayTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisLfuLogFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisMaxmemoryPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisNotifyKeyspaceEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>service_integrations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">integration_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ServiceIntegration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination_endpoint_id=None</em>, <em class="sig-param">destination_service_name=None</em>, <em class="sig-param">integration_type=None</em>, <em class="sig-param">logs_user_config=None</em>, <em class="sig-param">mirrormaker_user_config=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">source_endpoint_id=None</em>, <em class="sig-param">source_service_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegration" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination endpoint for the integration (if any)</p></li>
<li><p><strong>destination_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination service for the integration (if any)</p></li>
<li><p><strong>integration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the service integration</p></li>
<li><p><strong>logs_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Log integration specific user configurable settings</p></li>
<li><p><strong>mirrormaker_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Mirrormaker integration specific user configurable settings</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project the integration belongs to</p></li>
<li><p><strong>source_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source endpoint for the integration (if any)</p></li>
<li><p><strong>source_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source service for the integration (if any)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>logs_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchIndexDaysMax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchIndexPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>mirrormaker_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mirrormakerWhitelist</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegration.destination_endpoint_id">
<code class="sig-name descname">destination_endpoint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.destination_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination endpoint for the integration (if any)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegration.destination_service_name">
<code class="sig-name descname">destination_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.destination_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination service for the integration (if any)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegration.integration_type">
<code class="sig-name descname">integration_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.integration_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the service integration</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegration.logs_user_config">
<code class="sig-name descname">logs_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.logs_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Log integration specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchIndexDaysMax</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchIndexPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegration.mirrormaker_user_config">
<code class="sig-name descname">mirrormaker_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.mirrormaker_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Mirrormaker integration specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mirrormakerWhitelist</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegration.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project the integration belongs to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegration.source_endpoint_id">
<code class="sig-name descname">source_endpoint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.source_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Source endpoint for the integration (if any)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegration.source_service_name">
<code class="sig-name descname">source_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.source_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Source service for the integration (if any)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ServiceIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination_endpoint_id=None</em>, <em class="sig-param">destination_service_name=None</em>, <em class="sig-param">integration_type=None</em>, <em class="sig-param">logs_user_config=None</em>, <em class="sig-param">mirrormaker_user_config=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">source_endpoint_id=None</em>, <em class="sig-param">source_service_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination endpoint for the integration (if any)</p></li>
<li><p><strong>destination_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination service for the integration (if any)</p></li>
<li><p><strong>integration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the service integration</p></li>
<li><p><strong>logs_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Log integration specific user configurable settings</p></li>
<li><p><strong>mirrormaker_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Mirrormaker integration specific user configurable settings</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project the integration belongs to</p></li>
<li><p><strong>source_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source endpoint for the integration (if any)</p></li>
<li><p><strong>source_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source service for the integration (if any)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>logs_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchIndexDaysMax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchIndexPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>mirrormaker_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mirrormakerWhitelist</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ServiceIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceIntegrationEndpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ServiceIntegrationEndpoint</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">datadog_user_config=None</em>, <em class="sig-param">endpoint_name=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">external_elasticsearch_logs_user_config=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">prometheus_user_config=None</em>, <em class="sig-param">rsyslog_user_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>datadog_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Datadog specific user configurable settings</p></li>
<li><p><strong>endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service integration endpoint</p></li>
<li><p><strong>endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the service integration endpoint</p></li>
<li><p><strong>external_elasticsearch_logs_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – external elasticsearch specific user configurable settings</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project the service integration endpoint belongs to</p></li>
<li><p><strong>prometheus_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Prometheus specific user configurable settings</p></li>
<li><p><strong>rsyslog_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – rsyslog specific user configurable settings</p></li>
</ul>
</dd>
</dl>
<p>The <strong>datadog_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datadogApiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableConsumerStats</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPartitionContexts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">site</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>external_elasticsearch_logs_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ca</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexDaysMax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>prometheus_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">basicAuthPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">basicAuthUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rsyslog_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ca</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sd</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.datadog_user_config">
<code class="sig-name descname">datadog_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.datadog_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Datadog specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datadogApiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableConsumerStats</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPartitionContexts</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">site</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.endpoint_config">
<code class="sig-name descname">endpoint_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.endpoint_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Integration endpoint specific backend configuration</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.endpoint_name">
<code class="sig-name descname">endpoint_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the service integration endpoint</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.endpoint_type">
<code class="sig-name descname">endpoint_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.endpoint_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the service integration endpoint</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.external_elasticsearch_logs_user_config">
<code class="sig-name descname">external_elasticsearch_logs_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.external_elasticsearch_logs_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>external elasticsearch specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ca</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexDaysMax</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project the service integration endpoint belongs to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.prometheus_user_config">
<code class="sig-name descname">prometheus_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.prometheus_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Prometheus specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">basicAuthPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">basicAuthUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.rsyslog_user_config">
<code class="sig-name descname">rsyslog_user_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.rsyslog_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>rsyslog specific user configurable settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ca</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logline</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sd</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">datadog_user_config=None</em>, <em class="sig-param">endpoint_config=None</em>, <em class="sig-param">endpoint_name=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">external_elasticsearch_logs_user_config=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">prometheus_user_config=None</em>, <em class="sig-param">rsyslog_user_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceIntegrationEndpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>datadog_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Datadog specific user configurable settings</p></li>
<li><p><strong>endpoint_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Integration endpoint specific backend configuration</p></li>
<li><p><strong>endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service integration endpoint</p></li>
<li><p><strong>endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the service integration endpoint</p></li>
<li><p><strong>external_elasticsearch_logs_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – external elasticsearch specific user configurable settings</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project the service integration endpoint belongs to</p></li>
<li><p><strong>prometheus_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Prometheus specific user configurable settings</p></li>
<li><p><strong>rsyslog_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – rsyslog specific user configurable settings</p></li>
</ul>
</dd>
</dl>
<p>The <strong>datadog_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datadogApiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableConsumerStats</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPartitionContexts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">site</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>external_elasticsearch_logs_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ca</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexDaysMax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>prometheus_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">basicAuthPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">basicAuthUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rsyslog_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ca</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sd</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ServiceUser</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceUser" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the user to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the user to</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the user account</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.ServiceUser.access_cert">
<code class="sig-name descname">access_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceUser.access_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>Access certificate for the user if applicable for the service in question</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceUser.access_key">
<code class="sig-name descname">access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceUser.access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Access certificate key for the user if applicable for the service in question</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceUser.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceUser.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password of the user</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceUser.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceUser.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the user to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceUser.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceUser.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the user to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceUser.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceUser.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the user account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.ServiceUser.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.ServiceUser.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the user account</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ServiceUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_cert=None</em>, <em class="sig-param">access_key=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access certificate for the user if applicable for the service in question</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access certificate key for the user if applicable for the service in question</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password of the user</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the user to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the user to</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the user account</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the user account</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.ServiceUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.VpcPeeringConnection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">VpcPeeringConnection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">peer_cloud_account=None</em>, <em class="sig-param">peer_region=None</em>, <em class="sig-param">peer_vpc=None</em>, <em class="sig-param">vpc_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection" title="Permalink to this definition">¶</a></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>peer_cloud_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID or GCP project ID of the peered VPC</p></li>
<li><p><strong>peer_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS region of the peered VPC (if not in the same region as Aiven VPC)</p></li>
<li><p><strong>peer_vpc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS VPC ID or GCP VPC network name of the peered VPC</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC the peering connection belongs to</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aiven.VpcPeeringConnection.peer_cloud_account">
<code class="sig-name descname">peer_cloud_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peer_cloud_account" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS account ID or GCP project ID of the peered VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.VpcPeeringConnection.peer_region">
<code class="sig-name descname">peer_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peer_region" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS region of the peered VPC (if not in the same region as Aiven VPC)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.VpcPeeringConnection.peer_vpc">
<code class="sig-name descname">peer_vpc</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peer_vpc" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS VPC ID or GCP VPC network name of the peered VPC</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.VpcPeeringConnection.peering_connection_id">
<code class="sig-name descname">peering_connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peering_connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider identifier for the peering connection if available</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.VpcPeeringConnection.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.state" title="Permalink to this definition">¶</a></dt>
<dd><p>State of the peering connection</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.VpcPeeringConnection.state_info">
<code class="sig-name descname">state_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.state_info" title="Permalink to this definition">¶</a></dt>
<dd><p>State-specific help or error information</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aiven.VpcPeeringConnection.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC the peering connection belongs to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.VpcPeeringConnection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">peer_cloud_account=None</em>, <em class="sig-param">peer_region=None</em>, <em class="sig-param">peer_vpc=None</em>, <em class="sig-param">peering_connection_id=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">state_info=None</em>, <em class="sig-param">vpc_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpcPeeringConnection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>peer_cloud_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID or GCP project ID of the peered VPC</p></li>
<li><p><strong>peer_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS region of the peered VPC (if not in the same region as Aiven VPC)</p></li>
<li><p><strong>peer_vpc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS VPC ID or GCP VPC network name of the peered VPC</p></li>
<li><p><strong>peering_connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider identifier for the peering connection if available</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – State of the peering connection</p></li>
<li><p><strong>state_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – State-specific help or error information</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC the peering connection belongs to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aiven.VpcPeeringConnection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.VpcPeeringConnection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.get_elastic_search_acl">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_elastic_search_acl</code><span class="sig-paren">(</span><em class="sig-param">acls=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">extended_acl=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.get_elastic_search_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<p>The <strong>acls</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permission</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_aiven.get_kafka_connector">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka_connector</code><span class="sig-paren">(</span><em class="sig-param">config=None</em>, <em class="sig-param">connector_name=None</em>, <em class="sig-param">plugin_author=None</em>, <em class="sig-param">plugin_class=None</em>, <em class="sig-param">plugin_doc_url=None</em>, <em class="sig-param">plugin_title=None</em>, <em class="sig-param">plugin_type=None</em>, <em class="sig-param">plugin_version=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">tasks=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.get_kafka_connector" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<p>The <strong>tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">task</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_aiven.get_kafka_schema">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka_schema</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.get_kafka_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aiven.get_kafka_schema_configuration">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka_schema_configuration</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">subject_name=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.get_kafka_schema_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aiven.get_service">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param">cassandra=None</em>, <em class="sig-param">cassandra_user_config=None</em>, <em class="sig-param">cloud_name=None</em>, <em class="sig-param">components=None</em>, <em class="sig-param">elasticsearch=None</em>, <em class="sig-param">elasticsearch_user_config=None</em>, <em class="sig-param">grafana=None</em>, <em class="sig-param">grafana_user_config=None</em>, <em class="sig-param">influxdb=None</em>, <em class="sig-param">influxdb_user_config=None</em>, <em class="sig-param">kafka=None</em>, <em class="sig-param">kafka_connect=None</em>, <em class="sig-param">kafka_connect_user_config=None</em>, <em class="sig-param">kafka_user_config=None</em>, <em class="sig-param">maintenance_window_dow=None</em>, <em class="sig-param">maintenance_window_time=None</em>, <em class="sig-param">mysql=None</em>, <em class="sig-param">mysql_user_config=None</em>, <em class="sig-param">pg=None</em>, <em class="sig-param">pg_user_config=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">project_vpc_id=None</em>, <em class="sig-param">redis=None</em>, <em class="sig-param">redis_user_config=None</em>, <em class="sig-param">service_host=None</em>, <em class="sig-param">service_integrations=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">service_password=None</em>, <em class="sig-param">service_port=None</em>, <em class="sig-param">service_type=None</em>, <em class="sig-param">service_uri=None</em>, <em class="sig-param">service_username=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">termination_protection=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The <strong>cassandra_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">migrateSstableloader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>components</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">component</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaAuthenticationMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">route</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>elasticsearch</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">kibanaUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>elasticsearch_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableReplicationFactorAdjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actionAutoCreateIndexEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">actionDestructiveRequiresName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMaxContentLength</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesFielddataCacheSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesMemoryIndexBufferSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesQueriesCacheSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indicesQueryBoolMaxClauseCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reindexRemoteWhitelists</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolAnalyzeQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolAnalyzeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolForceMergeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolGetQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolGetSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolIndexQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolIndexSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchThrottledQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolSearchThrottledSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolWriteQueueSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threadPoolWriteSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexPatterns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIndexCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearchRequestTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOldSpaceSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIndexCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elasticsearch</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kibana</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryBasebackupName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>grafana_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alertingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alertingErrorOrTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alertingNodataOrNullvalues</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowEmbedding</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGenericOauth</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrganizations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGithub</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedOrganizations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teamIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGitlab</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">authGoogle</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">allowSignUp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowedDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieSamesite</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dashboardsVersionsToKeep</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproxySendUserHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataproxyTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableGravatar</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">editorsCanAdmin</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">externalImageStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bucketUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">googleAnalyticsUaId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">grafana</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">grafana</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">smtpServer</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fromAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">skipVerify</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAutoAssignOrg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userAutoAssignOrgRole</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">viewersCanEdit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>influxdb</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">database_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>influxdb_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">influxdb</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">influxdb</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>kafka</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access_cert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">restUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistryUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>kafka_connect_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerIsolationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerMaxPollRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetFlushIntervalMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>kafka_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoCreateTopicsEnable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compressionType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectionsMaxIdleMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultReplicationFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupMaxSessionTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupMinSessionTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMaxCompactionLagMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMinCleanableRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanerMinCompactionLagMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logCleanupPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMessageTimestampDifferenceMaxMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMessageTimestampType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logRetentionBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logRetentionHours</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logSegmentBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionsPerIp</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">messageMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numPartitions</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetsRetentionMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerPurgatoryPurgeIntervalRequests</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaFetchMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaFetchResponseMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">socketRequestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaAuthenticationMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sasl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaConnectConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerIsolationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerMaxPollRecords</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offsetFlushIntervalMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRest</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRestConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerEnableAutoCommit</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerRequestMaxBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">consumerRequestTimeoutMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerAcks</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">producerLingerMs</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">simpleconsumerPoolSizeMax</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafka_connect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kafkaRest</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistry</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemaRegistry</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
<p>The <strong>mysql_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupHour</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupMinute</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultTimeZone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupConcatMaxLen</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">informationSchemaStatsExpiry</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbFtMinTokenSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbFtServerStopwordTable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbLockWaitTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbOnlineAlterLogMaxSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">innodbRollbackOnTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAllowedPacket</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netReadTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">netWriteTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sqlRequirePrimaryKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mysqlVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mysql</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryTargetTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>pg</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dbname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicaUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslmode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>pg_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adminUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupHour</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupMinute</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumAnalyzeScaleFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumAnalyzeThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumMaxWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumNaptime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumCostDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumCostLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumScaleFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autovacuumVacuumThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deadlockTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleInTransactionSessionTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logAutovacuumMinDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logErrorVerbosity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logMinDurationStatement</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxLocksPerTransaction</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxParallelWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxParallelWorkersPerGather</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPredLocksPerTransaction</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPreparedTransactions</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStackDepth</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStandbyArchiveDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStandbyStreamingDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxWorkerProcesses</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgStatStatementsTrack</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tempFileLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trackActivityQuerySize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trackFunctions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">walWriterDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgReadReplica</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgServiceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">serverResetQueryAlways</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pglookout</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailoverReplicationTimeLag</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">pg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pgbouncer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recoveryTargetTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceToForkFrom</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timescaledb</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackgroundWorkers</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">variant</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>redis_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">migration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redis</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redis</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisLfuDecayTime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisLfuLogFactor</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisMaxmemoryPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisNotifyKeyspaceEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redisTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
<p>The <strong>service_integrations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">integration_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_aiven.get_service_integration_endpoint">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_service_integration_endpoint</code><span class="sig-paren">(</span><em class="sig-param">datadog_user_config=None</em>, <em class="sig-param">endpoint_config=None</em>, <em class="sig-param">endpoint_name=None</em>, <em class="sig-param">endpoint_type=None</em>, <em class="sig-param">external_elasticsearch_logs_user_config=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">prometheus_user_config=None</em>, <em class="sig-param">rsyslog_user_config=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.get_service_integration_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The <strong>datadog_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datadogApiKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableConsumerStats</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPartitionContexts</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">site</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>external_elasticsearch_logs_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ca</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexDaysMax</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>prometheus_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">basicAuthPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">basicAuthUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<p>The <strong>rsyslog_user_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ca</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logline</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sd</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

</div>
