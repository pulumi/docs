---
title: Module cloudbuild
title_tag: Module cloudbuild | Package pulumi_gcp | Python SDK
linktitle: cloudbuild
notitle: true
---

<div class="section" id="cloudbuild">
<h1>cloudbuild<a class="headerlink" href="#cloudbuild" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.cloudbuild"></span><dl class="class">
<dt id="pulumi_gcp.cloudbuild.Trigger">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudbuild.</code><code class="sig-name descname">Trigger</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">build=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">filename=None</em>, <em class="sig-param">github=None</em>, <em class="sig-param">ignored_files=None</em>, <em class="sig-param">included_files=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">substitutions=None</em>, <em class="sig-param">trigger_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for an automated build in response to source repository changes.</p>
<p>To get more information about Trigger, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/cloud-build/docs/api/reference/rest/">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/cloud-build/docs/running-builds/automate-builds">Automating builds using build triggers</a></p></li>
</ul>
</li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudbuild_trigger.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudbuild_trigger.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>build</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contents of the build template. Either a filename or build template must be provided.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the trigger.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the trigger is disabled or not. If true, the trigger will never result in a build.</p></li>
<li><p><strong>filename</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path, from the source root, to a file whose contents is used for the template. Either a filename or build template must
be provided.</p></li>
<li><p><strong>github</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the configuration of a trigger that creates a build whenever a GitHub event is received. One of
‘trigger_template’ or ‘github’ must be provided.</p></li>
<li><p><strong>ignored_files</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ignoredFiles and includedFiles are file glob matches using <a class="reference external" href="https://golang.org/pkg/path/filepath/#Match">https://golang.org/pkg/path/filepath/#Match</a> extended with
support for ‘<a href="#id1"><span class="problematic" id="id2">**</span></a>’. If ignoredFiles and changed files are both empty, then they are not used to determine whether or not
to trigger a build. If ignoredFiles is not empty, then we ignore any files that match any of the ignored_file globs. If
the change has no files that are outside of the ignoredFiles globs, then we do not trigger a build.</p></li>
<li><p><strong>included_files</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ignoredFiles and includedFiles are file glob matches using <a class="reference external" href="https://golang.org/pkg/path/filepath/#Match">https://golang.org/pkg/path/filepath/#Match</a> extended with
support for ‘<a href="#id3"><span class="problematic" id="id4">**</span></a>’. If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is empty,
then as far as this filter is concerned, we should trigger the build. If any of the files altered in the commit pass the
ignoredFiles filter and includedFiles is not empty, then we make sure that at least one of those files matches a
includedFiles glob. If not, then we do not trigger a build.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the trigger. Must be unique within the project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>substitutions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Substitutions data for Build resource.</p></li>
<li><p><strong>trigger_template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Template describing the types of source changes to trigger a build. Branch and tag names in trigger templates are
interpreted as regular expressions. Any branch or tag change that matches that regular expression will trigger a build.
One of ‘trigger_template’ or ‘github’ must be provided.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>build</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">images</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">steps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dir</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">entrypoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">envs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - an identifier for the resource with format <code class="docutils literal notranslate"><span class="pre">projects/{{project}}/triggers/{{trigger_id}}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretEnvs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitFors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>github</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pullRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">branch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commentControl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">push</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">branch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>trigger_template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commitSha</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dir</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.build">
<code class="sig-name descname">build</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.build" title="Permalink to this definition">¶</a></dt>
<dd><p>Contents of the build template. Either a filename or build template must be provided.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">images</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">steps</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dir</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">entrypoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">envs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - an identifier for the resource with format <code class="docutils literal notranslate"><span class="pre">projects/{{project}}/triggers/{{trigger_id}}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretEnvs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timing</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitFors</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time when the trigger was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the trigger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.disabled">
<code class="sig-name descname">disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the trigger is disabled or not. If true, the trigger will never result in a build.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.filename">
<code class="sig-name descname">filename</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.filename" title="Permalink to this definition">¶</a></dt>
<dd><p>Path, from the source root, to a file whose contents is used for the template. Either a filename or build template must
be provided.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.github">
<code class="sig-name descname">github</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.github" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the configuration of a trigger that creates a build whenever a GitHub event is received. One of
‘trigger_template’ or ‘github’ must be provided.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pullRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">branch</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commentControl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">push</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">branch</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tag</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.ignored_files">
<code class="sig-name descname">ignored_files</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.ignored_files" title="Permalink to this definition">¶</a></dt>
<dd><p>ignoredFiles and includedFiles are file glob matches using <a class="reference external" href="https://golang.org/pkg/path/filepath/#Match">https://golang.org/pkg/path/filepath/#Match</a> extended with
support for ‘**’. If ignoredFiles and changed files are both empty, then they are not used to determine whether or not
to trigger a build. If ignoredFiles is not empty, then we ignore any files that match any of the ignored_file globs. If
the change has no files that are outside of the ignoredFiles globs, then we do not trigger a build.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.included_files">
<code class="sig-name descname">included_files</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.included_files" title="Permalink to this definition">¶</a></dt>
<dd><p>ignoredFiles and includedFiles are file glob matches using <a class="reference external" href="https://golang.org/pkg/path/filepath/#Match">https://golang.org/pkg/path/filepath/#Match</a> extended with
support for ‘**’. If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is empty,
then as far as this filter is concerned, we should trigger the build. If any of the files altered in the commit pass the
ignoredFiles filter and includedFiles is not empty, then we make sure that at least one of those files matches a
includedFiles glob. If not, then we do not trigger a build.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the trigger. Must be unique within the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.substitutions">
<code class="sig-name descname">substitutions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.substitutions" title="Permalink to this definition">¶</a></dt>
<dd><p>Substitutions data for Build resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.trigger_id">
<code class="sig-name descname">trigger_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.trigger_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the trigger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudbuild.Trigger.trigger_template">
<code class="sig-name descname">trigger_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.trigger_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Template describing the types of source changes to trigger a build. Branch and tag names in trigger templates are
interpreted as regular expressions. Any branch or tag change that matches that regular expression will trigger a build.
One of ‘trigger_template’ or ‘github’ must be provided.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commitSha</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dir</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudbuild.Trigger.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">build=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">disabled=None</em>, <em class="sig-param">filename=None</em>, <em class="sig-param">github=None</em>, <em class="sig-param">ignored_files=None</em>, <em class="sig-param">included_files=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">substitutions=None</em>, <em class="sig-param">trigger_id=None</em>, <em class="sig-param">trigger_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Trigger resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>build</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contents of the build template. Either a filename or build template must be provided.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time when the trigger was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the trigger.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the trigger is disabled or not. If true, the trigger will never result in a build.</p></li>
<li><p><strong>filename</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path, from the source root, to a file whose contents is used for the template. Either a filename or build template must
be provided.</p></li>
<li><p><strong>github</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the configuration of a trigger that creates a build whenever a GitHub event is received. One of
‘trigger_template’ or ‘github’ must be provided.</p></li>
<li><p><strong>ignored_files</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ignoredFiles and includedFiles are file glob matches using <a class="reference external" href="https://golang.org/pkg/path/filepath/#Match">https://golang.org/pkg/path/filepath/#Match</a> extended with
support for ‘<a href="#id5"><span class="problematic" id="id6">**</span></a>’. If ignoredFiles and changed files are both empty, then they are not used to determine whether or not
to trigger a build. If ignoredFiles is not empty, then we ignore any files that match any of the ignored_file globs. If
the change has no files that are outside of the ignoredFiles globs, then we do not trigger a build.</p></li>
<li><p><strong>included_files</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ignoredFiles and includedFiles are file glob matches using <a class="reference external" href="https://golang.org/pkg/path/filepath/#Match">https://golang.org/pkg/path/filepath/#Match</a> extended with
support for ‘<a href="#id7"><span class="problematic" id="id8">**</span></a>’. If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is empty,
then as far as this filter is concerned, we should trigger the build. If any of the files altered in the commit pass the
ignoredFiles filter and includedFiles is not empty, then we make sure that at least one of those files matches a
includedFiles glob. If not, then we do not trigger a build.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the trigger. Must be unique within the project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>substitutions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Substitutions data for Build resource.</p></li>
<li><p><strong>trigger_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the trigger.</p></li>
<li><p><strong>trigger_template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Template describing the types of source changes to trigger a build. Branch and tag names in trigger templates are
interpreted as regular expressions. Any branch or tag change that matches that regular expression will trigger a build.
One of ‘trigger_template’ or ‘github’ must be provided.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>build</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">images</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">steps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dir</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">entrypoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">envs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - an identifier for the resource with format <code class="docutils literal notranslate"><span class="pre">projects/{{project}}/triggers/{{trigger_id}}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretEnvs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitFors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>github</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pullRequest</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">branch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commentControl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">push</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">branch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>trigger_template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commitSha</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dir</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudbuild.Trigger.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudbuild.Trigger.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudbuild.Trigger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
