---
title: Module resourcemanager
title_tag: Module resourcemanager | Package pulumi_gcp | Python SDK
linktitle: resourcemanager
notitle: true
---

<div class="section" id="resourcemanager">
<h1>resourcemanager<a class="headerlink" href="#resourcemanager" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.resourcemanager"></span><dl class="class">
<dt id="pulumi_gcp.resourcemanager.Lien">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.resourcemanager.</code><code class="sig-name descname">Lien</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">origin=None</em>, <em class="sig-param">parent=None</em>, <em class="sig-param">reason=None</em>, <em class="sig-param">restrictions=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien" title="Permalink to this definition">¶</a></dt>
<dd><p>A Lien represents an encumbrance on the actions that can be performed on a resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/resource_manager_lien.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/resource_manager_lien.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.</p></li>
<li><p><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
“projects/my-project-name”).</p></li>
<li><p><strong>reason</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.</p></li>
<li><p><strong>restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. [‘resourcemanager.projects.delete’]</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.resourcemanager.Lien.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of creation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.resourcemanager.Lien.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A system-generated unique identifier for this Lien.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.resourcemanager.Lien.origin">
<code class="sig-name descname">origin</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.resourcemanager.Lien.parent">
<code class="sig-name descname">parent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.parent" title="Permalink to this definition">¶</a></dt>
<dd><p>A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
“projects/my-project-name”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.resourcemanager.Lien.reason">
<code class="sig-name descname">reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.reason" title="Permalink to this definition">¶</a></dt>
<dd><p>Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.resourcemanager.Lien.restrictions">
<code class="sig-name descname">restrictions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.restrictions" title="Permalink to this definition">¶</a></dt>
<dd><p>The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. [‘resourcemanager.projects.delete’]</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.resourcemanager.Lien.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">origin=None</em>, <em class="sig-param">parent=None</em>, <em class="sig-param">reason=None</em>, <em class="sig-param">restrictions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Lien resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A system-generated unique identifier for this Lien.</p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A stable, user-visible/meaningful string identifying the origin of the Lien, intended to be inspected programmatically.
Maximum length of 200 characters.</p></li>
<li><p><strong>parent</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A reference to the resource this Lien is attached to. The server will validate the parent against those for which Liens
are supported. Since a variety of objects can have Liens against them, you must provide the type prefix (e.g.
“projects/my-project-name”).</p></li>
<li><p><strong>reason</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Concise user-visible strings indicating why an action cannot be performed on a resource. Maximum length of 200
characters.</p></li>
<li><p><strong>restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The types of operations which should be blocked as a result of this Lien. Each value should correspond to an IAM
permission. The server will validate the permissions against those for which Liens are supported. An empty list is
meaningless and will be rejected. e.g. [‘resourcemanager.projects.delete’]</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.resourcemanager.Lien.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.resourcemanager.Lien.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.resourcemanager.Lien.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
