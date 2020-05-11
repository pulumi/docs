---
title: Module appmesh
title_tag: Module appmesh | Package pulumi_aws | Python SDK
linktitle: appmesh
notitle: true
---

<div class="section" id="appmesh">
<h1>appmesh<a class="headerlink" href="#appmesh" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.appmesh"></span><dl class="py class">
<dt id="pulumi_aws.appmesh.Mesh">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appmesh.</code><code class="sig-name descname">Mesh</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Mesh" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS App Mesh service mesh resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">simple</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">Mesh</span><span class="p">(</span><span class="s2">&quot;simple&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">simple</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">Mesh</span><span class="p">(</span><span class="s2">&quot;simple&quot;</span><span class="p">,</span> <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;egressFilter&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;ALLOW_ALL&quot;</span><span class="p">,</span>
    <span class="p">},</span>
<span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the service mesh.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The service mesh specification to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">egressFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The egress filter rules for the service mesh.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The egress filter type. By default, the type is <code class="docutils literal notranslate"><span class="pre">DROP_ALL</span></code>.
Valid values are <code class="docutils literal notranslate"><span class="pre">ALLOW_ALL</span></code> and <code class="docutils literal notranslate"><span class="pre">DROP_ALL</span></code>.</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Mesh.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the service mesh.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Mesh.created_date">
<code class="sig-name descname">created_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the service mesh.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Mesh.last_updated_date">
<code class="sig-name descname">last_updated_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the service mesh.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Mesh.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for the service mesh.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Mesh.spec">
<code class="sig-name descname">spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The service mesh specification to apply.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">egressFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The egress filter rules for the service mesh.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The egress filter type. By default, the type is <code class="docutils literal notranslate"><span class="pre">DROP_ALL</span></code>.
Valid values are <code class="docutils literal notranslate"><span class="pre">ALLOW_ALL</span></code> and <code class="docutils literal notranslate"><span class="pre">DROP_ALL</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Mesh.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.appmesh.Mesh.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_updated_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Mesh resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the service mesh.</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the service mesh.</p></li>
<li><p><strong>last_updated_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last update date of the service mesh.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the service mesh.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The service mesh specification to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">egressFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The egress filter rules for the service mesh.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The egress filter type. By default, the type is <code class="docutils literal notranslate"><span class="pre">DROP_ALL</span></code>.
Valid values are <code class="docutils literal notranslate"><span class="pre">ALLOW_ALL</span></code> and <code class="docutils literal notranslate"><span class="pre">DROP_ALL</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.appmesh.Mesh.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.Mesh.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Mesh.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.Route">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appmesh.</code><code class="sig-name descname">Route</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mesh_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_router_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS App Mesh route resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">serviceb</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">Route</span><span class="p">(</span><span class="s2">&quot;serviceb&quot;</span><span class="p">,</span>
    <span class="n">mesh_name</span><span class="o">=</span><span class="n">aws_appmesh_mesh</span><span class="p">[</span><span class="s2">&quot;simple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;httpRoute&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;weightedTarget&quot;</span><span class="p">:</span> <span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;virtualNode&quot;</span><span class="p">:</span> <span class="n">aws_appmesh_virtual_node</span><span class="p">[</span><span class="s2">&quot;serviceb1&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
                        <span class="s2">&quot;weight&quot;</span><span class="p">:</span> <span class="mi">90</span><span class="p">,</span>
                    <span class="p">},</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;virtualNode&quot;</span><span class="p">:</span> <span class="n">aws_appmesh_virtual_node</span><span class="p">[</span><span class="s2">&quot;serviceb2&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
                        <span class="s2">&quot;weight&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">],</span>
            <span class="p">},</span>
            <span class="s2">&quot;match&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;prefix&quot;</span><span class="p">:</span> <span class="s2">&quot;/&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">virtual_router_name</span><span class="o">=</span><span class="n">aws_appmesh_virtual_router</span><span class="p">[</span><span class="s2">&quot;serviceb&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">serviceb</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">Route</span><span class="p">(</span><span class="s2">&quot;serviceb&quot;</span><span class="p">,</span>
    <span class="n">mesh_name</span><span class="o">=</span><span class="n">aws_appmesh_mesh</span><span class="p">[</span><span class="s2">&quot;simple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;httpRoute&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;weightedTarget&quot;</span><span class="p">:</span> <span class="p">[{</span>
                    <span class="s2">&quot;virtualNode&quot;</span><span class="p">:</span> <span class="n">aws_appmesh_virtual_node</span><span class="p">[</span><span class="s2">&quot;serviceb&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
                    <span class="s2">&quot;weight&quot;</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span>
                <span class="p">}],</span>
            <span class="p">},</span>
            <span class="s2">&quot;match&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;header&quot;</span><span class="p">:</span> <span class="p">[{</span>
                    <span class="s2">&quot;match&quot;</span><span class="p">:</span> <span class="p">{</span>
                        <span class="s2">&quot;prefix&quot;</span><span class="p">:</span> <span class="s2">&quot;123&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;clientRequestId&quot;</span><span class="p">,</span>
                <span class="p">}],</span>
                <span class="s2">&quot;method&quot;</span><span class="p">:</span> <span class="s2">&quot;POST&quot;</span><span class="p">,</span>
                <span class="s2">&quot;prefix&quot;</span><span class="p">:</span> <span class="s2">&quot;/&quot;</span><span class="p">,</span>
                <span class="s2">&quot;scheme&quot;</span><span class="p">:</span> <span class="s2">&quot;https&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">virtual_router_name</span><span class="o">=</span><span class="n">aws_appmesh_virtual_router</span><span class="p">[</span><span class="s2">&quot;serviceb&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">serviceb</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">Route</span><span class="p">(</span><span class="s2">&quot;serviceb&quot;</span><span class="p">,</span>
    <span class="n">mesh_name</span><span class="o">=</span><span class="n">aws_appmesh_mesh</span><span class="p">[</span><span class="s2">&quot;simple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;tcpRoute&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;weightedTarget&quot;</span><span class="p">:</span> <span class="p">[{</span>
                    <span class="s2">&quot;virtualNode&quot;</span><span class="p">:</span> <span class="n">aws_appmesh_virtual_node</span><span class="p">[</span><span class="s2">&quot;serviceb1&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
                    <span class="s2">&quot;weight&quot;</span><span class="p">:</span> <span class="mi">100</span><span class="p">,</span>
                <span class="p">}],</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">virtual_router_name</span><span class="o">=</span><span class="n">aws_appmesh_virtual_router</span><span class="p">[</span><span class="s2">&quot;serviceb&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the route.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the route.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The route specification to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>virtual_router_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual router in which to create the route.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">httpRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The HTTP routing information for the route.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The action to take if a match is determined.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedTargets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The targets that traffic is routed to when a request matches the route.
You can specify one or more targets and their relative weights with which to distribute traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The virtual node to associate with the weighted target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The relative weight of the weighted target. An integer between 0 and 100.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The criteria for determining an HTTP request match.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The client request headers to match on.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">invert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the match is on the opposite of the <code class="docutils literal notranslate"><span class="pre">match</span></code> method and value. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The method and value to match the header value sent with a request. Specify one match method.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exact</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header value sent by the client must match the specified value exactly.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the path with which to match requests.
This parameter must always start with /, which by itself matches all requests to the virtual router service name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The object that specifies the range of numbers that the header value sent by the client must be included in.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The end of the range.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The start of the range.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header value sent by the client must include the specified characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">suffix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header value sent by the client must end with the specified characters.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A name for the HTTP header in the client request that will be matched on.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client request header method to match on. Valid values: <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">CONNECT</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">TRACE</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the path with which to match requests.
This parameter must always start with /, which by itself matches all requests to the virtual router service name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client request header scheme to match on. Valid values: <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The priority for the route, between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.
Routes are matched based on the specified value, where <code class="docutils literal notranslate"><span class="pre">0</span></code> is the highest priority.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcpRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The TCP routing information for the route.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The action to take if a match is determined.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedTargets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The targets that traffic is routed to when a request matches the route.
You can specify one or more targets and their relative weights with which to distribute traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The virtual node to associate with the weighted target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The relative weight of the weighted target. An integer between 0 and 100.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Route.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Route.created_date">
<code class="sig-name descname">created_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Route.last_updated_date">
<code class="sig-name descname">last_updated_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Route.mesh_name">
<code class="sig-name descname">mesh_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.mesh_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service mesh in which to create the route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Route.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for the route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Route.spec">
<code class="sig-name descname">spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The route specification to apply.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">httpRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The HTTP routing information for the route.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The action to take if a match is determined.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedTargets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The targets that traffic is routed to when a request matches the route.
You can specify one or more targets and their relative weights with which to distribute traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The virtual node to associate with the weighted target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The relative weight of the weighted target. An integer between 0 and 100.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The criteria for determining an HTTP request match.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The client request headers to match on.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">invert</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the match is on the opposite of the <code class="docutils literal notranslate"><span class="pre">match</span></code> method and value. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The method and value to match the header value sent with a request. Specify one match method.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exact</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The header value sent by the client must match the specified value exactly.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the path with which to match requests.
This parameter must always start with /, which by itself matches all requests to the virtual router service name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The object that specifies the range of numbers that the header value sent by the client must be included in.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The end of the range.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The start of the range.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The header value sent by the client must include the specified characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">suffix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The header value sent by the client must end with the specified characters.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A name for the HTTP header in the client request that will be matched on.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client request header method to match on. Valid values: <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">CONNECT</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">TRACE</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the path with which to match requests.
This parameter must always start with /, which by itself matches all requests to the virtual router service name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client request header scheme to match on. Valid values: <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The priority for the route, between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.
Routes are matched based on the specified value, where <code class="docutils literal notranslate"><span class="pre">0</span></code> is the highest priority.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcpRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The TCP routing information for the route.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The action to take if a match is determined.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedTargets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The targets that traffic is routed to when a request matches the route.
You can specify one or more targets and their relative weights with which to distribute traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The virtual node to associate with the weighted target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The relative weight of the weighted target. An integer between 0 and 100.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Route.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.Route.virtual_router_name">
<code class="sig-name descname">virtual_router_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.Route.virtual_router_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual router in which to create the route.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.appmesh.Route.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_updated_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mesh_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_router_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Route.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Route resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the route.</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the route.</p></li>
<li><p><strong>last_updated_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last update date of the route.</p></li>
<li><p><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the route.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the route.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The route specification to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>virtual_router_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual router in which to create the route.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">httpRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The HTTP routing information for the route.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The action to take if a match is determined.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedTargets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The targets that traffic is routed to when a request matches the route.
You can specify one or more targets and their relative weights with which to distribute traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The virtual node to associate with the weighted target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The relative weight of the weighted target. An integer between 0 and 100.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The criteria for determining an HTTP request match.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The client request headers to match on.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">invert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the match is on the opposite of the <code class="docutils literal notranslate"><span class="pre">match</span></code> method and value. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The method and value to match the header value sent with a request. Specify one match method.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">exact</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header value sent by the client must match the specified value exactly.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the path with which to match requests.
This parameter must always start with /, which by itself matches all requests to the virtual router service name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The object that specifies the range of numbers that the header value sent by the client must be included in.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The end of the range.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The start of the range.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header value sent by the client must include the specified characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">suffix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header value sent by the client must end with the specified characters.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A name for the HTTP header in the client request that will be matched on.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client request header method to match on. Valid values: <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">CONNECT</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">TRACE</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the path with which to match requests.
This parameter must always start with /, which by itself matches all requests to the virtual router service name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client request header scheme to match on. Valid values: <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The priority for the route, between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">1000</span></code>.
Routes are matched based on the specified value, where <code class="docutils literal notranslate"><span class="pre">0</span></code> is the highest priority.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tcpRoute</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The TCP routing information for the route.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The action to take if a match is determined.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedTargets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The targets that traffic is routed to when a request matches the route.
You can specify one or more targets and their relative weights with which to distribute traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The virtual node to associate with the weighted target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The relative weight of the weighted target. An integer between 0 and 100.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.appmesh.Route.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.Route.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualNode">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appmesh.</code><code class="sig-name descname">VirtualNode</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mesh_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS App Mesh virtual node resource.</p>
<p>Because of backward incompatible API changes (read <a class="reference external" href="https://github.com/awslabs/aws-app-mesh-examples/issues/92">here</a>), <code class="docutils literal notranslate"><span class="pre">appmesh.VirtualNode</span></code> resource definitions created with provider versions earlier than v2.3.0 will need to be modified:</p>
<ul class="simple">
<li><p>Rename the <code class="docutils literal notranslate"><span class="pre">service_name</span></code> attribute of the <code class="docutils literal notranslate"><span class="pre">dns</span></code> object to <code class="docutils literal notranslate"><span class="pre">hostname</span></code>.</p></li>
<li><p>Replace the <code class="docutils literal notranslate"><span class="pre">backends</span></code> attribute of the <code class="docutils literal notranslate"><span class="pre">spec</span></code> object with one or more <code class="docutils literal notranslate"><span class="pre">backend</span></code> configuration blocks,
setting <code class="docutils literal notranslate"><span class="pre">virtual_service_name</span></code> to the name of the service.</p></li>
</ul>
<p>The state associated with existing resources will automatically be migrated.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">serviceb1</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">VirtualNode</span><span class="p">(</span><span class="s2">&quot;serviceb1&quot;</span><span class="p">,</span>
    <span class="n">mesh_name</span><span class="o">=</span><span class="n">aws_appmesh_mesh</span><span class="p">[</span><span class="s2">&quot;simple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;backend&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;virtualService&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;virtualServiceName&quot;</span><span class="p">:</span> <span class="s2">&quot;servicea.simpleapp.local&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">}],</span>
        <span class="s2">&quot;listener&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;portMapping&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">8080</span><span class="p">,</span>
                <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
        <span class="s2">&quot;serviceDiscovery&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;dns&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;hostname&quot;</span><span class="p">:</span> <span class="s2">&quot;serviceb.simpleapp.local&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">servicediscovery</span><span class="o">.</span><span class="n">HttpNamespace</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
<span class="n">serviceb1</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">VirtualNode</span><span class="p">(</span><span class="s2">&quot;serviceb1&quot;</span><span class="p">,</span>
    <span class="n">mesh_name</span><span class="o">=</span><span class="n">aws_appmesh_mesh</span><span class="p">[</span><span class="s2">&quot;simple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;backend&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;virtualService&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;virtualServiceName&quot;</span><span class="p">:</span> <span class="s2">&quot;servicea.simpleapp.local&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">}],</span>
        <span class="s2">&quot;listener&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;portMapping&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">8080</span><span class="p">,</span>
                <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
        <span class="s2">&quot;serviceDiscovery&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;awsCloudMap&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;attributes&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;stack&quot;</span><span class="p">:</span> <span class="s2">&quot;blue&quot;</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;namespaceName&quot;</span><span class="p">:</span> <span class="n">example</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                <span class="s2">&quot;serviceName&quot;</span><span class="p">:</span> <span class="s2">&quot;serviceb1&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">serviceb1</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">VirtualNode</span><span class="p">(</span><span class="s2">&quot;serviceb1&quot;</span><span class="p">,</span>
    <span class="n">mesh_name</span><span class="o">=</span><span class="n">aws_appmesh_mesh</span><span class="p">[</span><span class="s2">&quot;simple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;backend&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;virtualService&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;virtualServiceName&quot;</span><span class="p">:</span> <span class="s2">&quot;servicea.simpleapp.local&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">}],</span>
        <span class="s2">&quot;listener&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;healthCheck&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;healthyThreshold&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
                <span class="s2">&quot;intervalMillis&quot;</span><span class="p">:</span> <span class="mi">5000</span><span class="p">,</span>
                <span class="s2">&quot;path&quot;</span><span class="p">:</span> <span class="s2">&quot;/ping&quot;</span><span class="p">,</span>
                <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
                <span class="s2">&quot;timeoutMillis&quot;</span><span class="p">:</span> <span class="mi">2000</span><span class="p">,</span>
                <span class="s2">&quot;unhealthyThreshold&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="s2">&quot;portMapping&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">8080</span><span class="p">,</span>
                <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
        <span class="s2">&quot;serviceDiscovery&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;dns&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;hostname&quot;</span><span class="p">:</span> <span class="s2">&quot;serviceb.simpleapp.local&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">serviceb1</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">VirtualNode</span><span class="p">(</span><span class="s2">&quot;serviceb1&quot;</span><span class="p">,</span>
    <span class="n">mesh_name</span><span class="o">=</span><span class="n">aws_appmesh_mesh</span><span class="p">[</span><span class="s2">&quot;simple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;backend&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;virtualService&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;virtualServiceName&quot;</span><span class="p">:</span> <span class="s2">&quot;servicea.simpleapp.local&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">}],</span>
        <span class="s2">&quot;listener&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;portMapping&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">8080</span><span class="p">,</span>
                <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
        <span class="s2">&quot;logging&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;accessLog&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;file&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;path&quot;</span><span class="p">:</span> <span class="s2">&quot;/dev/stdout&quot;</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">},</span>
        <span class="p">},</span>
        <span class="s2">&quot;serviceDiscovery&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;dns&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;hostname&quot;</span><span class="p">:</span> <span class="s2">&quot;serviceb.simpleapp.local&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the virtual node.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the virtual node.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual node specification to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The backends to which the virtual node is expected to send outbound traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualService</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies a virtual service to use as a backend for a virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualServiceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the virtual service that is acting as a virtual node backend.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">listener</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The listeners from which the virtual node is expected to receive inbound traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The health check information for the listener.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">healthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive successful health checks that must occur before declaring listener healthy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalMillis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time period in milliseconds between each health check execution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination path for the health check request. This is only required if the specified protocol is <code class="docutils literal notranslate"><span class="pre">http</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The destination port for the health check request. This port must match the port defined in the <code class="docutils literal notranslate"><span class="pre">port_mapping</span></code> for the listener.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol for the health check request. Valid values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutMillis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of time to wait when receiving a response from the health check, in milliseconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">portMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The port mapping information for the listener.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port used for the port mapping.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol used for the port mapping. Valid values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">logging</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The inbound and outbound access logging information for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">accessLog</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The access log configuration for a virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The file object to send virtual node access logs to.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The file path to write access logs to. You can use <code class="docutils literal notranslate"><span class="pre">/dev/stdout</span></code> to send access logs to standard out.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceDiscovery</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The service discovery information for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">awsCloudMap</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies any AWS Cloud Map information for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespaceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the AWS Cloud Map namespace to use.
Use the <cite>``servicediscovery.HttpNamespace`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html">https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html</a>&gt;`_ resource to configure a Cloud Map namespace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the AWS Cloud Map service to use. Use the <cite>``servicediscovery.Service`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html">https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html</a>&gt;`_ resource to configure a Cloud Map service.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies the DNS service name for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The DNS host name for your virtual node.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.created_date">
<code class="sig-name descname">created_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the virtual node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.last_updated_date">
<code class="sig-name descname">last_updated_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the virtual node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.mesh_name">
<code class="sig-name descname">mesh_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.mesh_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service mesh in which to create the virtual node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for the virtual node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.spec">
<code class="sig-name descname">spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual node specification to apply.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The backends to which the virtual node is expected to send outbound traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualService</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies a virtual service to use as a backend for a virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualServiceName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the virtual service that is acting as a virtual node backend.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">listener</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The listeners from which the virtual node is expected to receive inbound traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The health check information for the listener.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">healthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of consecutive successful health checks that must occur before declaring listener healthy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalMillis</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The time period in milliseconds between each health check execution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The destination path for the health check request. This is only required if the specified protocol is <code class="docutils literal notranslate"><span class="pre">http</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The destination port for the health check request. This port must match the port defined in the <code class="docutils literal notranslate"><span class="pre">port_mapping</span></code> for the listener.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol for the health check request. Valid values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutMillis</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of time to wait when receiving a response from the health check, in milliseconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">portMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The port mapping information for the listener.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port used for the port mapping.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol used for the port mapping. Valid values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">logging</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The inbound and outbound access logging information for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">accessLog</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The access log configuration for a virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The file object to send virtual node access logs to.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The file path to write access logs to. You can use <code class="docutils literal notranslate"><span class="pre">/dev/stdout</span></code> to send access logs to standard out.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceDiscovery</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The service discovery information for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">awsCloudMap</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies any AWS Cloud Map information for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespaceName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the AWS Cloud Map namespace to use.
Use the <cite>``servicediscovery.HttpNamespace`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html">https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html</a>&gt;`_ resource to configure a Cloud Map namespace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the AWS Cloud Map service to use. Use the <cite>``servicediscovery.Service`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html">https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html</a>&gt;`_ resource to configure a Cloud Map service.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Specifies the DNS service name for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The DNS host name for your virtual node.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualNode.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.appmesh.VirtualNode.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_updated_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mesh_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualNode resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual node.</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the virtual node.</p></li>
<li><p><strong>last_updated_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last update date of the virtual node.</p></li>
<li><p><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the virtual node.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the virtual node.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual node specification to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backends</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The backends to which the virtual node is expected to send outbound traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualService</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies a virtual service to use as a backend for a virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualServiceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the virtual service that is acting as a virtual node backend.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">listener</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The listeners from which the virtual node is expected to receive inbound traffic.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The health check information for the listener.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">healthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive successful health checks that must occur before declaring listener healthy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalMillis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time period in milliseconds between each health check execution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination path for the health check request. This is only required if the specified protocol is <code class="docutils literal notranslate"><span class="pre">http</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The destination port for the health check request. This port must match the port defined in the <code class="docutils literal notranslate"><span class="pre">port_mapping</span></code> for the listener.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol for the health check request. Valid values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutMillis</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of time to wait when receiving a response from the health check, in milliseconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">portMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The port mapping information for the listener.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port used for the port mapping.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol used for the port mapping. Valid values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">logging</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The inbound and outbound access logging information for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">accessLog</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The access log configuration for a virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The file object to send virtual node access logs to.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The file path to write access logs to. You can use <code class="docutils literal notranslate"><span class="pre">/dev/stdout</span></code> to send access logs to standard out.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceDiscovery</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The service discovery information for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">awsCloudMap</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies any AWS Cloud Map information for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespaceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the AWS Cloud Map namespace to use.
Use the <cite>``servicediscovery.HttpNamespace`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html">https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html</a>&gt;`_ resource to configure a Cloud Map namespace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the AWS Cloud Map service to use. Use the <cite>``servicediscovery.Service`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html">https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html</a>&gt;`_ resource to configure a Cloud Map service.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Specifies the DNS service name for the virtual node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The DNS host name for your virtual node.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.appmesh.VirtualNode.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualNode.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualNode.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualRouter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appmesh.</code><code class="sig-name descname">VirtualRouter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mesh_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS App Mesh virtual router resource.</p>
<p>Because of backward incompatible API changes (read <a class="reference external" href="https://github.com/awslabs/aws-app-mesh-examples/issues/92">here</a> and <a class="reference external" href="https://github.com/awslabs/aws-app-mesh-examples/issues/94">here</a>), <code class="docutils literal notranslate"><span class="pre">appmesh.VirtualRouter</span></code> resource definitions created with provider versions earlier than v2.3.0 will need to be modified:</p>
<ul class="simple">
<li><p>Remove service <code class="docutils literal notranslate"><span class="pre">service_names</span></code> from the <code class="docutils literal notranslate"><span class="pre">spec</span></code> argument.
AWS has created a <code class="docutils literal notranslate"><span class="pre">appmesh.VirtualService</span></code> resource for each of service names.
These resource can be imported using <code class="docutils literal notranslate"><span class="pre">import</span></code>.</p></li>
<li><p>Add a <code class="docutils literal notranslate"><span class="pre">listener</span></code> configuration block to the <code class="docutils literal notranslate"><span class="pre">spec</span></code> argument.</p></li>
</ul>
<p>The state associated with existing resources will automatically be migrated.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">serviceb</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">VirtualRouter</span><span class="p">(</span><span class="s2">&quot;serviceb&quot;</span><span class="p">,</span>
    <span class="n">mesh_name</span><span class="o">=</span><span class="n">aws_appmesh_mesh</span><span class="p">[</span><span class="s2">&quot;simple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;listener&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;portMapping&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">8080</span><span class="p">,</span>
                <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the virtual router.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the virtual router.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual router specification to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">listener</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The listeners that the virtual router is expected to receive inbound traffic from.
Currently only one listener is supported per virtual router.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">portMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The port mapping information for the listener.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port used for the port mapping.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol used for the port mapping. Valid values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual router.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.created_date">
<code class="sig-name descname">created_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the virtual router.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.last_updated_date">
<code class="sig-name descname">last_updated_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the virtual router.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.mesh_name">
<code class="sig-name descname">mesh_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.mesh_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service mesh in which to create the virtual router.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for the virtual router.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.spec">
<code class="sig-name descname">spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual router specification to apply.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">listener</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The listeners that the virtual router is expected to receive inbound traffic from.
Currently only one listener is supported per virtual router.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">portMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The port mapping information for the listener.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port used for the port mapping.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol used for the port mapping. Valid values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualRouter.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.appmesh.VirtualRouter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_updated_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mesh_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualRouter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual router.</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the virtual router.</p></li>
<li><p><strong>last_updated_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last update date of the virtual router.</p></li>
<li><p><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the virtual router.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the virtual router.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual router specification to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">listener</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The listeners that the virtual router is expected to receive inbound traffic from.
Currently only one listener is supported per virtual router.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">portMapping</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The port mapping information for the listener.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port used for the port mapping.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol used for the port mapping. Valid values are <code class="docutils literal notranslate"><span class="pre">http</span></code> and <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.appmesh.VirtualRouter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualRouter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualRouter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appmesh.</code><code class="sig-name descname">VirtualService</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mesh_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS App Mesh virtual service resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">servicea</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">VirtualService</span><span class="p">(</span><span class="s2">&quot;servicea&quot;</span><span class="p">,</span>
    <span class="n">mesh_name</span><span class="o">=</span><span class="n">aws_appmesh_mesh</span><span class="p">[</span><span class="s2">&quot;simple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;provider&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;virtualNode&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;virtualNodeName&quot;</span><span class="p">:</span> <span class="n">aws_appmesh_virtual_node</span><span class="p">[</span><span class="s2">&quot;serviceb1&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">servicea</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">appmesh</span><span class="o">.</span><span class="n">VirtualService</span><span class="p">(</span><span class="s2">&quot;servicea&quot;</span><span class="p">,</span>
    <span class="n">mesh_name</span><span class="o">=</span><span class="n">aws_appmesh_mesh</span><span class="p">[</span><span class="s2">&quot;simple&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">spec</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;provider&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;virtualRouter&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;virtualRouterName&quot;</span><span class="p">:</span> <span class="n">aws_appmesh_virtual_router</span><span class="p">[</span><span class="s2">&quot;serviceb&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
            <span class="p">},</span>
        <span class="p">},</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the virtual service.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the virtual service.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual service specification to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The virtual node associated with a virtual service.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNodeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the virtual node that is acting as a service provider.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualRouter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The virtual router associated with a virtual service.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_router_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the virtual router that is acting as a service provider.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualService.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualService.created_date">
<code class="sig-name descname">created_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the virtual service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualService.last_updated_date">
<code class="sig-name descname">last_updated_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the virtual service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualService.mesh_name">
<code class="sig-name descname">mesh_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.mesh_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service mesh in which to create the virtual service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualService.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for the virtual service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualService.spec">
<code class="sig-name descname">spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.spec" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual service specification to apply.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNode</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The virtual node associated with a virtual service.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNodeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the virtual node that is acting as a service provider.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualRouter</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The virtual router associated with a virtual service.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_router_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the virtual router that is acting as a service provider.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.appmesh.VirtualService.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.appmesh.VirtualService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_updated_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mesh_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual service.</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the virtual service.</p></li>
<li><p><strong>last_updated_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last update date of the virtual service.</p></li>
<li><p><strong>mesh_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service mesh in which to create the virtual service.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for the virtual service.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The virtual service specification to apply.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The virtual node associated with a virtual service.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNodeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the virtual node that is acting as a service provider.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualRouter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The virtual router associated with a virtual service.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_router_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the virtual router that is acting as a service provider.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.appmesh.VirtualService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appmesh.VirtualService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appmesh.VirtualService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
