---
title: Module cs
title_tag: Module cs | Package pulumi_alicloud | Python SDK
linktitle: cs
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="cs">
<h1>cs<a class="headerlink" href="#cs" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.cs"></span><dl class="py class">
<dt id="pulumi_alicloud.cs.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blue_green</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blue_green_confirm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Application" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>DEPRECATED:</strong> This resource manages applications in swarm cluster only, which is being deprecated and will be replaced by Kubernetes cluster.</p>
</div></blockquote>
<p>This resource use an orchestration template to define and deploy a multi-container application. An application is created by using an orchestration template.
Each application can contain one or more services.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Application orchestration template must be a valid Docker Compose YAML template.</p>
<p><strong>NOTE:</strong> At present, this resource only support swarm cluster.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">Application</span><span class="p">(</span><span class="s2">&quot;app&quot;</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="s2">&quot;my-first-swarm&quot;</span><span class="p">,</span>
    <span class="n">environment</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;EXTERNAL_URL&quot;</span><span class="p">:</span> <span class="s2">&quot;123.123.123.123:8080&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">latest_image</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">template</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;wordpress.yml&quot;</span><span class="p">),</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;1.2&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blue_green</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wherther to use “Blue Green” method when release a new version. Default to false.</p></li>
<li><p><strong>blue_green_confirm</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to confirm a “Blue Green” application. Default to false. It will be ignored when <code class="docutils literal notranslate"><span class="pre">blue_green</span></code> is false.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The swarm cluster’s name.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of application.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key/value map used to replace the variable parameter in the Compose template.</p></li>
<li><p><strong>latest_image</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use latest docker image while each updating application. Default to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application deployment template and it must be <a class="reference external" href="https://docs.docker.com/compose/">Docker Compose format</a>.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application deploying version. Each updating, it must be different with current. Default to “1.0”</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.blue_green">
<code class="sig-name descname">blue_green</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.blue_green" title="Permalink to this definition">¶</a></dt>
<dd><p>Wherther to use “Blue Green” method when release a new version. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.blue_green_confirm">
<code class="sig-name descname">blue_green_confirm</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.blue_green_confirm" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to confirm a “Blue Green” application. Default to false. It will be ignored when <code class="docutils literal notranslate"><span class="pre">blue_green</span></code> is false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The swarm cluster’s name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.default_domain">
<code class="sig-name descname">default_domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.default_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The application default domain and it can be used to configure routing service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of application.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.environment">
<code class="sig-name descname">environment</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>A key/value map used to replace the variable parameter in the Compose template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.latest_image">
<code class="sig-name descname">latest_image</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.latest_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use latest docker image while each updating application. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.services">
<code class="sig-name descname">services</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.services" title="Permalink to this definition">¶</a></dt>
<dd><p>List of services in the application. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The current status of service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The application deploying version. Each updating, it must be different with current. Default to “1.0”</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.template">
<code class="sig-name descname">template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.template" title="Permalink to this definition">¶</a></dt>
<dd><p>The application deployment template and it must be <a class="reference external" href="https://docs.docker.com/compose/">Docker Compose format</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Application.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Application.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The application deploying version. Each updating, it must be different with current. Default to “1.0”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blue_green</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blue_green_confirm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blue_green</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wherther to use “Blue Green” method when release a new version. Default to false.</p></li>
<li><p><strong>blue_green_confirm</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to confirm a “Blue Green” application. Default to false. It will be ignored when <code class="docutils literal notranslate"><span class="pre">blue_green</span></code> is false.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The swarm cluster’s name.</p></li>
<li><p><strong>default_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application default domain and it can be used to configure routing service.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of application.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A key/value map used to replace the variable parameter in the Compose template.</p></li>
<li><p><strong>latest_image</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use latest docker image while each updating application. Default to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of services in the application. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The application deployment template and it must be <a class="reference external" href="https://docs.docker.com/compose/">Docker Compose format</a>.</p>
</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The application deploying version. Each updating, it must be different with current. Default to “1.0”</p></li>
</ul>
</dd>
</dl>
<p>The <strong>services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The application name. It should be 1-64 characters long, and can contain numbers, English letters and hyphens, but cannot start with hyphens.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The current status of service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The application deploying version. Each updating, it must be different with current. Default to “1.0”</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.AwaitableGetKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">AwaitableGetKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.AwaitableGetKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.AwaitableGetManagedKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">AwaitableGetManagedKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.AwaitableGetManagedKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.AwaitableGetRegistryEnterpriseInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">AwaitableGetRegistryEnterpriseInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.AwaitableGetRegistryEnterpriseInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.AwaitableGetRegistryEnterpriseNamespacesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">AwaitableGetRegistryEnterpriseNamespacesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.AwaitableGetRegistryEnterpriseNamespacesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.AwaitableGetRegistryEnterpriseReposResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">AwaitableGetRegistryEnterpriseReposResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repos</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.AwaitableGetRegistryEnterpriseReposResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.AwaitableGetRegistryEnterpriseSyncRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">AwaitableGetRegistryEnterpriseSyncRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_instance_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.AwaitableGetRegistryEnterpriseSyncRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.AwaitableGetServerlessKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">AwaitableGetServerlessKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.AwaitableGetServerlessKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">need_slb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_eip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Cluster resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_alicloud.cs.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">need_slb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_eip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.GetKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">GetKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.GetKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKubernetesClusters.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetKubernetesClustersResult.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetKubernetesClustersResult.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetKubernetesClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetKubernetesClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetKubernetesClustersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetKubernetesClustersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetKubernetesClustersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetKubernetesClustersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.GetManagedKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">GetManagedKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.GetManagedKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getManagedKubernetesClusters.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetManagedKubernetesClustersResult.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetManagedKubernetesClustersResult.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetManagedKubernetesClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetManagedKubernetesClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetManagedKubernetesClustersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetManagedKubernetesClustersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetManagedKubernetesClustersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetManagedKubernetesClustersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">GetRegistryEnterpriseInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryEnterpriseInstances.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry Enterprise Edition instances. Its element is an instance uuid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry Enterprise Editioninstances. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">GetRegistryEnterpriseNamespacesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryEnterpriseNamespaces.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry Enterprise Edition namespaces. Its element is a namespace uuid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of Container Registry Enterprise Edition instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of namespace names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult.namespaces">
<code class="sig-name descname">namespaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseNamespacesResult.namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry Enterprise Edition namespaces. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseReposResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">GetRegistryEnterpriseReposResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repos</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseReposResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryEnterpriseRepos.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry Enterprise Edition repositories. Its element is a repository id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of Container Registry Enterprise Edition instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of repository names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.namespace">
<code class="sig-name descname">namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Container Registry Enterprise Edition namespace where repo is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.repos">
<code class="sig-name descname">repos</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseReposResult.repos" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry Enterprise Edition namespaces. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">GetRegistryEnterpriseSyncRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_instance_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryEnterpriseSyncRules.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry Enterprise Edition sync rules. Its element is a sync rule uuid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of Container Registry Enterprise Edition local instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of sync rule names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Container Registry Enterprise Edition local namespace.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.repo_name">
<code class="sig-name descname">repo_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.repo_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Container Registry Enterprise Edition local repo.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Container Registry Enterprise Edition sync rules. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.target_instance_id">
<code class="sig-name descname">target_instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetRegistryEnterpriseSyncRulesResult.target_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of Container Registry Enterprise Edition target instance.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.GetServerlessKubernetesClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">GetServerlessKubernetesClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.GetServerlessKubernetesClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServerlessKubernetesClusters.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.GetServerlessKubernetesClustersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of matched Kubernetes clusters’ names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cs.Kubernetes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">Kubernetes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_audiences</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_ca_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_autoscaler_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_cloud_monitor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enterprise_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kube_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_nat_gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_cidr_mask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_name_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_account_issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_internet_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_ca</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Kubernetes resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] api_audiences: A list of API audiences for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>. Set this to <code class="docutils literal notranslate"><span class="pre">[&quot;kubernetes.default.svc&quot;]</span></code> if you want to enable the Token Volume Projection feature (requires specifying <code class="docutils literal notranslate"><span class="pre">service_account_issuer</span></code> as well.
:param pulumi.Input[str] availability_zone: The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.
:param pulumi.Input[str] client_cert: The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.
:param pulumi.Input[str] client_key: The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.
:param pulumi.Input[str] cluster_ca_cert: The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code>
:param pulumi.Input[str] cpu_policy: kubelet cpu policy. options: static|none. default: none.
:param pulumi.Input[bool] enable_ssh: Enable login to the node through SSH. default: false 
:param pulumi.Input[bool] exclude_autoscaler_nodes: Exclude autoscaler nodes from <code class="docutils literal notranslate"><span class="pre">worker_nodes</span></code>. default: false 
:param pulumi.Input[str] image_id: Custom Image support. Must based on CentOS7 or AliyunLinux2.
:param pulumi.Input[bool] install_cloud_monitor: Install cloud monitor agent on ECS. default: true 
:param pulumi.Input[bool] is_enterprise_security_group: Enable to create advanced security group. default: false. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/120621.htm">Advanced security group</a>.
:param pulumi.Input[str] key_name: The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[dict] kms_encryption_context: An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.
:param pulumi.Input[str] kube_config: The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.
:param pulumi.Input[bool] master_auto_renew: Enable master payment auto-renew, defaults to false.
:param pulumi.Input[float] master_auto_renew_period: Master payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.
:param pulumi.Input[str] master_disk_category: The system disk category of master node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.
:param pulumi.Input[float] master_disk_size: The system disk size of master node. Its valid value range [20~500] in GB. Default to 20.
:param pulumi.Input[str] master_instance_charge_type: Master payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.
:param pulumi.Input[list] master_instance_types: The instance type of master node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.
:param pulumi.Input[float] master_period: Master payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.
:param pulumi.Input[str] master_period_unit: Master payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.
:param pulumi.Input[str] name: The kubernetes cluster’s name. It is unique in one Alicloud account.
:param pulumi.Input[bool] new_nat_gateway: Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.
:param pulumi.Input[float] node_cidr_mask: The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24
:param pulumi.Input[str] node_name_mode: Each node name consists of a prefix, an IP substring, and a suffix. For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, IP substring length is 5, and the suffix is test, the node name will be aliyun.com00055test. 
:param pulumi.Input[str] password: The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[str] pod_cidr: [Flannel Specific] The CIDR block for the pod network when using Flannel. 
:param pulumi.Input[list] pod_vswitch_ids: [Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code> or <code class="docutils literal notranslate"><span class="pre">master_vswtich_ids</span></code> but must be in same availability zones.
:param pulumi.Input[str] proxy_mode: Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.
:param pulumi.Input[str] security_group_id: The ID of the security group to which the ECS instances in the cluster belong. If it is not specified, a new Security group will be built.
:param pulumi.Input[str] service_account_issuer: The issuer of the Service Account token for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>, corresponds to the <code class="docutils literal notranslate"><span class="pre">iss</span></code> field in the token payload. Set this to <code class="docutils literal notranslate"><span class="pre">&quot;kubernetes.default.svc&quot;</span></code> to enable the Token Volume Projection feature (requires specifying <code class="docutils literal notranslate"><span class="pre">api_audiences</span></code> as well).
:param pulumi.Input[str] service_cidr: The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.
:param pulumi.Input[bool] slb_internet_enabled: Whether to create internet load balancer for API Server. Default to true.
:param pulumi.Input[str] user_ca: The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.
:param pulumi.Input[str] user_data: Windows instances support batch and PowerShell scripts. If your script file is larger than 1 KB, we recommend that you upload the script to Object Storage Service (OSS) and pull it through the internal endpoint of your OSS bucket.
:param pulumi.Input[str] version: Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.
:param pulumi.Input[bool] worker_auto_renew: Enable worker payment auto-renew, defaults to false.
:param pulumi.Input[float] worker_auto_renew_period: Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.
:param pulumi.Input[list] worker_data_disks: The data disk configurations of worker nodes, such as the disk type and disk size.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">category</span><span class="p">:</span> <span class="n">the</span> <span class="nb">type</span> <span class="n">of</span> <span class="n">the</span> <span class="n">data</span> <span class="n">disks</span><span class="o">.</span> <span class="n">Valid</span> <span class="n">values</span><span class="p">:</span>
<span class="o">+</span> <span class="n">cloud</span><span class="p">:</span> <span class="n">basic</span> <span class="n">disks</span><span class="o">.</span>
<span class="o">+</span> <span class="n">cloud_efficiency</span><span class="p">:</span> <span class="n">ultra</span> <span class="n">disks</span><span class="o">.</span>
<span class="o">+</span> <span class="n">cloud_ssd</span><span class="p">:</span> <span class="n">SSDs</span><span class="o">.</span>
<span class="o">-</span> <span class="n">size</span><span class="p">:</span> <span class="n">the</span> <span class="n">size</span> <span class="n">of</span> <span class="n">a</span> <span class="n">data</span> <span class="n">disk</span><span class="o">.</span> <span class="n">Unit</span><span class="p">:</span> <span class="n">GiB</span><span class="o">.</span>
<span class="o">-</span> <span class="n">encrypted</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">whether</span> <span class="n">to</span> <span class="n">encrypt</span> <span class="n">data</span> <span class="n">disks</span><span class="o">.</span> <span class="n">Valid</span> <span class="n">values</span><span class="p">:</span> <span class="n">true</span> <span class="ow">and</span> <span class="n">false</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>worker_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>worker_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 40.</p></li>
<li><p><strong>worker_instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>worker_instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p></li>
<li><p><strong>worker_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.</p></li>
<li><p><strong>worker_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p></li>
<li><p><strong>worker_period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
</ul>
<p>The <strong>worker_data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.api_audiences">
<code class="sig-name descname">api_audiences</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.api_audiences" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of API audiences for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>. Set this to <code class="docutils literal notranslate"><span class="pre">[&quot;kubernetes.default.svc&quot;]</span></code> if you want to enable the Token Volume Projection feature (requires specifying <code class="docutils literal notranslate"><span class="pre">service_account_issuer</span></code> as well.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.client_cert">
<code class="sig-name descname">client_cert</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.client_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.client_key">
<code class="sig-name descname">client_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.client_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.cluster_ca_cert">
<code class="sig-name descname">cluster_ca_cert</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.cluster_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.connections">
<code class="sig-name descname">connections</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.connections" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of kubernetes cluster connection information. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Connections</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_internet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - API Server Internet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_intranet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - API Server Intranet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Master node SSH IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Service Access Domain.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.cpu_policy">
<code class="sig-name descname">cpu_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.cpu_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>kubelet cpu policy. options: static|none. default: none.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.enable_ssh">
<code class="sig-name descname">enable_ssh</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.enable_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable login to the node through SSH. default: false</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.exclude_autoscaler_nodes">
<code class="sig-name descname">exclude_autoscaler_nodes</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.exclude_autoscaler_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Exclude autoscaler nodes from <code class="docutils literal notranslate"><span class="pre">worker_nodes</span></code>. default: false</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom Image support. Must based on CentOS7 or AliyunLinux2.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.install_cloud_monitor">
<code class="sig-name descname">install_cloud_monitor</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.install_cloud_monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Install cloud monitor agent on ECS. default: true</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.is_enterprise_security_group">
<code class="sig-name descname">is_enterprise_security_group</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.is_enterprise_security_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable to create advanced security group. default: false. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/120621.htm">Advanced security group</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.key_name">
<code class="sig-name descname">key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.kube_config">
<code class="sig-name descname">kube_config</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.kube_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_auto_renew">
<code class="sig-name descname">master_auto_renew</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable master payment auto-renew, defaults to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_auto_renew_period">
<code class="sig-name descname">master_auto_renew_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Master payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_disk_category">
<code class="sig-name descname">master_disk_category</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk category of master node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_disk_size">
<code class="sig-name descname">master_disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk size of master node. Its valid value range [20~500] in GB. Default to 20.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_instance_charge_type">
<code class="sig-name descname">master_instance_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Master payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_instance_types">
<code class="sig-name descname">master_instance_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance type of master node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_nodes">
<code class="sig-name descname">master_nodes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of cluster master nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private IP address of node.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_period">
<code class="sig-name descname">master_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Master payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.master_period_unit">
<code class="sig-name descname">master_period_unit</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.master_period_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>Master payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The kubernetes cluster’s name. It is unique in one Alicloud account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.nat_gateway_id">
<code class="sig-name descname">nat_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.nat_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of nat gateway used to launch kubernetes cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.new_nat_gateway">
<code class="sig-name descname">new_nat_gateway</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.new_nat_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.node_cidr_mask">
<code class="sig-name descname">node_cidr_mask</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.node_cidr_mask" title="Permalink to this definition">¶</a></dt>
<dd><p>The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.node_name_mode">
<code class="sig-name descname">node_name_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.node_name_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Each node name consists of a prefix, an IP substring, and a suffix. For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, IP substring length is 5, and the suffix is test, the node name will be aliyun.com00055test.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.pod_cidr">
<code class="sig-name descname">pod_cidr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.pod_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>[Flannel Specific] The CIDR block for the pod network when using Flannel.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.pod_vswitch_ids">
<code class="sig-name descname">pod_vswitch_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.pod_vswitch_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>[Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code> or <code class="docutils literal notranslate"><span class="pre">master_vswtich_ids</span></code> but must be in same availability zones.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.proxy_mode">
<code class="sig-name descname">proxy_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.proxy_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group to which the ECS instances in the cluster belong. If it is not specified, a new Security group will be built.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.service_account_issuer">
<code class="sig-name descname">service_account_issuer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.service_account_issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>The issuer of the Service Account token for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>, corresponds to the <code class="docutils literal notranslate"><span class="pre">iss</span></code> field in the token payload. Set this to <code class="docutils literal notranslate"><span class="pre">&quot;kubernetes.default.svc&quot;</span></code> to enable the Token Volume Projection feature (requires specifying <code class="docutils literal notranslate"><span class="pre">api_audiences</span></code> as well).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.service_cidr">
<code class="sig-name descname">service_cidr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.service_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.slb_internet_enabled">
<code class="sig-name descname">slb_internet_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.slb_internet_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create internet load balancer for API Server. Default to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.slb_intranet">
<code class="sig-name descname">slb_intranet</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.slb_intranet" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of private load balancer where the current cluster master node is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.user_ca">
<code class="sig-name descname">user_ca</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.user_ca" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.user_data">
<code class="sig-name descname">user_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Windows instances support batch and PowerShell scripts. If your script file is larger than 1 KB, we recommend that you upload the script to Object Storage Service (OSS) and pull it through the internal endpoint of your OSS bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of VPC where the current cluster is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_auto_renew">
<code class="sig-name descname">worker_auto_renew</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable worker payment auto-renew, defaults to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_auto_renew_period">
<code class="sig-name descname">worker_auto_renew_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_data_disks">
<code class="sig-name descname">worker_data_disks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>The data disk configurations of worker nodes, such as the disk type and disk size.</p>
<ul class="simple">
<li><p>category: the type of the data disks. Valid values:</p></li>
<li><p>cloud: basic disks.</p></li>
<li><p>cloud_efficiency: ultra disks.</p></li>
<li><p>cloud_ssd: SSDs.</p></li>
<li><p>size: the size of a data disk. Unit: GiB.</p></li>
<li><p>encrypted: specifies whether to encrypt data disks. Valid values: true and false.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_disk_category">
<code class="sig-name descname">worker_disk_category</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_disk_size">
<code class="sig-name descname">worker_disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 40.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_instance_charge_type">
<code class="sig-name descname">worker_instance_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_instance_types">
<code class="sig-name descname">worker_instance_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_nodes">
<code class="sig-name descname">worker_nodes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of cluster worker nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private IP address of node.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_number">
<code class="sig-name descname">worker_number</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_period">
<code class="sig-name descname">worker_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_period_unit">
<code class="sig-name descname">worker_period_unit</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_period_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Kubernetes.worker_ram_role_name">
<code class="sig-name descname">worker_ram_role_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.worker_ram_role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The RamRole Name attached to worker node.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.Kubernetes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_audiences</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_ca_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_autoscaler_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_cloud_monitor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enterprise_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kube_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nat_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_nat_gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_cidr_mask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_name_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_account_issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_internet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_internet_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_intranet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_ca</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_ram_role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Kubernetes resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_audiences</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of API audiences for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>. Set this to <code class="docutils literal notranslate"><span class="pre">[&quot;kubernetes.default.svc&quot;]</span></code> if you want to enable the Token Volume Projection feature (requires specifying <code class="docutils literal notranslate"><span class="pre">service_account_issuer</span></code> as well.</p>
</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.</p></li>
<li><p><strong>client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p></li>
<li><p><strong>client_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p></li>
<li><p><strong>cluster_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p></li>
<li><p><strong>connections</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of kubernetes cluster connection information. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Connections</span></code>.</p></li>
<li><p><strong>cpu_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – kubelet cpu policy. options: static|none. default: none.</p></li>
<li><p><strong>enable_ssh</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable login to the node through SSH. default: false</p></li>
<li><p><strong>exclude_autoscaler_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Exclude autoscaler nodes from <code class="docutils literal notranslate"><span class="pre">worker_nodes</span></code>. default: false</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom Image support. Must based on CentOS7 or AliyunLinux2.</p></li>
<li><p><strong>install_cloud_monitor</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Install cloud monitor agent on ECS. default: true</p></li>
<li><p><strong>is_enterprise_security_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Enable to create advanced security group. default: false. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/120621.htm">Advanced security group</a>.</p>
</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
<li><p><strong>kube_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p></li>
<li><p><strong>master_auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable master payment auto-renew, defaults to false.</p></li>
<li><p><strong>master_auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Master payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p></li>
<li><p><strong>master_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The system disk category of master node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>master_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The system disk size of master node. Its valid value range [20~500] in GB. Default to 20.</p></li>
<li><p><strong>master_instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>master_instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance type of master node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p></li>
<li><p><strong>master_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of cluster master nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p></li>
<li><p><strong>master_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Master payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p></li>
<li><p><strong>master_period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><strong>nat_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of nat gateway used to launch kubernetes cluster.</p></li>
<li><p><strong>new_nat_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.</p></li>
<li><p><strong>node_cidr_mask</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24</p></li>
<li><p><strong>node_name_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Each node name consists of a prefix, an IP substring, and a suffix. For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, IP substring length is 5, and the suffix is test, the node name will be aliyun.com00055test.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>pod_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – [Flannel Specific] The CIDR block for the pod network when using Flannel.</p></li>
<li><p><strong>pod_vswitch_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – [Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code> or <code class="docutils literal notranslate"><span class="pre">master_vswtich_ids</span></code> but must be in same availability zones.</p></li>
<li><p><strong>proxy_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security group to which the ECS instances in the cluster belong. If it is not specified, a new Security group will be built.</p></li>
<li><p><strong>service_account_issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The issuer of the Service Account token for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>, corresponds to the <code class="docutils literal notranslate"><span class="pre">iss</span></code> field in the token payload. Set this to <code class="docutils literal notranslate"><span class="pre">&quot;kubernetes.default.svc&quot;</span></code> to enable the Token Volume Projection feature (requires specifying <code class="docutils literal notranslate"><span class="pre">api_audiences</span></code> as well).</p>
</p></li>
<li><p><strong>service_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.</p></li>
<li><p><strong>slb_internet_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create internet load balancer for API Server. Default to true.</p></li>
<li><p><strong>slb_intranet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of private load balancer where the current cluster master node is located.</p></li>
<li><p><strong>user_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Windows instances support batch and PowerShell scripts. If your script file is larger than 1 KB, we recommend that you upload the script to Object Storage Service (OSS) and pull it through the internal endpoint of your OSS bucket.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VPC where the current cluster is located.</p></li>
<li><p><strong>worker_auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable worker payment auto-renew, defaults to false.</p></li>
<li><p><strong>worker_auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p></li>
<li><p><strong>worker_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The data disk configurations of worker nodes, such as the disk type and disk size.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">category</span><span class="p">:</span> <span class="n">the</span> <span class="nb">type</span> <span class="n">of</span> <span class="n">the</span> <span class="n">data</span> <span class="n">disks</span><span class="o">.</span> <span class="n">Valid</span> <span class="n">values</span><span class="p">:</span>
<span class="o">+</span> <span class="n">cloud</span><span class="p">:</span> <span class="n">basic</span> <span class="n">disks</span><span class="o">.</span>
<span class="o">+</span> <span class="n">cloud_efficiency</span><span class="p">:</span> <span class="n">ultra</span> <span class="n">disks</span><span class="o">.</span>
<span class="o">+</span> <span class="n">cloud_ssd</span><span class="p">:</span> <span class="n">SSDs</span><span class="o">.</span>
<span class="o">-</span> <span class="n">size</span><span class="p">:</span> <span class="n">the</span> <span class="n">size</span> <span class="n">of</span> <span class="n">a</span> <span class="n">data</span> <span class="n">disk</span><span class="o">.</span> <span class="n">Unit</span><span class="p">:</span> <span class="n">GiB</span><span class="o">.</span>
<span class="o">-</span> <span class="n">encrypted</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">whether</span> <span class="n">to</span> <span class="n">encrypt</span> <span class="n">data</span> <span class="n">disks</span><span class="o">.</span> <span class="n">Valid</span> <span class="n">values</span><span class="p">:</span> <span class="n">true</span> <span class="ow">and</span> <span class="n">false</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>worker_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>worker_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 40.</p></li>
<li><p><strong>worker_instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>worker_instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p></li>
<li><p><strong>worker_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of cluster worker nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p></li>
<li><p><strong>worker_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.</p></li>
<li><p><strong>worker_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p></li>
<li><p><strong>worker_period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
<li><p><strong>worker_ram_role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RamRole Name attached to worker node.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
</ul>
<p>The <strong>connections</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_internet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API Server Internet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_intranet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API Server Intranet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Master node SSH IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Service Access Domain.</p></li>
</ul>
<p>The <strong>master_nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address of node.</p></li>
</ul>
<p>The <strong>worker_data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>worker_nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address of node.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.Kubernetes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.Kubernetes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Kubernetes.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">KubernetesAutoscaler</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cool_down_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">defer_scale_in_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodepools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ecs_ram_role_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">utilization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource will help you to manager cluster-autoscaler in Kubernetes Cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The scaling group must use CentOS7 or AliyunLinux2 as base image.</p>
<p><strong>NOTE:</strong> The cluster-autoscaler can only use the same size of instanceTypes in one scaling group.</p>
<p><strong>NOTE:</strong> Add Policy to RAM role of the node to deploy cluster-autoscaler if you need.</p>
<p><strong>NOTE:</strong> Available in 1.65.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">KubernetesAutoscaler</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">cluster_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cluster_id&quot;</span><span class="p">],</span>
    <span class="n">cool_down_duration</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;cool_down_duration&quot;</span><span class="p">],</span>
    <span class="n">defer_scale_in_duration</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;defer_scale_in_duration&quot;</span><span class="p">],</span>
    <span class="n">nodepools</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;id&quot;</span><span class="p">:</span> <span class="s2">&quot;scaling_group_id&quot;</span><span class="p">,</span>
        <span class="s2">&quot;labels&quot;</span><span class="p">:</span> <span class="s2">&quot;a=b&quot;</span><span class="p">,</span>
        <span class="s2">&quot;taints&quot;</span><span class="p">:</span> <span class="s2">&quot;c=d:NoSchedule&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">utilization</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;utilization&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of kubernetes cluster.</p></li>
<li><p><strong>cool_down_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cool_down_duration option of cluster-autoscaler.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>defer_scale_in_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The defer_scale_in_duration option of cluster-autoscaler.</p></li>
<li><p><strong>nodepools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – </p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>use_ecs_ram_role_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable autoscaler access to alibabacloud service by ecs ramrole token. default: false</p></li>
<li><p><strong>utilization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The utilization option of cluster-autoscaler.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nodepools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of kubernetes cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.cool_down_duration">
<code class="sig-name descname">cool_down_duration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.cool_down_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The cool_down_duration option of cluster-autoscaler.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.defer_scale_in_duration">
<code class="sig-name descname">defer_scale_in_duration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.defer_scale_in_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The defer_scale_in_duration option of cluster-autoscaler.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.nodepools">
<code class="sig-name descname">nodepools</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.nodepools" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">nodepools.id</span></code> - (Required) The scaling group id of the groups configured for cluster-autoscaler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodepools.taints</span></code> - (Required) The taints for the nodes in scaling group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodepools.labels</span></code> - (Required) The labels for the nodes in scaling group.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.use_ecs_ram_role_token">
<code class="sig-name descname">use_ecs_ram_role_token</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.use_ecs_ram_role_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable autoscaler access to alibabacloud service by ecs ramrole token. default: false</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.utilization">
<code class="sig-name descname">utilization</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.utilization" title="Permalink to this definition">¶</a></dt>
<dd><p>The utilization option of cluster-autoscaler.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cool_down_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">defer_scale_in_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodepools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_ecs_ram_role_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">utilization</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KubernetesAutoscaler resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of kubernetes cluster.</p></li>
<li><p><strong>cool_down_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cool_down_duration option of cluster-autoscaler.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>defer_scale_in_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The defer_scale_in_duration option of cluster-autoscaler.</p></li>
<li><p><strong>nodepools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – </p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>use_ecs_ram_role_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable autoscaler access to alibabacloud service by ecs ramrole token. default: false</p></li>
<li><p><strong>utilization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The utilization option of cluster-autoscaler.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nodepools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.KubernetesAutoscaler.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.KubernetesAutoscaler.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.ManagedKubernetes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">ManagedKubernetes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_audiences</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_ca_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_autoscaler_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_cloud_monitor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enterprise_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kube_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_nat_gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_cidr_mask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_name_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_account_issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_internet_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_ca</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ManagedKubernetes resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] api_audiences: A list of API audiences for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>. Set this to <code class="docutils literal notranslate"><span class="pre">[&quot;kubernetes.default.svc&quot;]</span></code> if you want to enable the Token Volume Projection feature.
:param pulumi.Input[str] availability_zone: The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.
:param pulumi.Input[str] client_cert: The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.
:param pulumi.Input[str] client_key: The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.
:param pulumi.Input[str] cluster_ca_cert: The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code>
:param pulumi.Input[str] cpu_policy: kubelet cpu policy. options: static|none. default: none.
:param pulumi.Input[bool] enable_ssh: Enable login to the node through SSH. default: false 
:param pulumi.Input[bool] exclude_autoscaler_nodes: Exclude autoscaler nodes from <code class="docutils literal notranslate"><span class="pre">worker_nodes</span></code>. default: false 
:param pulumi.Input[str] image_id: Custom Image support. Must based on CentOS7 or AliyunLinux2.
:param pulumi.Input[bool] install_cloud_monitor: Install cloud monitor agent on ECS. default: true 
:param pulumi.Input[bool] is_enterprise_security_group: Enable to create advanced security group. default: false. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/120621.htm">Advanced security group</a>.
:param pulumi.Input[str] key_name: The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[dict] kms_encryption_context: An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.
:param pulumi.Input[str] kube_config: The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.
:param pulumi.Input[str] name: The kubernetes cluster’s name. It is unique in one Alicloud account.
:param pulumi.Input[bool] new_nat_gateway: Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.
:param pulumi.Input[float] node_cidr_mask: The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24
:param pulumi.Input[str] node_name_mode: Each node name consists of a prefix, an IP substring, and a suffix. For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, IP substring length is 5, and the suffix is test, the node name will be aliyun.com00055test. 
:param pulumi.Input[str] password: The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.
:param pulumi.Input[str] pod_cidr: [Flannel Specific] The CIDR block for the pod network when using Flannel. 
:param pulumi.Input[list] pod_vswitch_ids: [Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code>.but must be in same availability zones.
:param pulumi.Input[str] proxy_mode: Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.
:param pulumi.Input[str] security_group_id: The ID of the security group to which the ECS instances in the cluster belong. If it is not specified, a new Security group will be built.
:param pulumi.Input[str] service_account_issuer: The issuer of the Service Account token for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>, corresponds to the <code class="docutils literal notranslate"><span class="pre">iss</span></code> field in the token payload. Set this to <code class="docutils literal notranslate"><span class="pre">kubernetes.default.svc</span></code> to enable the Token Volume Projection feature.
:param pulumi.Input[str] service_cidr: The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.
:param pulumi.Input[bool] slb_internet_enabled: Whether to create internet load balancer for API Server. Default to true.
:param pulumi.Input[str] user_ca: The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.
:param pulumi.Input[str] user_data: Windows instances support batch and PowerShell scripts. If your script file is larger than 1 KB, we recommend that you upload the script to Object Storage Service (OSS) and pull it through the internal endpoint of your OSS bucket.
:param pulumi.Input[str] version: Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.
:param pulumi.Input[bool] worker_auto_renew: Enable worker payment auto-renew, defaults to false.
:param pulumi.Input[float] worker_auto_renew_period: Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.
:param pulumi.Input[list] worker_data_disks: The data disk configurations of worker nodes, such as the disk type and disk size.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">category</span><span class="p">:</span> <span class="n">the</span> <span class="nb">type</span> <span class="n">of</span> <span class="n">the</span> <span class="n">data</span> <span class="n">disks</span><span class="o">.</span> <span class="n">Valid</span> <span class="n">values</span><span class="p">:</span>
<span class="o">+</span> <span class="n">cloud</span><span class="p">:</span> <span class="n">basic</span> <span class="n">disks</span><span class="o">.</span>
<span class="o">+</span> <span class="n">cloud_efficiency</span><span class="p">:</span> <span class="n">ultra</span> <span class="n">disks</span><span class="o">.</span>
<span class="o">+</span> <span class="n">cloud_ssd</span><span class="p">:</span> <span class="n">SSDs</span><span class="o">.</span>
<span class="o">-</span> <span class="n">size</span><span class="p">:</span> <span class="n">the</span> <span class="n">size</span> <span class="n">of</span> <span class="n">a</span> <span class="n">data</span> <span class="n">disk</span><span class="o">.</span> <span class="n">Unit</span><span class="p">:</span> <span class="n">GiB</span><span class="o">.</span>
<span class="o">-</span> <span class="n">encrypted</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">whether</span> <span class="n">to</span> <span class="n">encrypt</span> <span class="n">data</span> <span class="n">disks</span><span class="o">.</span> <span class="n">Valid</span> <span class="n">values</span><span class="p">:</span> <span class="n">true</span> <span class="ow">and</span> <span class="n">false</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>worker_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>worker_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 40.</p></li>
<li><p><strong>worker_instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>worker_instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p></li>
<li><p><strong>worker_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.</p></li>
<li><p><strong>worker_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p></li>
<li><p><strong>worker_period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
</ul>
<p>The <strong>worker_data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.api_audiences">
<code class="sig-name descname">api_audiences</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.api_audiences" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of API audiences for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>. Set this to <code class="docutils literal notranslate"><span class="pre">[&quot;kubernetes.default.svc&quot;]</span></code> if you want to enable the Token Volume Projection feature.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.client_cert">
<code class="sig-name descname">client_cert</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.client_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.client_key">
<code class="sig-name descname">client_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.client_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.cluster_ca_cert">
<code class="sig-name descname">cluster_ca_cert</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.cluster_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.connections">
<code class="sig-name descname">connections</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.connections" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of kubernetes cluster connection information. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Connections</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_internet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - API Server Internet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_intranet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - API Server Intranet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Service Access Domain.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.cpu_policy">
<code class="sig-name descname">cpu_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.cpu_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>kubelet cpu policy. options: static|none. default: none.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.enable_ssh">
<code class="sig-name descname">enable_ssh</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.enable_ssh" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable login to the node through SSH. default: false</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.exclude_autoscaler_nodes">
<code class="sig-name descname">exclude_autoscaler_nodes</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.exclude_autoscaler_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Exclude autoscaler nodes from <code class="docutils literal notranslate"><span class="pre">worker_nodes</span></code>. default: false</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom Image support. Must based on CentOS7 or AliyunLinux2.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.install_cloud_monitor">
<code class="sig-name descname">install_cloud_monitor</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.install_cloud_monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Install cloud monitor agent on ECS. default: true</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.is_enterprise_security_group">
<code class="sig-name descname">is_enterprise_security_group</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.is_enterprise_security_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable to create advanced security group. default: false. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/120621.htm">Advanced security group</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.key_name">
<code class="sig-name descname">key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.kube_config">
<code class="sig-name descname">kube_config</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.kube_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The kubernetes cluster’s name. It is unique in one Alicloud account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.nat_gateway_id">
<code class="sig-name descname">nat_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.nat_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of nat gateway used to launch kubernetes cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.new_nat_gateway">
<code class="sig-name descname">new_nat_gateway</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.new_nat_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.node_cidr_mask">
<code class="sig-name descname">node_cidr_mask</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.node_cidr_mask" title="Permalink to this definition">¶</a></dt>
<dd><p>The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.node_name_mode">
<code class="sig-name descname">node_name_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.node_name_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Each node name consists of a prefix, an IP substring, and a suffix. For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, IP substring length is 5, and the suffix is test, the node name will be aliyun.com00055test.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.pod_cidr">
<code class="sig-name descname">pod_cidr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.pod_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>[Flannel Specific] The CIDR block for the pod network when using Flannel.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.pod_vswitch_ids">
<code class="sig-name descname">pod_vswitch_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.pod_vswitch_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>[Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code>.but must be in same availability zones.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.proxy_mode">
<code class="sig-name descname">proxy_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.proxy_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group to which the ECS instances in the cluster belong. If it is not specified, a new Security group will be built.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.service_account_issuer">
<code class="sig-name descname">service_account_issuer</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.service_account_issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>The issuer of the Service Account token for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>, corresponds to the <code class="docutils literal notranslate"><span class="pre">iss</span></code> field in the token payload. Set this to <code class="docutils literal notranslate"><span class="pre">kubernetes.default.svc</span></code> to enable the Token Volume Projection feature.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.service_cidr">
<code class="sig-name descname">service_cidr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.service_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.slb_internet_enabled">
<code class="sig-name descname">slb_internet_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.slb_internet_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create internet load balancer for API Server. Default to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.slb_intranet">
<code class="sig-name descname">slb_intranet</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.slb_intranet" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of private load balancer where the current cluster master node is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.user_ca">
<code class="sig-name descname">user_ca</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.user_ca" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.user_data">
<code class="sig-name descname">user_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Windows instances support batch and PowerShell scripts. If your script file is larger than 1 KB, we recommend that you upload the script to Object Storage Service (OSS) and pull it through the internal endpoint of your OSS bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of VPC where the current cluster is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_auto_renew">
<code class="sig-name descname">worker_auto_renew</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable worker payment auto-renew, defaults to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_auto_renew_period">
<code class="sig-name descname">worker_auto_renew_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_data_disks">
<code class="sig-name descname">worker_data_disks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>The data disk configurations of worker nodes, such as the disk type and disk size.</p>
<ul class="simple">
<li><p>category: the type of the data disks. Valid values:</p></li>
<li><p>cloud: basic disks.</p></li>
<li><p>cloud_efficiency: ultra disks.</p></li>
<li><p>cloud_ssd: SSDs.</p></li>
<li><p>size: the size of a data disk. Unit: GiB.</p></li>
<li><p>encrypted: specifies whether to encrypt data disks. Valid values: true and false.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_disk_category">
<code class="sig-name descname">worker_disk_category</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_disk_size">
<code class="sig-name descname">worker_disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 40.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_instance_charge_type">
<code class="sig-name descname">worker_instance_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_instance_types">
<code class="sig-name descname">worker_instance_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_nodes">
<code class="sig-name descname">worker_nodes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of cluster worker nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private IP address of node.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_number">
<code class="sig-name descname">worker_number</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_period">
<code class="sig-name descname">worker_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_period_unit">
<code class="sig-name descname">worker_period_unit</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_period_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.worker_ram_role_name">
<code class="sig-name descname">worker_ram_role_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.worker_ram_role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The RamRole Name attached to worker node.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_audiences</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_ca_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssh</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclude_autoscaler_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">install_cloud_monitor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enterprise_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kube_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nat_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_nat_gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_cidr_mask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_name_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_account_issuer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_internet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_internet_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_intranet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_ca</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_ram_role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">worker_vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ManagedKubernetes resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_audiences</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of API audiences for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>. Set this to <code class="docutils literal notranslate"><span class="pre">[&quot;kubernetes.default.svc&quot;]</span></code> if you want to enable the Token Volume Projection feature.</p>
</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone where new kubernetes cluster will be located. If it is not be specified, the <code class="docutils literal notranslate"><span class="pre">vswitch_ids</span></code> should be set, its value will be vswitch’s zone.</p></li>
<li><p><strong>client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p></li>
<li><p><strong>client_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p></li>
<li><p><strong>cluster_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p></li>
<li><p><strong>connections</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of kubernetes cluster connection information. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Connections</span></code>.</p></li>
<li><p><strong>cpu_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – kubelet cpu policy. options: static|none. default: none.</p></li>
<li><p><strong>enable_ssh</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable login to the node through SSH. default: false</p></li>
<li><p><strong>exclude_autoscaler_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Exclude autoscaler nodes from <code class="docutils literal notranslate"><span class="pre">worker_nodes</span></code>. default: false</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Custom Image support. Must based on CentOS7 or AliyunLinux2.</p></li>
<li><p><strong>install_cloud_monitor</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Install cloud monitor agent on ECS. default: true</p></li>
<li><p><strong>is_enterprise_security_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Enable to create advanced security group. default: false. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/120621.htm">Advanced security group</a>.</p>
</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The keypair of ssh login cluster node, you have to create it first. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a cs kubernetes. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a cs kubernetes with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
<li><p><strong>kube_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><strong>nat_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of nat gateway used to launch kubernetes cluster.</p></li>
<li><p><strong>new_nat_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create a new nat gateway while creating kubernetes cluster. Default to true. Then openapi in Alibaba Cloud are not all on intranet, So turn this option on is a good choice.</p></li>
<li><p><strong>node_cidr_mask</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The node cidr block to specific how many pods can run on single node. 24-28 is allowed. 24 means 2^(32-24)-1=255 and the node can run at most 255 pods. default: 24</p></li>
<li><p><strong>node_name_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Each node name consists of a prefix, an IP substring, and a suffix. For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, IP substring length is 5, and the suffix is test, the node name will be aliyun.com00055test.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ssh login cluster node. You have to specify one of <code class="docutils literal notranslate"><span class="pre">password</span></code> <code class="docutils literal notranslate"><span class="pre">key_name</span></code> <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> fields.</p></li>
<li><p><strong>pod_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – [Flannel Specific] The CIDR block for the pod network when using Flannel.</p></li>
<li><p><strong>pod_vswitch_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – [Terway Specific] The vswitches for the pod network when using Terway.Be careful the <code class="docutils literal notranslate"><span class="pre">pod_vswitch_ids</span></code> can not equal to <code class="docutils literal notranslate"><span class="pre">worker_vswtich_ids</span></code>.but must be in same availability zones.</p></li>
<li><p><strong>proxy_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Proxy mode is option of kube-proxy. options: iptables|ipvs. default: ipvs.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security group to which the ECS instances in the cluster belong. If it is not specified, a new Security group will be built.</p></li>
<li><p><strong>service_account_issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The issuer of the Service Account token for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/160384.htm">Service Account Token Volume Projection</a>, corresponds to the <code class="docutils literal notranslate"><span class="pre">iss</span></code> field in the token payload. Set this to <code class="docutils literal notranslate"><span class="pre">kubernetes.default.svc</span></code> to enable the Token Volume Projection feature.</p>
</p></li>
<li><p><strong>service_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block for the service network. It cannot be duplicated with the VPC CIDR and CIDR used by Kubernetes cluster in VPC, cannot be modified after creation.</p></li>
<li><p><strong>slb_internet_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create internet load balancer for API Server. Default to true.</p></li>
<li><p><strong>slb_intranet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of private load balancer where the current cluster master node is located.</p></li>
<li><p><strong>user_ca</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of customized CA cert, you can use this CA to sign client certs to connect your cluster.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Windows instances support batch and PowerShell scripts. If your script file is larger than 1 KB, we recommend that you upload the script to Object Storage Service (OSS) and pull it through the internal endpoint of your OSS bucket.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired Kubernetes version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except you set a higher version number. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by ACK.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VPC where the current cluster is located.</p></li>
<li><p><strong>worker_auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable worker payment auto-renew, defaults to false.</p></li>
<li><p><strong>worker_auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Worker payment auto-renew period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of {“1”, “2”, “3”, “6”, “12”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”}.</p></li>
<li><p><strong>worker_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The data disk configurations of worker nodes, such as the disk type and disk size.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">category</span><span class="p">:</span> <span class="n">the</span> <span class="nb">type</span> <span class="n">of</span> <span class="n">the</span> <span class="n">data</span> <span class="n">disks</span><span class="o">.</span> <span class="n">Valid</span> <span class="n">values</span><span class="p">:</span>
<span class="o">+</span> <span class="n">cloud</span><span class="p">:</span> <span class="n">basic</span> <span class="n">disks</span><span class="o">.</span>
<span class="o">+</span> <span class="n">cloud_efficiency</span><span class="p">:</span> <span class="n">ultra</span> <span class="n">disks</span><span class="o">.</span>
<span class="o">+</span> <span class="n">cloud_ssd</span><span class="p">:</span> <span class="n">SSDs</span><span class="o">.</span>
<span class="o">-</span> <span class="n">size</span><span class="p">:</span> <span class="n">the</span> <span class="n">size</span> <span class="n">of</span> <span class="n">a</span> <span class="n">data</span> <span class="n">disk</span><span class="o">.</span> <span class="n">Unit</span><span class="p">:</span> <span class="n">GiB</span><span class="o">.</span>
<span class="o">-</span> <span class="n">encrypted</span><span class="p">:</span> <span class="n">specifies</span> <span class="n">whether</span> <span class="n">to</span> <span class="n">encrypt</span> <span class="n">data</span> <span class="n">disks</span><span class="o">.</span> <span class="n">Valid</span> <span class="n">values</span><span class="p">:</span> <span class="n">true</span> <span class="ow">and</span> <span class="n">false</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>worker_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The system disk category of worker node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>worker_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The system disk size of worker node. Its valid value range [20~32768] in GB. Default to 40.</p></li>
<li><p><strong>worker_instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment type. <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> or <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>worker_instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance type of worker node. Specify one type for single AZ Cluster, three types for MultiAZ Cluster.</p></li>
<li><p><strong>worker_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of cluster worker nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p></li>
<li><p><strong>worker_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The worker node number of the kubernetes cluster. Default to 3. It is limited up to 50 and if you want to enlarge it, please apply white list or contact with us.</p></li>
<li><p><strong>worker_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Worker payment period. When period unit is <code class="docutils literal notranslate"><span class="pre">Month</span></code>, it can be one of { “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}.  When period unit is <code class="docutils literal notranslate"><span class="pre">Week</span></code>, it can be one of {“1”, “2”, “3”, “4”}.</p></li>
<li><p><strong>worker_period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Worker payment period unit. <code class="docutils literal notranslate"><span class="pre">Month</span></code> or <code class="docutils literal notranslate"><span class="pre">Week</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Month</span></code>.</p></li>
<li><p><strong>worker_ram_role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RamRole Name attached to worker node.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
</ul>
<p>The <strong>connections</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_internet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API Server Internet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">api_server_intranet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API Server Intranet endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Service Access Domain.</p></li>
</ul>
<p>The <strong>worker_data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>worker_nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is unique in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address of node.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.ManagedKubernetes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.ManagedKubernetes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ManagedKubernetes.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.RegistryEnterpriseNamespace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">RegistryEnterpriseNamespace</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_create</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource will help you to manager Container Registry Enterprise Edition namespaces.</p>
<p>For information about Container Registry Enterprise Edition namespaces and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/145483.htm">Create a Namespace</a></p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.86.0+.</p>
<p><strong>NOTE:</strong> You need to set your registry password in Container Registry Enterprise Edition console before use this resource.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_namespace</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">RegistryEnterpriseNamespace</span><span class="p">(</span><span class="s2">&quot;my-namespace&quot;</span><span class="p">,</span>
    <span class="n">auto_create</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">default_visibility</span><span class="o">=</span><span class="s2">&quot;PUBLIC&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="s2">&quot;cri-xxx&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, when it set to true, repositories are automatically created when pushing new images. If it set to false, you create repository for images before pushing.</p></li>
<li><p><strong>default_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, default repository visibility in this namespace.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of Container Registry Enterprise Edition instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition namespace. It can contain 2 to 30 characters.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseNamespace.auto_create">
<code class="sig-name descname">auto_create</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseNamespace.auto_create" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, when it set to true, repositories are automatically created when pushing new images. If it set to false, you create repository for images before pushing.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseNamespace.default_visibility">
<code class="sig-name descname">default_visibility</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseNamespace.default_visibility" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, default repository visibility in this namespace.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseNamespace.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseNamespace.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of Container Registry Enterprise Edition instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseNamespace.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseNamespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Container Registry Enterprise Edition namespace. It can contain 2 to 30 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseNamespace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_create</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseNamespace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegistryEnterpriseNamespace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_create</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, when it set to true, repositories are automatically created when pushing new images. If it set to false, you create repository for images before pushing.</p></li>
<li><p><strong>default_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, default repository visibility in this namespace.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of Container Registry Enterprise Edition instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition namespace. It can contain 2 to 30 characters.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseNamespace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.RegistryEnterpriseNamespace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">RegistryEnterpriseRepo</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">summary</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource will help you to manager Container Registry Enterprise Edition repositories.</p>
<p>For information about Container Registry Enterprise Edition repository and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/145291.htm">Create a Repository</a></p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.86.0+.</p>
<p><strong>NOTE:</strong> You need to set your registry password in Container Registry Enterprise Edition console before use this resource.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_namespace</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">RegistryEnterpriseNamespace</span><span class="p">(</span><span class="s2">&quot;my-namespace&quot;</span><span class="p">,</span>
    <span class="n">auto_create</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">default_visibility</span><span class="o">=</span><span class="s2">&quot;PUBLIC&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="s2">&quot;cri-xxx&quot;</span><span class="p">)</span>
<span class="n">my_repo</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">RegistryEnterpriseRepo</span><span class="p">(</span><span class="s2">&quot;my-repo&quot;</span><span class="p">,</span>
    <span class="n">detail</span><span class="o">=</span><span class="s2">&quot;this is a public repo&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">my_namespace</span><span class="o">.</span><span class="n">instance_id</span><span class="p">,</span>
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
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of Container Registry Enterprise Edition instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition repository. It can contain 2 to 64 characters.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition namespace where repository is located. It can contain 2 to 30 characters.</p></li>
<li><p><strong>repo_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, repo’s visibility.</p></li>
<li><p><strong>summary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository general information. It can contain 1 to 100 characters.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo.detail">
<code class="sig-name descname">detail</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo.detail" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository specific information. MarkDown format is supported, and the length limit is 2000.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of Container Registry Enterprise Edition instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Container Registry Enterprise Edition repository. It can contain 2 to 64 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo.namespace">
<code class="sig-name descname">namespace</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Container Registry Enterprise Edition namespace where repository is located. It can contain 2 to 30 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo.repo_id">
<code class="sig-name descname">repo_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo.repo_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The uuid of Container Registry Enterprise Edition repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo.repo_type">
<code class="sig-name descname">repo_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo.repo_type" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, repo’s visibility.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo.summary">
<code class="sig-name descname">summary</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo.summary" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository general information. It can contain 1 to 100 characters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">summary</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegistryEnterpriseRepo resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>detail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository specific information. MarkDown format is supported, and the length limit is 2000.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of Container Registry Enterprise Edition instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition repository. It can contain 2 to 64 characters.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition namespace where repository is located. It can contain 2 to 30 characters.</p></li>
<li><p><strong>repo_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The uuid of Container Registry Enterprise Edition repository.</p></li>
<li><p><strong>repo_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">PUBLIC</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>, repo’s visibility.</p></li>
<li><p><strong>summary</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository general information. It can contain 1 to 100 characters.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.RegistryEnterpriseRepo.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseRepo.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">RegistryEnterpriseSyncRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_namespace_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_repo_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource will help you to manager Container Registry Enterprise Edition sync rules.</p>
<p>For information about Container Registry Enterprise Edition sync rules and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/145280.htm">Create a Sync Rule</a></p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.90.0+.</p>
<p><strong>NOTE:</strong> You need to set your registry password in Container Registry Enterprise Edition console before use this resource.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">RegistryEnterpriseSyncRule</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="s2">&quot;my-source-instance-id&quot;</span><span class="p">,</span>
    <span class="n">namespace_name</span><span class="o">=</span><span class="s2">&quot;my-source-namespace&quot;</span><span class="p">,</span>
    <span class="n">repo_name</span><span class="o">=</span><span class="s2">&quot;my-source-repo&quot;</span><span class="p">,</span>
    <span class="n">tag_filter</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
    <span class="n">target_instance_id</span><span class="o">=</span><span class="s2">&quot;my-target-instance-id&quot;</span><span class="p">,</span>
    <span class="n">target_namespace_name</span><span class="o">=</span><span class="s2">&quot;my-target-namespace&quot;</span><span class="p">,</span>
    <span class="n">target_region_id</span><span class="o">=</span><span class="s2">&quot;cn-hangzhou&quot;</span><span class="p">,</span>
    <span class="n">target_repo_name</span><span class="o">=</span><span class="s2">&quot;my-target-repo&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of Container Registry Enterprise Edition source instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition sync rule.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition source namespace. It can contain 2 to 30 characters.</p></li>
<li><p><strong>repo_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the source repository which should be set together with <code class="docutils literal notranslate"><span class="pre">target_repo_name</span></code>, if empty means that the synchronization scope is the entire namespace level.</p></li>
<li><p><strong>tag_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The regular expression used to filter image tags for synchronization in the source repository.</p></li>
<li><p><strong>target_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of Container Registry Enterprise Edition target instance to be synchronized.</p></li>
<li><p><strong>target_namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition target namespace to be synchronized. It can contain 2 to 30 characters.</p></li>
<li><p><strong>target_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target region to be synchronized.</p></li>
<li><p><strong>target_repo_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the target repository.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of Container Registry Enterprise Edition source instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Container Registry Enterprise Edition sync rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.namespace_name">
<code class="sig-name descname">namespace_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Container Registry Enterprise Edition source namespace. It can contain 2 to 30 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.repo_name">
<code class="sig-name descname">repo_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.repo_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the source repository which should be set together with <code class="docutils literal notranslate"><span class="pre">target_repo_name</span></code>, if empty means that the synchronization scope is the entire namespace level.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.rule_id">
<code class="sig-name descname">rule_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The uuid of Container Registry Enterprise Edition sync rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.sync_direction">
<code class="sig-name descname">sync_direction</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.sync_direction" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">FROM</span></code> or <code class="docutils literal notranslate"><span class="pre">TO</span></code>, the direction of synchronization. <code class="docutils literal notranslate"><span class="pre">FROM</span></code> means source instance, <code class="docutils literal notranslate"><span class="pre">TO</span></code> means target instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.sync_scope">
<code class="sig-name descname">sync_scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.sync_scope" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">REPO</span></code> or <code class="docutils literal notranslate"><span class="pre">NAMESPACE</span></code>,the scope that the synchronization rule applies.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.tag_filter">
<code class="sig-name descname">tag_filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.tag_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The regular expression used to filter image tags for synchronization in the source repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.target_instance_id">
<code class="sig-name descname">target_instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.target_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of Container Registry Enterprise Edition target instance to be synchronized.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.target_namespace_name">
<code class="sig-name descname">target_namespace_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.target_namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Container Registry Enterprise Edition target namespace to be synchronized. It can contain 2 to 30 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.target_region_id">
<code class="sig-name descname">target_region_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.target_region_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The target region to be synchronized.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.target_repo_name">
<code class="sig-name descname">target_repo_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.target_repo_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the target repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sync_direction</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sync_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_namespace_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_repo_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegistryEnterpriseSyncRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of Container Registry Enterprise Edition source instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition sync rule.</p></li>
<li><p><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition source namespace. It can contain 2 to 30 characters.</p></li>
<li><p><strong>repo_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the source repository which should be set together with <code class="docutils literal notranslate"><span class="pre">target_repo_name</span></code>, if empty means that the synchronization scope is the entire namespace level.</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The uuid of Container Registry Enterprise Edition sync rule.</p></li>
<li><p><strong>sync_direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">FROM</span></code> or <code class="docutils literal notranslate"><span class="pre">TO</span></code>, the direction of synchronization. <code class="docutils literal notranslate"><span class="pre">FROM</span></code> means source instance, <code class="docutils literal notranslate"><span class="pre">TO</span></code> means target instance.</p></li>
<li><p><strong>sync_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">REPO</span></code> or <code class="docutils literal notranslate"><span class="pre">NAMESPACE</span></code>,the scope that the synchronization rule applies.</p></li>
<li><p><strong>tag_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The regular expression used to filter image tags for synchronization in the source repository.</p></li>
<li><p><strong>target_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of Container Registry Enterprise Edition target instance to be synchronized.</p></li>
<li><p><strong>target_namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Container Registry Enterprise Edition target namespace to be synchronized. It can contain 2 to 30 characters.</p></li>
<li><p><strong>target_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target region to be synchronized.</p></li>
<li><p><strong>target_repo_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the target repository.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.RegistryEnterpriseSyncRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.RegistryEnterpriseSyncRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.ServerlessKubernetes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">ServerlessKubernetes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_ca_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_public_access_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_update</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kube_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_nat_gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ServerlessKubernetes resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] client_cert: The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.
:param pulumi.Input[str] client_key: The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.
:param pulumi.Input[str] cluster_ca_cert: The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code>
:param pulumi.Input[bool] deletion_protection: Whether enable the deletion protection or not.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">true</span><span class="p">:</span> <span class="n">Enable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
<span class="o">-</span> <span class="n">false</span><span class="p">:</span> <span class="n">Disable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>endpoint_public_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create internet  eip for API Server. Default to false.</p></li>
<li><p><strong>force_update</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Default false, when you want to change <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>, you have to set this field to true, then the cluster will be recreated.</p></li>
<li><p><strong>kube_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kubernetes cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><strong>new_nat_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create a new nat gateway while creating kubernetes cluster. Default to true.</p></li>
<li><p><strong>private_zone</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Privatezone if you need to use the service discovery feature within the serverless cluster. Default to false.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security group to which the ECS instances in the cluster belong. If it is not specified, a new Security group will be built.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Default nil, A map of tags assigned to the kubernetes cluster .</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vpc where new kubernetes cluster will be located. Specify one vpc’s id, if it is not specified, a new VPC  will be built.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Required, ForceNew) The vswitch where new kubernetes cluster will be located. Specify one vswitch’s id, if it is not specified, a new VPC and VSwicth will be built. It must be in the zone which <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> specified.</p></li>
<li><p><strong>vswitch_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The vswitches where new kubernetes cluster will be located.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is the only in one Alicloud account.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.client_cert">
<code class="sig-name descname">client_cert</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.client_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.client_key">
<code class="sig-name descname">client_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.client_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.cluster_ca_cert">
<code class="sig-name descname">cluster_ca_cert</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.cluster_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.deletion_protection">
<code class="sig-name descname">deletion_protection</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether enable the deletion protection or not.</p>
<ul class="simple">
<li><p>true: Enable deletion protection.</p></li>
<li><p>false: Disable deletion protection.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.endpoint_public_access_enabled">
<code class="sig-name descname">endpoint_public_access_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.endpoint_public_access_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create internet  eip for API Server. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.force_update">
<code class="sig-name descname">force_update</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.force_update" title="Permalink to this definition">¶</a></dt>
<dd><p>Default false, when you want to change <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>, you have to set this field to true, then the cluster will be recreated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.kube_config">
<code class="sig-name descname">kube_config</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.kube_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The kubernetes cluster’s name. It is the only in one Alicloud account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.new_nat_gateway">
<code class="sig-name descname">new_nat_gateway</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.new_nat_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create a new nat gateway while creating kubernetes cluster. Default to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.private_zone">
<code class="sig-name descname">private_zone</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.private_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable Privatezone if you need to use the service discovery feature within the serverless cluster. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group to which the ECS instances in the cluster belong. If it is not specified, a new Security group will be built.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Default nil, A map of tags assigned to the kubernetes cluster .</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The vpc where new kubernetes cluster will be located. Specify one vpc’s id, if it is not specified, a new VPC  will be built.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>(Required, ForceNew) The vswitch where new kubernetes cluster will be located. Specify one vswitch’s id, if it is not specified, a new VPC and VSwicth will be built. It must be in the zone which <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> specified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.vswitch_ids">
<code class="sig-name descname">vswitch_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.vswitch_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The vswitches where new kubernetes cluster will be located.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_ca_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_public_access_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_update</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kube_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_nat_gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerlessKubernetes resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-cert.pem</span></code>.</p></li>
<li><p><strong>client_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of client key, like <code class="docutils literal notranslate"><span class="pre">~/.kube/client-key.pem</span></code>.</p></li>
<li><p><strong>cluster_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of cluster ca certificate, like <code class="docutils literal notranslate"><span class="pre">~/.kube/cluster-ca-cert.pem</span></code></p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether enable the deletion protection or not.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">true</span><span class="p">:</span> <span class="n">Enable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
<span class="o">-</span> <span class="n">false</span><span class="p">:</span> <span class="n">Disable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>endpoint_public_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create internet  eip for API Server. Default to false.</p></li>
<li><p><strong>force_update</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Default false, when you want to change <code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>, you have to set this field to true, then the cluster will be recreated.</p></li>
<li><p><strong>kube_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of kube config, like <code class="docutils literal notranslate"><span class="pre">~/.kube/config</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The kubernetes cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><strong>new_nat_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create a new nat gateway while creating kubernetes cluster. Default to true.</p></li>
<li><p><strong>private_zone</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Privatezone if you need to use the service discovery feature within the serverless cluster. Default to false.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security group to which the ECS instances in the cluster belong. If it is not specified, a new Security group will be built.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Default nil, A map of tags assigned to the kubernetes cluster .</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vpc where new kubernetes cluster will be located. Specify one vpc’s id, if it is not specified, a new VPC  will be built.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Required, ForceNew) The vswitch where new kubernetes cluster will be located. Specify one vswitch’s id, if it is not specified, a new VPC and VSwicth will be built. It must be in the zone which <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> specified.</p></li>
<li><p><strong>vswitch_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The vswitches where new kubernetes cluster will be located.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The kubernetes cluster’s name. It is the only in one Alicloud account.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.ServerlessKubernetes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.ServerlessKubernetes.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.Swarm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">Swarm</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">need_slb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_eip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Swarm" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>DEPRECATED:</strong> This resource manages swarm cluster, which is being deprecated and will be replaced by Kubernetes cluster.</p>
</div></blockquote>
<p>This resource will help you to manager a Swarm Cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Swarm cluster only supports VPC network and you can specify a VPC network by filed <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_cluster</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">Swarm</span><span class="p">(</span><span class="s2">&quot;myCluster&quot;</span><span class="p">,</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.18.0.0/24&quot;</span><span class="p">,</span>
    <span class="n">disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_efficiency&quot;</span><span class="p">,</span>
    <span class="n">disk_size</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
    <span class="n">image_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;image_id&quot;</span><span class="p">],</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="s2">&quot;ecs.n4.small&quot;</span><span class="p">,</span>
    <span class="n">node_number</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;Yourpassword1234&quot;</span><span class="p">,</span>
    <span class="n">vswitch_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;vswitch_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block for the Container. It can not be same as the CIDR used by the VPC.
Valid value:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">0.0</span><span class="o">/</span><span class="mi">16</span>
<span class="o">-</span> <span class="mf">172.19</span><span class="o">-</span><span class="mf">30.0</span><span class="o">.</span><span class="mi">0</span><span class="o">/</span><span class="mi">16</span>
<span class="o">-</span> <span class="mf">10.0</span><span class="o">.</span><span class="mf">0.0</span><span class="o">/</span><span class="mi">16</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data disk category of ECS instance node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>, <code class="docutils literal notranslate"><span class="pre">ephemeral_essd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The data disk size of ECS instance node. Its valid value is 20~32768 GB. Default to 20.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image ID of ECS instance node used. Default to System automate allocated.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of ECS instance node.</p></li>
<li><p><strong>is_outdated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use outdated instance type. Default to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><strong>need_slb</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create the default simple routing Server Load Balancer instance for the cluster. The default value is true.</p></li>
<li><p><strong>node_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ECS node number of the container cluster. Its value choices are 1~50, and default to 1.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ECS instance node.</p></li>
<li><p><strong>release_eip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to release EIP after creating swarm cluster successfully. Default to false.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Field ‘size’ has been deprecated from provider version 1.9.1. New field ‘node_number’ replaces it.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ECS instance node. If it is not specified, the container cluster’s network mode will be <code class="docutils literal notranslate"><span class="pre">Classic</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.agent_version">
<code class="sig-name descname">agent_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.agent_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The nodes agent version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.cidr_block">
<code class="sig-name descname">cidr_block</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block for the Container. It can not be same as the CIDR used by the VPC.
Valid value:</p>
<ul class="simple">
<li><p>192.168.0.0/16</p></li>
<li><p>172.19-30.0.0/16</p></li>
<li><p>10.0.0.0/16</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.disk_category">
<code class="sig-name descname">disk_category</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>The data disk category of ECS instance node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>, <code class="docutils literal notranslate"><span class="pre">ephemeral_essd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.disk_size">
<code class="sig-name descname">disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The data disk size of ECS instance node. Its valid value is 20~32768 GB. Default to 20.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The image ID of ECS instance node used. Default to System automate allocated.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of ECS instance node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.is_outdated">
<code class="sig-name descname">is_outdated</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.is_outdated" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use outdated instance type. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The container cluster’s name. It is the only in one Alicloud account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.need_slb">
<code class="sig-name descname">need_slb</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.need_slb" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to create the default simple routing Server Load Balancer instance for the cluster. The default value is true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.node_number">
<code class="sig-name descname">node_number</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.node_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECS node number of the container cluster. Its value choices are 1~50, and default to 1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.nodes">
<code class="sig-name descname">nodes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of cluster nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Elastic IP address of node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The container cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private IP address of node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The node current status. It is different with instance status.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of ECS instance node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.release_eip">
<code class="sig-name descname">release_eip</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.release_eip" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to release EIP after creating swarm cluster successfully. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of security group where the current cluster worker node is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.size">
<code class="sig-name descname">size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Field ‘size’ has been deprecated from provider version 1.9.1. New field ‘node_number’ replaces it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.slb_id">
<code class="sig-name descname">slb_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.slb_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of load balancer where the current cluster worker node is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of VPC where the current cluster is located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cs.Swarm.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of ECS instance node. If it is not specified, the container cluster’s network mode will be <code class="docutils literal notranslate"><span class="pre">Classic</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.Swarm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">need_slb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_number</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_eip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slb_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Swarm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The nodes agent version.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block for the Container. It can not be same as the CIDR used by the VPC.
Valid value:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">0.0</span><span class="o">/</span><span class="mi">16</span>
<span class="o">-</span> <span class="mf">172.19</span><span class="o">-</span><span class="mf">30.0</span><span class="o">.</span><span class="mi">0</span><span class="o">/</span><span class="mi">16</span>
<span class="o">-</span> <span class="mf">10.0</span><span class="o">.</span><span class="mf">0.0</span><span class="o">/</span><span class="mi">16</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The data disk category of ECS instance node. Its valid value are <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>, <code class="docutils literal notranslate"><span class="pre">ephemeral_essd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The data disk size of ECS instance node. Its valid value is 20~32768 GB. Default to 20.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image ID of ECS instance node used. Default to System automate allocated.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of ECS instance node.</p></li>
<li><p><strong>is_outdated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use outdated instance type. Default to false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The container cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><strong>need_slb</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to create the default simple routing Server Load Balancer instance for the cluster. The default value is true.</p></li>
<li><p><strong>node_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ECS node number of the container cluster. Its value choices are 1~50, and default to 1.</p></li>
<li><p><strong>nodes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of cluster nodes. It contains several attributes to <code class="docutils literal notranslate"><span class="pre">Block</span> <span class="pre">Nodes</span></code>.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ECS instance node.</p></li>
<li><p><strong>release_eip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to release EIP after creating swarm cluster successfully. Default to false.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of security group where the current cluster worker node is located.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Field ‘size’ has been deprecated from provider version 1.9.1. New field ‘node_number’ replaces it.</p></li>
<li><p><strong>slb_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of load balancer where the current cluster worker node is located.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of VPC where the current cluster is located.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of ECS instance node. If it is not specified, the container cluster’s network mode will be <code class="docutils literal notranslate"><span class="pre">Classic</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>nodes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Elastic IP address of node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container cluster’s name. It is the only in one Alicloud account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address of node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The node current status. It is different with instance status.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cs.Swarm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.Swarm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.Swarm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cs.get_kubernetes_clusters">
<code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">get_kubernetes_clusters</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.get_kubernetes_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Service Kubernetes Clusters on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.34.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">k8s_clusters</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">get_kubernetes_clusters</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;my-first-k8s&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;my-first-k8s-json&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;output&quot;</span><span class="p">,</span> <span class="n">k8s_clusters</span><span class="o">.</span><span class="n">clusters</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – Cluster IDs to filter.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by cluster name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cs.get_managed_kubernetes_clusters">
<code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">get_managed_kubernetes_clusters</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.get_managed_kubernetes_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Service Managed Kubernetes Clusters on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.35.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">k8s_clusters</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">get_managed_kubernetes_clusters</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;my-first-k8s&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;my-first-k8s-json&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;output&quot;</span><span class="p">,</span> <span class="n">k8s_clusters</span><span class="o">.</span><span class="n">clusters</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – Cluster IDs to filter.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by cluster name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cs.get_registry_enterprise_instances">
<code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">get_registry_enterprise_instances</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.get_registry_enterprise_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Registry Enterprise Edition instances on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.86.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_instances</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">get_registry_enterprise_instances</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;my-instances&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;my-instances-json&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;output&quot;</span><span class="p">,</span> <span class="n">my_instances</span><span class="o">.</span><span class="n">instances</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of ids to filter results by instance id.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by instance name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cs.get_registry_enterprise_namespaces">
<code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">get_registry_enterprise_namespaces</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.get_registry_enterprise_namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Registry Enterprise Edition namespaces on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.86.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_namespaces</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">get_registry_enterprise_namespaces</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="s2">&quot;cri-xxx&quot;</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;my-namespace&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;my-namespace-json&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;output&quot;</span><span class="p">,</span> <span class="n">my_namespaces</span><span class="o">.</span><span class="n">namespaces</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of ids to filter results by namespace id.</p></li>
<li><p><strong>instance_id</strong> (<em>str</em>) – ID of Container Registry Enterprise Edition instance.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by namespace name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cs.get_registry_enterprise_repos">
<code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">get_registry_enterprise_repos</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.get_registry_enterprise_repos" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Registry Enterprise Edition repositories on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.87.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_repos</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">get_registry_enterprise_repos</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="s2">&quot;cri-xx&quot;</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;my-repos&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;my-repo-json&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;output&quot;</span><span class="p">,</span> <span class="n">my_repos</span><span class="o">.</span><span class="n">repos</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>enable_details</strong> (<em>bool</em>) – Boolean, false by default, only repository attributes are exported. Set to true if tags belong to this repository are needed. See <code class="docutils literal notranslate"><span class="pre">tags</span></code> in attributes.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of ids to filter results by repository id.</p></li>
<li><p><strong>instance_id</strong> (<em>str</em>) – ID of Container Registry Enterprise Edition instance.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by repository name.</p></li>
<li><p><strong>namespace</strong> (<em>str</em>) – Name of Container Registry Enterprise Edition namespace where the repositories are located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cs.get_registry_enterprise_sync_rules">
<code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">get_registry_enterprise_sync_rules</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repo_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.get_registry_enterprise_sync_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Registry Enterprise Edition sync rules on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.90.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">my_sync_rules</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">get_registry_enterprise_sync_rules</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="s2">&quot;cri-xxx&quot;</span><span class="p">,</span>
    <span class="n">namespace_name</span><span class="o">=</span><span class="s2">&quot;test-namespace&quot;</span><span class="p">,</span>
    <span class="n">repo_name</span><span class="o">=</span><span class="s2">&quot;test-repo&quot;</span><span class="p">,</span>
    <span class="n">target_instance_id</span><span class="o">=</span><span class="s2">&quot;cri-yyy&quot;</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;test-rule&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;output&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">my_sync_rules</span><span class="o">.</span><span class="n">rules</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of ids to filter results by sync rule id.</p></li>
<li><p><strong>instance_id</strong> (<em>str</em>) – ID of Container Registry Enterprise Edition local instance.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by sync rule name.</p></li>
<li><p><strong>namespace_name</strong> (<em>str</em>) – Name of Container Registry Enterprise Edition local namespace.</p></li>
<li><p><strong>repo_name</strong> (<em>str</em>) – Name of Container Registry Enterprise Edition local repo.</p></li>
<li><p><strong>target_instance_id</strong> (<em>str</em>) – ID of Container Registry Enterprise Edition target instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cs.get_serverless_kubernetes_clusters">
<code class="sig-prename descclassname">pulumi_alicloud.cs.</code><code class="sig-name descname">get_serverless_kubernetes_clusters</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cs.get_serverless_kubernetes_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list Container Service Serverless Kubernetes Clusters on Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.58.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">k8s_clusters</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cs</span><span class="o">.</span><span class="n">get_serverless_kubernetes_clusters</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;my-first-k8s&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;my-first-k8s-json&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;output&quot;</span><span class="p">,</span> <span class="n">k8s_clusters</span><span class="o">.</span><span class="n">clusters</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – Cluster IDs to filter.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by cluster name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
