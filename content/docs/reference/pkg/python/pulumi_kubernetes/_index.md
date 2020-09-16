---
title: Package pulumi_kubernetes
title_tag: Package pulumi_kubernetes | Python SDK
linktitle: pulumi_kubernetes
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "kubernetes" >}}

<div class="section" id="module-pulumi_kubernetes">
<span id="pulumi-kubernetes"></span><h1>Pulumi Kubernetes<a class="headerlink" href="#module-pulumi_kubernetes" title="Permalink to this headline">¶</a></h1>
<dl class="py class">
<dt id="pulumi_kubernetes.ConfigFile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.</code><code class="sig-name descname">ConfigFile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transformations</span><span class="p">:</span> <span class="n">Optional[Sequence[Callable[[Any, pulumi.resource.ResourceOptions], None]]]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_prefix</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.ConfigFile" title="Permalink to this definition">¶</a></dt>
<dd><p>ConfigFile creates a set of Kubernetes resources from a Kubernetes YAML file.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.yaml</span> <span class="kn">import</span> <span class="n">ConfigFile</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">ConfigFile</span><span class="p">(</span>
    <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">file</span><span class="o">=</span><span class="s2">&quot;foo.yaml&quot;</span><span class="p">,</span>
<span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.yaml</span> <span class="kn">import</span> <span class="n">ConfigFile</span>

<span class="c1"># Make every service private to the cluster, i.e., turn all services into ClusterIP instead of LoadBalancer.</span>
<span class="k">def</span> <span class="nf">make_service_private</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">opts</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;Service&quot;</span> <span class="ow">and</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;apiVersion&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;v1&quot;</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">t</span> <span class="o">=</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;spec&quot;</span><span class="p">][</span><span class="s2">&quot;type&quot;</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">t</span> <span class="o">==</span> <span class="s2">&quot;LoadBalancer&quot;</span><span class="p">:</span>
                <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;spec&quot;</span><span class="p">][</span><span class="s2">&quot;type&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;ClusterIP&quot;</span>
        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
            <span class="k">pass</span>


<span class="c1"># Set a resource alias for a previous name.</span>
<span class="k">def</span> <span class="nf">alias</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">opts</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;Deployment&quot;</span><span class="p">:</span>
        <span class="n">opts</span><span class="o">.</span><span class="n">aliases</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;oldName&quot;</span><span class="p">]</span>


<span class="c1"># Omit a resource from the Chart by transforming the specified resource definition to an empty List.</span>
<span class="k">def</span> <span class="nf">omit_resource</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">opts</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;Pod&quot;</span> <span class="ow">and</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;metadata&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;test&quot;</span><span class="p">:</span>
        <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;apiVersion&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;v1&quot;</span>
        <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;List&quot;</span>


<span class="n">example</span> <span class="o">=</span> <span class="n">ConfigFile</span><span class="p">(</span>
    <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">file</span><span class="o">=</span><span class="s2">&quot;foo.yaml&quot;</span><span class="p">,</span>
    <span class="n">transformations</span><span class="o">=</span><span class="p">[</span><span class="n">make_service_private</span><span class="p">,</span> <span class="n">alias</span><span class="p">,</span> <span class="n">omit_resource</span><span class="p">],</span>
<span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – A name for a resource.</p></li>
<li><p><strong>file</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – Path or a URL that uniquely identifies a file.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – A bag of optional settings that control a resource’s behavior.</p></li>
<li><p><strong>pulumi.ResourceOptions</strong><strong>]</strong><strong>, </strong><strong>None</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>transformations</strong> (<em>Optional</em><em>[</em><em>Sequence</em><em>[</em><em>Callable</em><em>[</em><em>[</em><em>Any</em><em>,</em>) – A set of
transformations to apply to Kubernetes resource definitions before registering with engine.</p></li>
<li><p><strong>resource_prefix</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional prefix for the auto-generated resource names.
Example: A resource created with resource_prefix=”foo” would produce a resource named “foo-resourceName”.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_kubernetes.ConfigFile.resources">
<code class="sig-name descname">resources</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.ConfigFile.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>Kubernetes resources contained in this ConfigFile.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kubernetes.ConfigFile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.ConfigFile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.ConfigFile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.ConfigFile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_kubernetes.ConfigFile.get_resource">
<code class="sig-name descname">get_resource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_version_kind</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>pulumi.resource.CustomResource<span class="p">]</span><span class="p">[</span>pulumi.resource.CustomResource<span class="p">]</span><a class="headerlink" href="#pulumi_kubernetes.ConfigFile.get_resource" title="Permalink to this definition">¶</a></dt>
<dd><p>get_resource returns a resource defined by a built-in Kubernetes group/version/kind and
name. For example: <code class="docutils literal notranslate"><span class="pre">get_resource(&quot;apps/v1/Deployment&quot;,</span> <span class="pre">&quot;nginx&quot;)</span></code></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_version_kind</strong> (<em>str</em>) – Group/Version/Kind of the resource, e.g., <code class="docutils literal notranslate"><span class="pre">apps/v1/Deployment</span></code></p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the resource to retrieve</p></li>
<li><p><strong>namespace</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – Optional namespace of the resource to retrieve</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_kubernetes.ConfigGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.</code><code class="sig-name descname">ConfigGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">files</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">yaml</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transformations</span><span class="p">:</span> <span class="n">Optional[Sequence[Callable[[Any, pulumi.resource.ResourceOptions], None]]]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_prefix</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.ConfigGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>ConfigGroup creates a set of Kubernetes resources from Kubernetes YAML text. The YAML text
may be supplied using any of the following methods:</p>
<ol class="arabic simple">
<li><p>Using a filename or a list of filenames:</p></li>
<li><p>Using a file pattern or a list of file patterns:</p></li>
<li><p>Using a literal string containing YAML, or a list of such strings:</p></li>
<li><p>Any combination of files, patterns, or YAML strings:</p></li>
</ol>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.yaml</span> <span class="kn">import</span> <span class="n">ConfigGroup</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">ConfigGroup</span><span class="p">(</span>
    <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">files</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo.yaml&quot;</span><span class="p">],</span>
<span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.yaml</span> <span class="kn">import</span> <span class="n">ConfigGroup</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">ConfigGroup</span><span class="p">(</span>
    <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">files</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo.yaml&quot;</span><span class="p">,</span> <span class="s2">&quot;bar.yaml&quot;</span><span class="p">],</span>
<span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.yaml</span> <span class="kn">import</span> <span class="n">ConfigGroup</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">ConfigGroup</span><span class="p">(</span>
    <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">files</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;yaml/*.yaml&quot;</span><span class="p">],</span>
<span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.yaml</span> <span class="kn">import</span> <span class="n">ConfigGroup</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">ConfigGroup</span><span class="p">(</span>
    <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">files</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo/*.yaml&quot;</span><span class="p">,</span> <span class="s2">&quot;bar/*.yaml&quot;</span><span class="p">],</span>
<span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.yaml</span> <span class="kn">import</span> <span class="n">ConfigGroup</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">ConfigGroup</span><span class="p">(</span>
    <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">yaml</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;&#39;&#39;</span>
<span class="s1">apiVersion: v1</span>
<span class="s1">kind: Namespace</span>
<span class="s1">metadata:</span>
<span class="s1">  name: foo</span>
<span class="s1">&#39;&#39;&#39;</span><span class="p">]</span>
<span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.yaml</span> <span class="kn">import</span> <span class="n">ConfigGroup</span>

<span class="c1"># Make every service private to the cluster, i.e., turn all services into ClusterIP instead of LoadBalancer.</span>
<span class="k">def</span> <span class="nf">make_service_private</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">opts</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;Service&quot;</span> <span class="ow">and</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;apiVersion&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;v1&quot;</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">t</span> <span class="o">=</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;spec&quot;</span><span class="p">][</span><span class="s2">&quot;type&quot;</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">t</span> <span class="o">==</span> <span class="s2">&quot;LoadBalancer&quot;</span><span class="p">:</span>
                <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;spec&quot;</span><span class="p">][</span><span class="s2">&quot;type&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;ClusterIP&quot;</span>
        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
            <span class="k">pass</span>


<span class="c1"># Set a resource alias for a previous name.</span>
<span class="k">def</span> <span class="nf">alias</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">opts</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;Deployment&quot;</span><span class="p">:</span>
        <span class="n">opts</span><span class="o">.</span><span class="n">aliases</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;oldName&quot;</span><span class="p">]</span>


<span class="c1"># Omit a resource from the Chart by transforming the specified resource definition to an empty List.</span>
<span class="k">def</span> <span class="nf">omit_resource</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">opts</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;Pod&quot;</span> <span class="ow">and</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;metadata&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;test&quot;</span><span class="p">:</span>
        <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;apiVersion&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;v1&quot;</span>
        <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;List&quot;</span>


<span class="n">example</span> <span class="o">=</span> <span class="n">ConfigGroup</span><span class="p">(</span>
    <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">files</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo.yaml&quot;</span><span class="p">],</span>
    <span class="n">transformations</span><span class="o">=</span><span class="p">[</span><span class="n">make_service_private</span><span class="p">,</span> <span class="n">alias</span><span class="p">,</span> <span class="n">omit_resource</span><span class="p">],</span>
<span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – A name for a resource.</p></li>
<li><p><strong>files</strong> (<em>Optional</em><em>[</em><em>Sequence</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Set of paths or a URLs that uniquely identify files.</p></li>
<li><p><strong>yaml</strong> (<em>Optional</em><em>[</em><em>Sequence</em><em>[</em><em>str</em><em>]</em><em>]</em>) – YAML text containing Kubernetes resource definitions.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – A bag of optional settings that control a resource’s behavior.</p></li>
<li><p><strong>pulumi.ResourceOptions</strong><strong>]</strong><strong>, </strong><strong>None</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>transformations</strong> (<em>Optional</em><em>[</em><em>Sequence</em><em>[</em><em>Callable</em><em>[</em><em>[</em><em>Any</em><em>,</em>) – A set of
transformations to apply to Kubernetes resource definitions before registering with engine.</p></li>
<li><p><strong>resource_prefix</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional prefix for the auto-generated resource names.
Example: A resource created with resource_prefix=”foo” would produce a resource named “foo-resourceName”.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_kubernetes.ConfigGroup.resources">
<code class="sig-name descname">resources</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.ConfigGroup.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>Kubernetes resources contained in this ConfigGroup.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kubernetes.ConfigGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.ConfigGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.ConfigGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.ConfigGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_kubernetes.ConfigGroup.get_resource">
<code class="sig-name descname">get_resource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_version_kind</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>pulumi.resource.CustomResource<span class="p">]</span><span class="p">[</span>pulumi.resource.CustomResource<span class="p">]</span><a class="headerlink" href="#pulumi_kubernetes.ConfigGroup.get_resource" title="Permalink to this definition">¶</a></dt>
<dd><p>get_resource returns a resource defined by a built-in Kubernetes group/version/kind and
name. For example: <code class="docutils literal notranslate"><span class="pre">get_resource(&quot;apps/v1/Deployment&quot;,</span> <span class="pre">&quot;nginx&quot;)</span></code></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_version_kind</strong> (<em>str</em>) – Group/Version/Kind of the resource, e.g., <code class="docutils literal notranslate"><span class="pre">apps/v1/Deployment</span></code></p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the resource to retrieve</p></li>
<li><p><strong>namespace</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – Optional namespace of the resource to retrieve</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_kubernetes.Directory">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.</code><code class="sig-name descname">Directory</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">directory</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transformations</span><span class="p">:</span> <span class="n">Optional[Sequence[Callable[[Any, pulumi.resource.ResourceOptions], None]]]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_prefix</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.Directory" title="Permalink to this definition">¶</a></dt>
<dd><p>Directory is a component representing a collection of resources described by a kustomize directory
(kustomization).</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.kustomize</span> <span class="kn">import</span> <span class="n">Directory</span>

<span class="n">hello_world</span> <span class="o">=</span> <span class="n">Directory</span><span class="p">(</span>
    <span class="s2">&quot;hello-world-local&quot;</span><span class="p">,</span>
    <span class="n">directory</span><span class="o">=</span><span class="s2">&quot;./helloWorld&quot;</span><span class="p">,</span>
<span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.kustomize</span> <span class="kn">import</span> <span class="n">Directory</span>

<span class="n">hello_world</span> <span class="o">=</span> <span class="n">Directory</span><span class="p">(</span>
    <span class="s2">&quot;hello-world-remote&quot;</span><span class="p">,</span>
    <span class="n">directory</span><span class="o">=</span><span class="s2">&quot;https://github.com/kubernetes-sigs/kustomize/tree/v3.3.1/examples/helloWorld&quot;</span><span class="p">,</span>
<span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pulumi_kubernetes.helm.v3</span> <span class="kn">import</span> <span class="n">Chart</span><span class="p">,</span> <span class="n">ChartOpts</span><span class="p">,</span> <span class="n">FetchOpts</span>

<span class="c1"># Make every service private to the cluster, i.e., turn all services into ClusterIP instead of LoadBalancer.</span>
<span class="k">def</span> <span class="nf">make_service_private</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">opts</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;Service&quot;</span> <span class="ow">and</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;apiVersion&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;v1&quot;</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">t</span> <span class="o">=</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;spec&quot;</span><span class="p">][</span><span class="s2">&quot;type&quot;</span><span class="p">]</span>
            <span class="k">if</span> <span class="n">t</span> <span class="o">==</span> <span class="s2">&quot;LoadBalancer&quot;</span><span class="p">:</span>
                <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;spec&quot;</span><span class="p">][</span><span class="s2">&quot;type&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;ClusterIP&quot;</span>
        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
            <span class="k">pass</span>


<span class="c1"># Set a resource alias for a previous name.</span>
<span class="k">def</span> <span class="nf">alias</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">opts</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;Deployment&quot;</span><span class="p">:</span>
        <span class="n">opts</span><span class="o">.</span><span class="n">aliases</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;oldName&quot;</span><span class="p">]</span>


<span class="c1"># Omit a resource from the Chart by transforming the specified resource definition to an empty List.</span>
<span class="k">def</span> <span class="nf">omit_resource</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">opts</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;Pod&quot;</span> <span class="ow">and</span> <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;metadata&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;test&quot;</span><span class="p">:</span>
        <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;apiVersion&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;v1&quot;</span>
        <span class="n">obj</span><span class="p">[</span><span class="s2">&quot;kind&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;List&quot;</span>


<span class="n">hello_world</span> <span class="o">=</span> <span class="n">Directory</span><span class="p">(</span>
    <span class="s2">&quot;hello-world-remote&quot;</span><span class="p">,</span>
    <span class="n">directory</span><span class="o">=</span><span class="s2">&quot;https://github.com/kubernetes-sigs/kustomize/tree/v3.3.1/examples/helloWorld&quot;</span><span class="p">,</span>
    <span class="n">transformations</span><span class="o">=</span><span class="p">[</span><span class="n">make_service_private</span><span class="p">,</span> <span class="n">alias</span><span class="p">,</span> <span class="n">omit_resource</span><span class="p">],</span>
<span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – A name for a resource.</p></li>
<li><p><strong>directory</strong> (<em>str</em>) – The directory containing the kustomization to apply. The value can be a local directory
or a folder in a git repository.
Example: ./helloWorld
Example: <a class="reference external" href="https://github.com/kubernetes-sigs/kustomize/tree/master/examples/helloWorld">https://github.com/kubernetes-sigs/kustomize/tree/master/examples/helloWorld</a></p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – A bag of optional settings that control a resource’s behavior.</p></li>
<li><p><strong>pulumi.ResourceOptions</strong><strong>]</strong><strong>, </strong><strong>None</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>transformations</strong> (<em>Optional</em><em>[</em><em>Sequence</em><em>[</em><em>Callable</em><em>[</em><em>[</em><em>Any</em><em>,</em>) – A set of
transformations to apply to Kubernetes resource definitions before registering with engine.</p></li>
<li><p><strong>resource_prefix</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional prefix for the auto-generated resource names.
Example: A resource created with resource_prefix=”foo” would produce a resource named “foo-resourceName”.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_kubernetes.Directory.resources">
<code class="sig-name descname">resources</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.Directory.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>Kubernetes resources contained in this Directory.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kubernetes.Directory.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.Directory.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.Directory.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span><span class="p">:</span> <span class="n">str</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.Directory.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_kubernetes.Directory.get_resource">
<code class="sig-name descname">get_resource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_version_kind</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output<span class="p">[</span>pulumi.resource.CustomResource<span class="p">]</span><span class="p">[</span>pulumi.resource.CustomResource<span class="p">]</span><a class="headerlink" href="#pulumi_kubernetes.Directory.get_resource" title="Permalink to this definition">¶</a></dt>
<dd><p>get_resource returns a resource defined by a built-in Kubernetes group/version/kind and
name. For example: <code class="docutils literal notranslate"><span class="pre">get_resource(&quot;apps/v1/Deployment&quot;,</span> <span class="pre">&quot;nginx&quot;)</span></code></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_version_kind</strong> (<em>str</em>) – Group/Version/Kind of the resource, e.g., <code class="docutils literal notranslate"><span class="pre">apps/v1/Deployment</span></code></p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the resource to retrieve</p></li>
<li><p><strong>namespace</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – Optional namespace of the resource to retrieve</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_kubernetes.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">context</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_dry_run</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfig</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">render_yaml_to_directory</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppress_deprecation_warnings</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the kubernetes package.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If present, the name of the kubeconfig cluster to use.</p></li>
<li><p><strong>context</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If present, the name of the kubeconfig context to use.</p></li>
<li><p><strong>enable_dry_run</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – BETA FEATURE - If present and set to true, enable server-side diff calculations.
This feature is in developer preview, and is disabled by default.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>This config can be specified in the following ways, using this precedence:
1. This `enableDryRun` parameter.
2. The `PULUMI_K8S_ENABLE_DRY_RUN` environment variable.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>kubeconfig</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of a kubeconfig file or the path to a kubeconfig file. If this is set, this config will be used instead of $KUBECONFIG.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If present, the default namespace to use. This flag is ignored for cluster-scoped resources.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>A namespace can be specified in multiple places, and the precedence is as follows:
1. `.metadata.namespace` set on the resource.
2. This `namespace` parameter.
3. `namespace` set for the active context in the kubeconfig.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>render_yaml_to_directory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BETA FEATURE - If present, render resource manifests to this directory. In this mode, resources will not
be created on a Kubernetes cluster, but the rendered manifests will be kept in sync with changes
to the Pulumi program. This feature is in developer preview, and is disabled by default.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Note</span> <span class="n">that</span> <span class="n">some</span> <span class="n">computed</span> <span class="n">Outputs</span> <span class="n">such</span> <span class="k">as</span> <span class="n">status</span> <span class="n">fields</span> <span class="n">will</span> <span class="ow">not</span> <span class="n">be</span> <span class="n">populated</span>
<span class="n">since</span> <span class="n">the</span> <span class="n">resources</span> <span class="n">are</span> <span class="ow">not</span> <span class="n">created</span> <span class="n">on</span> <span class="n">a</span> <span class="n">Kubernetes</span> <span class="n">cluster</span><span class="o">.</span> <span class="n">These</span> <span class="n">Output</span> <span class="n">values</span> <span class="n">will</span> <span class="n">remain</span> <span class="n">undefined</span><span class="p">,</span>
<span class="ow">and</span> <span class="n">may</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">an</span> <span class="n">error</span> <span class="k">if</span> <span class="n">they</span> <span class="n">are</span> <span class="n">referenced</span> <span class="n">by</span> <span class="n">other</span> <span class="n">resources</span><span class="o">.</span> <span class="n">Also</span> <span class="n">note</span> <span class="n">that</span> <span class="nb">any</span> <span class="n">secret</span> <span class="n">values</span>
<span class="n">used</span> <span class="ow">in</span> <span class="n">these</span> <span class="n">resources</span> <span class="n">will</span> <span class="n">be</span> <span class="n">rendered</span> <span class="ow">in</span> <span class="n">plaintext</span> <span class="n">to</span> <span class="n">the</span> <span class="n">resulting</span> <span class="n">YAML</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>suppress_deprecation_warnings</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If present and set to true, suppress apiVersion deprecation warnings from the CLI.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>This config can be specified in the following ways, using this precedence:
1. This `suppressDeprecationWarnings` parameter.
2. The `PULUMI_K8S_SUPPRESS_DEPRECATION_WARNINGS` environment variable.
</pre></div>
</div>
<dl class="py method">
<dt id="pulumi_kubernetes.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
