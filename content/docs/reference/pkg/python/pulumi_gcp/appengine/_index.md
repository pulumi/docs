---
title: Module appengine
---

<div class="section" id="appengine">
<h1>appengine<a class="headerlink" href="#appengine" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_gcp.appengine"></span><dl class="class">
<dt id="pulumi_gcp.appengine.Application">
<em class="property">class </em><code class="descclassname">pulumi_gcp.appengine.</code><code class="descname">Application</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auth_domain=None</em>, <em>feature_settings=None</em>, <em>location_id=None</em>, <em>project=None</em>, <em>serving_status=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of an App Engine application.</p>
<blockquote>
<div><dl class="docutils">
<dt>App Engine applications cannot be deleted once they’re created; you have to delete the</dt>
<dd>entire project to delete the application. This provider will report the application has been
successfully deleted; this is a limitation of this provider, and will go away in the future.
This provider is not able to delete App Engine applications.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auth_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to authenticate users with when using App Engine’s User API.</li>
<li><strong>feature_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A block of optional settings to configure specific App Engine features:</li>
<li><strong>location_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://cloud.google.com/appengine/docs/locations">location</a>
to serve the app from.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID to create the application under.
~&gt;<strong>NOTE</strong>: GCP only accepts project ID, not project number. If you are using number,
you may get a “Permission denied” error.</li>
<li><strong>serving_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The serving status of the app.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_application.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_application.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.auth_domain">
<code class="descname">auth_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.auth_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain to authenticate users with when using App Engine’s User API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.code_bucket">
<code class="descname">code_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.code_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCS bucket code is being stored in for this app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.default_bucket">
<code class="descname">default_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.default_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCS bucket content is being stored in for this app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.default_hostname">
<code class="descname">default_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.default_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The default hostname for this app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.feature_settings">
<code class="descname">feature_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.feature_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A block of optional settings to configure specific App Engine features:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.gcr_domain">
<code class="descname">gcr_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.gcr_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCR domain used for storing managed Docker images for this app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.location_id">
<code class="descname">location_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.location_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://cloud.google.com/appengine/docs/locations">location</a>
to serve the app from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique name of the app, usually <code class="docutils literal notranslate"><span class="pre">apps/{PROJECT_ID}</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID to create the application under.
~&gt;<strong>NOTE</strong>: GCP only accepts project ID, not project number. If you are using number,
you may get a “Permission denied” error.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.serving_status">
<code class="descname">serving_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.serving_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The serving status of the app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.url_dispatch_rules">
<code class="descname">url_dispatch_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.url_dispatch_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of dispatch rule blocks. Each block has a <code class="docutils literal notranslate"><span class="pre">domain</span></code>, <code class="docutils literal notranslate"><span class="pre">path</span></code>, and <code class="docutils literal notranslate"><span class="pre">service</span></code> field.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gcp.appengine.Application.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>auth_domain=None</em>, <em>code_bucket=None</em>, <em>default_bucket=None</em>, <em>default_hostname=None</em>, <em>feature_settings=None</em>, <em>gcr_domain=None</em>, <em>location_id=None</em>, <em>name=None</em>, <em>project=None</em>, <em>serving_status=None</em>, <em>url_dispatch_rules=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] auth_domain: The domain to authenticate users with when using App Engine’s User API.
:param pulumi.Input[str] code_bucket: The GCS bucket code is being stored in for this app.
:param pulumi.Input[str] default_bucket: The GCS bucket content is being stored in for this app.
:param pulumi.Input[str] default_hostname: The default hostname for this app.
:param pulumi.Input[dict] feature_settings: A block of optional settings to configure specific App Engine features:
:param pulumi.Input[str] gcr_domain: The GCR domain used for storing managed Docker images for this app.
:param pulumi.Input[str] location_id: The <a class="reference external" href="https://cloud.google.com/appengine/docs/locations">location</a></p>
<blockquote>
<div>to serve the app from.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name of the app, usually <code class="docutils literal notranslate"><span class="pre">apps/{PROJECT_ID}</span></code></li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID to create the application under.
~&gt;<strong>NOTE</strong>: GCP only accepts project ID, not project number. If you are using number,
you may get a “Permission denied” error.</li>
<li><strong>serving_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The serving status of the app.</li>
<li><strong>url_dispatch_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of dispatch rule blocks. Each block has a <code class="docutils literal notranslate"><span class="pre">domain</span></code>, <code class="docutils literal notranslate"><span class="pre">path</span></code>, and <code class="docutils literal notranslate"><span class="pre">service</span></code> field.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_application.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_application.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.Application.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.Application.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.FirewallRule">
<em class="property">class </em><code class="descclassname">pulumi_gcp.appengine.</code><code class="descname">FirewallRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>action=None</em>, <em>description=None</em>, <em>priority=None</em>, <em>project=None</em>, <em>source_range=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>A single firewall rule that is evaluated against incoming traffic
and provides an action to take on matched requests.</p>
<p>To get more information about FirewallRule, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules">API documentation</a></li>
<li>How-to Guides<ul>
<li><a class="reference external" href="https://cloud.google.com/appengine/docs/standard/python/creating-firewalls#creating_firewall_rules">Official Documentation</a></li>
</ul>
</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_firewall_rule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.appengine.FirewallRule.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gcp.appengine.FirewallRule.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>action=None</em>, <em>description=None</em>, <em>priority=None</em>, <em>project=None</em>, <em>source_range=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] project: The ID of the project in which the resource belongs.</p>
<blockquote>
<div>If it is not provided, the provider project is used.</div></blockquote>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/app_engine_firewall_rule.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.FirewallRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.FirewallRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
