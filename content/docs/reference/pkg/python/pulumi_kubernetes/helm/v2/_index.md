---
title: Module v2
title_tag: Module v2 | Package pulumi_kubernetes | Python SDK
linktitle: v2
notitle: true
---

<div class="section" id="module-pulumi_kubernetes.helm.v2">
<span id="v2"></span><h1>v2<a class="headerlink" href="#module-pulumi_kubernetes.helm.v2" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.BaseChartOpts">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.helm.v2.</code><code class="sig-name descname">BaseChartOpts</code><span class="sig-paren">(</span><em class="sig-param">namespace=None</em>, <em class="sig-param">values=None</em>, <em class="sig-param">transformations=None</em>, <em class="sig-param">resource_prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.BaseChartOpts" title="Permalink to this definition">¶</a></dt>
<dd><p>BaseChartOpts is a bag of common configuration options for a Helm chart.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>namespace</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Optional namespace to install chart resources into.</p></li>
<li><p><strong>values</strong> (<em>Optional</em><em>[</em><em>pulumi.Inputs</em><em>]</em>) – Optional overrides for chart values.</p></li>
<li><p><strong>Optional</strong><strong>[</strong><strong>pulumi.ResourceOptions</strong><strong>]</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>transformations</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>Tuple</em><em>[</em><em>Callable</em><em>,</em>) – Optional list
of transformations to apply to resources that will be created by this chart prior to creation.
Allows customization of the chart behaviour without directly modifying the chart itself.</p></li>
<li><p><strong>resource_prefix</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional prefix for the auto-generated resource names.
Example: A resource created with resource_prefix=”foo” would produce a resource named “foo-resourceName”.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.BaseChartOpts.namespace">
<code class="sig-name descname">namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.BaseChartOpts.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional namespace to install chart resources into.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.BaseChartOpts.values">
<code class="sig-name descname">values</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.BaseChartOpts.values" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional overrides for chart values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.BaseChartOpts.transformations">
<code class="sig-name descname">transformations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.BaseChartOpts.transformations" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional list of transformations to apply to resources that will be created by this chart prior to
creation. Allows customization of the chart behaviour without directly modifying the chart itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.BaseChartOpts.resource_prefix">
<code class="sig-name descname">resource_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.BaseChartOpts.resource_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional prefix for the auto-generated resource names.
Example: A resource created with resource_prefix=”foo” would produce a resource named “foo-resourceName”.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.Chart">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.helm.v2.</code><code class="sig-name descname">Chart</code><span class="sig-paren">(</span><em class="sig-param">release_name</em>, <em class="sig-param">config</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.Chart" title="Permalink to this definition">¶</a></dt>
<dd><p>Chart is a component representing a collection of resources described by an arbitrary Helm
Chart. The Chart can be fetched from any source that is accessible to the <code class="docutils literal notranslate"><span class="pre">helm</span></code> command
line. Values in the <code class="docutils literal notranslate"><span class="pre">values.yml</span></code> file can be overridden using <code class="docutils literal notranslate"><span class="pre">ChartOpts.values</span></code> (equivalent
to <code class="docutils literal notranslate"><span class="pre">--set</span></code> or having multiple <code class="docutils literal notranslate"><span class="pre">values.yml</span></code> files). Objects can be transformed arbitrarily by
supplying callbacks to <code class="docutils literal notranslate"><span class="pre">ChartOpts.transformations</span></code>.</p>
<p>Chart does not use Tiller. The Chart specified is copied and expanded locally; the semantics
are equivalent to running <code class="docutils literal notranslate"><span class="pre">helm</span> <span class="pre">template</span></code> and then using Pulumi to manage the resulting YAML
manifests. Any values that would be retrieved in-cluster are assigned fake values, and
none of Tiller’s server-side validity testing is executed.</p>
<p>Create an instance of the specified Helm chart.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>release_name</strong> (<em>str</em>) – Name of the Chart (e.g., nginx-ingress).</p></li>
<li><p><strong>LocalChartOpts</strong><strong>] </strong><strong>config</strong> (<em>Union</em><em>[</em><a class="reference internal" href="#pulumi_kubernetes.helm.v2.ChartOpts" title="pulumi_kubernetes.helm.v2.ChartOpts"><em>ChartOpts</em></a><em>,</em>) – Configuration options for the Chart.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – A bag of options that control this
resource’s behavior.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.Chart.resources">
<code class="sig-name descname">resources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.Chart.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>Kubernetes resources contained in this Chart.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kubernetes.helm.v2.Chart.get_resource">
<code class="sig-name descname">get_resource</code><span class="sig-paren">(</span><em class="sig-param">group_version_kind</em>, <em class="sig-param">name</em>, <em class="sig-param">namespace=None</em><span class="sig-paren">)</span> &#x2192; pulumi.output.Output[pulumi.resource.CustomResource][pulumi.resource.CustomResource]<a class="headerlink" href="#pulumi_kubernetes.helm.v2.Chart.get_resource" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.helm.v2.</code><code class="sig-name descname">ChartOpts</code><span class="sig-paren">(</span><em class="sig-param">chart</em>, <em class="sig-param">namespace=None</em>, <em class="sig-param">values=None</em>, <em class="sig-param">transformations=None</em>, <em class="sig-param">resource_prefix=None</em>, <em class="sig-param">repo=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">fetch_opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts" title="Permalink to this definition">¶</a></dt>
<dd><p>ChartOpts is a bag of configuration options for a remote Helm chart.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>chart</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the chart to deploy.  If <code class="docutils literal notranslate"><span class="pre">repo</span></code> is provided, this chart name
will be prefixed by the repo name.
Example: repo: “stable”, chart: “nginx-ingress” -&gt; “stable/nginx-ingress”
Example: chart: “stable/nginx-ingress” -&gt; “stable/nginx-ingress”</p></li>
<li><p><strong>namespace</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Optional namespace to install chart resources into.</p></li>
<li><p><strong>values</strong> (<em>Optional</em><em>[</em><em>pulumi.Inputs</em><em>]</em>) – Optional overrides for chart values.</p></li>
<li><p><strong>Optional</strong><strong>[</strong><strong>pulumi.ResourceOptions</strong><strong>]</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>transformations</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>Tuple</em><em>[</em><em>Callable</em><em>,</em>) – Optional list of
transformations to apply to resources that will be created by this chart prior to creation.
Allows customization of the chart behaviour without directly modifying the chart itself.</p></li>
<li><p><strong>resource_prefix</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional prefix for the auto-generated resource names.
Example: A resource created with resource_prefix=”foo” would produce a resource named “foo-resourceName”.</p></li>
<li><p><strong>repo</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – The repository name of the chart to deploy.
Example: “stable”</p></li>
<li><p><strong>version</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – The version of the chart to deploy. If not provided,
the latest version will be deployed.</p></li>
<li><p><strong>fetch_opts</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><a class="reference internal" href="#pulumi_kubernetes.helm.v2.FetchOpts" title="pulumi_kubernetes.helm.v2.FetchOpts"><em>FetchOpts</em></a><em>]</em><em>]</em>) – Additional options to customize the
fetching of the Helm chart.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.chart">
<code class="sig-name descname">chart</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.chart" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the chart to deploy.  If <code class="docutils literal notranslate"><span class="pre">repo</span></code> is provided, this chart name will be prefixed by the repo name.
Example: repo: “stable”, chart: “nginx-ingress” -&gt; “stable/nginx-ingress”
Example: chart: “stable/nginx-ingress” -&gt; “stable/nginx-ingress”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.repo">
<code class="sig-name descname">repo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.repo" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository name of the chart to deploy. 
Example: “stable”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the chart to deploy. If not provided, the latest version will be deployed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.fetch_opts">
<code class="sig-name descname">fetch_opts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.fetch_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional options to customize the fetching of the Helm chart.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.helm.v2.</code><code class="sig-name descname">FetchOpts</code><span class="sig-paren">(</span><em class="sig-param">version=None</em>, <em class="sig-param">ca_file=None</em>, <em class="sig-param">cert_file=None</em>, <em class="sig-param">key_file=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">keyring=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">repo=None</em>, <em class="sig-param">untar_dir=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">home=None</em>, <em class="sig-param">devel=None</em>, <em class="sig-param">prov=None</em>, <em class="sig-param">untar=None</em>, <em class="sig-param">verify=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts" title="Permalink to this definition">¶</a></dt>
<dd><p>FetchOpts is a bag of configuration options to customize the fetching of the Helm chart.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>version</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Specific version of a chart. If unset,
the latest version is fetched.</p></li>
<li><p><strong>ca_file</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Verify certificates of HTTPS-enabled
servers using this CA bundle.</p></li>
<li><p><strong>cert_file</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Identify HTTPS client using this SSL
certificate file.</p></li>
<li><p><strong>key_file</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Identify HTTPS client using this SSL
key file.</p></li>
<li><p><strong>destination</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Location to write the chart.
If this and [tardir] are specified, tardir is appended to this (default “.”).</p></li>
<li><p><strong>keyring</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Keyring containing public keys
(default “/Users/<span class="raw-html-m2r"><user></span>/.gnupg/pubring.gpg”).</p></li>
<li><p><strong>password</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Chart repository password.</p></li>
<li><p><strong>repo</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Chart repository url where to locate
the requested chart.</p></li>
<li><p><strong>untar_dir</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – If [untar] is specified, this flag
specifies the name of the directory into which the chart is
expanded (default “.”).</p></li>
<li><p><strong>username</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Chart repository username.</p></li>
<li><p><strong>home</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Location of your Helm config. Overrides
$HELM_HOME (default “/Users/<span class="raw-html-m2r"><user></span>/.helm”).</p></li>
<li><p><strong>devel</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em><em>]</em>) – Use development versions, too.
Equivalent to version ‘&gt;0.0.0-0’. If [version] is set, this is ignored.</p></li>
<li><p><strong>prov</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em><em>]</em>) – Fetch the provenance file, but don’t
perform verification.</p></li>
<li><p><strong>untar</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em><em>]</em>) – If set to false, will leave the
chart as a tarball after downloading.</p></li>
<li><p><strong>verify</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em><em>]</em>) – Verify the package against its signature.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specific version of a chart. If unset, the latest version is fetched.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.ca_file">
<code class="sig-name descname">ca_file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.ca_file" title="Permalink to this definition">¶</a></dt>
<dd><p>Verify certificates of HTTPS-enabled servers using this CA bundle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.cert_file">
<code class="sig-name descname">cert_file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.cert_file" title="Permalink to this definition">¶</a></dt>
<dd><p>Identify HTTPS client using this SSL certificate file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.key_file">
<code class="sig-name descname">key_file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.key_file" title="Permalink to this definition">¶</a></dt>
<dd><p>Identify HTTPS client using this SSL key file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Location to write the chart. If this and [tardir] are specified, tardir is appended
to this (default “.”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.keyring">
<code class="sig-name descname">keyring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.keyring" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyring containing public keys (default “/Users/alex/.gnupg/pubring.gpg”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Chart repository password.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.repo">
<code class="sig-name descname">repo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.repo" title="Permalink to this definition">¶</a></dt>
<dd><p>Chart repository url where to locate the requested chart.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.untar_dir">
<code class="sig-name descname">untar_dir</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.untar_dir" title="Permalink to this definition">¶</a></dt>
<dd><p>If [untar] is specified, this flag specifies the name of the directory into which
the chart is expanded (default “.”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Chart repository username.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.home">
<code class="sig-name descname">home</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.home" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of your Helm config. Overrides $HELM_HOME (default “/Users/alex/.helm”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.devel">
<code class="sig-name descname">devel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.devel" title="Permalink to this definition">¶</a></dt>
<dd><p>Use development versions, too. Equivalent to version ‘&gt;0.0.0-0’. If [version] is set,
this is ignored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.prov">
<code class="sig-name descname">prov</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.prov" title="Permalink to this definition">¶</a></dt>
<dd><p>Fetch the provenance file, but don’t perform verification.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.untar">
<code class="sig-name descname">untar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.untar" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to false, will leave the chart as a tarball after downloading.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.verify">
<code class="sig-name descname">verify</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.verify" title="Permalink to this definition">¶</a></dt>
<dd><p>Verify the package against its signature.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.LocalChartOpts">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.helm.v2.</code><code class="sig-name descname">LocalChartOpts</code><span class="sig-paren">(</span><em class="sig-param">path</em>, <em class="sig-param">namespace=None</em>, <em class="sig-param">values=None</em>, <em class="sig-param">transformations=None</em>, <em class="sig-param">resource_prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.LocalChartOpts" title="Permalink to this definition">¶</a></dt>
<dd><p>LocalChartOpts is a bag of configuration options for a local Helm chart.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the chart directory which contains the
<code class="docutils literal notranslate"><span class="pre">Chart.yaml</span></code> file.</p></li>
<li><p><strong>namespace</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Optional namespace to install chart resources into.</p></li>
<li><p><strong>values</strong> (<em>Optional</em><em>[</em><em>pulumi.Inputs</em><em>]</em>) – Optional overrides for chart values.</p></li>
<li><p><strong>Optional</strong><strong>[</strong><strong>pulumi.ResourceOptions</strong><strong>]</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>transformations</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>Tuple</em><em>[</em><em>Callable</em><em>,</em>) – Optional list of
transformations to apply to resources that will be created by this chart prior to creation.
Allows customization of the chart behaviour without directly modifying the chart itself.</p></li>
<li><p><strong>resource_prefix</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional prefix for the auto-generated resource names.
Example: A resource created with resource_prefix=”foo” would produce a resource named “foo-resourceName”.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.LocalChartOpts.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.LocalChartOpts.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the chart directory which contains the <code class="docutils literal notranslate"><span class="pre">Chart.yaml</span></code> file.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.TextIO">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.helm.v2.</code><code class="sig-name descname">TextIO</code><a class="headerlink" href="#pulumi_kubernetes.helm.v2.TextIO" title="Permalink to this definition">¶</a></dt>
<dd><p>Typed version of the return of open() in text mode.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_kubernetes.helm.v2.get_version">
<code class="sig-prename descclassname">pulumi_kubernetes.helm.v2.</code><code class="sig-name descname">get_version</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.get_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the Semver-formatted version of the package containing this file.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_kubernetes.helm.v2.mkdtemp">
<code class="sig-prename descclassname">pulumi_kubernetes.helm.v2.</code><code class="sig-name descname">mkdtemp</code><span class="sig-paren">(</span><em class="sig-param">suffix=None</em>, <em class="sig-param">prefix=None</em>, <em class="sig-param">dir=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.mkdtemp" title="Permalink to this definition">¶</a></dt>
<dd><p>User-callable function to create and return a unique temporary
directory.  The return value is the pathname of the directory.</p>
<p>Arguments are as for mkstemp, except that the ‘text’ argument is
not accepted.</p>
<p>The directory is readable, writable, and searchable only by the
creating user.</p>
<p>Caller is responsible for deleting the directory when done with it.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_kubernetes.helm.v2.mkstemp">
<code class="sig-prename descclassname">pulumi_kubernetes.helm.v2.</code><code class="sig-name descname">mkstemp</code><span class="sig-paren">(</span><em class="sig-param">suffix=None</em>, <em class="sig-param">prefix=None</em>, <em class="sig-param">dir=None</em>, <em class="sig-param">text=False</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.mkstemp" title="Permalink to this definition">¶</a></dt>
<dd><p>User-callable function to create and return a unique temporary
file.  The return value is a pair (fd, name) where fd is the
file descriptor returned by os.open, and name is the filename.</p>
<p>If ‘suffix’ is not None, the file name will end with that suffix,
otherwise there will be no suffix.</p>
<p>If ‘prefix’ is not None, the file name will begin with that prefix,
otherwise a default prefix is used.</p>
<p>If ‘dir’ is not None, the file will be created in that directory,
otherwise a default directory is used.</p>
<p>If ‘text’ is specified and true, the file is opened in text
mode.  Else (the default) the file is opened in binary mode.  On
some operating systems, this makes no difference.</p>
<p>If any of ‘suffix’, ‘prefix’ and ‘dir’ are not None, they must be the
same type.  If they are bytes, the returned name will be bytes; str
otherwise.</p>
<p>The file is readable and writable only by the creating user ID.
If the operating system uses permission bits to indicate whether a
file is executable, the file is executable by no one. The file
descriptor is not inherited by children of this process.</p>
<p>Caller is responsible for deleting the file when done with it.</p>
</dd></dl>

</div>
