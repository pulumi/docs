---
title: Package pulumi_docker
title_tag: Package pulumi_docker | Python SDK
linktitle: pulumi_docker
notitle: true
---

<div class="section" id="pulumi-docker">
<h1>Pulumi Docker<a class="headerlink" href="#pulumi-docker" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-docker">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-docker/issues">pulumi/pulumi-docker repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-docker/issues">terraform-providers/terraform-provider-docker repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_docker"></span><dl class="py class">
<dt id="pulumi_docker.AwaitableGetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">AwaitableGetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.AwaitableGetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_docker.AwaitableGetRegistryImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">AwaitableGetRegistryImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sha256_digest</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.AwaitableGetRegistryImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_docker.Container">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Container</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attach</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capabilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">command</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_set</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_shares</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destroy_grace_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_searches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domainname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entrypoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">envs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_adds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthcheck</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipc_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">links</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retry_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory_swap</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mounts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">must_run</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_aliases</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks_advanced</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pid_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileged</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">publish_all_ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restart</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shm_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sysctls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tmpfs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ulimits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uploads</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">userns_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">working_dir</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Container" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the lifecycle of a Docker container.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attach</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true attach to the container after its creation and waits the end of his execution.</p></li>
<li><p><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See Capabilities below for details.</p></li>
<li><p><strong>command</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The command to use to start the
container. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span> <span class="pre">-f</span> <span class="pre">baz.conf</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;baz.conf&quot;]</span></code>.</p></li>
<li><p><strong>cpu_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. <code class="docutils literal notranslate"><span class="pre">0-1</span></code>.</p></li>
<li><p><strong>cpu_shares</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – CPU shares (relative weight) for the container.</p></li>
<li><p><strong>destroy_grace_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If defined will attempt to stop the container before destroying. Container will be destroyed after <code class="docutils literal notranslate"><span class="pre">n</span></code> seconds or on successful stop.</p></li>
<li><p><strong>devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Devices below for details.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of DNS servers.</p></li>
<li><p><strong>dns_opts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of DNS options used by the DNS provider(s), see <code class="docutils literal notranslate"><span class="pre">resolv.conf</span></code> documentation for valid list of options.</p></li>
<li><p><strong>dns_searches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.</p></li>
<li><p><strong>domainname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name of the container.</p></li>
<li><p><strong>entrypoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span></code>
when starting a container, set the entrypoint to be
<code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;]</span></code>.</p></li>
<li><p><strong>envs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Environment variables to set.</p></li>
<li><p><strong>group_adds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Add additional groups to run as.</p></li>
<li><p><strong>healthcheck</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See Healthcheck below for details.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hostname of the container.</p></li>
<li><p><strong>hosts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Hostname to add.</p></li>
<li><p><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the image to back this container.
The easiest way to get this value is to use the <code class="docutils literal notranslate"><span class="pre">.RemoteImage</span></code> resource
as is shown in the example above.</p></li>
<li><p><strong>ipc_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IPC sharing mode for the container. Possible values are: <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">shareable</span></code>, <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Adding labels.</p></li>
<li><p><strong>links</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of links for link based
connectivity between containers that are running on the same host.</p></li>
<li><p><strong>log_driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The logging driver to use for the container.
Defaults to “json-file”.</p></li>
<li><p><strong>log_opts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/value pairs to use as options for
the logging driver.</p></li>
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Save the container logs (<code class="docutils literal notranslate"><span class="pre">attach</span></code> must be enabled).</p></li>
<li><p><strong>max_retry_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum amount of times to an attempt
a restart when <code class="docutils literal notranslate"><span class="pre">restart</span></code> is set to “on-failure”</p></li>
<li><p><strong>memory</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The memory limit for the container in MBs.</p></li>
<li><p><strong>mounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Mounts below for details.</p></li>
<li><p><strong>network_aliases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Network aliases of the container for user-defined networks only. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p></li>
<li><p><strong>network_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network mode of the container.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Id of the networks in which the
container is. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p></li>
<li><p><strong>networks_advanced</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Networks Advanced below for details. If this block has priority to the deprecated <code class="docutils literal notranslate"><span class="pre">network_alias</span></code> and <code class="docutils literal notranslate"><span class="pre">network</span></code> properties.</p></li>
<li><p><strong>pid_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PID (Process) Namespace mode for the container. Either <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p></li>
<li><p><strong>ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Ports below for details.</p></li>
<li><p><strong>privileged</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Run container in privileged mode.</p></li>
<li><p><strong>publish_all_ports</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Publish all ports of the container.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, this volume will be readonly.
Defaults to false.</p></li>
<li><p><strong>restart</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The restart policy for the container. Must be
one of “no”, “on-failure”, “always”, “unless-stopped”.</p></li>
<li><p><strong>shm_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of <code class="docutils literal notranslate"><span class="pre">/dev/shm</span></code> in MBs.</p></li>
<li><p><strong>start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, then the Docker container will be
started after creation. If false, then the container is only created.</p></li>
<li><p><strong>sysctls</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of kernel parameters (sysctls) to set in the container.</p></li>
<li><p><strong>tmpfs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of container directories which should be replaced by <code class="docutils literal notranslate"><span class="pre">tmpfs</span> <span class="pre">mounts</span></code>, and their corresponding mount options.</p></li>
<li><p><strong>ulimits</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Ulimits below for
details.</p></li>
<li><p><strong>uploads</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See File Upload below for details.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User used for run the first process. Format is
<code class="docutils literal notranslate"><span class="pre">user</span></code> or <code class="docutils literal notranslate"><span class="pre">user:group</span></code> which user and group can be passed literraly or
by name.</p></li>
<li><p><strong>userns_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the usernamespace mode for the container when usernamespace remapping option is enabled.</p></li>
<li><p><strong>volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Volumes below for details.</p></li>
<li><p><strong>working_dir</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The working directory for commands to run in</p></li>
</ul>
</dd>
</dl>
<p>The <strong>capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - list of linux capabilities to add.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - list of linux capabilities to drop.</p></li>
</ul>
<p>The <strong>devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path in the container where the
device will be binded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path on the host where the device
is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The cgroup permissions given to the
container to access the device.
Defaults to <code class="docutils literal notranslate"><span class="pre">rwm</span></code>.</p></li>
</ul>
<p>The <strong>healthcheck</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Time between running the check <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Consecutive failures needed to report unhealthy. Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Start period for the container to initialize before counting retries towards unstable <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Command to run to check health. For example, to run <code class="docutils literal notranslate"><span class="pre">curl</span> <span class="pre">-f</span> <span class="pre">http://localhost/health</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;CMD&quot;,</span> <span class="pre">&quot;curl&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;http://localhost/health&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum time to allow one check to run <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
</ul>
<p>The <strong>hosts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Hostname to add.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IP address this hostname should resolve to.</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
<p>The <strong>mounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bindOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">bind</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">propagation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A propagation mode with the value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, this volume will be readonly.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mount source (e.g., a volume name, a host path)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmpfsOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">tmpf</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The permission mode for the tmpfs mount in an integer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size for the tmpfs mount in bytes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mount type: valid values are <code class="docutils literal notranslate"><span class="pre">bind|volume|tmpfs</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">volume</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">driverOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Options for the driver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Adding labels.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">noCopy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to populate volume with data from the target.</p></li>
</ul>
</li>
</ul>
<p>The <strong>networks_advanced</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aliases</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The network aliases of the container in the specific network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IPV4 address of the container in the specific network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IPV6 address of the container in the specific network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the network.</p></li>
</ul>
<p>The <strong>ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">external</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Port exposed out of the container. If not given a free random port <code class="docutils literal notranslate"><span class="pre">&gt;=</span> <span class="pre">32768</span></code> will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">internal</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Port within the container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IP address this hostname should resolve to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Protocol that can be used over this port,
defaults to <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
</ul>
<p>The <strong>ulimits</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hard</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">soft</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>uploads</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentBase64</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">executable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, the file will be uploaded with user
executable permission.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - path to a file in the container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A filename that references a file which will be uploaded as the object content. This allows for large file uploads that do not get stored in state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If using <code class="docutils literal notranslate"><span class="pre">source</span></code>, this will force an update if the file content has updated but the filename has not.</p></li>
</ul>
<p>The <strong>volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path in the container where the
device will be binded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromContainer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container where the volume is
coming from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path on the host where the device
is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, this volume will be readonly.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the docker volume which
should be mounted.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_docker.Container.attach">
<code class="sig-name descname">attach</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.attach" title="Permalink to this definition">¶</a></dt>
<dd><p>If true attach to the container after its creation and waits the end of his execution.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.bridge">
<code class="sig-name descname">bridge</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.bridge" title="Permalink to this definition">¶</a></dt>
<dd><p>The network bridge of the container as read from its NetworkSettings.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.capabilities">
<code class="sig-name descname">capabilities</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>See Capabilities below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - list of linux capabilities to add.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drops</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - list of linux capabilities to drop.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.command">
<code class="sig-name descname">command</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.command" title="Permalink to this definition">¶</a></dt>
<dd><p>The command to use to start the
container. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span> <span class="pre">-f</span> <span class="pre">baz.conf</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;baz.conf&quot;]</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.container_logs">
<code class="sig-name descname">container_logs</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.container_logs" title="Permalink to this definition">¶</a></dt>
<dd><p>The logs of the container if its execution is done (<code class="docutils literal notranslate"><span class="pre">attach</span></code> must be disabled).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.cpu_set">
<code class="sig-name descname">cpu_set</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.cpu_set" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. <code class="docutils literal notranslate"><span class="pre">0-1</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.cpu_shares">
<code class="sig-name descname">cpu_shares</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.cpu_shares" title="Permalink to this definition">¶</a></dt>
<dd><p>CPU shares (relative weight) for the container.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.destroy_grace_seconds">
<code class="sig-name descname">destroy_grace_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.destroy_grace_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>If defined will attempt to stop the container before destroying. Container will be destroyed after <code class="docutils literal notranslate"><span class="pre">n</span></code> seconds or on successful stop.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.devices">
<code class="sig-name descname">devices</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.devices" title="Permalink to this definition">¶</a></dt>
<dd><p>See Devices below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path in the container where the
device will be binded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path on the host where the device
is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The cgroup permissions given to the
container to access the device.
Defaults to <code class="docutils literal notranslate"><span class="pre">rwm</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.dns">
<code class="sig-name descname">dns</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.dns" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of DNS servers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.dns_opts">
<code class="sig-name descname">dns_opts</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.dns_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of DNS options used by the DNS provider(s), see <code class="docutils literal notranslate"><span class="pre">resolv.conf</span></code> documentation for valid list of options.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.dns_searches">
<code class="sig-name descname">dns_searches</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.dns_searches" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.domainname">
<code class="sig-name descname">domainname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.domainname" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name of the container.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.entrypoints">
<code class="sig-name descname">entrypoints</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.entrypoints" title="Permalink to this definition">¶</a></dt>
<dd><p>The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span></code>
when starting a container, set the entrypoint to be
<code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;]</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.envs">
<code class="sig-name descname">envs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.envs" title="Permalink to this definition">¶</a></dt>
<dd><p>Environment variables to set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.exit_code">
<code class="sig-name descname">exit_code</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.exit_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The exit code of the container if its execution is done (<code class="docutils literal notranslate"><span class="pre">must_run</span></code> must be disabled).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.gateway">
<code class="sig-name descname">gateway</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The network gateway of the container as read from its
NetworkSettings.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.group_adds">
<code class="sig-name descname">group_adds</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.group_adds" title="Permalink to this definition">¶</a></dt>
<dd><p>Add additional groups to run as.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.healthcheck">
<code class="sig-name descname">healthcheck</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.healthcheck" title="Permalink to this definition">¶</a></dt>
<dd><p>See Healthcheck below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Time between running the check <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Consecutive failures needed to report unhealthy. Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Start period for the container to initialize before counting retries towards unstable <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tests</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Command to run to check health. For example, to run <code class="docutils literal notranslate"><span class="pre">curl</span> <span class="pre">-f</span> <span class="pre">http://localhost/health</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;CMD&quot;,</span> <span class="pre">&quot;curl&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;http://localhost/health&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Maximum time to allow one check to run <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.hostname">
<code class="sig-name descname">hostname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>Hostname of the container.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.hosts">
<code class="sig-name descname">hosts</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.hosts" title="Permalink to this definition">¶</a></dt>
<dd><p>Hostname to add.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Hostname to add.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - IP address this hostname should resolve to.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.image">
<code class="sig-name descname">image</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.image" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the image to back this container.
The easiest way to get this value is to use the <code class="docutils literal notranslate"><span class="pre">.RemoteImage</span></code> resource
as is shown in the example above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.ip_address">
<code class="sig-name descname">ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP address of the container’s first network it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.ip_prefix_length">
<code class="sig-name descname">ip_prefix_length</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.ip_prefix_length" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP prefix length of the container as read from its
NetworkSettings.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.ipc_mode">
<code class="sig-name descname">ipc_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.ipc_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>IPC sharing mode for the container. Possible values are: <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">shareable</span></code>, <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Adding labels.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the label</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.links">
<code class="sig-name descname">links</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.links" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of links for link based
connectivity between containers that are running on the same host.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.log_driver">
<code class="sig-name descname">log_driver</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.log_driver" title="Permalink to this definition">¶</a></dt>
<dd><p>The logging driver to use for the container.
Defaults to “json-file”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.log_opts">
<code class="sig-name descname">log_opts</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.log_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/value pairs to use as options for
the logging driver.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.logs">
<code class="sig-name descname">logs</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>Save the container logs (<code class="docutils literal notranslate"><span class="pre">attach</span></code> must be enabled).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.max_retry_count">
<code class="sig-name descname">max_retry_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.max_retry_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of times to an attempt
a restart when <code class="docutils literal notranslate"><span class="pre">restart</span></code> is set to “on-failure”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.memory">
<code class="sig-name descname">memory</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.memory" title="Permalink to this definition">¶</a></dt>
<dd><p>The memory limit for the container in MBs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.mounts">
<code class="sig-name descname">mounts</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.mounts" title="Permalink to this definition">¶</a></dt>
<dd><p>See Mounts below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bindOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">bind</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">propagation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A propagation mode with the value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true, this volume will be readonly.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The mount source (e.g., a volume name, a host path)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The container path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmpfsOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">tmpf</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The permission mode for the tmpfs mount in an integer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size for the tmpfs mount in bytes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The mount type: valid values are <code class="docutils literal notranslate"><span class="pre">bind|volume|tmpfs</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">volume</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">driverOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Options for the driver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Adding labels.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the label</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">noCopy</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to populate volume with data from the target.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.network_aliases">
<code class="sig-name descname">network_aliases</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.network_aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>Network aliases of the container for user-defined networks only. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.network_datas">
<code class="sig-name descname">network_datas</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.network_datas" title="Permalink to this definition">¶</a></dt>
<dd><p>(Map of a block) The IP addresses of the container on each
network. Key are the network names, values are the IP addresses.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gateway</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The network gateway of the container as read from its
NetworkSettings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP address of the container’s first network it.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_prefix_length</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP prefix length of the container as read from its
NetworkSettings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.network_mode">
<code class="sig-name descname">network_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.network_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Network mode of the container.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.networks">
<code class="sig-name descname">networks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the networks in which the
container is. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.networks_advanced">
<code class="sig-name descname">networks_advanced</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.networks_advanced" title="Permalink to this definition">¶</a></dt>
<dd><p>See Networks Advanced below for details. If this block has priority to the deprecated <code class="docutils literal notranslate"><span class="pre">network_alias</span></code> and <code class="docutils literal notranslate"><span class="pre">network</span></code> properties.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aliases</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The network aliases of the container in the specific network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IPV4 address of the container in the specific network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6Address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IPV6 address of the container in the specific network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the network.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.pid_mode">
<code class="sig-name descname">pid_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.pid_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The PID (Process) Namespace mode for the container. Either <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.ports">
<code class="sig-name descname">ports</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.ports" title="Permalink to this definition">¶</a></dt>
<dd><p>See Ports below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">external</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Port exposed out of the container. If not given a free random port <code class="docutils literal notranslate"><span class="pre">&gt;=</span> <span class="pre">32768</span></code> will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">internal</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Port within the container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - IP address this hostname should resolve to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Protocol that can be used over this port,
defaults to <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.privileged">
<code class="sig-name descname">privileged</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.privileged" title="Permalink to this definition">¶</a></dt>
<dd><p>Run container in privileged mode.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.publish_all_ports">
<code class="sig-name descname">publish_all_ports</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.publish_all_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>Publish all ports of the container.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.read_only">
<code class="sig-name descname">read_only</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, this volume will be readonly.
Defaults to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.restart">
<code class="sig-name descname">restart</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.restart" title="Permalink to this definition">¶</a></dt>
<dd><p>The restart policy for the container. Must be
one of “no”, “on-failure”, “always”, “unless-stopped”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.shm_size">
<code class="sig-name descname">shm_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.shm_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of <code class="docutils literal notranslate"><span class="pre">/dev/shm</span></code> in MBs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.start">
<code class="sig-name descname">start</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.start" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, then the Docker container will be
started after creation. If false, then the container is only created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.sysctls">
<code class="sig-name descname">sysctls</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.sysctls" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of kernel parameters (sysctls) to set in the container.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.tmpfs">
<code class="sig-name descname">tmpfs</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.tmpfs" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of container directories which should be replaced by <code class="docutils literal notranslate"><span class="pre">tmpfs</span> <span class="pre">mounts</span></code>, and their corresponding mount options.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.ulimits">
<code class="sig-name descname">ulimits</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.ulimits" title="Permalink to this definition">¶</a></dt>
<dd><p>See Ulimits below for
details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hard</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">soft</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.uploads">
<code class="sig-name descname">uploads</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.uploads" title="Permalink to this definition">¶</a></dt>
<dd><p>See File Upload below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentBase64</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">executable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true, the file will be uploaded with user
executable permission.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - path to a file in the container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A filename that references a file which will be uploaded as the object content. This allows for large file uploads that do not get stored in state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceHash</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If using <code class="docutils literal notranslate"><span class="pre">source</span></code>, this will force an update if the file content has updated but the filename has not.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.user">
<code class="sig-name descname">user</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.user" title="Permalink to this definition">¶</a></dt>
<dd><p>User used for run the first process. Format is
<code class="docutils literal notranslate"><span class="pre">user</span></code> or <code class="docutils literal notranslate"><span class="pre">user:group</span></code> which user and group can be passed literraly or
by name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.userns_mode">
<code class="sig-name descname">userns_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.userns_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the usernamespace mode for the container when usernamespace remapping option is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.volumes">
<code class="sig-name descname">volumes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.volumes" title="Permalink to this definition">¶</a></dt>
<dd><p>See Volumes below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path in the container where the
device will be binded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromContainer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The container where the volume is
coming from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path on the host where the device
is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If true, this volume will be readonly.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the docker volume which
should be mounted.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Container.working_dir">
<code class="sig-name descname">working_dir</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Container.working_dir" title="Permalink to this definition">¶</a></dt>
<dd><p>The working directory for commands to run in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attach</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bridge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capabilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">command</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_set</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_shares</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destroy_grace_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_searches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domainname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entrypoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">envs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exit_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_adds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthcheck</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_prefix_length</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipc_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">links</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retry_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory_swap</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mounts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">must_run</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_aliases</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_datas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks_advanced</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pid_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileged</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">publish_all_ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restart</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shm_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sysctls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tmpfs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ulimits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uploads</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">userns_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">working_dir</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Container.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Container resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attach</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true attach to the container after its creation and waits the end of his execution.</p></li>
<li><p><strong>bridge</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network bridge of the container as read from its NetworkSettings.</p></li>
<li><p><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See Capabilities below for details.</p></li>
<li><p><strong>command</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The command to use to start the
container. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span> <span class="pre">-f</span> <span class="pre">baz.conf</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;baz.conf&quot;]</span></code>.</p></li>
<li><p><strong>container_logs</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The logs of the container if its execution is done (<code class="docutils literal notranslate"><span class="pre">attach</span></code> must be disabled).</p></li>
<li><p><strong>cpu_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. <code class="docutils literal notranslate"><span class="pre">0-1</span></code>.</p></li>
<li><p><strong>cpu_shares</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – CPU shares (relative weight) for the container.</p></li>
<li><p><strong>destroy_grace_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If defined will attempt to stop the container before destroying. Container will be destroyed after <code class="docutils literal notranslate"><span class="pre">n</span></code> seconds or on successful stop.</p></li>
<li><p><strong>devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Devices below for details.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of DNS servers.</p></li>
<li><p><strong>dns_opts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of DNS options used by the DNS provider(s), see <code class="docutils literal notranslate"><span class="pre">resolv.conf</span></code> documentation for valid list of options.</p></li>
<li><p><strong>dns_searches</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.</p></li>
<li><p><strong>domainname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name of the container.</p></li>
<li><p><strong>entrypoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span></code>
when starting a container, set the entrypoint to be
<code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;]</span></code>.</p></li>
<li><p><strong>envs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Environment variables to set.</p></li>
<li><p><strong>exit_code</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The exit code of the container if its execution is done (<code class="docutils literal notranslate"><span class="pre">must_run</span></code> must be disabled).</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The network gateway of the container as read from its
NetworkSettings.</p></li>
<li><p><strong>group_adds</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Add additional groups to run as.</p></li>
<li><p><strong>healthcheck</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See Healthcheck below for details.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hostname of the container.</p></li>
<li><p><strong>hosts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Hostname to add.</p></li>
<li><p><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the image to back this container.
The easiest way to get this value is to use the <code class="docutils literal notranslate"><span class="pre">.RemoteImage</span></code> resource
as is shown in the example above.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP address of the container’s first network it.</p></li>
<li><p><strong>ip_prefix_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP prefix length of the container as read from its
NetworkSettings.</p></li>
<li><p><strong>ipc_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IPC sharing mode for the container. Possible values are: <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">shareable</span></code>, <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Adding labels.</p></li>
<li><p><strong>links</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set of links for link based
connectivity between containers that are running on the same host.</p></li>
<li><p><strong>log_driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The logging driver to use for the container.
Defaults to “json-file”.</p></li>
<li><p><strong>log_opts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/value pairs to use as options for
the logging driver.</p></li>
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Save the container logs (<code class="docutils literal notranslate"><span class="pre">attach</span></code> must be enabled).</p></li>
<li><p><strong>max_retry_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum amount of times to an attempt
a restart when <code class="docutils literal notranslate"><span class="pre">restart</span></code> is set to “on-failure”</p></li>
<li><p><strong>memory</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The memory limit for the container in MBs.</p></li>
<li><p><strong>mounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Mounts below for details.</p></li>
<li><p><strong>network_aliases</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Network aliases of the container for user-defined networks only. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p></li>
<li><p><strong>network_datas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – (Map of a block) The IP addresses of the container on each
network. Key are the network names, values are the IP addresses.</p></li>
<li><p><strong>network_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network mode of the container.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Id of the networks in which the
container is. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p></li>
<li><p><strong>networks_advanced</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Networks Advanced below for details. If this block has priority to the deprecated <code class="docutils literal notranslate"><span class="pre">network_alias</span></code> and <code class="docutils literal notranslate"><span class="pre">network</span></code> properties.</p></li>
<li><p><strong>pid_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PID (Process) Namespace mode for the container. Either <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p></li>
<li><p><strong>ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Ports below for details.</p></li>
<li><p><strong>privileged</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Run container in privileged mode.</p></li>
<li><p><strong>publish_all_ports</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Publish all ports of the container.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, this volume will be readonly.
Defaults to false.</p></li>
<li><p><strong>restart</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The restart policy for the container. Must be
one of “no”, “on-failure”, “always”, “unless-stopped”.</p></li>
<li><p><strong>shm_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of <code class="docutils literal notranslate"><span class="pre">/dev/shm</span></code> in MBs.</p></li>
<li><p><strong>start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, then the Docker container will be
started after creation. If false, then the container is only created.</p></li>
<li><p><strong>sysctls</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of kernel parameters (sysctls) to set in the container.</p></li>
<li><p><strong>tmpfs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of container directories which should be replaced by <code class="docutils literal notranslate"><span class="pre">tmpfs</span> <span class="pre">mounts</span></code>, and their corresponding mount options.</p></li>
<li><p><strong>ulimits</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Ulimits below for
details.</p></li>
<li><p><strong>uploads</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See File Upload below for details.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User used for run the first process. Format is
<code class="docutils literal notranslate"><span class="pre">user</span></code> or <code class="docutils literal notranslate"><span class="pre">user:group</span></code> which user and group can be passed literraly or
by name.</p></li>
<li><p><strong>userns_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the usernamespace mode for the container when usernamespace remapping option is enabled.</p></li>
<li><p><strong>volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Volumes below for details.</p></li>
<li><p><strong>working_dir</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The working directory for commands to run in</p></li>
</ul>
</dd>
</dl>
<p>The <strong>capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - list of linux capabilities to add.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - list of linux capabilities to drop.</p></li>
</ul>
<p>The <strong>devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path in the container where the
device will be binded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path on the host where the device
is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">permissions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The cgroup permissions given to the
container to access the device.
Defaults to <code class="docutils literal notranslate"><span class="pre">rwm</span></code>.</p></li>
</ul>
<p>The <strong>healthcheck</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Time between running the check <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Consecutive failures needed to report unhealthy. Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Start period for the container to initialize before counting retries towards unstable <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Command to run to check health. For example, to run <code class="docutils literal notranslate"><span class="pre">curl</span> <span class="pre">-f</span> <span class="pre">http://localhost/health</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;CMD&quot;,</span> <span class="pre">&quot;curl&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;http://localhost/health&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum time to allow one check to run <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
</ul>
<p>The <strong>hosts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Hostname to add.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IP address this hostname should resolve to.</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
<p>The <strong>mounts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bindOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">bind</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">propagation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A propagation mode with the value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, this volume will be readonly.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mount source (e.g., a volume name, a host path)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmpfsOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">tmpf</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The permission mode for the tmpfs mount in an integer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size for the tmpfs mount in bytes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mount type: valid values are <code class="docutils literal notranslate"><span class="pre">bind|volume|tmpfs</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">volume</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">driverOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Options for the driver.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Adding labels.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">noCopy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to populate volume with data from the target.</p></li>
</ul>
</li>
</ul>
<p>The <strong>network_datas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gateway</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The network gateway of the container as read from its
NetworkSettings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP address of the container’s first network it.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_prefix_length</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP prefix length of the container as read from its
NetworkSettings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>networks_advanced</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aliases</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The network aliases of the container in the specific network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IPV4 address of the container in the specific network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv6Address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IPV6 address of the container in the specific network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the network.</p></li>
</ul>
<p>The <strong>ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">external</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Port exposed out of the container. If not given a free random port <code class="docutils literal notranslate"><span class="pre">&gt;=</span> <span class="pre">32768</span></code> will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">internal</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Port within the container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IP address this hostname should resolve to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Protocol that can be used over this port,
defaults to <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
</ul>
<p>The <strong>ulimits</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hard</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">soft</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>uploads</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contentBase64</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">executable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, the file will be uploaded with user
executable permission.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - path to a file in the container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A filename that references a file which will be uploaded as the object content. This allows for large file uploads that do not get stored in state.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceHash</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If using <code class="docutils literal notranslate"><span class="pre">source</span></code>, this will force an update if the file content has updated but the filename has not.</p></li>
</ul>
<p>The <strong>volumes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path in the container where the
device will be binded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fromContainer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container where the volume is
coming from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path on the host where the device
is located.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If true, this volume will be readonly.
Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the docker volume which
should be mounted.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Container.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.Container.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Container.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.GetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">GetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.GetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetwork.</p>
<dl class="py attribute">
<dt id="pulumi_docker.GetNetworkResult.driver">
<code class="sig-name descname">driver</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.GetNetworkResult.driver" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional, string) The driver of the Docker network. 
Possible values are <code class="docutils literal notranslate"><span class="pre">bridge</span></code>, <code class="docutils literal notranslate"><span class="pre">host</span></code>, <code class="docutils literal notranslate"><span class="pre">overlay</span></code>, <code class="docutils literal notranslate"><span class="pre">macvlan</span></code>.
See [docker docs][networkdocs] for more details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.GetNetworkResult.options">
<code class="sig-name descname">options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.GetNetworkResult.options" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional, map) Only available with bridge networks. See
[docker docs][bridgeoptionsdocs] for more details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">internal</span></code> (Optional, bool) Boolean flag for whether the network is internal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipam_config</span></code> (Optional, map) See IPAM below for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (Optional, string) Scope of the network. One of <code class="docutils literal notranslate"><span class="pre">swarm</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>, or <code class="docutils literal notranslate"><span class="pre">local</span></code>.</p></li>
</ul>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_docker.GetRegistryImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">GetRegistryImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sha256_digest</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.GetRegistryImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryImage.</p>
<dl class="py attribute">
<dt id="pulumi_docker.GetRegistryImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.GetRegistryImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_docker.Network">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attachable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_duplicate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ingress</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Network" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Docker Network. This can be used alongside
<a class="reference external" href="https://www.terraform.io/docs/providers/docker/r/container.html">docker_container</a>
to create virtual networks within the docker environment.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attachable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable manual container attachment to the network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>check_duplicate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Requests daemon to check for networks
with same name.</p></li>
<li><p><strong>driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the network driver to use. Defaults to
<code class="docutils literal notranslate"><span class="pre">bridge</span></code> driver.</p></li>
<li><p><strong>ingress</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Create swarm routing-mesh network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>internal</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Restrict external access to the network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ipam_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See IPAM config below for
details.</p></li>
<li><p><strong>ipam_driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Driver used by the custom IP scheme of the
network.</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable IPv6 networking.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Labels below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker network.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Network specific options to be used by
the drivers.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ipam_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auxAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gateway</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_docker.Network.attachable">
<code class="sig-name descname">attachable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.attachable" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable manual container attachment to the network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Network.check_duplicate">
<code class="sig-name descname">check_duplicate</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.check_duplicate" title="Permalink to this definition">¶</a></dt>
<dd><p>Requests daemon to check for networks
with same name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Network.driver">
<code class="sig-name descname">driver</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.driver" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the network driver to use. Defaults to
<code class="docutils literal notranslate"><span class="pre">bridge</span></code> driver.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Network.ingress">
<code class="sig-name descname">ingress</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.ingress" title="Permalink to this definition">¶</a></dt>
<dd><p>Create swarm routing-mesh network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Network.internal">
<code class="sig-name descname">internal</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.internal" title="Permalink to this definition">¶</a></dt>
<dd><p>Restrict external access to the network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Network.ipam_configs">
<code class="sig-name descname">ipam_configs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.ipam_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>See IPAM config below for
details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auxAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gateway</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRange</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Network.ipam_driver">
<code class="sig-name descname">ipam_driver</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.ipam_driver" title="Permalink to this definition">¶</a></dt>
<dd><p>Driver used by the custom IP scheme of the
network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Network.ipv6">
<code class="sig-name descname">ipv6</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable IPv6 networking.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Network.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>See Labels below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the label</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Network.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Network.options">
<code class="sig-name descname">options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Network.options" title="Permalink to this definition">¶</a></dt>
<dd><p>Network specific options to be used by
the drivers.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attachable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_duplicate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ingress</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Network.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Network resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attachable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable manual container attachment to the network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>check_duplicate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Requests daemon to check for networks
with same name.</p></li>
<li><p><strong>driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the network driver to use. Defaults to
<code class="docutils literal notranslate"><span class="pre">bridge</span></code> driver.</p></li>
<li><p><strong>ingress</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Create swarm routing-mesh network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>internal</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Restrict external access to the network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>ipam_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See IPAM config below for
details.</p></li>
<li><p><strong>ipam_driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Driver used by the custom IP scheme of the
network.</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable IPv6 networking.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Labels below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker network.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Network specific options to be used by
the drivers.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ipam_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auxAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gateway</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Network.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.Network.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Network.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_material</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert_material</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_material</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the docker package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ca_material</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded content of Docker host CA certificate</p></li>
<li><p><strong>cert_material</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded content of Docker client certificate</p></li>
<li><p><strong>cert_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to directory with Docker TLS config</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Docker daemon address</p></li>
<li><p><strong>key_material</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM-encoded content of Docker client private key</p></li>
</ul>
</dd>
</dl>
<p>The <strong>registry_auth</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configFile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configFileContent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py method">
<dt id="pulumi_docker.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.RemoteImage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">RemoteImage</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_locally</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_triggers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.RemoteImage" title="Permalink to this definition">¶</a></dt>
<dd><p>Pulls a Docker image to a given Docker host from a Docker Registry.</p>
<p>This resource will <em>not</em> pull new layers of the image automatically unless used in
conjunction with <cite>`</cite>.getRegistryImage`` &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/docker/d/registry_image.html">https://www.terraform.io/docs/providers/docker/d/registry_image.html</a>&gt;`_
data source to update the <code class="docutils literal notranslate"><span class="pre">pull_triggers</span></code> field.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>keep_locally</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, then the Docker image won’t be
deleted on destroy operation. If this is false, it will delete the image from
the docker local storage on destroy operation.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker image, including any tags or SHA256 repo digests.</p></li>
<li><p><strong>pull_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>Deprecated</strong>, use <code class="docutils literal notranslate"><span class="pre">pull_triggers</span></code> instead.</p></li>
<li><p><strong>pull_triggers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of values which cause an
image pull when changed. This is used to store the image digest from the
registry when using the <code class="docutils literal notranslate"><span class="pre">.getRegistryImage</span></code> <a class="reference external" href="https://www.terraform.io/docs/providers/docker/d/registry_image.html">data source</a>
to trigger an image update.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_docker.RemoteImage.keep_locally">
<code class="sig-name descname">keep_locally</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.RemoteImage.keep_locally" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, then the Docker image won’t be
deleted on destroy operation. If this is false, it will delete the image from
the docker local storage on destroy operation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.RemoteImage.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.RemoteImage.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker image, including any tags or SHA256 repo digests.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.RemoteImage.pull_trigger">
<code class="sig-name descname">pull_trigger</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.RemoteImage.pull_trigger" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>Deprecated</strong>, use <code class="docutils literal notranslate"><span class="pre">pull_triggers</span></code> instead.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.RemoteImage.pull_triggers">
<code class="sig-name descname">pull_triggers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.RemoteImage.pull_triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of values which cause an
image pull when changed. This is used to store the image digest from the
registry when using the <code class="docutils literal notranslate"><span class="pre">.getRegistryImage</span></code> <a class="reference external" href="https://www.terraform.io/docs/providers/docker/d/registry_image.html">data source</a>
to trigger an image update.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.RemoteImage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_locally</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_triggers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.RemoteImage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RemoteImage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>keep_locally</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, then the Docker image won’t be
deleted on destroy operation. If this is false, it will delete the image from
the docker local storage on destroy operation.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker image, including any tags or SHA256 repo digests.</p></li>
<li><p><strong>pull_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>Deprecated</strong>, use <code class="docutils literal notranslate"><span class="pre">pull_triggers</span></code> instead.</p></li>
<li><p><strong>pull_triggers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>List of values which cause an
image pull when changed. This is used to store the image digest from the
registry when using the <code class="docutils literal notranslate"><span class="pre">.getRegistryImage</span></code> <a class="reference external" href="https://www.terraform.io/docs/providers/docker/d/registry_image.html">data source</a>
to trigger an image update.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.RemoteImage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.RemoteImage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.RemoteImage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.RemoteImage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.Secret">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Secret</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the secrets of a Docker service in a swarm.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64 encoded data of the secret.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Labels below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker secret.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_docker.Secret.data">
<code class="sig-name descname">data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Secret.data" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64 encoded data of the secret.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Secret.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Secret.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>See Labels below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the label</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Secret.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Secret.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker secret.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Secret.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Secret.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Secret resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64 encoded data of the secret.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Labels below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker secret.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Secret.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Secret.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.Secret.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Secret.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">converge_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rollback_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Service resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] auth: See Auth below for details.
:param pulumi.Input[dict] converge_config: See Converge Config below for details.
:param pulumi.Input[dict] endpoint_spec: See EndpointSpec below for details.
:param pulumi.Input[list] labels: See Labels below for details.
:param pulumi.Input[dict] mode: See Mode below for details.
:param pulumi.Input[str] name: The name of the Docker service.
:param pulumi.Input[dict] rollback_config: See RollbackConfig below for details.
:param pulumi.Input[dict] task_spec: See TaskSpec below for details.
:param pulumi.Input[dict] update_config: See UpdateConfig below for details.</p>
<p>The <strong>auth</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to use for authenticating to the registry. If this is blank, the <code class="docutils literal notranslate"><span class="pre">DOCKER_REGISTRY_PASS</span></code> is also be checked.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The address of the registry server</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to use for authenticating to the registry. If this is blank, the <code class="docutils literal notranslate"><span class="pre">DOCKER_REGISTRY_USER</span></code> is also be checked.</p></li>
</ul>
<p>The <strong>converge_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Time between each the check to check docker endpoint <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. For example, to check if
all tasks are up when a service is created, or to check if all tasks are successfully updated on an update. Default: <code class="docutils literal notranslate"><span class="pre">7s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The timeout of the service to reach the desired state <code class="docutils literal notranslate"><span class="pre">(s|m)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">3m</span></code>.</p></li>
</ul>
<p>The <strong>endpoint_spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mode of resolution to use for internal load balancing between tasks. <code class="docutils literal notranslate"><span class="pre">(vip|dnsrr)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">vip</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Ports below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Docker service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Protocol that can be used over this port: <code class="docutils literal notranslate"><span class="pre">tcp|udp|sctp</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publishMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the mode in which the port is to be published: <code class="docutils literal notranslate"><span class="pre">ingress|host</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publishedPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port on the swarm hosts. If not set the value of <code class="docutils literal notranslate"><span class="pre">target_port</span></code> will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Port inside the container.</p></li>
</ul>
</li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
<p>The <strong>mode</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">global</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - set it to <code class="docutils literal notranslate"><span class="pre">true</span></code> to run the service in the global mode</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - , which contains atm only the amount of <code class="docutils literal notranslate"><span class="pre">replicas</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">replicas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>rollback_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Delay between restart attempts <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>
all tasks are up when a service is created, or to check if all tasks are successfully updated on an update. Default: <code class="docutils literal notranslate"><span class="pre">7s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action on update failure: <code class="docutils literal notranslate"><span class="pre">pause|continue|rollback</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailureRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The failure rate to tolerate during an update as <code class="docutils literal notranslate"><span class="pre">float</span></code>. <strong>Important:</strong> the <code class="docutils literal notranslate"><span class="pre">float</span></code>need to be wrapped in a <code class="docutils literal notranslate"><span class="pre">string</span></code> to avoid internal
casting and precision errors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">monitor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Duration after each task update to monitor for failure <code class="docutils literal notranslate"><span class="pre">(ns|us|ms|s|m|h)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Update order either ‘stop-first’ or ‘start-first’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parallelism</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of tasks to be updated in one iteration simultaneously (0 to update all at once).</p></li>
</ul>
<p>The <strong>task_spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See ContainerSpec below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Arguments to the command.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The command to be run in the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Configs below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">configId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ConfigID represents the ID of the specific config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the config that this references, but internally it is just provided for lookup/display purposes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileGid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the file GID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Represents the FileMode of the file. Defaults: <code class="docutils literal notranslate"><span class="pre">0444</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the final filename in the filesystem. The specific target file that the config data is written within the docker container, e.g. <code class="docutils literal notranslate"><span class="pre">/root/config/config.json</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the file UID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">dir</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The working directory for commands to run in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See DNS Config below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nameservers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The IP addresses of the name servers, for example, <code class="docutils literal notranslate"><span class="pre">8.8.8.8</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of internal resolver variables to be modified, for example, <code class="docutils literal notranslate"><span class="pre">debug</span></code>, <code class="docutils literal notranslate"><span class="pre">ndots:3</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">searches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A search list for host-name lookup.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">env</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of environment variables in the form VAR=value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of additional groups that the container process will run as.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Healthcheck below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Time between running the check <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Consecutive failures needed to report unhealthy. Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Start period for the container to initialize before counting retries towards unstable <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Command to run to check health. For example, to run <code class="docutils literal notranslate"><span class="pre">curl</span> <span class="pre">-f</span> <span class="pre">http://localhost/health</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;CMD&quot;,</span> <span class="pre">&quot;curl&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;http://localhost/health&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum time to allow one check to run <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname to use for the container, as a valid RFC 1123 hostname.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of hostname/IP mappings to add to the container’s hosts file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ip</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The image used to create the Docker service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isolation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Isolation technology of the containers running the service. (Windows only). Valid values are: <code class="docutils literal notranslate"><span class="pre">default|process|hyperv</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Labels below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mounts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Mounts below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bindOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">bind</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">propagation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A propagation mode with the value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Mount the container’s root filesystem as read only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mount source (e.g., a volume name, a host path)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmpfsOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">tmpf</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - See Mode below for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size for the tmpfs mount in bytes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SELinux type label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">volume</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">driverOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Labels below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">noCopy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to populate volume with data from the target.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privileges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Privileges below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">credentialSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - For managed service account (Windows only)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Load credential spec from this file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">registry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Load credential spec from this value in the Windows registry.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">seLinuxContext</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - SELinux labels of the container</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Disable SELinux</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SELinux level label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SELinux role label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SELinux type label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user inside the container.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Mount the container’s root filesystem as read only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secrets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Secrets below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fileGid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the file GID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Represents the FileMode of the file. Defaults: <code class="docutils literal notranslate"><span class="pre">0444</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the final filename in the filesystem. The specific target file that the secret data is written within the docker container, e.g. <code class="docutils literal notranslate"><span class="pre">/root/secret/secret.json</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the file UID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ConfigID represents the ID of the specific secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the secret that this references, but internally it is just provided for lookup/display purposes</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">stopGracePeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amount of time to wait for the container to terminate before forcefully removing it <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stopSignal</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Signal to stop the container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user inside the container.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceUpdate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A counter that triggers an update even if no relevant parameters have been changed. See <a class="reference external" href="https://github.com/docker/swarmkit/blob/master/api/specs.proto#L126">Docker Spec</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_driver</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Log Driver below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The logging driver to use. Either <code class="docutils literal notranslate"><span class="pre">(none|json-file|syslog|journald|gelf|fluentd|awslogs|splunk|etwlogs|gcplogs)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The options for the logging driver, e.g.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Ids of the networks in which the container will be put in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Placement below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">constraints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of constraints. e.g.: <code class="docutils literal notranslate"><span class="pre">node.role==manager</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">platforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Platforms stores all the platforms that the service’s image can run on</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">architecture</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The architecture, e.g., <code class="docutils literal notranslate"><span class="pre">amd64</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operation system, e.g., <code class="docutils literal notranslate"><span class="pre">linux</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Preferences provide a way to make the scheduler aware of factors such as topology. They are provided in order from highest to lowest precedence, e.g.: <code class="docutils literal notranslate"><span class="pre">spread=node.role.manager</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Resources below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">limits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Describes the resources which can be advertised by a node and requested by a task.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">genericResources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - User-defined resources can be either Integer resources (e.g, SSD=3) or String resources (e.g, GPU=UUID1)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">discreteResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Integer resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The String resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of memory in bytes the container allocates</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nanoCpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least 1000000</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">reservation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An object describing the resources which can be advertised by a node and requested by a task.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">genericResources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - User-defined resources can be either Integer resources (e.g, SSD=3) or String resources (e.g, GPU=UUID1)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">discreteResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Integer resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The String resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of memory in bytes the container allocates</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nanoCpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least 1000000</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">restartPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Restart Policy below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">condition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Condition for restart: <code class="docutils literal notranslate"><span class="pre">(none|on-failure|any)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Delay between restart attempts <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum attempts to restart a given container before giving up (default value is <code class="docutils literal notranslate"><span class="pre">0</span></code>, which is ignored)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time window used to evaluate the restart policy (default value is <code class="docutils literal notranslate"><span class="pre">0</span></code>, which is unbounded) <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Runtime is the type of runtime specified for the task executor. See <a class="reference external" href="https://github.com/moby/moby/blob/master/api/types/swarm/runtime.go">Docker Runtime</a>.</p></li>
</ul>
<p>The <strong>update_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Delay between updates <code class="docutils literal notranslate"><span class="pre">(ns|us|ms|s|m|h)</span></code>, e.g. <code class="docutils literal notranslate"><span class="pre">5s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action on update failure: <code class="docutils literal notranslate"><span class="pre">pause|continue|rollback</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailureRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The failure rate to tolerate during an update as <code class="docutils literal notranslate"><span class="pre">float</span></code>. <strong>Important:</strong> the <code class="docutils literal notranslate"><span class="pre">float</span></code>need to be wrapped in a <code class="docutils literal notranslate"><span class="pre">string</span></code> to avoid internal
casting and precision errors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">monitor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Duration after each task update to monitor for failure <code class="docutils literal notranslate"><span class="pre">(ns|us|ms|s|m|h)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Update order either ‘stop-first’ or ‘start-first’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parallelism</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of tasks to be updated in one iteration simultaneously (0 to update all at once).</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_docker.Service.auth">
<code class="sig-name descname">auth</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Service.auth" title="Permalink to this definition">¶</a></dt>
<dd><p>See Auth below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password to use for authenticating to the registry. If this is blank, the <code class="docutils literal notranslate"><span class="pre">DOCKER_REGISTRY_PASS</span></code> is also be checked.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The address of the registry server</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username to use for authenticating to the registry. If this is blank, the <code class="docutils literal notranslate"><span class="pre">DOCKER_REGISTRY_USER</span></code> is also be checked.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Service.converge_config">
<code class="sig-name descname">converge_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Service.converge_config" title="Permalink to this definition">¶</a></dt>
<dd><p>See Converge Config below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Time between each the check to check docker endpoint <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. For example, to check if
all tasks are up when a service is created, or to check if all tasks are successfully updated on an update. Default: <code class="docutils literal notranslate"><span class="pre">7s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The timeout of the service to reach the desired state <code class="docutils literal notranslate"><span class="pre">(s|m)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">3m</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Service.endpoint_spec">
<code class="sig-name descname">endpoint_spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Service.endpoint_spec" title="Permalink to this definition">¶</a></dt>
<dd><p>See EndpointSpec below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The mode of resolution to use for internal load balancing between tasks. <code class="docutils literal notranslate"><span class="pre">(vip|dnsrr)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">vip</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - See Ports below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Docker service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Protocol that can be used over this port: <code class="docutils literal notranslate"><span class="pre">tcp|udp|sctp</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publishMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Represents the mode in which the port is to be published: <code class="docutils literal notranslate"><span class="pre">ingress|host</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publishedPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port on the swarm hosts. If not set the value of <code class="docutils literal notranslate"><span class="pre">target_port</span></code> will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Port inside the container.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Service.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Service.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>See Labels below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the label</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Service.mode">
<code class="sig-name descname">mode</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Service.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>See Mode below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">global</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - set it to <code class="docutils literal notranslate"><span class="pre">true</span></code> to run the service in the global mode</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicated</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - , which contains atm only the amount of <code class="docutils literal notranslate"><span class="pre">replicas</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">replicas</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Service.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Service.rollback_config">
<code class="sig-name descname">rollback_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Service.rollback_config" title="Permalink to this definition">¶</a></dt>
<dd><p>See RollbackConfig below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Delay between restart attempts <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>
all tasks are up when a service is created, or to check if all tasks are successfully updated on an update. Default: <code class="docutils literal notranslate"><span class="pre">7s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Action on update failure: <code class="docutils literal notranslate"><span class="pre">pause|continue|rollback</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailureRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The failure rate to tolerate during an update as <code class="docutils literal notranslate"><span class="pre">float</span></code>. <strong>Important:</strong> the <code class="docutils literal notranslate"><span class="pre">float</span></code>need to be wrapped in a <code class="docutils literal notranslate"><span class="pre">string</span></code> to avoid internal
casting and precision errors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">monitor</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Duration after each task update to monitor for failure <code class="docutils literal notranslate"><span class="pre">(ns|us|ms|s|m|h)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Update order either ‘stop-first’ or ‘start-first’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parallelism</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of tasks to be updated in one iteration simultaneously (0 to update all at once).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Service.task_spec">
<code class="sig-name descname">task_spec</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Service.task_spec" title="Permalink to this definition">¶</a></dt>
<dd><p>See TaskSpec below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - See ContainerSpec below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Arguments to the command.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The command to be run in the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - See Configs below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">configId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ConfigID represents the ID of the specific config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the config that this references, but internally it is just provided for lookup/display purposes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileGid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Represents the file GID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Represents the FileMode of the file. Defaults: <code class="docutils literal notranslate"><span class="pre">0444</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Represents the final filename in the filesystem. The specific target file that the config data is written within the docker container, e.g. <code class="docutils literal notranslate"><span class="pre">/root/config/config.json</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Represents the file UID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">dir</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The working directory for commands to run in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - See DNS Config below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nameservers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The IP addresses of the name servers, for example, <code class="docutils literal notranslate"><span class="pre">8.8.8.8</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">options</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of internal resolver variables to be modified, for example, <code class="docutils literal notranslate"><span class="pre">debug</span></code>, <code class="docutils literal notranslate"><span class="pre">ndots:3</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">searches</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A search list for host-name lookup.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">env</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A list of environment variables in the form VAR=value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of additional groups that the container process will run as.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - See Healthcheck below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Time between running the check <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Consecutive failures needed to report unhealthy. Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Start period for the container to initialize before counting retries towards unstable <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tests</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Command to run to check health. For example, to run <code class="docutils literal notranslate"><span class="pre">curl</span> <span class="pre">-f</span> <span class="pre">http://localhost/health</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;CMD&quot;,</span> <span class="pre">&quot;curl&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;http://localhost/health&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Maximum time to allow one check to run <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname to use for the container, as a valid RFC 1123 hostname.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A list of hostname/IP mappings to add to the container’s hosts file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ip</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The image used to create the Docker service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isolation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Isolation technology of the containers running the service. (Windows only). Valid values are: <code class="docutils literal notranslate"><span class="pre">default|process|hyperv</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - See Labels below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the label</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mounts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - See Mounts below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bindOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">bind</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">propagation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A propagation mode with the value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Mount the container’s root filesystem as read only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The mount source (e.g., a volume name, a host path)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The container path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmpfsOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">tmpf</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - See Mode below for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size for the tmpfs mount in bytes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - SELinux type label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">volume</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">driverOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - See Labels below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the label</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">noCopy</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to populate volume with data from the target.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privileges</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - See Privileges below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">credentialSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - For managed service account (Windows only)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Load credential spec from this file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">registry</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Load credential spec from this value in the Windows registry.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">seLinuxContext</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - SELinux labels of the container</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Disable SELinux</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - SELinux level label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - SELinux role label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - SELinux type label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user inside the container.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Mount the container’s root filesystem as read only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secrets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - See Secrets below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fileGid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Represents the file GID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Represents the FileMode of the file. Defaults: <code class="docutils literal notranslate"><span class="pre">0444</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Represents the final filename in the filesystem. The specific target file that the secret data is written within the docker container, e.g. <code class="docutils literal notranslate"><span class="pre">/root/secret/secret.json</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUid</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Represents the file UID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ConfigID represents the ID of the specific secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the secret that this references, but internally it is just provided for lookup/display purposes</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">stopGracePeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amount of time to wait for the container to terminate before forcefully removing it <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stopSignal</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Signal to stop the container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user inside the container.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceUpdate</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - A counter that triggers an update even if no relevant parameters have been changed. See <a class="reference external" href="https://github.com/docker/swarmkit/blob/master/api/specs.proto#L126">Docker Spec</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_driver</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - See Log Driver below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The logging driver to use. Either <code class="docutils literal notranslate"><span class="pre">(none|json-file|syslog|journald|gelf|fluentd|awslogs|splunk|etwlogs|gcplogs)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">options</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The options for the logging driver, e.g.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Ids of the networks in which the container will be put in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - See Placement below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">constraints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An array of constraints. e.g.: <code class="docutils literal notranslate"><span class="pre">node.role==manager</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">platforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Platforms stores all the platforms that the service’s image can run on</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">architecture</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The architecture, e.g., <code class="docutils literal notranslate"><span class="pre">amd64</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The operation system, e.g., <code class="docutils literal notranslate"><span class="pre">linux</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Preferences provide a way to make the scheduler aware of factors such as topology. They are provided in order from highest to lowest precedence, e.g.: <code class="docutils literal notranslate"><span class="pre">spread=node.role.manager</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - See Resources below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">limits</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Describes the resources which can be advertised by a node and requested by a task.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">genericResources</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - User-defined resources can be either Integer resources (e.g, SSD=3) or String resources (e.g, GPU=UUID1)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">discreteResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The Integer resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The String resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of memory in bytes the container allocates</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nanoCpus</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least 1000000</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">reservation</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An object describing the resources which can be advertised by a node and requested by a task.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">genericResources</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - User-defined resources can be either Integer resources (e.g, SSD=3) or String resources (e.g, GPU=UUID1)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">discreteResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The Integer resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The String resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of memory in bytes the container allocates</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nanoCpus</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least 1000000</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">restartPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - See Restart Policy below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">condition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Condition for restart: <code class="docutils literal notranslate"><span class="pre">(none|on-failure|any)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Delay between restart attempts <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum attempts to restart a given container before giving up (default value is <code class="docutils literal notranslate"><span class="pre">0</span></code>, which is ignored)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The time window used to evaluate the restart policy (default value is <code class="docutils literal notranslate"><span class="pre">0</span></code>, which is unbounded) <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Runtime is the type of runtime specified for the task executor. See <a class="reference external" href="https://github.com/moby/moby/blob/master/api/types/swarm/runtime.go">Docker Runtime</a>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Service.update_config">
<code class="sig-name descname">update_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Service.update_config" title="Permalink to this definition">¶</a></dt>
<dd><p>See UpdateConfig below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Delay between updates <code class="docutils literal notranslate"><span class="pre">(ns|us|ms|s|m|h)</span></code>, e.g. <code class="docutils literal notranslate"><span class="pre">5s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Action on update failure: <code class="docutils literal notranslate"><span class="pre">pause|continue|rollback</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailureRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The failure rate to tolerate during an update as <code class="docutils literal notranslate"><span class="pre">float</span></code>. <strong>Important:</strong> the <code class="docutils literal notranslate"><span class="pre">float</span></code>need to be wrapped in a <code class="docutils literal notranslate"><span class="pre">string</span></code> to avoid internal
casting and precision errors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">monitor</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Duration after each task update to monitor for failure <code class="docutils literal notranslate"><span class="pre">(ns|us|ms|s|m|h)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Update order either ‘stop-first’ or ‘start-first’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parallelism</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of tasks to be updated in one iteration simultaneously (0 to update all at once).</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">converge_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rollback_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See Auth below for details.</p></li>
<li><p><strong>converge_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See Converge Config below for details.</p></li>
<li><p><strong>endpoint_spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See EndpointSpec below for details.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Labels below for details.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See Mode below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker service.</p></li>
<li><p><strong>rollback_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See RollbackConfig below for details.</p></li>
<li><p><strong>task_spec</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See TaskSpec below for details.</p></li>
<li><p><strong>update_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See UpdateConfig below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to use for authenticating to the registry. If this is blank, the <code class="docutils literal notranslate"><span class="pre">DOCKER_REGISTRY_PASS</span></code> is also be checked.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The address of the registry server</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to use for authenticating to the registry. If this is blank, the <code class="docutils literal notranslate"><span class="pre">DOCKER_REGISTRY_USER</span></code> is also be checked.</p></li>
</ul>
<p>The <strong>converge_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Time between each the check to check docker endpoint <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. For example, to check if
all tasks are up when a service is created, or to check if all tasks are successfully updated on an update. Default: <code class="docutils literal notranslate"><span class="pre">7s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The timeout of the service to reach the desired state <code class="docutils literal notranslate"><span class="pre">(s|m)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">3m</span></code>.</p></li>
</ul>
<p>The <strong>endpoint_spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mode of resolution to use for internal load balancing between tasks. <code class="docutils literal notranslate"><span class="pre">(vip|dnsrr)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">vip</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Ports below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Docker service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Protocol that can be used over this port: <code class="docutils literal notranslate"><span class="pre">tcp|udp|sctp</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">tcp</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publishMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the mode in which the port is to be published: <code class="docutils literal notranslate"><span class="pre">ingress|host</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publishedPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port on the swarm hosts. If not set the value of <code class="docutils literal notranslate"><span class="pre">target_port</span></code> will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Port inside the container.</p></li>
</ul>
</li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
<p>The <strong>mode</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">global</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - set it to <code class="docutils literal notranslate"><span class="pre">true</span></code> to run the service in the global mode</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicated</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - , which contains atm only the amount of <code class="docutils literal notranslate"><span class="pre">replicas</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">replicas</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>rollback_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Delay between restart attempts <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>
all tasks are up when a service is created, or to check if all tasks are successfully updated on an update. Default: <code class="docutils literal notranslate"><span class="pre">7s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action on update failure: <code class="docutils literal notranslate"><span class="pre">pause|continue|rollback</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailureRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The failure rate to tolerate during an update as <code class="docutils literal notranslate"><span class="pre">float</span></code>. <strong>Important:</strong> the <code class="docutils literal notranslate"><span class="pre">float</span></code>need to be wrapped in a <code class="docutils literal notranslate"><span class="pre">string</span></code> to avoid internal
casting and precision errors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">monitor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Duration after each task update to monitor for failure <code class="docutils literal notranslate"><span class="pre">(ns|us|ms|s|m|h)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Update order either ‘stop-first’ or ‘start-first’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parallelism</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of tasks to be updated in one iteration simultaneously (0 to update all at once).</p></li>
</ul>
<p>The <strong>task_spec</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See ContainerSpec below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Arguments to the command.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The command to be run in the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Configs below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">configId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ConfigID represents the ID of the specific config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">configName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the config that this references, but internally it is just provided for lookup/display purposes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileGid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the file GID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Represents the FileMode of the file. Defaults: <code class="docutils literal notranslate"><span class="pre">0444</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the final filename in the filesystem. The specific target file that the config data is written within the docker container, e.g. <code class="docutils literal notranslate"><span class="pre">/root/config/config.json</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the file UID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">dir</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The working directory for commands to run in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See DNS Config below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nameservers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The IP addresses of the name servers, for example, <code class="docutils literal notranslate"><span class="pre">8.8.8.8</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of internal resolver variables to be modified, for example, <code class="docutils literal notranslate"><span class="pre">debug</span></code>, <code class="docutils literal notranslate"><span class="pre">ndots:3</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">searches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A search list for host-name lookup.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">env</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of environment variables in the form VAR=value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of additional groups that the container process will run as.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthcheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Healthcheck below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Time between running the check <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Consecutive failures needed to report unhealthy. Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Start period for the container to initialize before counting retries towards unstable <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tests</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Command to run to check health. For example, to run <code class="docutils literal notranslate"><span class="pre">curl</span> <span class="pre">-f</span> <span class="pre">http://localhost/health</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;CMD&quot;,</span> <span class="pre">&quot;curl&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;http://localhost/health&quot;]</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum time to allow one check to run <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">0s</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname to use for the container, as a valid RFC 1123 hostname.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of hostname/IP mappings to add to the container’s hosts file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ip</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The image used to create the Docker service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isolation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Isolation technology of the containers running the service. (Windows only). Valid values are: <code class="docutils literal notranslate"><span class="pre">default|process|hyperv</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Labels below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">mounts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Mounts below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bindOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">bind</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">propagation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A propagation mode with the value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Mount the container’s root filesystem as read only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The mount source (e.g., a volume name, a host path)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container path.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tmpfsOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">tmpf</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - See Mode below for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size for the tmpfs mount in bytes.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SELinux type label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optional configuration for the <code class="docutils literal notranslate"><span class="pre">volume</span></code> type.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">driverName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">driverOptions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Labels below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the label</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">noCopy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to populate volume with data from the target.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">privileges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Privileges below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">credentialSpec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - For managed service account (Windows only)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">file</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Load credential spec from this file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">registry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Load credential spec from this value in the Windows registry.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">seLinuxContext</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - SELinux labels of the container</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Disable SELinux</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">level</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SELinux level label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SELinux role label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - SELinux type label</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user inside the container.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">read_only</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Mount the container’s root filesystem as read only.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secrets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See Secrets below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fileGid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the file GID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Represents the FileMode of the file. Defaults: <code class="docutils literal notranslate"><span class="pre">0444</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the final filename in the filesystem. The specific target file that the secret data is written within the docker container, e.g. <code class="docutils literal notranslate"><span class="pre">/root/secret/secret.json</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUid</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Represents the file UID. Defaults: <code class="docutils literal notranslate"><span class="pre">0</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ConfigID represents the ID of the specific secret.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the secret that this references, but internally it is just provided for lookup/display purposes</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">stopGracePeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amount of time to wait for the container to terminate before forcefully removing it <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stopSignal</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Signal to stop the container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user inside the container.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceUpdate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - A counter that triggers an update even if no relevant parameters have been changed. See <a class="reference external" href="https://github.com/docker/swarmkit/blob/master/api/specs.proto#L126">Docker Spec</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_driver</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Log Driver below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The logging driver to use. Either <code class="docutils literal notranslate"><span class="pre">(none|json-file|syslog|journald|gelf|fluentd|awslogs|splunk|etwlogs|gcplogs)</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">options</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The options for the logging driver, e.g.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">networks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Ids of the networks in which the container will be put in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placement</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Placement below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">constraints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An array of constraints. e.g.: <code class="docutils literal notranslate"><span class="pre">node.role==manager</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">platforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Platforms stores all the platforms that the service’s image can run on</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">architecture</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The architecture, e.g., <code class="docutils literal notranslate"><span class="pre">amd64</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The operation system, e.g., <code class="docutils literal notranslate"><span class="pre">linux</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Preferences provide a way to make the scheduler aware of factors such as topology. They are provided in order from highest to lowest precedence, e.g.: <code class="docutils literal notranslate"><span class="pre">spread=node.role.manager</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Resources below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">limits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Describes the resources which can be advertised by a node and requested by a task.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">genericResources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - User-defined resources can be either Integer resources (e.g, SSD=3) or String resources (e.g, GPU=UUID1)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">discreteResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Integer resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The String resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of memory in bytes the container allocates</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nanoCpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least 1000000</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">reservation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An object describing the resources which can be advertised by a node and requested by a task.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">genericResources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - User-defined resources can be either Integer resources (e.g, SSD=3) or String resources (e.g, GPU=UUID1)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">discreteResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The Integer resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedResourcesSpecs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The String resources, delimited by <code class="docutils literal notranslate"><span class="pre">=</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryBytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of memory in bytes the container allocates</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nanoCpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least 1000000</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">restartPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See Restart Policy below for details.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">condition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Condition for restart: <code class="docutils literal notranslate"><span class="pre">(none|on-failure|any)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Delay between restart attempts <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum attempts to restart a given container before giving up (default value is <code class="docutils literal notranslate"><span class="pre">0</span></code>, which is ignored)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">window</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time window used to evaluate the restart policy (default value is <code class="docutils literal notranslate"><span class="pre">0</span></code>, which is unbounded) <code class="docutils literal notranslate"><span class="pre">(ms|s|m|h)</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">runtime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Runtime is the type of runtime specified for the task executor. See <a class="reference external" href="https://github.com/moby/moby/blob/master/api/types/swarm/runtime.go">Docker Runtime</a>.</p></li>
</ul>
<p>The <strong>update_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">delay</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Delay between updates <code class="docutils literal notranslate"><span class="pre">(ns|us|ms|s|m|h)</span></code>, e.g. <code class="docutils literal notranslate"><span class="pre">5s</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action on update failure: <code class="docutils literal notranslate"><span class="pre">pause|continue|rollback</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxFailureRatio</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The failure rate to tolerate during an update as <code class="docutils literal notranslate"><span class="pre">float</span></code>. <strong>Important:</strong> the <code class="docutils literal notranslate"><span class="pre">float</span></code>need to be wrapped in a <code class="docutils literal notranslate"><span class="pre">string</span></code> to avoid internal
casting and precision errors.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">monitor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Duration after each task update to monitor for failure <code class="docutils literal notranslate"><span class="pre">(ns|us|ms|s|m|h)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Update order either ‘stop-first’ or ‘start-first’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parallelism</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of tasks to be updated in one iteration simultaneously (0 to update all at once).</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.ServiceConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">ServiceConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.ServiceConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the configuration of a Docker service in a swarm.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64 encoded data of the config.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker config.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_docker.ServiceConfig.data">
<code class="sig-name descname">data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.ServiceConfig.data" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64 encoded data of the config.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.ServiceConfig.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.ServiceConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker config.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.ServiceConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.ServiceConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64 encoded data of the config.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker config.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.ServiceConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.ServiceConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.ServiceConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.ServiceConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.Volume">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver_opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and destroys a volume in Docker. This can be used alongside
<a class="reference external" href="https://www.terraform.io/docs/providers/docker/r/container.html">docker_container</a>
to prepare volumes that can be shared across containers.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Driver type for the volume (defaults to local).</p></li>
<li><p><strong>driver_opts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options specific to the driver.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – User-defined key/value metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker volume (generated if not
provided).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_docker.Volume.driver">
<code class="sig-name descname">driver</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Volume.driver" title="Permalink to this definition">¶</a></dt>
<dd><p>Driver type for the volume (defaults to local).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Volume.driver_opts">
<code class="sig-name descname">driver_opts</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Volume.driver_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>Options specific to the driver.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Volume.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Volume.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined key/value metadata.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Volume.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Volume.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker volume (generated if not
provided).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver_opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mountpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Driver type for the volume (defaults to local).</p></li>
<li><p><strong>driver_opts</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options specific to the driver.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – User-defined key/value metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker volume (generated if not
provided).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Volume.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.Volume.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_docker.get_network">
<code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">get_network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.get_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Finds a specific docker network and returns information about it.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>str</em>) – The id of the Docker network.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the Docker network.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_docker.get_registry_image">
<code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">get_registry_image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.get_registry_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Reads the image metadata from a Docker Registry. Used in conjunction with the
<a class="reference external" href="https://www.terraform.io/docs/providers/docker/r/image.html">docker_image</a> resource to keep an image up
to date on the latest available version of the tag.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the Docker image, including any tags. e.g. <code class="docutils literal notranslate"><span class="pre">alpine:latest</span></code></p>
</dd>
</dl>
</dd></dl>

</div>
