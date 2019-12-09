---
title: Module yaml
title_tag: Module yaml | Package pulumi_kubernetes | Python SDK
linktitle: yaml
notitle: true
---

<div class="section" id="module-pulumi_kubernetes.yaml">
<span id="yaml"></span><h1>yaml<a class="headerlink" href="#module-pulumi_kubernetes.yaml" title="Permalink to this headline">¶</a></h1>
<dl class="function">
<dt id="pulumi_kubernetes.yaml.copy">
<code class="sig-prename descclassname">pulumi_kubernetes.yaml.</code><code class="sig-name descname">copy</code><span class="sig-paren">(</span><em class="sig-param">x</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.yaml.copy" title="Permalink to this definition">¶</a></dt>
<dd><p>Shallow copy operation on arbitrary Python objects.</p>
<p>See the module’s <strong>doc</strong> string for more info.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_kubernetes.yaml.getargspec">
<code class="sig-prename descclassname">pulumi_kubernetes.yaml.</code><code class="sig-name descname">getargspec</code><span class="sig-paren">(</span><em class="sig-param">func</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.yaml.getargspec" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the names and default values of a function’s parameters.</p>
<p>A tuple of four things is returned: (args, varargs, keywords, defaults).
‘args’ is a list of the argument names, including keyword-only argument names.
‘varargs’ and ‘keywords’ are the names of the * and ** parameters or None.
‘defaults’ is an n-tuple of the default values of the last n parameters.</p>
<p>This function is deprecated, as it does not support annotations or
keyword-only parameters and will raise ValueError if either is present
on the supplied callable.</p>
<p>For a more structured introspection API, use inspect.signature() instead.</p>
<p>Alternatively, use getfullargspec() for an API with a similar namedtuple
based interface, but full support for annotations and keyword-only
parameters.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.yaml.CustomResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.yaml.</code><code class="sig-name descname">CustomResource</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">api_version</em>, <em class="sig-param">kind</em>, <em class="sig-param">spec=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.yaml.CustomResource" title="Permalink to this definition">¶</a></dt>
<dd><p>CustomResource represents an instance of a CustomResourceDefinition (CRD). For example, the
CoreOS Prometheus operator exposes a CRD <code class="docutils literal notranslate"><span class="pre">monitoring.coreos.com/ServiceMonitor</span></code>; to
instantiate this as a Pulumi resource, one could call <code class="docutils literal notranslate"><span class="pre">new</span> <span class="pre">CustomResource</span></code>, passing the
<code class="docutils literal notranslate"><span class="pre">ServiceMonitor</span></code> resource definition as an argument.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – <em>Unique</em> name used to register this resource with Pulumi.</p></li>
<li><p><strong>api_version</strong> (<em>str</em>) – The API version of the apiExtensions.CustomResource we
wish to select, as specified by the CustomResourceDefinition that defines it on the
API server.</p></li>
<li><p><strong>kind</strong> (<em>str</em>) – The kind of the apiextensions.CustomResource we wish to select,
as specified by the CustomResourceDefinition that defines it on the API server.</p></li>
<li><p><strong>spec</strong> (<em>pulumi.Input</em><em>[</em><em>Any</em><em>]</em>) – Specification of the CustomResource.</p></li>
<li><p><strong>metadata</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>Any</em><em>]</em><em>]</em>) – Standard object metadata; More info:
<a class="reference external" href="https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata</a>.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – A bag of options that control this
resource’s behavior.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_kubernetes.yaml.CustomResource.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">api_version</em>, <em class="sig-param">kind</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.yaml.CustomResource.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the state of an existing <code class="docutils literal notranslate"><span class="pre">CustomResource</span></code> resource, as identified by <code class="docutils literal notranslate"><span class="pre">id</span></code>.
Typically this ID  is of the form [namespace]/[name]; if [namespace] is omitted,
then (per Kubernetes convention) the ID becomes default/[name].</p>
<p>Pulumi will keep track of this resource using <code class="docutils literal notranslate"><span class="pre">resource_name</span></code> as the Pulumi ID.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – <em>Unique</em> name used to register this resource with Pulumi.</p></li>
<li><p><strong>api_version</strong> (<em>str</em>) – The API version of the apiExtensions.CustomResource we
wish to select, as specified by the CustomResourceDefinition that defines it on the
API server.</p></li>
<li><p><strong>kind</strong> (<em>str</em>) – The kind of the apiextensions.CustomResource we wish to select,
as specified by the CustomResourceDefinition that defines it on the API server.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An ID for the Kubernetes resource to retrieve.
Takes the form <span class="raw-html-m2r"><namespace></span>/<span class="raw-html-m2r"><name></span> or <span class="raw-html-m2r"><name></span>.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – A bag of options that control this
resource’s behavior.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.yaml.CustomResource.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.yaml.CustomResource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.yaml.CustomResource.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.yaml.CustomResource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.yaml.ConfigFile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.yaml.</code><code class="sig-name descname">ConfigFile</code><span class="sig-paren">(</span><em class="sig-param">name</em>, <em class="sig-param">file_id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">transformations=None</em>, <em class="sig-param">resource_prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.yaml.ConfigFile" title="Permalink to this definition">¶</a></dt>
<dd><p>ConfigFile creates a set of Kubernetes resources from a Kubernetes YAML file.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – A name for a resource.</p></li>
<li><p><strong>file_id</strong> (<em>str</em>) – Path or a URL that uniquely identifies a file.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – A bag of optional settings that control a resource’s behavior.</p></li>
<li><p><strong>Optional</strong><strong>[</strong><strong>pulumi.ResourceOptions</strong><strong>]</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>transformations</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>Tuple</em><em>[</em><em>Callable</em><em>,</em>) – A set of
transformations to apply to Kubernetes resource definitions before registering with engine.</p></li>
<li><p><strong>resource_prefix</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional prefix for the auto-generated resource names.
Example: A resource created with resource_prefix=”foo” would produce a resource named “foo-resourceName”.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.yaml.ConfigFile.resources">
<code class="sig-name descname">resources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.yaml.ConfigFile.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>Kubernetes resources contained in this ConfigFile.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.yaml.ConfigFile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.yaml.ConfigFile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.yaml.ConfigFile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop: str</em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_kubernetes.yaml.ConfigFile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_kubernetes.yaml.ConfigFile.get_resource">
<code class="sig-name descname">get_resource</code><span class="sig-paren">(</span><em class="sig-param">group_version_kind</em>, <em class="sig-param">name</em>, <em class="sig-param">namespace=None</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[pulumi.resource.CustomResource][pulumi.resource.CustomResource]<a class="headerlink" href="#pulumi_kubernetes.yaml.ConfigFile.get_resource" title="Permalink to this definition">¶</a></dt>
<dd><p>get_resource returns a resource defined by a built-in Kubernetes group/version/kind and
name. For example: <code class="docutils literal notranslate"><span class="pre">get_resource(&quot;apps/v1/Deployment&quot;,</span> <span class="pre">&quot;nginx&quot;)</span></code></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_version_kind</strong> (<em>str</em>) – Group/Version/Kind of the resource, e.g., <code class="docutils literal notranslate"><span class="pre">apps/v1/Deployment</span></code></p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the resource to retrieve</p></li>
<li><p><strong>namespace</strong> (<em>str</em>) – Optional namespace of the resource to retrieve</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</dd></dl>

</div>
