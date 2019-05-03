<div class="section" id="module-pulumi_kubernetes.helm.v2">
<span id="v2"></span><h1>v2<a class="headerlink" href="#module-pulumi_kubernetes.helm.v2" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.Callable">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">Callable</code><a class="headerlink" href="#pulumi_kubernetes.helm.v2.Callable" title="Permalink to this definition">¶</a></dt>
<dd><p>Callable type; Callable[[int], str] is a function of (int) -&gt; str.</p>
<p>The subscription syntax must always be used with exactly two
values: the argument list and the return type.  The argument list
must be a list of types or ellipsis; the return type must be a single type.</p>
<p>There is no syntax to indicate optional or keyword arguments,
such function types are rarely used as callback types.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.Chart">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">Chart</code><span class="sig-paren">(</span><em>release_name: str, config: Union[pulumi_kubernetes.helm.v2.helm.ChartOpts, pulumi_kubernetes.helm.v2.helm.LocalChartOpts], opts: Optional[pulumi.resource.ResourceOptions] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.Chart" title="Permalink to this definition">¶</a></dt>
<dd><p>Chart is a component representing a collection of resources described by an arbitrary Helm
Chart. The Chart can be fetched from any source that is accessible to the <code class="docutils literal notranslate"><span class="pre">helm</span></code> command
line. Values in the <code class="docutils literal notranslate"><span class="pre">values.yml</span></code> file can be overridden using <code class="docutils literal notranslate"><span class="pre">ChartOpts.values</span></code> (equivalent
to <code class="docutils literal notranslate"><span class="pre">--set</span></code> or having multiple <code class="docutils literal notranslate"><span class="pre">values.yml</span></code> files). Objects can be transformed arbitrarily by
supplying callbacks to <code class="docutils literal notranslate"><span class="pre">ChartOpts.transformations</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">Chart</span></code> does not use Tiller. The Chart specified is copied and expanded locally; any values
that would be retrieved in-cluster would be assigned fake values, and none of Tiller’s
server-side validity testing is executed.</p>
<p>The semantics of <code class="docutils literal notranslate"><span class="pre">update</span></code> on a Chart are identical to those of Helm and kubectl; for example,
unlike a “normal” Pulumi program, updating a ConfigMap does not trigger a cascading update
among Deployments that reference it.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>release_name</strong> (<em>str</em>) – Name of the Chart (e.g., nginx-ingress).</li>
<li><strong>LocalChartOpts</strong><strong>] </strong><strong>config</strong> (<em>Union</em><em>[</em><a class="reference internal" href="#pulumi_kubernetes.helm.v2.ChartOpts" title="pulumi_kubernetes.helm.v2.ChartOpts"><em>ChartOpts</em></a><em>,</em>) – Configuration options for the Chart.</li>
<li><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – A bag of options that control this
resource’s behavior.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">ChartOpts</code><span class="sig-paren">(</span><em>chart: Union[T, Awaitable[T], Output[T]], namespace: Optional[Union[T, Awaitable[T], Output[T]]] = None, values: Optional[Mapping[str, Union[T, Awaitable[T], Output[T]]]] = None, transformations: Optional[List[Callable]] = None, repo: Optional[Union[T, Awaitable[T], Output[T]]] = None, version: Optional[Union[T, Awaitable[T], Output[T]]] = None, fetch_opts: Optional[Union[T, Awaitable[T], Output[T]]] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts" title="Permalink to this definition">¶</a></dt>
<dd><p>ChartOpts is a bag of configuration options for a remote Helm chart.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>chart</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The chart to deploy.  If [repo] is provided, this chart name is
looked up in the given repository. Otherwise, this chart name must be a fully qualified
chart URL or <code class="docutils literal notranslate"><span class="pre">repo/chartname</span></code>.</li>
<li><strong>namespace</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Optional namespace to install chart resources into.</li>
<li><strong>values</strong> (<em>Optional</em><em>[</em><em>pulumi.Inputs</em><em>]</em>) – Optional overrides for chart values.</li>
<li><strong>transformations</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_kubernetes.helm.v2.List" title="pulumi_kubernetes.helm.v2.List"><em>List</em></a><em>[</em><a class="reference internal" href="#pulumi_kubernetes.helm.v2.Callable" title="pulumi_kubernetes.helm.v2.Callable"><em>Callable</em></a><em>]</em>) – Optional list of transformations to apply to
resources that will be created by this chart prior to creation. Allows customization of the
chart behaviour without directly modifying the chart itself.</li>
<li><strong>repo</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – The repository containing the desired chart.  If not
provided, [chart] must be a fully qualified chart URL or repo/chartname.</li>
<li><strong>version</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – The version of the chart to deploy. If not provided,
the latest version will be deployed.</li>
<li><strong>fetch_opts</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><a class="reference internal" href="#pulumi_kubernetes.helm.v2.FetchOpts" title="pulumi_kubernetes.helm.v2.FetchOpts"><em>FetchOpts</em></a><em>]</em><em>]</em>) – Additional options to customize the
fetching of the Helm chart.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.chart">
<code class="descname">chart</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.chart" title="Permalink to this definition">¶</a></dt>
<dd><p>The chart to deploy.  If [repo] is provided, this chart name is looked up in the given repository.
Otherwise, this chart name must be a fully qualified chart URL or <code class="docutils literal notranslate"><span class="pre">repo/chartname</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.namespace">
<code class="descname">namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional namespace to install chart resources into.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.values">
<code class="descname">values</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.values" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional overrides for chart values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.transformations">
<code class="descname">transformations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.transformations" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional list of transformations to apply to resources that will be created by this chart prior to
creation. Allows customization of the chart behaviour without directly modifying the chart itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.repo">
<code class="descname">repo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.repo" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository containing the desired chart.  If not provided, [chart] must be a fully qualified
chart URL or repo/chartname.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the chart to deploy. If not provided, the latest version will be deployed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.ChartOpts.fetch_opts">
<code class="descname">fetch_opts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts.fetch_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional options to customize the fetching of the Helm chart.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">FetchOpts</code><span class="sig-paren">(</span><em>version: Optional[Union[T, Awaitable[T], Output[T]]] = None, ca_file: Optional[Union[T, Awaitable[T], Output[T]]] = None, cert_file: Optional[Union[T, Awaitable[T], Output[T]]] = None, key_file: Optional[Union[T, Awaitable[T], Output[T]]] = None, destination: Optional[Union[T, Awaitable[T], Output[T]]] = None, keyring: Optional[Union[T, Awaitable[T], Output[T]]] = None, password: Optional[Union[T, Awaitable[T], Output[T]]] = None, repo: Optional[Union[T, Awaitable[T], Output[T]]] = None, untar_dir: Optional[Union[T, Awaitable[T], Output[T]]] = None, username: Optional[Union[T, Awaitable[T], Output[T]]] = None, home: Optional[Union[T, Awaitable[T], Output[T]]] = None, devel: Optional[Union[T, Awaitable[T], Output[T]]] = None, prov: Optional[Union[T, Awaitable[T], Output[T]]] = None, untar: Optional[Union[T, Awaitable[T], Output[T]]] = None, verify: Optional[Union[T, Awaitable[T], Output[T]]] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts" title="Permalink to this definition">¶</a></dt>
<dd><p>FetchOpts is a bag of configuration options to customize the fetching of the Helm chart.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>version</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Specific version of a chart. If unset,
the latest version is fetched.</li>
<li><strong>ca_file</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Verify certificates of HTTPS-enabled
servers using this CA bundle.</li>
<li><strong>cert_file</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Identify HTTPS client using this SSL
certificate file.</li>
<li><strong>key_file</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Identify HTTPS client using this SSL
key file.</li>
<li><strong>destination</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Location to write the chart.
If this and [tardir] are specified, tardir is appended to this (default “.”).</li>
<li><strong>keyring</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Keyring containing public keys
(default “/Users/<span class="raw-html-m2r"><user></span>/.gnupg/pubring.gpg”).</li>
<li><strong>password</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Chart repository password.</li>
<li><strong>repo</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Chart repository url where to locate
the requested chart.</li>
<li><strong>untar_dir</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – If [untar] is specified, this flag
specifies the name of the directory into which the chart is
expanded (default “.”).</li>
<li><strong>username</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Chart repository username.</li>
<li><strong>home</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Location of your Helm config. Overrides
$HELM_HOME (default “/Users/<span class="raw-html-m2r"><user></span>/.helm”).</li>
<li><strong>devel</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em><em>]</em>) – Use development versions, too.
Equivalent to version ‘&gt;0.0.0-0’. If [version] is set, this is ignored.</li>
<li><strong>prov</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em><em>]</em>) – Fetch the provenance file, but don’t
perform verification.</li>
<li><strong>untar</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em><em>]</em>) – If set to false, will leave the
chart as a tarball after downloading.</li>
<li><strong>verify</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em><em>]</em>) – Verify the package against its signature.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specific version of a chart. If unset, the latest version is fetched.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.ca_file">
<code class="descname">ca_file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.ca_file" title="Permalink to this definition">¶</a></dt>
<dd><p>Verify certificates of HTTPS-enabled servers using this CA bundle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.cert_file">
<code class="descname">cert_file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.cert_file" title="Permalink to this definition">¶</a></dt>
<dd><p>Identify HTTPS client using this SSL certificate file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.key_file">
<code class="descname">key_file</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.key_file" title="Permalink to this definition">¶</a></dt>
<dd><p>Identify HTTPS client using this SSL key file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.destination">
<code class="descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Location to write the chart. If this and [tardir] are specified, tardir is appended
to this (default “.”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.keyring">
<code class="descname">keyring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.keyring" title="Permalink to this definition">¶</a></dt>
<dd><p>Keyring containing public keys (default “/Users/alex/.gnupg/pubring.gpg”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Chart repository password.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.repo">
<code class="descname">repo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.repo" title="Permalink to this definition">¶</a></dt>
<dd><p>Chart repository url where to locate the requested chart.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.untar_dir">
<code class="descname">untar_dir</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.untar_dir" title="Permalink to this definition">¶</a></dt>
<dd><p>If [untar] is specified, this flag specifies the name of the directory into which
the chart is expanded (default “.”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Chart repository username.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.home">
<code class="descname">home</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.home" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of your Helm config. Overrides $HELM_HOME (default “/Users/alex/.helm”).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.devel">
<code class="descname">devel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.devel" title="Permalink to this definition">¶</a></dt>
<dd><p>Use development versions, too. Equivalent to version ‘&gt;0.0.0-0’. If [version] is set,
this is ignored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.prov">
<code class="descname">prov</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.prov" title="Permalink to this definition">¶</a></dt>
<dd><p>Fetch the provenance file, but don’t perform verification.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.untar">
<code class="descname">untar</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.untar" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to false, will leave the chart as a tarball after downloading.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.FetchOpts.verify">
<code class="descname">verify</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts.verify" title="Permalink to this definition">¶</a></dt>
<dd><p>Verify the package against its signature.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.List">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">List</code><a class="headerlink" href="#pulumi_kubernetes.helm.v2.List" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.LocalChartOpts">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">LocalChartOpts</code><span class="sig-paren">(</span><em>path: Union[T, Awaitable[T], Output[T]], namespace: Optional[Union[T, Awaitable[T], Output[T]]] = None, values: Optional[Mapping[str, Union[T, Awaitable[T], Output[T]]]] = None, transformations: Optional[List[Callable]] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.LocalChartOpts" title="Permalink to this definition">¶</a></dt>
<dd><p>LocalChartOpts is a bag of configuration options for a local Helm chart.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path to the chart directory which contains the
<code class="docutils literal notranslate"><span class="pre">Chart.yaml</span></code> file.</li>
<li><strong>namespace</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – Optional namespace to install chart resources into.</li>
<li><strong>values</strong> (<em>Optional</em><em>[</em><em>pulumi.Inputs</em><em>]</em>) – Optional overrides for chart values.</li>
<li><strong>transformations</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="#pulumi_kubernetes.helm.v2.List" title="pulumi_kubernetes.helm.v2.List"><em>List</em></a><em>[</em><a class="reference internal" href="#pulumi_kubernetes.helm.v2.Callable" title="pulumi_kubernetes.helm.v2.Callable"><em>Callable</em></a><em>]</em><em>]</em>) – Optional list of transformations to apply to
resources that will be created by this chart prior to creation. Allows customization of the
chart behaviour without directly modifying the chart itself.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.LocalChartOpts.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.LocalChartOpts.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the chart directory which contains the <code class="docutils literal notranslate"><span class="pre">Chart.yaml</span></code> file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.LocalChartOpts.namespace">
<code class="descname">namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.LocalChartOpts.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional namespace to install chart resources into.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.LocalChartOpts.values">
<code class="descname">values</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.LocalChartOpts.values" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional overrides for chart values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kubernetes.helm.v2.LocalChartOpts.transformations">
<code class="descname">transformations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kubernetes.helm.v2.LocalChartOpts.transformations" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional list of transformations to apply to resources that will be created by this chart prior to
creation. Allows customization of the chart behaviour without directly modifying the chart itself.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_kubernetes.helm.v2.NamedTemporaryFile">
<code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">NamedTemporaryFile</code><span class="sig-paren">(</span><em>mode='w+b'</em>, <em>buffering=-1</em>, <em>encoding=None</em>, <em>newline=None</em>, <em>suffix=None</em>, <em>prefix=None</em>, <em>dir=None</em>, <em>delete=True</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.NamedTemporaryFile" title="Permalink to this definition">¶</a></dt>
<dd><p>Create and return a temporary file.
Arguments:
‘prefix’, ‘suffix’, ‘dir’ – as for mkstemp.
‘mode’ – the mode argument to io.open (default “w+b”).
‘buffering’ – the buffer size argument to io.open (default -1).
‘encoding’ – the encoding argument to io.open (default None)
‘newline’ – the newline argument to io.open (default None)
‘delete’ – whether the file is deleted on close (default True).
The file is created as mkstemp() would do it.</p>
<p>Returns an object with a file-like interface; the name of the file
is accessible as its ‘name’ attribute.  The file will be automatically
deleted when it is closed unless the ‘delete’ argument is set to False.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.TemporaryDirectory">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">TemporaryDirectory</code><span class="sig-paren">(</span><em>suffix=None</em>, <em>prefix=None</em>, <em>dir=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.TemporaryDirectory" title="Permalink to this definition">¶</a></dt>
<dd><p>Create and return a temporary directory.  This has the same
behavior as mkdtemp but can be used as a context manager.  For
example:</p>
<p>Upon exiting the context, the directory and everything contained
in it are removed.</p>
</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.Tuple">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">Tuple</code><a class="headerlink" href="#pulumi_kubernetes.helm.v2.Tuple" title="Permalink to this definition">¶</a></dt>
<dd><p>Tuple type; Tuple[X, Y] is the cross-product type of X and Y.</p>
<p>Example: Tuple[T1, T2] is a tuple of two elements corresponding
to type variables T1 and T2.  Tuple[int, float, str] is a tuple
of an int, a float and a string.</p>
<p>To specify a variable-length tuple of homogeneous type, use Tuple[T, …].</p>
</dd></dl>

</div>
