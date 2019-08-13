---
title: Module v2
---

<div class="section" id="module-pulumi_kubernetes.helm.v2">
<span id="v2"></span><h1>v2<a class="headerlink" href="#module-pulumi_kubernetes.helm.v2" title="Permalink to this headline">¶</a></h1>
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
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">ChartOpts</code><span class="sig-paren">(</span><em>chart: Union[str, Awaitable[str], Output[T]], namespace: Union[str, Awaitable[str], Output[T], None] = None, values: Optional[Mapping[str, Union[Any, Awaitable[Any], Output[T]]]] = None, transformations: Optional[List[Callable]] = None, resource_prefix: Optional[str] = None, repo: Union[str, Awaitable[str], Output[T], None] = None, version: Union[str, Awaitable[str], Output[T], None] = None, fetch_opts: Union[pulumi_kubernetes.helm.v2.helm.FetchOpts, Awaitable[pulumi_kubernetes.helm.v2.helm.FetchOpts], Output[T], None] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.ChartOpts" title="Permalink to this definition">¶</a></dt>
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
<li><strong>transformations</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>Callable</em><em>]</em>) – Optional list of transformations to apply to
resources that will be created by this chart prior to creation. Allows customization of the
chart behaviour without directly modifying the chart itself.</li>
<li><strong>resource_prefix</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional prefix for the auto-generated resource names.
Example: A resource created with resource_prefix=”foo” would produce a resource named “foo-resourceName”.</li>
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
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">FetchOpts</code><span class="sig-paren">(</span><em>version: Union[str, Awaitable[str], Output[T], None] = None, ca_file: Union[str, Awaitable[str], Output[T], None] = None, cert_file: Union[str, Awaitable[str], Output[T], None] = None, key_file: Union[str, Awaitable[str], Output[T], None] = None, destination: Union[str, Awaitable[str], Output[T], None] = None, keyring: Union[str, Awaitable[str], Output[T], None] = None, password: Union[str, Awaitable[str], Output[T], None] = None, repo: Union[str, Awaitable[str], Output[T], None] = None, untar_dir: Union[str, Awaitable[str], Output[T], None] = None, username: Union[str, Awaitable[str], Output[T], None] = None, home: Union[str, Awaitable[str], Output[T], None] = None, devel: Union[bool, Awaitable[bool], Output[T], None] = None, prov: Union[bool, Awaitable[bool], Output[T], None] = None, untar: Union[bool, Awaitable[bool], Output[T], None] = None, verify: Union[bool, Awaitable[bool], Output[T], None] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.FetchOpts" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kubernetes.helm.v2.LocalChartOpts">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">LocalChartOpts</code><span class="sig-paren">(</span><em>path: Union[str, Awaitable[str], Output[T]], namespace: Union[str, Awaitable[str], Output[T], None] = None, values: Optional[Mapping[str, Union[Any, Awaitable[Any], Output[T]]]] = None, transformations: Optional[List[Callable]] = None, resource_prefix: Optional[str] = None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.LocalChartOpts" title="Permalink to this definition">¶</a></dt>
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
<li><strong>transformations</strong> (<em>Optional</em><em>[</em><em>List</em><em>[</em><em>Callable</em><em>]</em><em>]</em>) – Optional list of transformations to apply to
resources that will be created by this chart prior to creation. Allows customization of the
chart behaviour without directly modifying the chart itself.</li>
<li><strong>resource_prefix</strong> (<em>Optional</em><em>[</em><em>str</em><em>]</em>) – An optional prefix for the auto-generated resource names.
Example: A resource created with resource_prefix=”foo” would produce a resource named “foo-resourceName”.</li>
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

</dd></dl>

<dl class="class">
<dt id="pulumi_kubernetes.helm.v2.TextIO">
<em class="property">class </em><code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">TextIO</code><a class="headerlink" href="#pulumi_kubernetes.helm.v2.TextIO" title="Permalink to this definition">¶</a></dt>
<dd><p>Typed version of the return of open() in text mode.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_kubernetes.helm.v2.mkdtemp">
<code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">mkdtemp</code><span class="sig-paren">(</span><em>suffix=None</em>, <em>prefix=None</em>, <em>dir=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.mkdtemp" title="Permalink to this definition">¶</a></dt>
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
<code class="descclassname">pulumi_kubernetes.helm.v2.</code><code class="descname">mkstemp</code><span class="sig-paren">(</span><em>suffix=None</em>, <em>prefix=None</em>, <em>dir=None</em>, <em>text=False</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.helm.v2.mkstemp" title="Permalink to this definition">¶</a></dt>
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
