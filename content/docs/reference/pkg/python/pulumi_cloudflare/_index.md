---
title: Package pulumi_cloudflare
title_tag: Package pulumi_cloudflare | Python SDK
linktitle: pulumi_cloudflare
notitle: true
---

<div class="section" id="pulumi-cloudflare">
<h1>Pulumi Cloudflare<a class="headerlink" href="#pulumi-cloudflare" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-cloudflare/issues">pulumi/pulumi-cloudflare repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/issues">terraform-providers/terraform-provider-cloudflare repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_cloudflare"></span><dl class="class">
<dt id="pulumi_cloudflare.AccessApplication">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessApplication</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">session_duration=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Application resource. Access Applications
are used to restrict access to a whole application using an
authorisation gateway managed by Cloudflare.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_application.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_application.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccessApplication.aud">
<code class="sig-name descname">aud</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.aud" title="Permalink to this definition">¶</a></dt>
<dd><p>Application Audience (AUD) Tag of the application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessApplication.domain">
<code class="sig-name descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessApplication.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessApplication.session_duration">
<code class="sig-name descname">session_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.session_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessApplication.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessApplication.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aud=None</em>, <em class="sig-param">domain=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">session_duration=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessApplication resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aud</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Audience (AUD) Tag of the application</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The complete URL of the asset you wish to put
Cloudflare Access in front of. Can include subdomains or paths. Or both.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>session_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often a user will be forced to
re-authorise. Must be one of <code class="docutils literal notranslate"><span class="pre">30m</span></code>, <code class="docutils literal notranslate"><span class="pre">6h</span></code>, <code class="docutils literal notranslate"><span class="pre">12h</span></code>, <code class="docutils literal notranslate"><span class="pre">24h</span></code>, <code class="docutils literal notranslate"><span class="pre">168h</span></code>, <code class="docutils literal notranslate"><span class="pre">730h</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_application.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_application.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessApplication.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessApplication.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">excludes=None</em>, <em class="sig-param">includes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">requires=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Group resource. Access Groups are used
in conjunction with Access Policies to restrict access to a
particular resource based on group membership.</p>
<p><code class="docutils literal notranslate"><span class="pre">require</span></code>, <code class="docutils literal notranslate"><span class="pre">exclude</span></code> and <code class="docutils literal notranslate"><span class="pre">include</span></code> arguments share the available
conditions which can be applied. The conditions are:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> - (Optional) A list of IP addresses or ranges. Example:
<code class="docutils literal notranslate"><span class="pre">ip</span> <span class="pre">=</span> <span class="pre">[&quot;1.2.3.4&quot;,</span> <span class="pre">&quot;10.0.0.0/2&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> - (Optional) A list of email addresses. Example:
<code class="docutils literal notranslate"><span class="pre">email</span> <span class="pre">=</span> <span class="pre">[&quot;test&#64;example.com&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_domain</span></code> - (Optional) A list of email domains. Example:
<code class="docutils literal notranslate"><span class="pre">email_domain</span> <span class="pre">=</span> <span class="pre">[&quot;example.com&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> - (Optional) Boolean indicating permitting access for all
requests. Example: <code class="docutils literal notranslate"><span class="pre">everyone</span> <span class="pre">=</span> <span class="pre">true</span></code></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account the group is
associated with.</p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Group.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>excludes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>requires</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_group.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccessGroup.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the account the group is
associated with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessGroup.excludes">
<code class="sig-name descname">excludes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessGroup.includes">
<code class="sig-name descname">includes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.includes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessGroup.requires">
<code class="sig-name descname">requires</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.requires" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">excludes=None</em>, <em class="sig-param">includes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">requires=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account the group is
associated with.</p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Group.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>excludes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>requires</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_group.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessIdentityProvider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessIdentityProvider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">configs=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Identity Provider resource. Identity Providers are
used as an authentication or authorisation source within Access.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Provider configuration from the [developer documentation][access_identity_provider_guide].</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Identity Provider configuration.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider type to use. Must be one of: <code class="docutils literal notranslate"><span class="pre">&quot;centrify&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;facebook&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google-apps&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;oidc&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;github&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;saml&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;linkedin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;azureAD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;okta&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onetimepin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onelogin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;yandex&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appsDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certsUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">directoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailAttributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpPublicCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktaAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneloginAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoTargetUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_identity_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_identity_provider.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccessIdentityProvider.configs">
<code class="sig-name descname">configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.configs" title="Permalink to this definition">¶</a></dt>
<dd><p>Provider configuration from the [developer documentation][access_identity_provider_guide].</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appsDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certsUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">directoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailAttributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpPublicCert</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktaAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneloginAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoTargetUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessIdentityProvider.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Identity Provider configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessIdentityProvider.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type to use. Must be one of: <code class="docutils literal notranslate"><span class="pre">&quot;centrify&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;facebook&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google-apps&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;oidc&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;github&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;saml&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;linkedin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;azureAD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;okta&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onetimepin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onelogin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;yandex&quot;</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">configs=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessIdentityProvider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Provider configuration from the [developer documentation][access_identity_provider_guide].</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Identity Provider configuration.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The provider type to use. Must be one of: <code class="docutils literal notranslate"><span class="pre">&quot;centrify&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;facebook&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google-apps&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;oidc&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;github&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;google&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;saml&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;linkedin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;azureAD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;okta&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onetimepin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;onelogin&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;yandex&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appsDomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">centrifyAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certsUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">directoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailAttributeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idpPublicCert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oktaAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oneloginAccount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">signRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssoTargetUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">supportGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tokenUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_identity_provider.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_identity_provider.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessIdentityProvider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessIdentityProvider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessIdentityProvider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">decision=None</em>, <em class="sig-param">excludes=None</em>, <em class="sig-param">includes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">precedence=None</em>, <em class="sig-param">requires=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Access Policy resource. Access Policies are used
in conjunction with Access Applications to restrict access to a
particular resource.</p>
<p><code class="docutils literal notranslate"><span class="pre">require</span></code>, <code class="docutils literal notranslate"><span class="pre">exclude</span></code> and <code class="docutils literal notranslate"><span class="pre">include</span></code> arguments share the available
conditions which can be applied. The conditions are:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> - (Optional) A list of IP addresses or ranges. Example:
<code class="docutils literal notranslate"><span class="pre">ip</span> <span class="pre">=</span> <span class="pre">[&quot;1.2.3.4&quot;,</span> <span class="pre">&quot;10.0.0.0/2&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> - (Optional) A list of email addresses. Example:
<code class="docutils literal notranslate"><span class="pre">email</span> <span class="pre">=</span> <span class="pre">[&quot;test&#64;example.com&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_domain</span></code> - (Optional) A list of email domains. Example:
<code class="docutils literal notranslate"><span class="pre">email_domain</span> <span class="pre">=</span> <span class="pre">[&quot;example.com&quot;]</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> - (Optional) Boolean indicating permitting access for all
requests. Example: <code class="docutils literal notranslate"><span class="pre">everyone</span> <span class="pre">=</span> <span class="pre">true</span></code></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application the policy is
associated with.</p></li>
<li><p><strong>decision</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>precedence</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The unique precedence for policies on a single application. Integer.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be
added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>excludes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>requires</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.application_id">
<code class="sig-name descname">application_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.application_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the application the policy is
associated with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.decision">
<code class="sig-name descname">decision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.decision" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.excludes">
<code class="sig-name descname">excludes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.excludes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.includes">
<code class="sig-name descname">includes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.includes" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the Access Application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.precedence">
<code class="sig-name descname">precedence</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.precedence" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique precedence for policies on a single application. Integer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.requires">
<code class="sig-name descname">requires</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.requires" title="Permalink to this definition">¶</a></dt>
<dd><p>A series of access conditions, see below for
full list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessPolicy.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be
added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_id=None</em>, <em class="sig-param">decision=None</em>, <em class="sig-param">excludes=None</em>, <em class="sig-param">includes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">precedence=None</em>, <em class="sig-param">requires=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the application the policy is
associated with.</p></li>
<li><p><strong>decision</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action Access will take if the policy matches the user.
Allowed values: <code class="docutils literal notranslate"><span class="pre">allow</span></code>, <code class="docutils literal notranslate"><span class="pre">deny</span></code>, <code class="docutils literal notranslate"><span class="pre">bypass</span></code></p></li>
<li><p><strong>excludes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>includes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the Access Application.</p></li>
<li><p><strong>precedence</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The unique precedence for policies on a single application. Integer.</p></li>
<li><p><strong>requires</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A series of access conditions, see below for
full list.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be
added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>excludes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>includes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>requires</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailDomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">everyone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ips</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">notes=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare IP Firewall Access Rule resource. Access control can be applied on basis of IP addresses, IP ranges, AS numbers or countries.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Rule configuration to apply to a matched request. It’s a complex value. See description below.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A personal note about the rule. Typically used as a reminder or explanation for the rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request property to target. Allowed values: “ip”, “ip6”, “ip_range”, “asn”, “country”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to target. Depends on target’s type.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccessRule.configuration">
<code class="sig-name descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Rule configuration to apply to a matched request. It’s a complex value. See description below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The request property to target. Allowed values: “ip”, “ip6”, “ip_range”, “asn”, “country”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value to target. Depends on target’s type.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessRule.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessRule.notes">
<code class="sig-name descname">notes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>A personal note about the rule. Typically used as a reminder or explanation for the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessRule.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the access rule should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">notes=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Rule configuration to apply to a matched request. It’s a complex value. See description below.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “whitelist”, “js_challenge”</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A personal note about the rule. Typically used as a reminder or explanation for the rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request property to target. Allowed values: “ip”, “ip6”, “ip_range”, “asn”, “country”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to target. Depends on target’s type.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessServiceToken">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccessServiceToken</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken" title="Permalink to this definition">¶</a></dt>
<dd><p>Access Service Tokens are used for service-to-service communication
when an application is behind Cloudflare Access.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account where the Access
Service is being created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the token’s intent.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_service_token.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_service_token.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccessServiceToken.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the account where the Access
Service is being created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessServiceToken.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>UUID client ID associated with the Service Token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessServiceToken.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>A secret for interacting with Access protocols.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccessServiceToken.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name of the token’s intent.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessServiceToken.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccessServiceToken resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the account where the Access
Service is being created.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UUID client ID associated with the Service Token.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A secret for interacting with Access protocols.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name of the token’s intent.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_service_token.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/access_service_token.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccessServiceToken.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccessServiceToken.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccessServiceToken.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccountMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AccountMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">email_address=None</em>, <em class="sig-param">role_ids=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare account members.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</p></li>
<li><p><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of account role IDs that you want to assign to a member.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/account_member.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/account_member.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.AccountMember.email_address">
<code class="sig-name descname">email_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccountMember.email_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.AccountMember.role_ids">
<code class="sig-name descname">role_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.AccountMember.role_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of account role IDs that you want to assign to a member.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccountMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">email_address=None</em>, <em class="sig-param">role_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address of the user who you wish to manage. Note: Following creation, this field becomes read only via the API and cannot be updated.</p></li>
<li><p><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of account role IDs that you want to assign to a member.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/account_member.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/account_member.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.AccountMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AccountMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AccountMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Argo">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Argo</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">smart_routing=None</em>, <em class="sig-param">tiered_caching=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloudflare Argo controls the routing to your origin and tiered caching options to speed up your website browsing experience.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tiered_caching</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID that you wish to manage Argo on.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/argo.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/argo.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.Argo.smart_routing">
<code class="sig-name descname">smart_routing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Argo.smart_routing" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Argo.tiered_caching">
<code class="sig-name descname">tiered_caching</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Argo.tiered_caching" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Argo.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Argo.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID that you wish to manage Argo on.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Argo.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">smart_routing=None</em>, <em class="sig-param">tiered_caching=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Argo resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>smart_routing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether smart routing is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tiered_caching</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether tiered caching is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">on</span></code> or <code class="docutils literal notranslate"><span class="pre">off</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID that you wish to manage Argo on.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/argo.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/argo.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Argo.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Argo.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Argo.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.AwaitableGetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param">cidr_blocks=None</em>, <em class="sig-param">ipv4_cidr_blocks=None</em>, <em class="sig-param">ipv6_cidr_blocks=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.AwaitableGetWafGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetWafGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetWafGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.AwaitableGetWafPackagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetWafPackagesResult</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">packages=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetWafPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.AwaitableGetWafRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetWafRulesResult</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetWafRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.CustomPages">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">CustomPages</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare custom error pages.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of where the custom page source is located.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/custom_pages.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/custom_pages.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.CustomPages.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.CustomPages.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.CustomPages.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of where the custom page source is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.CustomPages.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomPages.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.CustomPages.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomPages resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> must be provided. If
<code class="docutils literal notranslate"><span class="pre">account_id</span></code> is present, it will override the zone setting.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of custom page you wish to update. Must
be one of <code class="docutils literal notranslate"><span class="pre">basic_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">waf_block</span></code>,
<code class="docutils literal notranslate"><span class="pre">ratelimit_block</span></code>, <code class="docutils literal notranslate"><span class="pre">country_challenge</span></code>, <code class="docutils literal notranslate"><span class="pre">ip_block</span></code>, <code class="docutils literal notranslate"><span class="pre">under_attack</span></code>,
<code class="docutils literal notranslate"><span class="pre">500_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">1000_errors</span></code>, <code class="docutils literal notranslate"><span class="pre">always_online</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of where the custom page source is located.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the custom pages should be
updated. Either <code class="docutils literal notranslate"><span class="pre">zone_id</span></code> or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> must be provided.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/custom_pages.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/custom_pages.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.CustomPages.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomPages.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomPages.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomSsl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">CustomSsl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_ssl_options=None</em>, <em class="sig-param">custom_ssl_priorities=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare custom ssl resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_ssl_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The certificate, private key and associated optional parameters, such as bundle_method, geo_restrictions, and type.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone id to the custom ssl cert should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_ssl_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bundle_method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Method of building intermediate certificate chain. A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. Valid values are <code class="docutils literal notranslate"><span class="pre">ubiquitous</span></code> (default), <code class="docutils literal notranslate"><span class="pre">optimal</span></code>, <code class="docutils literal notranslate"><span class="pre">force</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Certificate certificate and the intermediate(s)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geo_restrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the region where your private key can be held locally. Valid values are <code class="docutils literal notranslate"><span class="pre">us</span></code>, <code class="docutils literal notranslate"><span class="pre">eu</span></code>, <code class="docutils literal notranslate"><span class="pre">highest_security</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Certificate’s private key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to enable support for legacy clients which do not include SNI in the TLS handshake. Valid values are <code class="docutils literal notranslate"><span class="pre">legacy_custom</span></code> (default), <code class="docutils literal notranslate"><span class="pre">sni_custom</span></code>.</p></li>
</ul>
<p>The <strong>custom_ssl_priorities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/custom_ssl.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/custom_ssl.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.CustomSsl.custom_ssl_options">
<code class="sig-name descname">custom_ssl_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.custom_ssl_options" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate, private key and associated optional parameters, such as bundle_method, geo_restrictions, and type.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bundle_method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Method of building intermediate certificate chain. A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. Valid values are <code class="docutils literal notranslate"><span class="pre">ubiquitous</span></code> (default), <code class="docutils literal notranslate"><span class="pre">optimal</span></code>, <code class="docutils literal notranslate"><span class="pre">force</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Certificate certificate and the intermediate(s)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geo_restrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the region where your private key can be held locally. Valid values are <code class="docutils literal notranslate"><span class="pre">us</span></code>, <code class="docutils literal notranslate"><span class="pre">eu</span></code>, <code class="docutils literal notranslate"><span class="pre">highest_security</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Certificate’s private key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to enable support for legacy clients which do not include SNI in the TLS handshake. Valid values are <code class="docutils literal notranslate"><span class="pre">legacy_custom</span></code> (default), <code class="docutils literal notranslate"><span class="pre">sni_custom</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.CustomSsl.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone id to the custom ssl cert should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.CustomSsl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_ssl_options=None</em>, <em class="sig-param">custom_ssl_priorities=None</em>, <em class="sig-param">expires_on=None</em>, <em class="sig-param">hosts=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">modified_on=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">signature=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">uploaded_on=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomSsl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_ssl_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The certificate, private key and associated optional parameters, such as bundle_method, geo_restrictions, and type.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone id to the custom ssl cert should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_ssl_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bundle_method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Method of building intermediate certificate chain. A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. Valid values are <code class="docutils literal notranslate"><span class="pre">ubiquitous</span></code> (default), <code class="docutils literal notranslate"><span class="pre">optimal</span></code>, <code class="docutils literal notranslate"><span class="pre">force</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Certificate certificate and the intermediate(s)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geo_restrictions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the region where your private key can be held locally. Valid values are <code class="docutils literal notranslate"><span class="pre">us</span></code>, <code class="docutils literal notranslate"><span class="pre">eu</span></code>, <code class="docutils literal notranslate"><span class="pre">highest_security</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Certificate’s private key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to enable support for legacy clients which do not include SNI in the TLS handshake. Valid values are <code class="docutils literal notranslate"><span class="pre">legacy_custom</span></code> (default), <code class="docutils literal notranslate"><span class="pre">sni_custom</span></code>.</p></li>
</ul>
<p>The <strong>custom_ssl_priorities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/custom_ssl.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/custom_ssl.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.CustomSsl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.CustomSsl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.CustomSsl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Filter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Filter</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expression=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">ref=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Filter expressions that can be referenced across multiple features, e.g. Firewall Rule. The expression format is similar to <a class="reference external" href="https://www.wireshark.org/docs/man-pages/wireshark-filter.html">Wireshark Display Filter</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the purpose of the filter.</p></li>
<li><p><strong>expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter expression to be used.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter is currently paused. Boolean value.</p></li>
<li><p><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short reference tag to quickly select related rules.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/filter.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/filter.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A note that you can use to describe the purpose of the filter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.expression">
<code class="sig-name descname">expression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter expression to be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.paused">
<code class="sig-name descname">paused</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this filter is currently paused. Boolean value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.ref">
<code class="sig-name descname">ref</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.ref" title="Permalink to this definition">¶</a></dt>
<dd><p>Short reference tag to quickly select related rules.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Filter.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Filter.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the Filter should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Filter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expression=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">ref=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Filter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the purpose of the filter.</p></li>
<li><p><strong>expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter expression to be used.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter is currently paused. Boolean value.</p></li>
<li><p><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Short reference tag to quickly select related rules.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/filter.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/filter.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Filter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Filter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Filter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.FirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">FirewallRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">filter_id=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">products=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Define Firewall rules using filter expressions for more control over how traffic is matched to the rule.
A filter expression permits selecting traffic by multiple criteria allowing greater freedom in rule creation.</p>
<p>Filter expressions needs to be created first before using Firewall Rule. See Filter.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”, “bypass”. Enterprise plan also allows “log”.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the rule to help identify it.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter based firewall rule is currently paused. Boolean value.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</p></li>
<li><p><strong>products</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of products to bypass for a request when the bypass action is used. Allowed values: “zoneLockdown”, “uaBlock”, “bic”, “hot”, “securityLevel”, “rateLimit”, “waf”.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/firewall_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.action">
<code class="sig-name descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”, “bypass”. Enterprise plan also allows “log”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the rule to help identify it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.paused">
<code class="sig-name descname">paused</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this filter based firewall rule is currently paused. Boolean value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.products">
<code class="sig-name descname">products</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.products" title="Permalink to this definition">¶</a></dt>
<dd><p>List of products to bypass for a request when the bypass action is used. Allowed values: “zoneLockdown”, “uaBlock”, “bic”, “hot”, “securityLevel”, “rateLimit”, “waf”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.FirewallRule.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone to which the Filter should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.FirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">filter_id=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">products=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to apply to a matched request. Allowed values: “block”, “challenge”, “allow”, “js_challenge”, “bypass”. Enterprise plan also allows “log”.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the rule to help identify it.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this filter based firewall rule is currently paused. Boolean value.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.</p></li>
<li><p><strong>products</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of products to bypass for a request when the bypass action is used. Allowed values: “zoneLockdown”, “uaBlock”, “bic”, “hot”, “securityLevel”, “rateLimit”, “waf”.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone to which the Filter should be added.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/firewall_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.FirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.FirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.GetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param">cidr_blocks=None</em>, <em class="sig-param">ipv4_cidr_blocks=None</em>, <em class="sig-param">ipv6_cidr_blocks=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpRanges.</p>
<dl class="attribute">
<dt id="pulumi_cloudflare.GetIpRangesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetIpRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.GetWafGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetWafGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetWafGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWafGroups.</p>
<dl class="attribute">
<dt id="pulumi_cloudflare.GetWafGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetWafGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.GetWafPackagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetWafPackagesResult</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">packages=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetWafPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWafPackages.</p>
<dl class="attribute">
<dt id="pulumi_cloudflare.GetWafPackagesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetWafPackagesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.GetWafRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetWafRulesResult</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetWafRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWafRules.</p>
<dl class="attribute">
<dt id="pulumi_cloudflare.GetWafRulesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetWafRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="attribute">
<dt id="pulumi_cloudflare.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudflare.LoadBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_pool_ids=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">fallback_pool_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pop_pools=None</em>, <em class="sig-param">proxied=None</em>, <em class="sig-param">region_pools=None</em>, <em class="sig-param">session_affinity=None</em>, <em class="sig-param">steering_policy=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Load Balancer resource. This sits in front of a number of defined pools of origins and provides various options for geographically-aware load balancing. Note that the load balancing feature must be enabled in your Clouflare account before you can use this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_pool_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</p></li>
<li><p><strong>fallback_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pool ID to use when all other pools are detected as unhealthy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name (FQDN, including the zone) to associate with the load balancer.</p></li>
<li><p><strong>pop_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>region_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</p></li>
<li><p><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.  Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cookie&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;ip_cookie&quot;</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>steering_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determine which method the load balancer uses to determine the fastest route to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the load balancer to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>pop_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A 3-letter code for the Point-of-Presence. Allowed values can be found in the list of datacenters on the <a class="reference external" href="https://www.cloudflarestatus.com/">status page</a>. Multiple entries should not be specified with the same PoP.</p></li>
</ul>
<p>The <strong>region_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A region code which must be in the list defined <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>. Multiple entries should not be specified with the same region.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.created_on">
<code class="sig-name descname">created_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.default_pool_ids">
<code class="sig-name descname">default_pool_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.default_pool_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.fallback_pool_id">
<code class="sig-name descname">fallback_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.fallback_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The pool ID to use when all other pools are detected as unhealthy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.modified_on">
<code class="sig-name descname">modified_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name (FQDN, including the zone) to associate with the load balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.pop_pools">
<code class="sig-name descname">pop_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.pop_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pop</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A 3-letter code for the Point-of-Presence. Allowed values can be found in the list of datacenters on the <a class="reference external" href="https://www.cloudflarestatus.com/">status page</a>. Multiple entries should not be specified with the same PoP.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.proxied">
<code class="sig-name descname">proxied</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.proxied" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.region_pools">
<code class="sig-name descname">region_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.region_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A region code which must be in the list defined <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>. Multiple entries should not be specified with the same region.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.session_affinity">
<code class="sig-name descname">session_affinity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.session_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.  Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cookie&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;ip_cookie&quot;</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.steering_policy">
<code class="sig-name descname">steering_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.steering_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Determine which method the load balancer uses to determine the fastest route to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancer.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID to add the load balancer to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created_on=None</em>, <em class="sig-param">default_pool_ids=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">fallback_pool_id=None</em>, <em class="sig-param">modified_on=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pop_pools=None</em>, <em class="sig-param">proxied=None</em>, <em class="sig-param">region_pools=None</em>, <em class="sig-param">session_affinity=None</em>, <em class="sig-param">steering_policy=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was created.</p></li>
<li><p><strong>default_pool_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of pool IDs ordered by their failover priority. Used whenever region/pop pools are not defined.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the load balancer. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code> (enabled).</p></li>
<li><p><strong>fallback_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pool ID to use when all other pools are detected as unhealthy.</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was last modified.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name (FQDN, including the zone) to associate with the load balancer.</p></li>
<li><p><strong>pop_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers. Fields documented below.</p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the hostname gets Cloudflare’s origin protection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>region_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing mappings of region/country codes to a list of pool IDs (ordered by their failover priority) for the given region. Fields documented below.</p></li>
<li><p><strong>session_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available.  Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;none&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;cookie&quot;</span></code>, and <code class="docutils literal notranslate"><span class="pre">&quot;ip_cookie&quot;</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>steering_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Determine which method the load balancer uses to determine the fastest route to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;geo&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;dynamic_latency&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;random&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time to live (TTL) of this load balancer’s DNS <code class="docutils literal notranslate"><span class="pre">name</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">proxied</span></code> - this cannot be set for proxied load balancers. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the load balancer to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>pop_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A 3-letter code for the Point-of-Presence. Allowed values can be found in the list of datacenters on the <a class="reference external" href="https://www.cloudflarestatus.com/">status page</a>. Multiple entries should not be specified with the same PoP.</p></li>
</ul>
<p>The <strong>region_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">poolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of pool IDs in failover priority to use for traffic reaching the given PoP.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A region code which must be in the list defined <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>. Multiple entries should not be specified with the same region.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LoadBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerMonitor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LoadBalancerMonitor</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_insecure=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expected_body=None</em>, <em class="sig-param">expected_codes=None</em>, <em class="sig-param">follow_redirects=None</em>, <em class="sig-param">headers=None</em>, <em class="sig-param">interval=None</em>, <em class="sig-param">method=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">retries=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor" title="Permalink to this definition">¶</a></dt>
<dd><p>If you’re using Cloudflare’s Load Balancing to load-balance across multiple origin servers or data centers, you configure one of these Monitors to actively check the availability of those servers over HTTP(S) or TCP.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not validate the certificate when monitor use HTTPS. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>expected_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”. Default: “”.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code>. Only valid and required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>follow_redirects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Follow redirects if returned by the origin. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The header name.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use for the health check. Valid values are any valid HTTP verb if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp”. Default: “GET” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or “connection_established” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp” .</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint path to health check against. Default: “/”. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timeout (in seconds) before marking the health check as failed. Default: 5.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’. Default: “http”.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of string values for the header.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer_monitor.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer_monitor.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.allow_insecure">
<code class="sig-name descname">allow_insecure</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.allow_insecure" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not validate the certificate when monitor use HTTPS. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.created_on">
<code class="sig-name descname">created_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer monitor was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.expected_body">
<code class="sig-name descname">expected_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.expected_body" title="Permalink to this definition">¶</a></dt>
<dd><p>A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”. Default: “”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.expected_codes">
<code class="sig-name descname">expected_codes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.expected_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code>. Only valid and required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.follow_redirects">
<code class="sig-name descname">follow_redirects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.follow_redirects" title="Permalink to this definition">¶</a></dt>
<dd><p>Follow redirects if returned by the origin. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.headers">
<code class="sig-name descname">headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>The header name.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of string values for the header.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.interval">
<code class="sig-name descname">interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.method">
<code class="sig-name descname">method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.method" title="Permalink to this definition">¶</a></dt>
<dd><p>The method to use for the health check. Valid values are any valid HTTP verb if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp”. Default: “GET” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or “connection_established” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp” .</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.modified_on">
<code class="sig-name descname">modified_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer monitor was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint path to health check against. Default: “/”. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.retries">
<code class="sig-name descname">retries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.retries" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The timeout (in seconds) before marking the health check as failed. Default: 5.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’. Default: “http”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_insecure=None</em>, <em class="sig-param">created_on=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expected_body=None</em>, <em class="sig-param">expected_codes=None</em>, <em class="sig-param">follow_redirects=None</em>, <em class="sig-param">headers=None</em>, <em class="sig-param">interval=None</em>, <em class="sig-param">method=None</em>, <em class="sig-param">modified_on=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">retries=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerMonitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not validate the certificate when monitor use HTTPS. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer monitor was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>expected_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”. Default: “”.</p></li>
<li><p><strong>expected_codes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The expected HTTP response code or code range of the health check. Eg <code class="docutils literal notranslate"><span class="pre">2xx</span></code>. Only valid and required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>follow_redirects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Follow redirects if returned by the origin. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The header name.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use for the health check. Valid values are any valid HTTP verb if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or <code class="docutils literal notranslate"><span class="pre">connection_established</span></code> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp”. Default: “GET” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”, or “connection_established” if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “tcp” .</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer monitor was last modified.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint path to health check against. Default: “/”. Only valid if <code class="docutils literal notranslate"><span class="pre">type</span></code> is “http” or “https”.</p></li>
<li><p><strong>retries</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timeout (in seconds) before marking the health check as failed. Default: 5.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use for the healthcheck. Currently supported protocols are ‘HTTP’, ‘HTTPS’ and ‘TCP’. Default: “http”.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">header</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of string values for the header.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer_monitor.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer_monitor.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LoadBalancerMonitor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerMonitor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerMonitor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LoadBalancerPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">check_regions=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">minimum_origins=None</em>, <em class="sig-param">monitor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification_email=None</em>, <em class="sig-param">origins=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Load Balancer pool resource. This provides a pool of origins that can be used by a Cloudflare Load Balancer. Note that the load balancing feature must be enabled in your Clouflare account before you can use this resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>check_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><strong>minimum_origins</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</p></li>
<li><p><strong>monitor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Monitor to use for health checking origins within this pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-identifiable name for the origin.</p></li>
<li><p><strong>notification_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address to send health status notifications to. This can be an individual mailbox or a mailing list.</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>origins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address (IPv4 or IPv6) of the origin, or the publicly addressable hostname. Hostnames entered here should resolve directly to the origin, and not be a hostname proxied by Cloudflare.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A human-identifiable name for the origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The weight (0.01 - 1.00) of this origin, relative to other origins in the pool. Equal values mean equal weighting. A weight of 0 means traffic will not be sent to this origin, but health is still checked. Default: 1.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer_pool.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.check_regions">
<code class="sig-name descname">check_regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.check_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.created_on">
<code class="sig-name descname">created_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Free text description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.minimum_origins">
<code class="sig-name descname">minimum_origins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.minimum_origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.modified_on">
<code class="sig-name descname">modified_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the load balancer was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.monitor">
<code class="sig-name descname">monitor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Monitor to use for health checking origins within this pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-identifiable name for the origin.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.notification_email">
<code class="sig-name descname">notification_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.notification_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address to send health status notifications to. This can be an individual mailbox or a mailing list.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LoadBalancerPool.origins">
<code class="sig-name descname">origins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP address (IPv4 or IPv6) of the origin, or the publicly addressable hostname. Hostnames entered here should resolve directly to the origin, and not be a hostname proxied by Cloudflare.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A human-identifiable name for the origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The weight (0.01 - 1.00) of this origin, relative to other origins in the pool. Equal values mean equal weighting. A weight of 0 means traffic will not be sent to this origin, but health is still checked. Default: 1.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LoadBalancerPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">check_regions=None</em>, <em class="sig-param">created_on=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">minimum_origins=None</em>, <em class="sig-param">modified_on=None</em>, <em class="sig-param">monitor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification_email=None</em>, <em class="sig-param">origins=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>check_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan. Region codes can be found <a class="reference external" href="https://support.cloudflare.com/hc/en-us/articles/115000540888-Load-Balancing-Geographic-Regions">here</a>.</p>
</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Free text description.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><strong>minimum_origins</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1.</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the load balancer was last modified.</p></li>
<li><p><strong>monitor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Monitor to use for health checking origins within this pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-identifiable name for the origin.</p></li>
<li><p><strong>notification_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address to send health status notifications to. This can be an individual mailbox or a mailing list.</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy. It’s a complex value. See description below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>origins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address (IPv4 or IPv6) of the origin, or the publicly addressable hostname. Hostnames entered here should resolve directly to the origin, and not be a hostname proxied by Cloudflare.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable (the default) this origin within the Pool. Disabled origins will not receive traffic and are excluded from health checks. The origin will only be disabled for the current pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A human-identifiable name for the origin.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The weight (0.01 - 1.00) of this origin, relative to other origins in the pool. Equal values mean equal weighting. A weight of 0 means traffic will not be sent to this origin, but health is still checked. Default: 1.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/load_balancer_pool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LoadBalancerPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LoadBalancerPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LoadBalancerPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogpushJob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">LogpushJob</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination_conf=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">logpull_options=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ownership_challenge=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which manages Cloudflare logpush jobs.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_conf</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p></li>
<li><p><strong>logpull_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options">Logpull options documentation</a>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logpush job to create. Must match the regular expression <code class="docutils literal notranslate"><span class="pre">^[a-zA-Z0-9\-\.]*$</span></code>.</p></li>
<li><p><strong>ownership_challenge</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage">Developer documentation</a>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the logpush job should be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/logpush_job.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/logpush_job.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.LogpushJob.destination_conf">
<code class="sig-name descname">destination_conf</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.destination_conf" title="Permalink to this definition">¶</a></dt>
<dd><p>Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LogpushJob.logpull_options">
<code class="sig-name descname">logpull_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.logpull_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options">Logpull options documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LogpushJob.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the logpush job to create. Must match the regular expression <code class="docutils literal notranslate"><span class="pre">^[a-zA-Z0-9\-\.]*$</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LogpushJob.ownership_challenge">
<code class="sig-name descname">ownership_challenge</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.ownership_challenge" title="Permalink to this definition">¶</a></dt>
<dd><p>Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage">Developer documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.LogpushJob.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID where the logpush job should be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LogpushJob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination_conf=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">logpull_options=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ownership_challenge=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogpushJob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_conf</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Uniquely identifies a resource (such as an s3 bucket) where data will be pushed. Additional configuration parameters supported by the destination may be included. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#destination">Logpush destination documentation</a>.</p>
</p></li>
<li><p><strong>logpull_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Configuration string for the Logshare API. It specifies things like requested fields and timestamp formats. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#options">Logpull options documentation</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the logpush job to create. Must match the regular expression <code class="docutils literal notranslate"><span class="pre">^[a-zA-Z0-9\-\.]*$</span></code>.</p></li>
<li><p><strong>ownership_challenge</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Ownership challenge token to prove destination ownership. See <a class="reference external" href="https://developers.cloudflare.com/logs/logpush/logpush-configuration-api/understanding-logpush-api/#usage">Developer documentation</a>.</p>
</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID where the logpush job should be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/logpush_job.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/logpush_job.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.LogpushJob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.LogpushJob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.LogpushJob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.OriginCaCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">OriginCaCertificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">csr=None</em>, <em class="sig-param">hostnames=None</em>, <em class="sig-param">request_type=None</em>, <em class="sig-param">requested_validity=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Origin CA certificate used to protect traffic to your origin without involving a third party Certificate Authority.</p>
<p><strong>This resource requires you use your Origin CA Key as the ``api_user_service_key``.</strong></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Signing Request. Must be newline-encoded.</p></li>
<li><p><strong>hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of hostnames or wildcard names bound to the certificate.</p></li>
<li><p><strong>request_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The signature type desired on the certificate.</p></li>
<li><p><strong>requested_validity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days for which the certificate should be valid.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/origin_ca_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/origin_ca_certificate.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The Origin CA certificate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.csr">
<code class="sig-name descname">csr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.csr" title="Permalink to this definition">¶</a></dt>
<dd><p>The Certificate Signing Request. Must be newline-encoded.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.expires_on">
<code class="sig-name descname">expires_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.expires_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The datetime when the certificate will expire.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.hostnames">
<code class="sig-name descname">hostnames</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of hostnames or wildcard names bound to the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.request_type">
<code class="sig-name descname">request_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.request_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The signature type desired on the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.OriginCaCertificate.requested_validity">
<code class="sig-name descname">requested_validity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.requested_validity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days for which the certificate should be valid.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.OriginCaCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">csr=None</em>, <em class="sig-param">expires_on=None</em>, <em class="sig-param">hostnames=None</em>, <em class="sig-param">request_type=None</em>, <em class="sig-param">requested_validity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OriginCaCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Origin CA certificate</p></li>
<li><p><strong>csr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Certificate Signing Request. Must be newline-encoded.</p></li>
<li><p><strong>expires_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datetime when the certificate will expire.</p></li>
<li><p><strong>hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of hostnames or wildcard names bound to the certificate.</p></li>
<li><p><strong>request_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The signature type desired on the certificate.</p></li>
<li><p><strong>requested_validity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of days for which the certificate should be valid.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/origin_ca_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/origin_ca_certificate.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.OriginCaCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.OriginCaCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.OriginCaCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.PageRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">PageRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare page rule resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The actions taken by the page rule, options given below.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the page rule is active or disabled.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL pattern to target with the page rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the page rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Time To Live for the browser cache. <code class="docutils literal notranslate"><span class="pre">0</span></code> means ‘Respect Existing Headers’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassCacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value of cookie name to conditionally bypass cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheByDeviceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheDeceptionArmor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the cache level to <code class="docutils literal notranslate"><span class="pre">&quot;bypass&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;basic&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;simplified&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;aggressive&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;cache_everything&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value of cookie name to conditionally cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableApps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disablePerformance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableRailgun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableSecurity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Time To Live for the edge cache.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">explicitCacheControl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether origin Cache-Control action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The URL to forward to, and with what status. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The status code to use for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to which the page rule should forward.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeaderOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the Host header to send.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minifies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The configuration for HTML, CSS and JS minification. See below for full list of options.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether CSS should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether HTML should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether Javascript should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;lossless&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;lossy&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolveOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overridden origin server name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">respectStrongEtag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the rocket loader to <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the security level to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;essentially_off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;low&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;medium&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;high&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;under_attack&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the SSL mode to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;flexible&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;full&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;strict&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;origin_pull&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/page_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/page_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.actions">
<code class="sig-name descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>The actions taken by the page rule, options given below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Time To Live for the browser cache. <code class="docutils literal notranslate"><span class="pre">0</span></code> means ‘Respect Existing Headers’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassCacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String value of cookie name to conditionally bypass cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheByDeviceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheDeceptionArmor</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to set the cache level to <code class="docutils literal notranslate"><span class="pre">&quot;bypass&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;basic&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;simplified&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;aggressive&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;cache_everything&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String value of cookie name to conditionally cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableApps</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disablePerformance</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableRailgun</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableSecurity</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Time To Live for the edge cache.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">explicitCacheControl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether origin Cache-Control action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The URL to forward to, and with what status. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The status code to use for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL to which the page rule should forward.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeaderOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the Host header to send.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minifies</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The configuration for HTML, CSS and JS minification. See below for full list of options.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether CSS should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether HTML should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether Javascript should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;lossless&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;lossy&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolveOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Overridden origin server name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">respectStrongEtag</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to set the rocket loader to <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to set the security level to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;essentially_off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;low&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;medium&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;high&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;under_attack&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to set the SSL mode to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;flexible&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;full&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;strict&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;origin_pull&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the page rule is active or disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.target">
<code class="sig-name descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL pattern to target with the page rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.PageRule.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.PageRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to which the page rule should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.PageRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PageRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The actions taken by the page rule, options given below.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The priority of the page rule among others for this target, the higher the number the higher the priority as per <a class="reference external" href="https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule">API documentation</a>.</p>
</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the page rule is active or disabled.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL pattern to target with the page rule.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the page rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Time To Live for the browser cache. <code class="docutils literal notranslate"><span class="pre">0</span></code> means ‘Respect Existing Headers’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bypassCacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value of cookie name to conditionally bypass cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheByDeviceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheDeceptionArmor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the cache level to <code class="docutils literal notranslate"><span class="pre">&quot;bypass&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;basic&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;simplified&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;aggressive&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;cache_everything&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheOnCookie</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value of cookie name to conditionally cache the page.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableApps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disablePerformance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableRailgun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableSecurity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean of whether this action is enabled. Default: false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Time To Live for the edge cache.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">explicitCacheControl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether origin Cache-Control action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forwardingUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The URL to forward to, and with what status. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The status code to use for the redirection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to which the page rule should forward.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostHeaderOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the Host header to send.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minifies</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The configuration for HTML, CSS and JS minification. See below for full list of options.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether CSS should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether HTML should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether Javascript should be minified. Valid values are <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;lossless&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;lossy&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resolveOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Overridden origin server name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">respectStrongEtag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the rocket loader to <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the security level to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;essentially_off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;low&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;medium&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;high&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;under_attack&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to set the SSL mode to <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;flexible&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;full&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;strict&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;origin_pull&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether this action is <code class="docutils literal notranslate"><span class="pre">&quot;on&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;off&quot;</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/page_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/page_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.PageRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.PageRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.PageRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">api_client_logging=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">api_token=None</em>, <em class="sig-param">api_user_service_key=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">max_backoff=None</em>, <em class="sig-param">min_backoff=None</em>, <em class="sig-param">retries=None</em>, <em class="sig-param">rps=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the cloudflare package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/index.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_cloudflare.Provider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Provider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/index.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.RateLimit">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">RateLimit</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">bypass_url_patterns=None</em>, <em class="sig-param">correlate=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">match=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">threshold=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare rate limit resource for a given zone. This can be used to limit the traffic you receive zone-wide, or matching more specific types of requests/responses.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The action to be performed when the threshold of matched traffic within the period defined is exceeded.</p></li>
<li><p><strong>bypass_url_patterns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – URLs matching the patterns specified here will be excluded from rate limiting.</p></li>
<li><p><strong>correlate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>match</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply rate limiting to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of action to perform. Allowable values are ‘simulate’, ‘ban’, ‘challenge’ and ‘js_challenge’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The body to return, the content here should conform to the content_type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content-type of the body, must be one of: ‘text/plain’, ‘text/xml’, ‘application/json’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time in seconds as an integer to perform the mitigation action. This field is required if the <code class="docutils literal notranslate"><span class="pre">mode</span></code> is either <code class="docutils literal notranslate"><span class="pre">simulate</span></code> or <code class="docutils literal notranslate"><span class="pre">ban</span></code>. Must be the same or greater than the period (min: 1, max: 86400).</p></li>
</ul>
<p>The <strong>correlate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">by</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If set to ‘nat’, NAT support will be enabled for rate limiting.</p></li>
</ul>
<p>The <strong>match</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Matches HTTP requests (from the client to Cloudflare). See definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Methods, can be a subset [‘POST’,’PUT’] or all [‘_ALL_’]. Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Schemes, can be one [‘HTTPS’], both [‘HTTP’,’HTTPS’] or all [‘_ALL_’].  Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL pattern to match comprised of the host and path, i.e. example.org/path. Wildcard are expanded to match applicable traffic, query strings are not matched. Use * for all traffic to your zone. Default: ‘<a href="#id16"><span class="problematic" id="id17">*</span></a>’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originTraffic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Only count traffic that has come from your origin servers. If true, cached items that Cloudflare serve will not count towards rate limiting. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statuses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Status codes, can be one [403], many [401,403] or indicate all by not providing this value.</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/rate_limit.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/rate_limit.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.action">
<code class="sig-name descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to be performed when the threshold of matched traffic within the period defined is exceeded.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of action to perform. Allowable values are ‘simulate’, ‘ban’, ‘challenge’ and ‘js_challenge’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The body to return, the content here should conform to the content_type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The content-type of the body, must be one of: ‘text/plain’, ‘text/xml’, ‘application/json’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The time in seconds as an integer to perform the mitigation action. This field is required if the <code class="docutils literal notranslate"><span class="pre">mode</span></code> is either <code class="docutils literal notranslate"><span class="pre">simulate</span></code> or <code class="docutils literal notranslate"><span class="pre">ban</span></code>. Must be the same or greater than the period (min: 1, max: 86400).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.bypass_url_patterns">
<code class="sig-name descname">bypass_url_patterns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.bypass_url_patterns" title="Permalink to this definition">¶</a></dt>
<dd><p>URLs matching the patterns specified here will be excluded from rate limiting.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.correlate">
<code class="sig-name descname">correlate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.correlate" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">by</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If set to ‘nat’, NAT support will be enabled for rate limiting.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.disabled">
<code class="sig-name descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.match">
<code class="sig-name descname">match</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.match" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Matches HTTP requests (from the client to Cloudflare). See definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - HTTP Methods, can be a subset [‘POST’,’PUT’] or all [‘_ALL_’]. Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - HTTP Schemes, can be one [‘HTTPS’], both [‘HTTP’,’HTTPS’] or all [‘_ALL_’].  Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL pattern to match comprised of the host and path, i.e. example.org/path. Wildcard are expanded to match applicable traffic, query strings are not matched. Use * for all traffic to your zone. Default: ‘<a href="#id18"><span class="problematic" id="id19">*</span></a>’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originTraffic</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Only count traffic that has come from your origin servers. If true, cached items that Cloudflare serve will not count towards rate limiting. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statuses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - HTTP Status codes, can be one [403], many [401,403] or indicate all by not providing this value.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.threshold">
<code class="sig-name descname">threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.RateLimit.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.RateLimit.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply rate limiting to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.RateLimit.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">bypass_url_patterns=None</em>, <em class="sig-param">correlate=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">match=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">threshold=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RateLimit resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The action to be performed when the threshold of matched traffic within the period defined is exceeded.</p></li>
<li><p><strong>bypass_url_patterns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – URLs matching the patterns specified here will be excluded from rate limiting.</p></li>
<li><p><strong>correlate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this ratelimit is currently disabled. Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>match</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply rate limiting to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>action</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of action to perform. Allowable values are ‘simulate’, ‘ban’, ‘challenge’ and ‘js_challenge’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The body to return, the content here should conform to the content_type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The content-type of the body, must be one of: ‘text/plain’, ‘text/xml’, ‘application/json’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time in seconds as an integer to perform the mitigation action. This field is required if the <code class="docutils literal notranslate"><span class="pre">mode</span></code> is either <code class="docutils literal notranslate"><span class="pre">simulate</span></code> or <code class="docutils literal notranslate"><span class="pre">ban</span></code>. Must be the same or greater than the period (min: 1, max: 86400).</p></li>
</ul>
<p>The <strong>correlate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">by</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If set to ‘nat’, NAT support will be enabled for rate limiting.</p></li>
</ul>
<p>The <strong>match</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">request</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Matches HTTP requests (from the client to Cloudflare). See definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">methods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Methods, can be a subset [‘POST’,’PUT’] or all [‘_ALL_’]. Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schemes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Schemes, can be one [‘HTTPS’], both [‘HTTP’,’HTTPS’] or all [‘_ALL_’].  Default: [‘_ALL_’].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL pattern to match comprised of the host and path, i.e. example.org/path. Wildcard are expanded to match applicable traffic, query strings are not matched. Use * for all traffic to your zone. Default: ‘<a href="#id20"><span class="problematic" id="id21">*</span></a>’.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">originTraffic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Only count traffic that has come from your origin servers. If true, cached items that Cloudflare serve will not count towards rate limiting. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statuses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - HTTP Status codes, can be one [403], many [401,403] or indicate all by not providing this value.</p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/rate_limit.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/rate_limit.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.RateLimit.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.RateLimit.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.RateLimit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Record">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Record</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">proxied=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare record resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the record</p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the record</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the record to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>data</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">altitude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fingerprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_tag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matching_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_horz</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_vert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The priority of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proto</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replacement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The type of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/record.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/record.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.Record.created_on">
<code class="sig-name descname">created_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.created_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the record was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.data">
<code class="sig-name descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.data" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">altitude</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest_type</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fingerprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_tag</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matching_type</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_horz</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_vert</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preference</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The priority of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proto</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replacement</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The type of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.hostname">
<code class="sig-name descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A key-value map of string metadata Cloudflare associates with the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.modified_on">
<code class="sig-name descname">modified_on</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.modified_on" title="Permalink to this definition">¶</a></dt>
<dd><p>The RFC3339 timestamp of when the record was last modified</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.proxiable">
<code class="sig-name descname">proxiable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.proxiable" title="Permalink to this definition">¶</a></dt>
<dd><p>Shows whether this record can be proxied, must be true if setting <code class="docutils literal notranslate"><span class="pre">proxied=true</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.proxied">
<code class="sig-name descname">proxied</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.proxied" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the record</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Record.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Record.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to add the record to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Record.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created_on=None</em>, <em class="sig-param">data=None</em>, <em class="sig-param">hostname=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">modified_on=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">proxiable=None</em>, <em class="sig-param">proxied=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Record resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the record was created</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or <code class="docutils literal notranslate"><span class="pre">value</span></code> must be specified</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the record</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key-value map of string metadata Cloudflare associates with the record</p></li>
<li><p><strong>modified_on</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RFC3339 timestamp of when the record was last modified</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the record</p></li>
<li><p><strong>proxiable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Shows whether this record can be proxied, must be true if setting <code class="docutils literal notranslate"><span class="pre">proxied=true</span></code></p></li>
<li><p><strong>proxied</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the record gets Cloudflare’s origin protection; defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The TTL of the record (<a class="reference external" href="https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record">automatic: ‘1’</a>)</p>
</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the record</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (string) value of the record. Either this or <code class="docutils literal notranslate"><span class="pre">data</span></code> must be specified</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the record to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>data</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">algorithm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">altitude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">digest_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fingerprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_tag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lat_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_degrees</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">long_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">matching_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_horz</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">precision_vert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The priority of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">proto</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replacement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The type of the record</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/record.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/record.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Record.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Record.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Record.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.SpectrumApplication">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">SpectrumApplication</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dns=None</em>, <em class="sig-param">ip_firewall=None</em>, <em class="sig-param">origin_directs=None</em>, <em class="sig-param">origin_dns=None</em>, <em class="sig-param">origin_port=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">proxy_protocol=None</em>, <em class="sig-param">tls=None</em>, <em class="sig-param">traffic_type=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Spectrum Application. You can extend the power of Cloudflare’s DDoS, TLS, and IP Firewall to your other TCP-based services.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The name and type of DNS record for the Spectrum application. Fields documented below.</p></li>
<li><p><strong>ip_firewall</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>origin_directs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</p></li>
<li><p><strong>origin_dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A destination DNS addresses to the origin. Fields documented below.</p></li>
<li><p><strong>origin_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</p></li>
<li><p><strong>proxy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables a proxy protocol to the origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, <code class="docutils literal notranslate"><span class="pre">v2</span></code>, and <code class="docutils literal notranslate"><span class="pre">simple</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tls</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>traffic_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set’s application type. Valid values are: <code class="docutils literal notranslate"><span class="pre">direct</span></code>, <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the application to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of DNS record associated with the application. Valid values: <code class="docutils literal notranslate"><span class="pre">CNAME</span></code>.</p></li>
</ul>
<p>The <strong>origin_dns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/spectrum_application.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/spectrum_application.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.dns">
<code class="sig-name descname">dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The name and type of DNS record for the Spectrum application. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of DNS record associated with the application. Valid values: <code class="docutils literal notranslate"><span class="pre">CNAME</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.ip_firewall">
<code class="sig-name descname">ip_firewall</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.ip_firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_directs">
<code class="sig-name descname">origin_directs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_directs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_dns">
<code class="sig-name descname">origin_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>A destination DNS addresses to the origin. Fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.origin_port">
<code class="sig-name descname">origin_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.origin_port" title="Permalink to this definition">¶</a></dt>
<dd><p>If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.proxy_protocol">
<code class="sig-name descname">proxy_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.proxy_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables a proxy protocol to the origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, <code class="docutils literal notranslate"><span class="pre">v2</span></code>, and <code class="docutils literal notranslate"><span class="pre">simple</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.tls">
<code class="sig-name descname">tls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.tls" title="Permalink to this definition">¶</a></dt>
<dd><p>TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.traffic_type">
<code class="sig-name descname">traffic_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.traffic_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Set’s application type. Valid values are: <code class="docutils literal notranslate"><span class="pre">direct</span></code>, <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.SpectrumApplication.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to add the application to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.SpectrumApplication.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dns=None</em>, <em class="sig-param">ip_firewall=None</em>, <em class="sig-param">origin_directs=None</em>, <em class="sig-param">origin_dns=None</em>, <em class="sig-param">origin_port=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">proxy_protocol=None</em>, <em class="sig-param">tls=None</em>, <em class="sig-param">traffic_type=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SpectrumApplication resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The name and type of DNS record for the Spectrum application. Fields documented below.</p></li>
<li><p><strong>ip_firewall</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables the IP Firewall for this application. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>origin_directs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of destination addresses to the origin. e.g. <code class="docutils literal notranslate"><span class="pre">tcp://192.0.2.1:22</span></code>.</p></li>
<li><p><strong>origin_dns</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A destination DNS addresses to the origin. Fields documented below.</p></li>
<li><p><strong>origin_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If using <code class="docutils literal notranslate"><span class="pre">origin_dns</span></code> this is a required attribute. Origin port to proxy traffice to e.g. <code class="docutils literal notranslate"><span class="pre">22</span></code>.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port configuration at Cloudflare’s edge. e.g. <code class="docutils literal notranslate"><span class="pre">tcp/22</span></code>.</p></li>
<li><p><strong>proxy_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enables a proxy protocol to the origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">v1</span></code>, <code class="docutils literal notranslate"><span class="pre">v2</span></code>, and <code class="docutils literal notranslate"><span class="pre">simple</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>tls</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS configuration option for Cloudflare to connect to your origin. Valid values are: <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">flexible</span></code>, <code class="docutils literal notranslate"><span class="pre">full</span></code> and <code class="docutils literal notranslate"><span class="pre">strict</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>traffic_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set’s application type. Valid values are: <code class="docutils literal notranslate"><span class="pre">direct</span></code>, <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to add the application to</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of DNS record associated with the application. Valid values: <code class="docutils literal notranslate"><span class="pre">CNAME</span></code>.</p></li>
</ul>
<p>The <strong>origin_dns</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Fully qualified domain name of the origin e.g. origin-ssh.example.com.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/spectrum_application.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/spectrum_application.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.SpectrumApplication.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.SpectrumApplication.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.SpectrumApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WafGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF rule group resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall groups.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule Group ID.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the group, can be one of [“on”, “off”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the group.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_group.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.WafGroup.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafGroup.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The WAF Rule Group ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafGroup.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafGroup.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of the group, can be one of [“on”, “off”].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafGroup.package_id">
<code class="sig-name descname">package_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafGroup.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Package that contains the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafGroup.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafGroup.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WafGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WafGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule Group ID.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the group, can be one of [“on”, “off”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the group.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_group.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WafGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafPackage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WafPackage</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action_mode=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">sensitivity=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF rule package resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall packages.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action mode of the package, can be one of [“block”, “challenge”, “simulate”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Package ID.</p></li>
<li><p><strong>sensitivity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sensitivity of the package, can be one of [“high”, “medium”, “low”, “off”].</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_package.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_package.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.WafPackage.action_mode">
<code class="sig-name descname">action_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafPackage.action_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The action mode of the package, can be one of [“block”, “challenge”, “simulate”].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafPackage.package_id">
<code class="sig-name descname">package_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafPackage.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The WAF Package ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafPackage.sensitivity">
<code class="sig-name descname">sensitivity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafPackage.sensitivity" title="Permalink to this definition">¶</a></dt>
<dd><p>The sensitivity of the package, can be one of [“high”, “medium”, “low”, “off”].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafPackage.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafPackage.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WafPackage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action_mode=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">sensitivity=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WafPackage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action mode of the package, can be one of [“block”, “challenge”, “simulate”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Package ID.</p></li>
<li><p><strong>sensitivity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sensitivity of the package, can be one of [“high”, “medium”, “low”, “off”].</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_package.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_package.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WafPackage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafPackage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafPackage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WafRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">rule_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare WAF rule resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall rules.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the rule.</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule ID.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.WafRule.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Group that contains the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafRule.mode">
<code class="sig-name descname">mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafRule.package_id">
<code class="sig-name descname">package_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF Rule Package that contains the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafRule.rule_id">
<code class="sig-name descname">rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The WAF Rule ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WafRule.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WafRule.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to apply to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WafRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">mode=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">rule_id=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WafRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Group that contains the rule.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode of the rule, can be one of [“block”, “challenge”, “default”, “disable”, “simulate”].</p></li>
<li><p><strong>package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF Rule Package that contains the rule.</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The WAF Rule ID.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to apply to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/waf_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WafRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WafRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WafRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerRoute">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkerRoute</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">pattern=None</em>, <em class="sig-param">script_name=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare worker route resource. A route will also require a <code class="docutils literal notranslate"><span class="pre">.WorkerScript</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://developers.cloudflare.com/workers/about/routes/">route pattern</a></p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `script_name` Which worker script to run for requests that match the route pattern. If `script_name` is empty, workers will be skipped for matching requests.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the route to.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/worker_route.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/worker_route.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerRoute.pattern">
<code class="sig-name descname">pattern</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://developers.cloudflare.com/workers/about/routes/">route pattern</a></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">script_name</span></code> Which worker script to run for requests that match the route pattern. If <code class="docutils literal notranslate"><span class="pre">script_name</span></code> is empty, workers will be skipped for matching requests.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerRoute.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID to add the route to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WorkerRoute.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">pattern=None</em>, <em class="sig-param">script_name=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkerRoute resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://developers.cloudflare.com/workers/about/routes/">route pattern</a></p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `script_name` Which worker script to run for requests that match the route pattern. If `script_name` is empty, workers will be skipped for matching requests.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID to add the route to.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/worker_route.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/worker_route.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WorkerRoute.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerRoute.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerScript">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkerScript</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">kv_namespace_bindings=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare worker script resource. In order for a script to be active, you’ll also need to setup a <code class="docutils literal notranslate"><span class="pre">.WorkerRoute</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script content.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the binding.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>kv_namespace_bindings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for the binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of KV namespace.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/worker_script.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/worker_script.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerScript.content">
<code class="sig-name descname">content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The script content.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WorkerScript.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the binding.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WorkerScript.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content=None</em>, <em class="sig-param">kv_namespace_bindings=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkerScript resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The script content.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the binding.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>kv_namespace_bindings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name for the binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of KV namespace.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/worker_script.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/worker_script.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WorkerScript.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkerScript.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkerScript.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKv">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkersKv</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">namespace_id=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Workers KV Pair.  <em>NOTE:</em>  This resource uses the Cloudflare account APIs.  This requires setting the <code class="docutils literal notranslate"><span class="pre">CLOUDFLARE_ACCOUNT_ID</span></code> environment variable or <code class="docutils literal notranslate"><span class="pre">account_id</span></code> provider argument.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Workers KV namespace in which you want to create the KV pair</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string value to be stored in the key</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/workers_kv.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/workers_kv.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.WorkersKv.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The key name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WorkersKv.namespace_id">
<code class="sig-name descname">namespace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Workers KV namespace in which you want to create the KV pair</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.WorkersKv.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The string value to be stored in the key</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WorkersKv.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">namespace_id=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkersKv resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key name</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Workers KV namespace in which you want to create the KV pair</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string value to be stored in the key</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/workers_kv.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/workers_kv.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WorkersKv.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKv.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKv.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKvNamespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">WorkersKvNamespace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Workers KV Namespace</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace you wish to create.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/workers_kv_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/workers_kv_namespace.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.WorkersKvNamespace.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the namespace you wish to create.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WorkersKvNamespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">title=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkersKvNamespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the namespace you wish to create.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/workers_kv_namespace.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/workers_kv_namespace.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.WorkersKvNamespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.WorkersKvNamespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.WorkersKvNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Zone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">Zone</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">jump_start=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Zone resource. Zone is the basic resource for working with Cloudflare and is roughly equivalent to a domain name that the user purchases.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>jump_start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone name which will be added.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.jump_start">
<code class="sig-name descname">jump_start</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.jump_start" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.name_servers">
<code class="sig-name descname">name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloudflare-assigned name servers. This is only populated for zones that use Cloudflare DNS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.paused">
<code class="sig-name descname">paused</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the zone. Valid values: <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">initializing</span></code>, <code class="docutils literal notranslate"><span class="pre">moved</span></code>, <code class="docutils literal notranslate"><span class="pre">deleted</span></code>, <code class="docutils literal notranslate"><span class="pre">deactivated</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.type" title="Permalink to this definition">¶</a></dt>
<dd><p>A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.vanity_name_servers">
<code class="sig-name descname">vanity_name_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.vanity_name_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Vanity Nameservers (if set).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">meta.wildcard_proxiable</span></code> - Indicates whether wildcard DNS records can receive Cloudflare security and performance features.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">meta.phishing_detected</span></code> - Indicates if URLs on the zone have been identified as hosting phishing content.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.verification_key">
<code class="sig-name descname">verification_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.verification_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the TXT record value to validate domain ownership. This is only populated for zones of type <code class="docutils literal notranslate"><span class="pre">partial</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.Zone.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.Zone.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone name which will be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Zone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">jump_start=None</em>, <em class="sig-param">meta=None</em>, <em class="sig-param">name_servers=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vanity_name_servers=None</em>, <em class="sig-param">verification_key=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Zone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>jump_start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether to scan for DNS records on creation. Ignored after zone is created. Default: false.</p></li>
<li><p><strong>name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Cloudflare-assigned name servers. This is only populated for zones that use Cloudflare DNS.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone is paused (traffic bypasses Cloudflare). Default: false.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the commercial plan to apply to the zone, can be updated once the one is created; one of <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">pro</span></code>, <code class="docutils literal notranslate"><span class="pre">business</span></code>, <code class="docutils literal notranslate"><span class="pre">enterprise</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the zone. Valid values: <code class="docutils literal notranslate"><span class="pre">active</span></code>, <code class="docutils literal notranslate"><span class="pre">pending</span></code>, <code class="docutils literal notranslate"><span class="pre">initializing</span></code>, <code class="docutils literal notranslate"><span class="pre">moved</span></code>, <code class="docutils literal notranslate"><span class="pre">deleted</span></code>, <code class="docutils literal notranslate"><span class="pre">deactivated</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup. Valid values: <code class="docutils literal notranslate"><span class="pre">full</span></code>, <code class="docutils literal notranslate"><span class="pre">partial</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">full</span></code>.</p></li>
<li><p><strong>vanity_name_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Vanity Nameservers (if set).</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `meta.wildcard_proxiable` - Indicates whether wildcard DNS records can receive Cloudflare security and performance features.
* `meta.phishing_detected` - Indicates if URLs on the zone have been identified as hosting phishing content.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>verification_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains the TXT record value to validate domain ownership. This is only populated for zones of type <code class="docutils literal notranslate"><span class="pre">partial</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone name which will be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>meta</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">phishing_detected</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">wildcard_proxiable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.Zone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.Zone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneLockdown">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">ZoneLockdown</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">configurations=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">urls=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cloudflare Zone Lockdown resource. Zone Lockdown allows you to define one or more URLs (with wildcard matching on the domain or path) that will only permit access if the request originates from an IP address that matches a safelist of one or more IP addresses and/or IP ranges.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone lockdown is currently paused. Default: false.</p></li>
<li><p><strong>urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request property to target. Allowed values: “ip”, “ip_range”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to target. Depends on target’s type. IP addresses should just be standard IPv4/IPv6 notation i.e. <code class="docutils literal notranslate"><span class="pre">198.51.100.4</span></code> or <code class="docutils literal notranslate"><span class="pre">2001:db8::/32</span></code> and IP ranges in CIDR format i.e. <code class="docutils literal notranslate"><span class="pre">198.51.0.0/16</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone_lockdown.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone_lockdown.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.configurations">
<code class="sig-name descname">configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The request property to target. Allowed values: “ip”, “ip_range”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value to target. Depends on target’s type. IP addresses should just be standard IPv4/IPv6 notation i.e. <code class="docutils literal notranslate"><span class="pre">198.51.100.4</span></code> or <code class="docutils literal notranslate"><span class="pre">2001:db8::/32</span></code> and IP ranges in CIDR format i.e. <code class="docutils literal notranslate"><span class="pre">198.51.0.0/16</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.paused">
<code class="sig-name descname">paused</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean of whether this zone lockdown is currently paused. Default: false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.urls">
<code class="sig-name descname">urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneLockdown.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to which the access rule should be added.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.ZoneLockdown.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">configurations=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">paused=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">urls=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneLockdown resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It’s a complex value. See description below.   The order of the configuration entries is unimportant.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean of whether this zone lockdown is currently paused. Default: false.</p></li>
<li><p><strong>urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which the access rule should be added.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The request property to target. Allowed values: “ip”, “ip_range”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value to target. Depends on target’s type. IP addresses should just be standard IPv4/IPv6 notation i.e. <code class="docutils literal notranslate"><span class="pre">198.51.100.4</span></code> or <code class="docutils literal notranslate"><span class="pre">2001:db8::/32</span></code> and IP ranges in CIDR format i.e. <code class="docutils literal notranslate"><span class="pre">198.51.0.0/16</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone_lockdown.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone_lockdown.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.ZoneLockdown.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneLockdown.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneLockdown.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneSettingsOverride">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">ZoneSettingsOverride</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which customizes Cloudflare zone settings. Note that after destroying this resource Zone Settings will be reset to their initial values.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which apply settings.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">brotli</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">challengeTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cnameFlattening</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developmentMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">h2Prioritization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hotlinkProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageResizing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUpload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (Required)”on”/”off”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileRedirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticOnion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefetchPreload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privacyPass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudoIpv4</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeSubdomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nosniff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls12Only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls13</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websockets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zeroRtt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone_settings_override.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone_settings_override.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.initial_settings">
<code class="sig-name descname">initial_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.initial_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings present in the zone at the time the resource is created. This will be used to restore the original settings when this resource is destroyed. Shares the same schema as the <code class="docutils literal notranslate"><span class="pre">settings</span></code> attribute (Above).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">brotli</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">challengeTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cnameFlattening</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developmentMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">h2Prioritization</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hotlinkProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http3</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageResizing</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUpload</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minify</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (Required)”on”/”off”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileRedirect</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripUri</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticOnion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefetchPreload</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privacyPass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudoIpv4</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeSubdomains</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nosniff</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preload</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls12Only</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls13</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websockets</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zeroRtt</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.readonly_settings">
<code class="sig-name descname">readonly_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.readonly_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Which of the current <code class="docutils literal notranslate"><span class="pre">settings</span></code> are not able to be set by the user. Which settings these are is determined by plan level and user permissions.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">zone_status</span></code>. A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone_type</span></code>. Status of the zone. Valid values: active, pending, initializing, moved, deleted, deactivated.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.settings">
<code class="sig-name descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">brotli</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">challengeTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cnameFlattening</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developmentMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">h2Prioritization</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hotlinkProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http3</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageResizing</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUpload</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minify</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (Required)”on”/”off”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileRedirect</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripUri</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticOnion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefetchPreload</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privacyPass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudoIpv4</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeSubdomains</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nosniff</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preload</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls12Only</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls13</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websockets</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zeroRtt</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS zone ID to which apply settings.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">initial_settings=None</em>, <em class="sig-param">initial_settings_read_at=None</em>, <em class="sig-param">readonly_settings=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">zone_status=None</em>, <em class="sig-param">zone_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneSettingsOverride resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>initial_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings present in the zone at the time the resource is created. This will be used to restore the original settings when this resource is destroyed. Shares the same schema as the <code class="docutils literal notranslate"><span class="pre">settings</span></code> attribute (Above).</p></li>
<li><p><strong>readonly_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Which of the current <code class="docutils literal notranslate"><span class="pre">settings</span></code> are not able to be set by the user. Which settings these are is determined by plan level and user permissions.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `zone_status`. A full zone implies that DNS is hosted with Cloudflare. A partial zone is typically a partner-hosted zone or a CNAME setup.
* `zone_type`. Status of the zone. Valid values: active, pending, initializing, moved, deleted, deactivated.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings overrides that will be applied to the zone. If a setting is not specified the existing setting will be used. For a full list of available settings see below.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS zone ID to which apply settings.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>initial_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">brotli</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">challengeTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cnameFlattening</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developmentMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">h2Prioritization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hotlinkProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageResizing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUpload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (Required)”on”/”off”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileRedirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticOnion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefetchPreload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privacyPass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudoIpv4</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeSubdomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nosniff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls12Only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls13</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websockets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zeroRtt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysOnline</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alwaysUseHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">automaticHttpsRewrites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">brotli</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">browserCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">challengeTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cnameFlattening</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">developmentMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">edgeCacheTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailObfuscation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">h2Prioritization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hotlinkProtection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http2</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageResizing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipGeolocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUpload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTlsVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minify</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">css</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">html</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (Required)”on”/”off”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">js</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mirage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileRedirect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileSubdomain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String value</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - “on”/”off”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stripUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">opportunisticOnion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">originErrorPagePassThru</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">polish</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefetchPreload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privacyPass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pseudoIpv4</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseBuffering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rocketLoader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeSubdomains</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nosniff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preload</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - true/false</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverSideExclude</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortQueryStringForCache</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls12Only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls13</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsClientAuth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trueClientIpHeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">waf</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">webp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">websockets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zeroRtt</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone_settings_override.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/r/zone_settings_override.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudflare.ZoneSettingsOverride.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.ZoneSettingsOverride.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.ZoneSettingsOverride.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudflare.get_ip_ranges">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_ip_ranges</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the [IP ranges][1] of Cloudflare edge nodes.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/d/ip_ranges.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/d/ip_ranges.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudflare.get_waf_groups">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_waf_groups</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_waf_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up [WAF Rule Groups][1].</p>
<p>The <strong>filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/d/waf_groups.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/d/waf_groups.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudflare.get_waf_packages">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_waf_packages</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_waf_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up [WAF Rule Packages][1].</p>
<p>The <strong>filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action_mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">detectionMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sensitivity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/d/waf_packages.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/d/waf_packages.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudflare.get_waf_rules">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_waf_rules</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">package_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_waf_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up [WAF Rules][1].</p>
<p>The <strong>filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/d/waf_rules.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/d/waf_rules.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudflare.get_zones">
<code class="sig-prename descclassname">pulumi_cloudflare.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudflare.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to look up [Zone][1] records.</p>
<p>The <strong>filter</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paused</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/d/zones.html.markdown">https://github.com/terraform-providers/terraform-provider-cloudflare/blob/master/website/docs/d/zones.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
