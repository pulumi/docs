---
title: Module cr
title_tag: Module cr | Package pulumi_alicloud | Python SDK
linktitle: cr
notitle: true
---

<div class="section" id="cr">
<h1>cr<a class="headerlink" href="#cr" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.cr"></span><dl class="py class">
<dt id="pulumi_alicloud.cr.AwaitableGetNamespacesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cr.</code><code class="sig-name descname">AwaitableGetNamespacesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.AwaitableGetNamespacesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cr.AwaitableGetReposResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cr.</code><code class="sig-name descname">AwaitableGetReposResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repos</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.AwaitableGetReposResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cr.GetNamespacesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cr.</code><code class="sig-name descname">GetNamespacesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.GetNamespacesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNamespaces.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cr.GetNamespacesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.GetNamespacesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.GetNamespacesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.GetNamespacesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry namespaces. Its element is a namespace name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.GetNamespacesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.GetNamespacesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of namespace names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.GetNamespacesResult.namespaces">
<code class="sig-name descname">namespaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.GetNamespacesResult.namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry namespaces. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cr.GetReposResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cr.</code><code class="sig-name descname">GetReposResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repos</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.GetReposResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRepos.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cr.GetReposResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.GetReposResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.GetReposResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.GetReposResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry Repositories. Its element is set to <code class="docutils literal notranslate"><span class="pre">names</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.GetReposResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.GetReposResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of repository names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.GetReposResult.namespace">
<code class="sig-name descname">namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.GetReposResult.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of container registry namespace where repo is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.GetReposResult.repos">
<code class="sig-name descname">repos</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.GetReposResult.repos" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry Namespaces. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cr.Namespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cr.</code><code class="sig-name descname">Namespace</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_create</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.Namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource will help you to manager Container Registry namespaces.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.34.0+.</p>
<p><strong>NOTE:</strong> You need to set your registry password in Container Registry console before use this resource.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_namespace</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cr</span><span class="o">.</span><span class="n">Namespace</span><span class="p">(</span><span class="s2">&quot;my-namespace&quot;</span><span class="p">,</span>
    <span class="n">auto_create</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">default_visibility</span><span class="o">=</span><span class="s2">&quot;PUBLIC&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, when it set to true, repositories are automatically created when pushing new images. If it set to false, you create repository for images before pushing.</p></li>
<li><p><strong>default_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, default repository visibility in this namespace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry namespace.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cr.Namespace.auto_create">
<code class="sig-name descname">auto_create</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.Namespace.auto_create" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, when it set to true, repositories are automatically created when pushing new images. If it set to false, you create repository for images before pushing.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.Namespace.default_visibility">
<code class="sig-name descname">default_visibility</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.Namespace.default_visibility" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, default repository visibility in this namespace.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.Namespace.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.Namespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Container Registry namespace.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cr.Namespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_create</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.Namespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Namespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, when it set to true, repositories are automatically created when pushing new images. If it set to false, you create repository for images before pushing.</p></li>
<li><p><strong>default_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, default repository visibility in this namespace.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry namespace.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cr.Namespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.Namespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cr.Namespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.Namespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cr.Repo">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cr.</code><code class="sig-name descname">Repo</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">summary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.Repo" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource will help you to manager Container Registry repositories.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.35.0+.</p>
<p><strong>NOTE:</strong> You need to set your registry password in Container Registry console before use this resource.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_namespace</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cr</span><span class="o">.</span><span class="n">Namespace</span><span class="p">(</span><span class="s2">&quot;my-namespace&quot;</span><span class="p">,</span>
    <span class="n">auto_create</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">default_visibility</span><span class="o">=</span><span class="s2">&quot;PUBLIC&quot;</span><span class="p">)</span>
<span class="n">my_repo</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cr</span><span class="o">.</span><span class="n">Repo</span><span class="p">(</span><span class="s2">&quot;my-repo&quot;</span><span class="p">,</span>
    <span class="n">detail</span><span class="o">=</span><span class="s2">&quot;this is a public repo&quot;</span><span class="p">,</span>
    <span class="n">namespace</span><span class="o">=</span><span class="n">my_namespace</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">repo_type</span><span class="o">=</span><span class="s2">&quot;PUBLIC&quot;</span><span class="p">,</span>
    <span class="n">summary</span><span class="o">=</span><span class="s2">&quot;this is summary of my new repo&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>detail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository specific information. MarkDown format is supported, and the length limit is 2000.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of container registry repository.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of container registry namespace where repository is located.</p></li>
<li><p><strong>repo_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, repo’s visibility.</p></li>
<li><p><strong>summary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository general information. It can contain 1 to 80 characters.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cr.Repo.detail">
<code class="sig-name descname">detail</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.Repo.detail" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository specific information. MarkDown format is supported, and the length limit is 2000.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.Repo.domain_list">
<code class="sig-name descname">domain_list</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.Repo.domain_list" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository domain list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">internal</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Domain of internal endpoint, only in some regions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Domain of public endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Domain of vpc endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.Repo.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.Repo.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of container registry repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.Repo.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.Repo.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of container registry namespace where repository is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.Repo.repo_type">
<code class="sig-name descname">repo_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.Repo.repo_type" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, repo’s visibility.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cr.Repo.summary">
<code class="sig-name descname">summary</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cr.Repo.summary" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository general information. It can contain 1 to 80 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cr.Repo.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_list</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">summary</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.Repo.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Repo resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>detail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository specific information. MarkDown format is supported, and the length limit is 2000.</p></li>
<li><p><strong>domain_list</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The repository domain list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of container registry repository.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of container registry namespace where repository is located.</p></li>
<li><p><strong>repo_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, repo’s visibility.</p></li>
<li><p><strong>summary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository general information. It can contain 1 to 80 characters.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>domain_list</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">internal</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Domain of internal endpoint, only in some regions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Domain of public endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Domain of vpc endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cr.Repo.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.Repo.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cr.Repo.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.Repo.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_alicloud.cr.get_namespaces">
<code class="sig-prename descclassname">pulumi_alicloud.cr.</code><code class="sig-name descname">get_namespaces</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.get_namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Registry namespaces on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.35.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_namespaces</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cr</span><span class="o">.</span><span class="n">get_namespaces</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;my-namespace&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;my-namespace-json&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;output&quot;</span><span class="p">,</span> <span class="n">my_namespaces</span><span class="o">.</span><span class="n">namespaces</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by namespace name.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cr.get_repos">
<code class="sig-prename descclassname">pulumi_alicloud.cr.</code><code class="sig-name descname">get_repos</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cr.get_repos" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Registry repositories on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.35.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_repos</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cr</span><span class="o">.</span><span class="n">get_repos</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;my-repos&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;my-repo-json&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;output&quot;</span><span class="p">,</span> <span class="n">my_repos</span><span class="o">.</span><span class="n">repos</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>enable_details</strong> (<em>bool</em>) – Boolean, false by default, only repository attributes are exported. Set to true if domain list and tags belong to this repository are needed. See <code class="docutils literal notranslate"><span class="pre">tags</span></code> in attributes.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by repository name.</p></li>
<li><p><strong>namespace</strong> (<em>str</em>) – Name of container registry namespace where the repositories are located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
