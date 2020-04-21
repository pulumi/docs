---
title: Module appengine
title_tag: Module appengine | Package pulumi_gcp | Python SDK
linktitle: appengine
notitle: true
---

<div class="section" id="appengine">
<h1>appengine<a class="headerlink" href="#appengine" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.appengine"></span><dl class="class">
<dt id="pulumi_gcp.appengine.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.appengine.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auth_domain=None</em>, <em class="sig-param">feature_settings=None</em>, <em class="sig-param">iap=None</em>, <em class="sig-param">location_id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">serving_status=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of an App Engine application.</p>
<blockquote>
<div><dl class="simple">
<dt>App Engine applications cannot be deleted once they’re created; you have to delete the</dt><dd><p>entire project to delete the application. This provider will report the application has been
successfully deleted; this is a limitation of the provider, and will go away in the future.
This provider is not able to delete App Engine applications.</p>
</dd>
</dl>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to authenticate users with when using App Engine’s User API.</p></li>
<li><p><strong>feature_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A block of optional settings to configure specific App Engine features:</p></li>
<li><p><strong>iap</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings for enabling Cloud Identity Aware Proxy</p></li>
<li><p><strong>location_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://cloud.google.com/appengine/docs/locations">location</a>
to serve the app from.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID to create the application under.
~&gt;<strong>NOTE</strong>: GCP only accepts project ID, not project number. If you are using number,
you may get a “Permission denied” error.</p></li>
<li><p><strong>serving_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The serving status of the app.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>feature_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">splitHealthChecks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to false to use the legacy health check instead of the readiness
and liveness checks.</p></li>
</ul>
<p>The <strong>iap</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientSecretSha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.app_id">
<code class="sig-name descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the app, usually <code class="docutils literal notranslate"><span class="pre">{PROJECT_ID}</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.auth_domain">
<code class="sig-name descname">auth_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.auth_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain to authenticate users with when using App Engine’s User API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.code_bucket">
<code class="sig-name descname">code_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.code_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCS bucket code is being stored in for this app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.default_bucket">
<code class="sig-name descname">default_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.default_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCS bucket content is being stored in for this app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.default_hostname">
<code class="sig-name descname">default_hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.default_hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The default hostname for this app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.feature_settings">
<code class="sig-name descname">feature_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.feature_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A block of optional settings to configure specific App Engine features:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">splitHealthChecks</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set to false to use the legacy health check instead of the readiness
and liveness checks.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.gcr_domain">
<code class="sig-name descname">gcr_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.gcr_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCR domain used for storing managed Docker images for this app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.iap">
<code class="sig-name descname">iap</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.iap" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings for enabling Cloud Identity Aware Proxy</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientSecretSha256</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.location_id">
<code class="sig-name descname">location_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.location_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://cloud.google.com/appengine/docs/locations">location</a>
to serve the app from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique name of the app, usually <code class="docutils literal notranslate"><span class="pre">apps/{PROJECT_ID}</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID to create the application under.
~&gt;<strong>NOTE</strong>: GCP only accepts project ID, not project number. If you are using number,
you may get a “Permission denied” error.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.serving_status">
<code class="sig-name descname">serving_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.serving_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The serving status of the app.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.Application.url_dispatch_rules">
<code class="sig-name descname">url_dispatch_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.Application.url_dispatch_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of dispatch rule blocks. Each block has a <code class="docutils literal notranslate"><span class="pre">domain</span></code>, <code class="docutils literal notranslate"><span class="pre">path</span></code>, and <code class="docutils literal notranslate"><span class="pre">service</span></code> field.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_id=None</em>, <em class="sig-param">auth_domain=None</em>, <em class="sig-param">code_bucket=None</em>, <em class="sig-param">default_bucket=None</em>, <em class="sig-param">default_hostname=None</em>, <em class="sig-param">feature_settings=None</em>, <em class="sig-param">gcr_domain=None</em>, <em class="sig-param">iap=None</em>, <em class="sig-param">location_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">serving_status=None</em>, <em class="sig-param">url_dispatch_rules=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the app, usually <code class="docutils literal notranslate"><span class="pre">{PROJECT_ID}</span></code></p></li>
<li><p><strong>auth_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to authenticate users with when using App Engine’s User API.</p></li>
<li><p><strong>code_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCS bucket code is being stored in for this app.</p></li>
<li><p><strong>default_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCS bucket content is being stored in for this app.</p></li>
<li><p><strong>default_hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default hostname for this app.</p></li>
<li><p><strong>feature_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A block of optional settings to configure specific App Engine features:</p></li>
<li><p><strong>gcr_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCR domain used for storing managed Docker images for this app.</p></li>
<li><p><strong>iap</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings for enabling Cloud Identity Aware Proxy</p></li>
<li><p><strong>location_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://cloud.google.com/appengine/docs/locations">location</a>
to serve the app from.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name of the app, usually <code class="docutils literal notranslate"><span class="pre">apps/{PROJECT_ID}</span></code></p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID to create the application under.
~&gt;<strong>NOTE</strong>: GCP only accepts project ID, not project number. If you are using number,
you may get a “Permission denied” error.</p></li>
<li><p><strong>serving_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The serving status of the app.</p></li>
<li><p><strong>url_dispatch_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of dispatch rule blocks. Each block has a <code class="docutils literal notranslate"><span class="pre">domain</span></code>, <code class="docutils literal notranslate"><span class="pre">path</span></code>, and <code class="docutils literal notranslate"><span class="pre">service</span></code> field.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>feature_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">splitHealthChecks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to false to use the legacy health check instead of the readiness
and liveness checks.</p></li>
</ul>
<p>The <strong>iap</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauth2ClientSecretSha256</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>url_dispatch_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.ApplicationUrlDispatchRules">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.appengine.</code><code class="sig-name descname">ApplicationUrlDispatchRules</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dispatch_rules=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.ApplicationUrlDispatchRules" title="Permalink to this definition">¶</a></dt>
<dd><p>Rules to match an HTTP request and dispatch that request to a service.</p>
<p>To get more information about ApplicationUrlDispatchRules, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps#UrlDispatchRule">API documentation</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dispatch_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Rules to match an HTTP request and dispatch that request to a service.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dispatch_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.appengine.ApplicationUrlDispatchRules.dispatch_rules">
<code class="sig-name descname">dispatch_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.ApplicationUrlDispatchRules.dispatch_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Rules to match an HTTP request and dispatch that request to a service.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.ApplicationUrlDispatchRules.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.ApplicationUrlDispatchRules.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.ApplicationUrlDispatchRules.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dispatch_rules=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.ApplicationUrlDispatchRules.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationUrlDispatchRules resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dispatch_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Rules to match an HTTP request and dispatch that request to a service.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dispatch_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.ApplicationUrlDispatchRules.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.ApplicationUrlDispatchRules.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.ApplicationUrlDispatchRules.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.ApplicationUrlDispatchRules.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.DomainMapping">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.appengine.</code><code class="sig-name descname">DomainMapping</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">override_strategy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">ssl_settings=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.DomainMapping" title="Permalink to this definition">¶</a></dt>
<dd><p>A domain serving an App Engine application.</p>
<p>To get more information about DomainMapping, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/appengine/docs/standard/python/mapping-custom-domains">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Relative name of the domain serving the application. Example: example.com.</p></li>
<li><p><strong>override_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>ssl_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ssl_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pendingManagedCertificateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslManagementType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.appengine.DomainMapping.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.DomainMapping.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Relative name of the domain serving the application. Example: example.com.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.DomainMapping.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.DomainMapping.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Full path to the DomainMapping resource in the API. Example: apps/myapp/domainMapping/example.com.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.DomainMapping.override_strategy">
<code class="sig-name descname">override_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.DomainMapping.override_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.DomainMapping.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.DomainMapping.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.DomainMapping.resource_records">
<code class="sig-name descname">resource_records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.DomainMapping.resource_records" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource records required to configure this domain mapping. These records must be added to the domain’s DNS
configuration in order to serve the application via this domain mapping.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rrdata</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.DomainMapping.ssl_settings">
<code class="sig-name descname">ssl_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.DomainMapping.ssl_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pendingManagedCertificateId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslManagementType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.DomainMapping.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">override_strategy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">resource_records=None</em>, <em class="sig-param">ssl_settings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.DomainMapping.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainMapping resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Relative name of the domain serving the application. Example: example.com.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Full path to the DomainMapping resource in the API. Example: apps/myapp/domainMapping/example.com.</p></li>
<li><p><strong>override_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>resource_records</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The resource records required to configure this domain mapping. These records must be added to the domain’s DNS
configuration in order to serve the application via this domain mapping.</p></li>
<li><p><strong>ssl_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>resource_records</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rrdata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ssl_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pendingManagedCertificateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslManagementType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.DomainMapping.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.DomainMapping.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.DomainMapping.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.DomainMapping.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.EngineSplitTraffic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.appengine.</code><code class="sig-name descname">EngineSplitTraffic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">migrate_traffic=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">split=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.EngineSplitTraffic" title="Permalink to this definition">¶</a></dt>
<dd><p>Traffic routing configuration for versions within a single service. Traffic splits define how traffic directed to the service is assigned to versions.</p>
<p>To get more information about ServiceSplitTraffic, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services">API documentation</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>migrate_traffic</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true traffic will be migrated to this version.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service these settings apply to.</p></li>
<li><p><strong>split</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Mapping that defines fractional HTTP traffic diversion to different versions within the service.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>split</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shardBy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.appengine.EngineSplitTraffic.migrate_traffic">
<code class="sig-name descname">migrate_traffic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.EngineSplitTraffic.migrate_traffic" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to true traffic will be migrated to this version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.EngineSplitTraffic.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.EngineSplitTraffic.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.EngineSplitTraffic.service">
<code class="sig-name descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.EngineSplitTraffic.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service these settings apply to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.EngineSplitTraffic.split">
<code class="sig-name descname">split</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.EngineSplitTraffic.split" title="Permalink to this definition">¶</a></dt>
<dd><p>Mapping that defines fractional HTTP traffic diversion to different versions within the service.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocations</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shardBy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.EngineSplitTraffic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">migrate_traffic=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">split=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.EngineSplitTraffic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EngineSplitTraffic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>migrate_traffic</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to true traffic will be migrated to this version.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service these settings apply to.</p></li>
<li><p><strong>split</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Mapping that defines fractional HTTP traffic diversion to different versions within the service.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>split</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shardBy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.EngineSplitTraffic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.EngineSplitTraffic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.EngineSplitTraffic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.EngineSplitTraffic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.FirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.appengine.</code><code class="sig-name descname">FirewallRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">source_range=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>A single firewall rule that is evaluated against incoming traffic
and provides an action to take on matched requests.</p>
<p>To get more information about FirewallRule, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/appengine/docs/standard/python/creating-firewalls#creating_firewall_rules">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to take if this rule matches.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional string description of this rule.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A positive integer that defines the order of rule evaluation. Rules with the lowest priority are evaluated first. A
default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action
of this rule can be modified by the user.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>source_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address or range, defined using CIDR notation, of requests that this rule applies to.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.appengine.FirewallRule.action">
<code class="sig-name descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to take if this rule matches.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FirewallRule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional string description of this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FirewallRule.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>A positive integer that defines the order of rule evaluation. Rules with the lowest priority are evaluated first. A
default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action
of this rule can be modified by the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FirewallRule.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FirewallRule.source_range">
<code class="sig-name descname">source_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.source_range" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address or range, defined using CIDR notation, of requests that this rule applies to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.FirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">source_range=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to take if this rule matches.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional string description of this rule.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A positive integer that defines the order of rule evaluation. Rules with the lowest priority are evaluated first. A
default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action
of this rule can be modified by the user.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>source_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address or range, defined using CIDR notation, of requests that this rule applies to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.FirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.FirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.FlexibleAppVersion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.appengine.</code><code class="sig-name descname">FlexibleAppVersion</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_config=None</em>, <em class="sig-param">automatic_scaling=None</em>, <em class="sig-param">beta_settings=None</em>, <em class="sig-param">default_expiration=None</em>, <em class="sig-param">delete_service_on_destroy=None</em>, <em class="sig-param">deployment=None</em>, <em class="sig-param">endpoints_api_service=None</em>, <em class="sig-param">entrypoint=None</em>, <em class="sig-param">env_variables=None</em>, <em class="sig-param">inbound_services=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">liveness_check=None</em>, <em class="sig-param">manual_scaling=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">nobuild_files_regex=None</em>, <em class="sig-param">noop_on_destroy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">readiness_check=None</em>, <em class="sig-param">resources=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">runtime_api_version=None</em>, <em class="sig-param">runtime_channel=None</em>, <em class="sig-param">runtime_main_executable_path=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">serving_status=None</em>, <em class="sig-param">version_id=None</em>, <em class="sig-param">vpc_access_connector=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Flexible App Version resource to create a new version of flexible GAE Application. Based on Google Compute Engine,
the App Engine flexible environment automatically scales your app up and down while also balancing the load.
Learn about the differences between the standard environment and the flexible environment
at <a class="reference external" href="https://cloud.google.com/appengine/docs/the-appengine-environments">https://cloud.google.com/appengine/docs/the-appengine-environments</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> The App Engine flexible environment service account uses the member ID <code class="docutils literal notranslate"><span class="pre">service-[YOUR_PROJECT_NUMBER]&#64;gae-api-prod.google.com.iam.gserviceaccount.com</span></code>
It should have the App Engine Flexible Environment Service Agent role, which will be applied when the <code class="docutils literal notranslate"><span class="pre">appengineflex.googleapis.com</span></code> service is enabled.</p>
</div></blockquote>
<p>To get more information about FlexibleAppVersion, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/appengine/docs/flexible">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Serving configuration for Google Cloud Endpoints.</p></li>
<li><p><strong>automatic_scaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Automatic scaling is based on request rate, response latencies, and other application metrics.</p></li>
<li><p><strong>beta_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata settings that are supplied to this version to enable beta runtime features.</p></li>
<li><p><strong>default_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.</p></li>
<li><p><strong>delete_service_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the service will be deleted if it is the last version.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>deployment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Code and application artifacts that make up this version.</p></li>
<li><p><strong>endpoints_api_service</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Code and application artifacts that make up this version.</p></li>
<li><p><strong>entrypoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The entrypoint for the application.</p></li>
<li><p><strong>env_variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.</p></li>
<li><p><strong>inbound_services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Before an application can receive email or XMPP messages, the application must be configured to enable the service.</p></li>
<li><p><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.</p></li>
<li><p><strong>liveness_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.</p></li>
<li><p><strong>manual_scaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Extra network settings</p></li>
<li><p><strong>nobuild_files_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Files that match this pattern will not be built into this version. Only applicable for Go runtimes.</p></li>
<li><p><strong>noop_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the application version will not be deleted.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>readiness_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.</p></li>
<li><p><strong>resources</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Machine resources for a version.</p></li>
<li><p><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired runtime. Example python27.</p></li>
<li><p><strong>runtime_api_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
<a class="reference external" href="https://cloud.google.com/appengine/docs/standard//config/appref">https://cloud.google.com/appengine/docs/standard//config/appref</a></p></li>
<li><p><strong>runtime_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The channel of the runtime to use. Only available for some runtimes.</p></li>
<li><p><strong>runtime_main_executable_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path or name of the app’s main executable.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AppEngine service resource</p></li>
<li><p><strong>serving_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Relative name of the version within the service. For example, ‘v1’. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,”default”, “latest”, and any name with the prefix “ah-“.</p></li>
<li><p><strong>vpc_access_connector</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enables VPC connectivity for standard apps.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>api_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authFailAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">login</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>automatic_scaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">coolDownPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregationWindowLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReadBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReadOpsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetWriteBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetWriteOpsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentRequests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPendingLatency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTotalInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minIdleInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minPendingLatency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTotalInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReceivedBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReceivedPacketsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetSentBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetSentPacketsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">targetConcurrentRequests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetRequestCountPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>deployment</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudBuildOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appYamlPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudBuildTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">files</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha1Sum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filesCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>endpoints_api_service</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableTraceSampling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rolloutStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>entrypoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shell</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>liveness_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>manual_scaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>network</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">forwardedPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">session_affinity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>readiness_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appStartTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>resources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>vpc_access_connector</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.api_config">
<code class="sig-name descname">api_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.api_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Serving configuration for Google Cloud Endpoints.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authFailAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">login</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.automatic_scaling">
<code class="sig-name descname">automatic_scaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.automatic_scaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Automatic scaling is based on request rate, response latencies, and other application metrics.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">coolDownPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregationWindowLength</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReadBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReadOpsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetWriteBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetWriteOpsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentRequests</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPendingLatency</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTotalInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minIdleInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minPendingLatency</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTotalInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReceivedBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReceivedPacketsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetSentBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetSentPacketsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">targetConcurrentRequests</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetRequestCountPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.beta_settings">
<code class="sig-name descname">beta_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.beta_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Metadata settings that are supplied to this version to enable beta runtime features.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.default_expiration">
<code class="sig-name descname">default_expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.default_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.delete_service_on_destroy">
<code class="sig-name descname">delete_service_on_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.delete_service_on_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the service will be deleted if it is the last version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.deployment">
<code class="sig-name descname">deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Code and application artifacts that make up this version.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudBuildOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appYamlPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudBuildTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">files</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha1Sum</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zip</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filesCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.endpoints_api_service">
<code class="sig-name descname">endpoints_api_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.endpoints_api_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Code and application artifacts that make up this version.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableTraceSampling</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rolloutStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.entrypoint">
<code class="sig-name descname">entrypoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.entrypoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The entrypoint for the application.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shell</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.env_variables">
<code class="sig-name descname">env_variables</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.env_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.inbound_services">
<code class="sig-name descname">inbound_services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.inbound_services" title="Permalink to this definition">¶</a></dt>
<dd><p>Before an application can receive email or XMPP messages, the application must be configured to enable the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.instance_class">
<code class="sig-name descname">instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.liveness_check">
<code class="sig-name descname">liveness_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.liveness_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.manual_scaling">
<code class="sig-name descname">manual_scaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.manual_scaling" title="Permalink to this definition">¶</a></dt>
<dd><p>A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instances</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier for this object. Format specified above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Extra network settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">forwardedPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTag</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">session_affinity</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.nobuild_files_regex">
<code class="sig-name descname">nobuild_files_regex</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.nobuild_files_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>Files that match this pattern will not be built into this version. Only applicable for Go runtimes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.noop_on_destroy">
<code class="sig-name descname">noop_on_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.noop_on_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the application version will not be deleted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.readiness_check">
<code class="sig-name descname">readiness_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.readiness_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appStartTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.resources">
<code class="sig-name descname">resources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>Machine resources for a version.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskGb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryGb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.runtime">
<code class="sig-name descname">runtime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.runtime" title="Permalink to this definition">¶</a></dt>
<dd><p>Desired runtime. Example python27.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.runtime_api_version">
<code class="sig-name descname">runtime_api_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.runtime_api_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
<a class="reference external" href="https://cloud.google.com/appengine/docs/standard//config/appref">https://cloud.google.com/appengine/docs/standard//config/appref</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.runtime_channel">
<code class="sig-name descname">runtime_channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.runtime_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The channel of the runtime to use. Only available for some runtimes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.runtime_main_executable_path">
<code class="sig-name descname">runtime_main_executable_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.runtime_main_executable_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path or name of the app’s main executable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.service">
<code class="sig-name descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.service" title="Permalink to this definition">¶</a></dt>
<dd><p>AppEngine service resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.serving_status">
<code class="sig-name descname">serving_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.serving_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.version_id">
<code class="sig-name descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Relative name of the version within the service. For example, ‘v1’. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,”default”, “latest”, and any name with the prefix “ah-“.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.vpc_access_connector">
<code class="sig-name descname">vpc_access_connector</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.vpc_access_connector" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables VPC connectivity for standard apps.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier for this object. Format specified above.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_config=None</em>, <em class="sig-param">automatic_scaling=None</em>, <em class="sig-param">beta_settings=None</em>, <em class="sig-param">default_expiration=None</em>, <em class="sig-param">delete_service_on_destroy=None</em>, <em class="sig-param">deployment=None</em>, <em class="sig-param">endpoints_api_service=None</em>, <em class="sig-param">entrypoint=None</em>, <em class="sig-param">env_variables=None</em>, <em class="sig-param">inbound_services=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">liveness_check=None</em>, <em class="sig-param">manual_scaling=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">nobuild_files_regex=None</em>, <em class="sig-param">noop_on_destroy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">readiness_check=None</em>, <em class="sig-param">resources=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">runtime_api_version=None</em>, <em class="sig-param">runtime_channel=None</em>, <em class="sig-param">runtime_main_executable_path=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">serving_status=None</em>, <em class="sig-param">version_id=None</em>, <em class="sig-param">vpc_access_connector=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FlexibleAppVersion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Serving configuration for Google Cloud Endpoints.</p></li>
<li><p><strong>automatic_scaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Automatic scaling is based on request rate, response latencies, and other application metrics.</p></li>
<li><p><strong>beta_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Metadata settings that are supplied to this version to enable beta runtime features.</p></li>
<li><p><strong>default_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding
StaticFilesHandler does not specify its own expiration time.</p></li>
<li><p><strong>delete_service_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the service will be deleted if it is the last version.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>deployment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Code and application artifacts that make up this version.</p></li>
<li><p><strong>endpoints_api_service</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Code and application artifacts that make up this version.</p></li>
<li><p><strong>entrypoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The entrypoint for the application.</p></li>
<li><p><strong>env_variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Environment variables available to the application. As these are not returned in the API request, Terraform will not
detect any changes made outside of the Terraform config.</p></li>
<li><p><strong>inbound_services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Before an application can receive email or XMPP messages, the application must be configured to enable the service.</p></li>
<li><p><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance class that is used to run this version. Valid values are AutomaticScaling: F1, F2, F4, F4_1G ManualScaling: B1,
B2, B4, B8, B4_1G Defaults to F1 for AutomaticScaling and B1 for ManualScaling.</p></li>
<li><p><strong>liveness_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.</p></li>
<li><p><strong>manual_scaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of
its memory over time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier for this object. Format specified above.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Extra network settings</p></li>
<li><p><strong>nobuild_files_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Files that match this pattern will not be built into this version. Only applicable for Go runtimes.</p></li>
<li><p><strong>noop_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the application version will not be deleted.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>readiness_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.</p></li>
<li><p><strong>resources</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Machine resources for a version.</p></li>
<li><p><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired runtime. Example python27.</p></li>
<li><p><strong>runtime_api_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
<a class="reference external" href="https://cloud.google.com/appengine/docs/standard//config/appref">https://cloud.google.com/appengine/docs/standard//config/appref</a></p></li>
<li><p><strong>runtime_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The channel of the runtime to use. Only available for some runtimes.</p></li>
<li><p><strong>runtime_main_executable_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path or name of the app’s main executable.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AppEngine service resource</p></li>
<li><p><strong>serving_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Current serving status of this version. Only the versions with a SERVING status create instances and can be billed.
Defaults to SERVING.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Relative name of the version within the service. For example, ‘v1’. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,”default”, “latest”, and any name with the prefix “ah-“.</p></li>
<li><p><strong>vpc_access_connector</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enables VPC connectivity for standard apps.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>api_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authFailAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">login</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>automatic_scaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">coolDownPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregationWindowLength</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReadBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReadOpsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetWriteBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetWriteOpsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentRequests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPendingLatency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTotalInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minIdleInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minPendingLatency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTotalInstances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReceivedBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReceivedPacketsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetSentBytesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetSentPacketsPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestUtilization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">targetConcurrentRequests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetRequestCountPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>deployment</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudBuildOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appYamlPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudBuildTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">container</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">files</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha1Sum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filesCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>endpoints_api_service</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableTraceSampling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rolloutStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>entrypoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shell</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>liveness_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>manual_scaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instances</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>network</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">forwardedPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">session_affinity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>readiness_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appStartTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">checkInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>resources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>vpc_access_connector</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.FlexibleAppVersion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.FlexibleAppVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.StandardAppVersion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.appengine.</code><code class="sig-name descname">StandardAppVersion</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">delete_service_on_destroy=None</em>, <em class="sig-param">deployment=None</em>, <em class="sig-param">entrypoint=None</em>, <em class="sig-param">env_variables=None</em>, <em class="sig-param">handlers=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">libraries=None</em>, <em class="sig-param">noop_on_destroy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">runtime_api_version=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">threadsafe=None</em>, <em class="sig-param">version_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Standard App Version resource to create a new version of standard GAE Application.
Currently supporting Zip and File Containers.
Currently does not support async operation checking.</p>
<p>To get more information about StandardAppVersion, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/appengine/docs/standard">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_service_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the service will be deleted if it is the last version.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>deployment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Code and application artifacts that make up this version.</p></li>
<li><p><strong>entrypoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The entrypoint for the application.</p></li>
<li><p><strong>env_variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Environment variables available to the application.</p></li>
<li><p><strong>handlers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the
request and other request handlers are not attempted.</p></li>
<li><p><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance class that is used to run this version. Valid values are AutomaticScaling F1, F2, F4, F4_1G (Only
AutomaticScaling is supported at the moment)</p></li>
<li><p><strong>libraries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration for third-party Python runtime libraries that are required by the application.</p></li>
<li><p><strong>noop_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the application version will not be deleted.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired runtime. Example python27.</p></li>
<li><p><strong>runtime_api_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
<a class="reference external" href="https://cloud.google.com/appengine/docs/standard//config/appref">https://cloud.google.com/appengine/docs/standard//config/appref</a></p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AppEngine service resource</p></li>
<li><p><strong>threadsafe</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether multiple requests can be dispatched to this version at once.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Relative name of the version within the service. For example, ‘v1’. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,”default”, “latest”, and any name with the prefix “ah-“.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>deployment</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">files</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha1Sum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filesCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>entrypoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shell</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>handlers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authFailAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">login</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectHttpResponseCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">staticFiles</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationReadable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mimeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireMatchingFile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uploadPathRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>libraries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.delete_service_on_destroy">
<code class="sig-name descname">delete_service_on_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.delete_service_on_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the service will be deleted if it is the last version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.deployment">
<code class="sig-name descname">deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Code and application artifacts that make up this version.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">files</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha1Sum</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zip</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filesCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.entrypoint">
<code class="sig-name descname">entrypoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.entrypoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The entrypoint for the application.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shell</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.env_variables">
<code class="sig-name descname">env_variables</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.env_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>Environment variables available to the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.handlers">
<code class="sig-name descname">handlers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.handlers" title="Permalink to this definition">¶</a></dt>
<dd><p>An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the
request and other request handlers are not attempted.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authFailAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">login</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectHttpResponseCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">staticFiles</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationReadable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mimeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireMatchingFile</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uploadPathRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.instance_class">
<code class="sig-name descname">instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance class that is used to run this version. Valid values are AutomaticScaling F1, F2, F4, F4_1G (Only
AutomaticScaling is supported at the moment)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.libraries">
<code class="sig-name descname">libraries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.libraries" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for third-party Python runtime libraries that are required by the application.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier for this object. Format specified above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.noop_on_destroy">
<code class="sig-name descname">noop_on_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.noop_on_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the application version will not be deleted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.runtime">
<code class="sig-name descname">runtime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.runtime" title="Permalink to this definition">¶</a></dt>
<dd><p>Desired runtime. Example python27.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.runtime_api_version">
<code class="sig-name descname">runtime_api_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.runtime_api_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
<a class="reference external" href="https://cloud.google.com/appengine/docs/standard//config/appref">https://cloud.google.com/appengine/docs/standard//config/appref</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.service">
<code class="sig-name descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.service" title="Permalink to this definition">¶</a></dt>
<dd><p>AppEngine service resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.threadsafe">
<code class="sig-name descname">threadsafe</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.threadsafe" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether multiple requests can be dispatched to this version at once.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.appengine.StandardAppVersion.version_id">
<code class="sig-name descname">version_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.version_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Relative name of the version within the service. For example, ‘v1’. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,”default”, “latest”, and any name with the prefix “ah-“.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.StandardAppVersion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">delete_service_on_destroy=None</em>, <em class="sig-param">deployment=None</em>, <em class="sig-param">entrypoint=None</em>, <em class="sig-param">env_variables=None</em>, <em class="sig-param">handlers=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">libraries=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">noop_on_destroy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">runtime_api_version=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">threadsafe=None</em>, <em class="sig-param">version_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing StandardAppVersion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_service_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the service will be deleted if it is the last version.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>deployment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Code and application artifacts that make up this version.</p></li>
<li><p><strong>entrypoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The entrypoint for the application.</p></li>
<li><p><strong>env_variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Environment variables available to the application.</p></li>
<li><p><strong>handlers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the
request and other request handlers are not attempted.</p></li>
<li><p><strong>instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance class that is used to run this version. Valid values are AutomaticScaling F1, F2, F4, F4_1G (Only
AutomaticScaling is supported at the moment)</p></li>
<li><p><strong>libraries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration for third-party Python runtime libraries that are required by the application.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier for this object. Format specified above.</p></li>
<li><p><strong>noop_on_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the application version will not be deleted.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired runtime. Example python27.</p></li>
<li><p><strong>runtime_api_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at
<a class="reference external" href="https://cloud.google.com/appengine/docs/standard//config/appref">https://cloud.google.com/appengine/docs/standard//config/appref</a></p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AppEngine service resource</p></li>
<li><p><strong>threadsafe</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether multiple requests can be dispatched to this version at once.</p></li>
<li><p><strong>version_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Relative name of the version within the service. For example, ‘v1’. Version names can contain only lowercase letters,
numbers, or hyphens. Reserved names,”default”, “latest”, and any name with the prefix “ah-“.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>deployment</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">files</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha1Sum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">filesCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>entrypoint</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shell</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>handlers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authFailAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">login</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectHttpResponseCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">script</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scriptPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">staticFiles</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationReadable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mimeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireMatchingFile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">uploadPathRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>libraries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identifier for this object. Format specified above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.appengine.StandardAppVersion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.appengine.StandardAppVersion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.appengine.StandardAppVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
