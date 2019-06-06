---
---

<div class="section" id="module-pulumi_cloudflare">
<span id="pulumi-cloudflare"></span><h1>Pulumi Cloudflare<a class="headerlink" href="#module-pulumi_cloudflare" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_cloudflare.AccessApplication">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">AccessApplication</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>domain=None</em>, <em>name=None</em>, <em>session_duration=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Application resource. Access Applications
are used to restrict access to a whole application using an
authorisation gateway managed by Cloudflare.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</li>
<li><strong>session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccessApplication.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessApplication.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessApplication.session_duration">
<code class="descname">session_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.session_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessApplication.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessApplication.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessApplication.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessPolicy">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">AccessPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_id=None</em>, <em>decision=None</em>, <em>excludes=None</em>, <em>includes=None</em>, <em>name=None</em>, <em>precedence=None</em>, <em>requires=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Policy resource. Access Policies are used
in conjunction with Access Applications to restrict access to a
particular resource.</p>
<p><code class="docutils literal notranslate"><span class="pre">require</span></code>, <code class="docutils literal notranslate"><span class="pre">exclude</span></code> and <code class="docutils literal notranslate"><span class="pre">include</span></code> arguments share the available
conditions which can be applied. The conditions are:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">ip</span></code> - (Optional) A list of IP addresses or ranges. Example:
<code class="docutils literal notranslate"><span class="pre">ip</span> <span class="pre">=</span> <span class="pre">[&quot;1.2.3.4&quot;,</span> <span class="pre">&quot;10.0.0.0/2&quot;]</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">email</span></code> - (Optional) A list of email addresses. Example:
<code class="docutils literal notranslate"><span class="pre">email</span> <span class="pre">=</span> <span class="pre">[&quot;test&#64;example.com&quot;]</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">email_domain</span></code> - (Optional) A list of email domains. Example:
<code class="docutils literal notranslate"><span class="pre">email_domain</span> <span class="pre">=</span> <span class="pre">[&quot;example.com&quot;]</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">everyone</span></code> - (Optional) Boolean indicating permitting access for all
requests. Example: <code class="docutils literal notranslate"><span class="pre">everyone</span> <span class="pre">=</span> <span class="pre">true</span></code></li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application the policy is
associated with.</li>
<li><strong>decision</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></li>
<li><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</li>
<li><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</li>
<li><strong>precedence</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The unique precedence for policies on a single application. Integer.</li>
<li><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be
added.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.application_id">
<code class="descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the application the policy is
associated with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.decision">
<code class="descname">decision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.decision" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.excludes">
<code class="descname">excludes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.includes">
<code class="descname">includes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.includes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.precedence">
<code class="descname">precedence</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.precedence" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique precedence for policies on a single application. Integer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.requires">
<code class="descname">requires</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.requires" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be
added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessRule">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">AccessRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>configuration=None</em>, <em>mode=None</em>, <em>notes=None</em>, <em>zone=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare IP Firewall Access Rule resource. Access control can be applied on basis of IP addresses, IP ranges, AS numbers or countries.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Rule configuration to apply to a matched request. It’s a complex value. See description below.</li>
<li><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</li>
<li><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A personal note about the rule. Typically used as a reminder or explanation for the rule.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added. Will be resolved to <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> upon creation.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccessRule.configuration">
<code class="descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Rule configuration to apply to a matched request. It’s a complex value. See description below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessRule.mode">
<code class="descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessRule.notes">
<code class="descname">notes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>A personal note about the rule. Typically used as a reminder or explanation for the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessRule.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be added. Will be resolved to <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> upon creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessRule.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccountMember">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">AccountMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>email_address=None</em>, <em>role_ids=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare account members.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>email_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</li>
<li><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of account role IDs that you want to assign to a member.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccountMember.email_address">
<code class="descname">email_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccountMember.email_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccountMember.role_ids">
<code class="descname">role_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccountMember.role_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of account role IDs that you want to assign to a member.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccountMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccountMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Argo">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">Argo</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>smart_routing=None</em>, <em>tiered_caching=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloudflare Argo controls the routing to your origin and tiered caching options to speed up your website browsing experience.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</li>
<li><strong>tiered_caching</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID that you wish to manage Argo on.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.Argo.smart_routing">
<code class="descname">smart_routing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Argo.smart_routing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Argo.tiered_caching">
<code class="descname">tiered_caching</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Argo.tiered_caching" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Argo.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Argo.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID that you wish to manage Argo on.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Argo.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Argo.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomPages">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">CustomPages</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_id=None</em>, <em>state=None</em>, <em>type=None</em>, <em>url=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare custom error pages.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</li>
<li><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Managed state of the custom page. Must be one of
<code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">customised</span></code>. If the value is <code class="docutils literal notranslate"><span class="pre">default</span></code> it will be removed
from the Terraform state management.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</li>
<li><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of where the custom page source is located.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.CustomPages.account_id">
<code class="descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.CustomPages.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Managed state of the custom page. Must be one of
<code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">customised</span></code>. If the value is <code class="docutils literal notranslate"><span class="pre">default</span></code> it will be removed
from the Terraform state management.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.CustomPages.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.CustomPages.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of where the custom page source is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.CustomPages.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.CustomPages.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomPages.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Filter">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">Filter</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>expression=None</em>, <em>paused=None</em>, <em>ref=None</em>, <em>zone=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Filter expressions that can be referenced across multiple features, e.g. Firewall Rule. The expression format is similar to <a class="reference external" href="https://www.wireshark.org/docs/man-pages/wireshark-filter.html">Wireshark Display Filter</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the purpose of the filter.</li>
<li><strong>expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter expression to be used.</li>
<li><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter is currently paused. Boolean value.</li>
<li><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short reference tag to quickly select related rules.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added. Will be resolved to <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> upon creation.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A note that you can use to describe the purpose of the filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.expression">
<code class="descname">expression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter expression to be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.paused">
<code class="descname">paused</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this filter is currently paused. Boolean value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.ref">
<code class="descname">ref</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.ref" title="Permalink to this definition">¶</a></dt>
<dd><p>Short reference tag to quickly select related rules.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the Filter should be added. Will be resolved to <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> upon creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the Filter should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Filter.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Filter.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.FirewallRule">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">FirewallRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>action=None</em>, <em>description=None</em>, <em>filter_id=None</em>, <em>paused=None</em>, <em>priority=None</em>, <em>zone=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Define Firewall rules using filter expressions for more control over how traffic is matched to the rule.
A filter expression permits selecting traffic by multiple criteria allowing greater freedom in rule creation.</p>
<p>Filter expressions needs to be created first before using Firewall Rule. See Filter.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”. Enterprise plan also allows “log”.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the rule to help identify it.</li>
<li><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter based firewall rule is currently paused. Boolean value.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Firewall Rule should be added. Will be resolved to <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> upon creation.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.action">
<code class="descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”. Enterprise plan also allows “log”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the rule to help identify it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.paused">
<code class="descname">paused</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this filter based firewall rule is currently paused. Boolean value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the Firewall Rule should be added. Will be resolved to <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> upon creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the Filter should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.FirewallRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.FirewallRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.GetIpRangesResult">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">GetIpRangesResult</code><span class="sig-paren">(</span><em>cidr_blocks=None</em>, <em>ipv4_cidr_blocks=None</em>, <em>ipv6_cidr_blocks=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpRanges.</p>
<dl class="attribute">
<dt id="pulumi_cloudflare.GetIpRangesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.GetZonesResult">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">GetZonesResult</code><span class="sig-paren">(</span><em>filter=None</em>, <em>zones=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="attribute">
<dt id="pulumi_cloudflare.GetZonesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.LoadBalancer">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">LoadBalancer</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>default_pool_ids=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>fallback_pool_id=None</em>, <em>name=None</em>, <em>pop_pools=None</em>, <em>proxied=None</em>, <em>region_pools=None</em>, <em>session_affinity=None</em>, <em>steering_policy=None</em>, <em>ttl=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Load Balancer resource. This sits in front of a number of defined pools of origins and provides various options for geographically-aware load balancing. Note that the load balancing feature must be enabled in your Clouflare account before you can use this resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>default_pool_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</li>
<li><strong>fallback_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pool ID to use when all other pools are detected as unhealthy.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name (FQDN, including the zone) to associate with the load balancer.</li>
<li><strong>pop_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</li>
<li><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>region_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</li>
<li><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.</li>
<li><strong>steering_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determine which method the load balancer uses to determine the fastest route to your origin. Valid values  are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</li>
<li><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone to add the load balancer to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.created_on">
<code class="descname">created_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.default_pool_ids">
<code class="descname">default_pool_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.default_pool_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.fallback_pool_id">
<code class="descname">fallback_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.fallback_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The pool ID to use when all other pools are detected as unhealthy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.modified_on">
<code class="descname">modified_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name (FQDN, including the zone) to associate with the load balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.pop_pools">
<code class="descname">pop_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.pop_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.proxied">
<code class="descname">proxied</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.proxied" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.region_pools">
<code class="descname">region_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.region_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.session_affinity">
<code class="descname">session_affinity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.session_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.steering_policy">
<code class="descname">steering_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.steering_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Determine which method the load balancer uses to determine the fastest route to your origin. Valid values  are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.ttl">
<code class="descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone to add the load balancer to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID associated with the specified <code class="docutils literal notranslate"><span class="pre">zone</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LoadBalancer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerMonitor">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">LoadBalancerMonitor</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_insecure=None</em>, <em>description=None</em>, <em>expected_body=None</em>, <em>expected_codes=None</em>, <em>follow_redirects=None</em>, <em>headers=None</em>, <em>interval=None</em>, <em>method=None</em>, <em>path=None</em>, <em>port=None</em>, <em>retries=None</em>, <em>timeout=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor" title="Permalink to this definition">¶</a></dt>
<dd><p>If you’re using Cloudflare’s Load Balancing to load-balance across multiple origin servers or data centers, you configure one of these Monitors to actively check the availability of those servers over HTTP(S).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not validate the certificate when monitor use HTTPS.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</li>
<li><strong>expected_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.</li>
<li><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code></li>
<li><strong>follow_redirects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Follow redirects if returned by the origin.</li>
<li><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The header name.</li>
<li><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</li>
<li><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP method to use for the health check. Default: “GET”.</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint path to health check against. Default: “/”.</li>
<li><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</li>
<li><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timeout (in seconds) before marking the health check as failed. Default: 5.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’ and ‘HTTPS’. Default: “http”.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.allow_insecure">
<code class="descname">allow_insecure</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.allow_insecure" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not validate the certificate when monitor use HTTPS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.created_on">
<code class="descname">created_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer monitor was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.expected_body">
<code class="descname">expected_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.expected_body" title="Permalink to this definition">¶</a></dt>
<dd><p>A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.expected_codes">
<code class="descname">expected_codes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.expected_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.follow_redirects">
<code class="descname">follow_redirects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.follow_redirects" title="Permalink to this definition">¶</a></dt>
<dd><p>Follow redirects if returned by the origin.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.headers">
<code class="descname">headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>The header name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.interval">
<code class="descname">interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.method">
<code class="descname">method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP method to use for the health check. Default: “GET”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.modified_on">
<code class="descname">modified_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer monitor was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint path to health check against. Default: “/”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.retries">
<code class="descname">retries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.retries" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.timeout">
<code class="descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The timeout (in seconds) before marking the health check as failed. Default: 5.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’ and ‘HTTPS’. Default: “http”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerMonitor.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerPool">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">LoadBalancerPool</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>check_regions=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>minimum_origins=None</em>, <em>monitor=None</em>, <em>name=None</em>, <em>notification_email=None</em>, <em>origins=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Load Balancer pool resource. This provides a pool of origins that can be used by a Cloudflare Load Balancer. Note that the load balancing feature must be enabled in your Clouflare account before you can use this resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>check_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</li>
<li><strong>minimum_origins</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</li>
<li><strong>monitor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Monitor to use for health checking origins within this pool.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-identifiable name for the origin.</li>
<li><strong>notification_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address to send health status notifications to. This can be an individual mailbox or a mailing list.</li>
<li><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.check_regions">
<code class="descname">check_regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.check_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.created_on">
<code class="descname">created_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.minimum_origins">
<code class="descname">minimum_origins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.minimum_origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.modified_on">
<code class="descname">modified_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.monitor">
<code class="descname">monitor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Monitor to use for health checking origins within this pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-identifiable name for the origin.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.notification_email">
<code class="descname">notification_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.notification_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address to send health status notifications to. This can be an individual mailbox or a mailing list.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.origins">
<code class="descname">origins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LoadBalancerPool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerPool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogpushJob">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">LogpushJob</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>destination_conf=None</em>, <em>enabled=None</em>, <em>logpull_options=None</em>, <em>name=None</em>, <em>ownership_challenge=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare logpush jobs.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ownership_challenge</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/tutorials/tutorial-logpush-curl/">https://developers.cloudflare.com/logs/tutorials/tutorial-logpush-curl/</a></li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.LogpushJob.ownership_challenge">
<code class="descname">ownership_challenge</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.ownership_challenge" title="Permalink to this definition">¶</a></dt>
<dd><p>Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/tutorials/tutorial-logpush-curl/">https://developers.cloudflare.com/logs/tutorials/tutorial-logpush-curl/</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LogpushJob.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogpushJob.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.PageRule">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">PageRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>actions=None</em>, <em>priority=None</em>, <em>status=None</em>, <em>target=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare page rule resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The actions taken by the page rule, options given below.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</li>
<li><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the page rule is active or disabled.</li>
<li><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL pattern to target with the page rule.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the page rule should be added.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.actions">
<code class="descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>The actions taken by the page rule, options given below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the page rule is active or disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.target">
<code class="descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL pattern to target with the page rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the page rule should be added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the zone in which the page rule will be applied.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.PageRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.PageRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Provider">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_client_logging=None</em>, <em>email=None</em>, <em>max_backoff=None</em>, <em>min_backoff=None</em>, <em>org_id=None</em>, <em>retries=None</em>, <em>rps=None</em>, <em>token=None</em>, <em>use_org_from_zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the cloudflare package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://pulumi.io/reference/programming-model.html#providers">documentation</a> for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="method">
<dt id="pulumi_cloudflare.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.RateLimit">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">RateLimit</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>action=None</em>, <em>bypass_url_patterns=None</em>, <em>correlate=None</em>, <em>description=None</em>, <em>disabled=None</em>, <em>match=None</em>, <em>period=None</em>, <em>threshold=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare rate limit resource for a given zone. This can be used to limit the traffic you receive zone-wide, or matching more specific types of requests/responses.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The action to be performed when the threshold of matched traffic within the period defined is exceeded.</li>
<li><strong>bypass_url_patterns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – URLs matching the patterns specified here will be excluded from rate limiting.</li>
<li><strong>correlate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</li>
<li><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>match</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</li>
<li><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</li>
<li><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to apply rate limiting to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.action">
<code class="descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to be performed when the threshold of matched traffic within the period defined is exceeded.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.bypass_url_patterns">
<code class="descname">bypass_url_patterns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.bypass_url_patterns" title="Permalink to this definition">¶</a></dt>
<dd><p>URLs matching the patterns specified here will be excluded from rate limiting.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.correlate">
<code class="descname">correlate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.correlate" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.disabled">
<code class="descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.match">
<code class="descname">match</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.match" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.period">
<code class="descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.threshold">
<code class="descname">threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to apply rate limiting to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.RateLimit.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.RateLimit.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Record">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">Record</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>data=None</em>, <em>domain=None</em>, <em>name=None</em>, <em>priority=None</em>, <em>proxied=None</em>, <em>ttl=None</em>, <em>type=None</em>, <em>value=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare record resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to add the record to</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the record</li>
<li><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the record</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.Record.created_on">
<code class="descname">created_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the record was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.data">
<code class="descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.data" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to add the record to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.hostname">
<code class="descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.metadata">
<code class="descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value map of string metadata cloudflare associates with the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.modified_on">
<code class="descname">modified_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the record was last modified</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.proxiable">
<code class="descname">proxiable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.proxiable" title="Permalink to this definition">¶</a></dt>
<dd><p>Shows whether this record can be proxied, must be true if setting <code class="docutils literal notranslate"><span class="pre">proxied=true</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.proxied">
<code class="descname">proxied</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.proxied" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.ttl">
<code class="descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone id of the record</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Record.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Record.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.SpectrumApplication">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">SpectrumApplication</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>dns=None</em>, <em>ip_firewall=None</em>, <em>origin_directs=None</em>, <em>origin_dns=None</em>, <em>origin_port=None</em>, <em>protocol=None</em>, <em>proxy_protocol=None</em>, <em>tls=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Spectrum Application. You can extend the power of Cloudflare’s DDoS, TLS, and IP Firewall to your other TCP-based services.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The name and type of DNS record for the Spectrum application. Fields documented below.</li>
<li><strong>ip_firewall</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>origin_directs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</li>
<li><strong>origin_dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A destination DNS addresses to the origin. Fields documented below.</li>
<li><strong>origin_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</li>
<li><strong>proxy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables Proxy Protocol v1 to the origin. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>tls</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.dns">
<code class="descname">dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The name and type of DNS record for the Spectrum application. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.ip_firewall">
<code class="descname">ip_firewall</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.ip_firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_directs">
<code class="descname">origin_directs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_directs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_dns">
<code class="descname">origin_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>A destination DNS addresses to the origin. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_port">
<code class="descname">origin_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_port" title="Permalink to this definition">¶</a></dt>
<dd><p>If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.proxy_protocol">
<code class="descname">proxy_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.proxy_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables Proxy Protocol v1 to the origin. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.tls">
<code class="descname">tls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.tls" title="Permalink to this definition">¶</a></dt>
<dd><p>TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.SpectrumApplication.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.SpectrumApplication.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafRule">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">WafRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>mode=None</em>, <em>rule_id=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF rule resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall rules.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”].</li>
<li><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule ID.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to apply to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.WafRule.mode">
<code class="descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafRule.package_id">
<code class="descname">package_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Package that contains the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafRule.rule_id">
<code class="descname">rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The WAF Rule ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafRule.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to apply to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafRule.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WafRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerRoute">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">WorkerRoute</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>enabled=None</em>, <em>pattern=None</em>, <em>script_name=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare worker route resource. A route will also require a <code class="docutils literal notranslate"><span class="pre">cloudflare_worker_script</span></code>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://developers.cloudflare.com/workers/api/route-matching/">route pattern</a></li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone to add the route to.</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerRoute.pattern">
<code class="descname">pattern</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://developers.cloudflare.com/workers/api/route-matching/">route pattern</a></p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (For single-script accounts only) Whether to run the worker script for requests that match the route pattern. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">script_name</span></code> (For multi-script accounts only) Which worker script to run for requests that match the route pattern. If <code class="docutils literal notranslate"><span class="pre">script_name</span></code> is empty, workers will be skipped for matching requests.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerRoute.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone to add the route to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerRoute.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone id of the route</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WorkerRoute.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerRoute.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerScript">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">WorkerScript</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>content=None</em>, <em>name=None</em>, <em>zone=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare worker script resource. In order for a script to be active, you’ll also need to setup a <code class="docutils literal notranslate"><span class="pre">cloudflare_worker_route</span></code>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script content.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the script.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone for the script.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone id of the script (only for non-multi-script resources)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerScript.content">
<code class="descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The script content.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerScript.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the script.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerScript.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone for the script.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerScript.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone id of the script (only for non-multi-script resources)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WorkerScript.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerScript.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Zone">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">Zone</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>jump_start=None</em>, <em>paused=None</em>, <em>plan=None</em>, <em>type=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Zone resource. Zone is the basic resource for working with Cloudflare and is roughly equivalent to a domain name that the user purchases.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>jump_start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</li>
<li><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</li>
<li><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone name which will be added.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.jump_start">
<code class="descname">jump_start</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.jump_start" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.name_servers">
<code class="descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloudflare-assigned name servers. This is only populated for zones that use Cloudflare DNS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.paused">
<code class="descname">paused</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.plan">
<code class="descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the zone. Valid values: <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">initializing</span></code>, <code class="docutils literal notranslate"><span class="pre">moved</span></code>, <code class="docutils literal notranslate"><span class="pre">deleted</span></code>, <code class="docutils literal notranslate"><span class="pre">deactivated</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.type" title="Permalink to this definition">¶</a></dt>
<dd><p>A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.vanity_name_servers">
<code class="descname">vanity_name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.vanity_name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Vanity Nameservers (if set).</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">meta.wildcard_proxiable</span></code> - Indicates whether wildcard DNS records can receive Cloudflare security and performance features.</li>
<li><code class="docutils literal notranslate"><span class="pre">meta.phishing_detected</span></code> - Indicates if URLs on the zone have been identified as hosting phishing content.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone name which will be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Zone.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Zone.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneLockdown">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">ZoneLockdown</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>configurations=None</em>, <em>description=None</em>, <em>paused=None</em>, <em>urls=None</em>, <em>zone=None</em>, <em>zone_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Zone Lockdown resource. Zone Lockdown allows you to define one or more URLs (with wildcard matching on the domain or path) that will only permit access if the request originates from an IP address that matches a safelist of one or more IP addresses and/or IP ranges.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</li>
<li><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone lockdown is currently paused. Default: false.</li>
<li><strong>urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the lockdown will be added. Will be resolved to <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> upon creation.</li>
<li><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.configurations">
<code class="descname">configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.paused">
<code class="descname">paused</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether this zone lockdown is currently paused. Default: false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.urls">
<code class="descname">urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the lockdown will be added. Will be resolved to <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> upon creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.zone_id">
<code class="descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.ZoneLockdown.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneLockdown.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneSettingsOverride">
<em class="property">class </em><code class="descclassname">pulumi_cloudflare.</code><code class="descname">ZoneSettingsOverride</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>settings=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which customizes Cloudflare zone settings. Note that after destroying this resource Zone Settings will be reset to their initial values.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which apply settings.</li>
<li><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.initial_settings">
<code class="descname">initial_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.initial_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings present in the zone at the time the resource is created. This will be used to restore the original settings when this resource is destroyed. Shares the same schema as the <code class="docutils literal notranslate"><span class="pre">settings</span></code> attribute (Above).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which apply settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.readonly_settings">
<code class="descname">readonly_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.readonly_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Which of the current <code class="docutils literal notranslate"><span class="pre">settings</span></code> are not able to be set by the user. Which settings these are is determined by plan level and user permissions.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">zone_status</span></code>. A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup.</li>
<li><code class="docutils literal notranslate"><span class="pre">zone_type</span></code>. Status of the zone. Valid values: active, pending, initializing, moved, deleted, deactivated.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.settings">
<code class="descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneSettingsOverride.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.get_ip_ranges">
<code class="descclassname">pulumi_cloudflare.</code><code class="descname">get_ip_ranges</code><span class="sig-paren">(</span><em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the [IP ranges][1] of Cloudflare edge nodes.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudflare.get_zones">
<code class="descclassname">pulumi_cloudflare.</code><code class="descname">get_zones</code><span class="sig-paren">(</span><em>filter=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up [Zone][1] records.</p>
</dd></dl>

</div>
