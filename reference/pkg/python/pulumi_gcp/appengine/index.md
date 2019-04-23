<div class="section" id="module-pulumi_gcp.appengine">
<span id="appengine"></span><h1>appengine<a class="headerlink" href="#module-pulumi_gcp.appengine" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.appengine.Application">
<em class="property">class </em><code class="descclassname">pulumi_gcp.appengine.</code><code class="descname">Application</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auth_domain=None</em>, <em>feature_settings=None</em>, <em>location_id=None</em>, <em>project=None</em>, <em>serving_status=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of an App Engine application.</p>
<blockquote>
<div><dl class="docutils">
<dt>App Engine applications cannot be deleted once they’re created; you have to delete the</dt>
<dd>entire project to delete the application. Terraform will report the application has been
successfully deleted; this is a limitation of Terraform, and will go away in the future.
Terraform is not able to delete App Engine applications.</dd>
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
<li><strong>serving_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The serving status of the app.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
<dt id="pulumi_gcp.appengine.Application.serving_status">
<code class="descname">serving_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.serving_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The serving status of the app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.url_dispatch_rules">
<code class="descname">url_dispatch_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.url_dispatch_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of dispatch rule blocks. Each block has a <code class="docutils literal notranslate"><span class="pre">domain</span></code>, <code class="docutils literal notranslate"><span class="pre">path</span></code>, and <code class="docutils literal notranslate"><span class="pre">service</span></code> field.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_gcp.appengine.</code><code class="descname">FirewallRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>action=None</em>, <em>description=None</em>, <em>priority=None</em>, <em>project=None</em>, <em>source_range=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule" title="Permalink to this definition">¶</a></dt>
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
<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=app_engine_firewall_rule_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div><table class="docutils field-list" frame="void" rules="none">
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
<dl class="attribute">
<dt id="pulumi_gcp.appengine.FirewallRule.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
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
