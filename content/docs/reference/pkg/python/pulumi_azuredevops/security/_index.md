---
title: Module security
title_tag: Module security | Package pulumi_azuredevops | Python SDK
linktitle: security
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuredevops" >}}

<div class="section" id="security">
<h1>security<a class="headerlink" href="#security" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuredevops/issues">pulumi/pulumi-azuredevops repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops/issues">terraform-providers/terraform-provider-azuredevops repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuredevops.security"></span><dl class="py class">
<dt id="pulumi_azuredevops.security.ResourceAuthorization">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.security.</code><code class="sig-name descname">ResourceAuthorization</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.security.ResourceAuthorization" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages authorization of resources, e.g. for access in build pipelines.</p>
<p>Currently supported resources: service endpoint (aka service connection, endpoint).</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span> <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Test Project&quot;</span><span class="p">)</span>
<span class="n">bitbucket_account</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">service_endpoint</span><span class="o">.</span><span class="n">BitBucket</span><span class="p">(</span><span class="s2">&quot;bitbucketAccount&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;xxxx&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;xxxx&quot;</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;test-bitbucket&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">)</span>
<span class="n">auth</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">security</span><span class="o">.</span><span class="n">ResourceAuthorization</span><span class="p">(</span><span class="s2">&quot;auth&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">resource_id</span><span class="o">=</span><span class="n">bitbucket_account</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">authorized</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/build/resources/authorize%20definition%20resources?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Authorize Definition Resource</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to allow public access in the project. Type: boolean.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name. Type: string.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource to authorize. Type: string.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the resource to authorize. Type: string. Valid values: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>, <code class="docutils literal notranslate"><span class="pre">queue</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azuredevops.security.ResourceAuthorization.authorized">
<code class="sig-name descname">authorized</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.security.ResourceAuthorization.authorized" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to true to allow public access in the project. Type: boolean.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.security.ResourceAuthorization.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.security.ResourceAuthorization.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name. Type: string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.security.ResourceAuthorization.resource_id">
<code class="sig-name descname">resource_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.security.ResourceAuthorization.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resource to authorize. Type: string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.security.ResourceAuthorization.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.security.ResourceAuthorization.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the resource to authorize. Type: string. Valid values: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>, <code class="docutils literal notranslate"><span class="pre">queue</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.security.ResourceAuthorization.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.security.ResourceAuthorization.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceAuthorization resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to allow public access in the project. Type: boolean.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name. Type: string.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource to authorize. Type: string.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the resource to authorize. Type: string. Valid values: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>, <code class="docutils literal notranslate"><span class="pre">queue</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.security.ResourceAuthorization.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.security.ResourceAuthorization.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.security.ResourceAuthorization.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.security.ResourceAuthorization.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
