---
title: Package pulumi_docker
title_tag: Package pulumi_docker | Python SDK
linktitle: pulumi_docker
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "docker" >}}

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
<dt id="pulumi_docker.CacheFrom">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">CacheFrom</code><a class="headerlink" href="#pulumi_docker.CacheFrom" title="Permalink to this definition">¶</a></dt>
<dd><p>CacheFrom may be used to specify build stages to use for the Docker build cache. The final image
is always implicitly included.</p>
<dl class="py attribute">
<dt id="pulumi_docker.CacheFrom.stages">
<code class="sig-name descname">stages</code><em class="property">: Optional[Sequence[pulumi.Input[pulumi.Input[str]]]]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.CacheFrom.stages" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional list of build stages to use for caching. Each build stage in this list will be
built explicitly and pushed to the target repository. A given stage’s image will be tagged as
“[stage-name]”.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_docker.Container">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Container</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attach</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capabilities</span><span class="p">:</span> <span class="n">Union[ContainerCapabilitiesArgs, Mapping[str, Any], Awaitable[Union[ContainerCapabilitiesArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">command</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_set</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_shares</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destroy_grace_seconds</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerDeviceArgs, Mapping[str, Any], Awaitable[Union[ContainerDeviceArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerDeviceArgs, Mapping[str, Any], Awaitable[Union[ContainerDeviceArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_opts</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_searches</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domainname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entrypoints</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">envs</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_adds</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthcheck</span><span class="p">:</span> <span class="n">Union[ContainerHealthcheckArgs, Mapping[str, Any], Awaitable[Union[ContainerHealthcheckArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosts</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerHostArgs, Mapping[str, Any], Awaitable[Union[ContainerHostArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerHostArgs, Mapping[str, Any], Awaitable[Union[ContainerHostArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipc_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerLabelArgs, Mapping[str, Any], Awaitable[Union[ContainerLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerLabelArgs, Mapping[str, Any], Awaitable[Union[ContainerLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">links</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_driver</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_opts</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retry_count</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory_swap</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mounts</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerMountArgs, Mapping[str, Any], Awaitable[Union[ContainerMountArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerMountArgs, Mapping[str, Any], Awaitable[Union[ContainerMountArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">must_run</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_aliases</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks_advanced</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerNetworksAdvancedArgs, Mapping[str, Any], Awaitable[Union[ContainerNetworksAdvancedArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerNetworksAdvancedArgs, Mapping[str, Any], Awaitable[Union[ContainerNetworksAdvancedArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pid_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerPortArgs, Mapping[str, Any], Awaitable[Union[ContainerPortArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerPortArgs, Mapping[str, Any], Awaitable[Union[ContainerPortArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileged</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">publish_all_ports</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restart</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rm</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shm_size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sysctls</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tmpfs</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ulimits</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerUlimitArgs, Mapping[str, Any], Awaitable[Union[ContainerUlimitArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerUlimitArgs, Mapping[str, Any], Awaitable[Union[ContainerUlimitArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uploads</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerUploadArgs, Mapping[str, Any], Awaitable[Union[ContainerUploadArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerUploadArgs, Mapping[str, Any], Awaitable[Union[ContainerUploadArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">userns_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volumes</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerVolumeArgs, Mapping[str, Any], Awaitable[Union[ContainerVolumeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerVolumeArgs, Mapping[str, Any], Awaitable[Union[ContainerVolumeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">working_dir</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Container" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the lifecycle of a Docker container.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_docker</span> <span class="k">as</span> <span class="nn">docker</span>

<span class="c1"># Find the latest Ubuntu precise image.</span>
<span class="n">ubuntu_remote_image</span> <span class="o">=</span> <span class="n">docker</span><span class="o">.</span><span class="n">RemoteImage</span><span class="p">(</span><span class="s2">&quot;ubuntuRemoteImage&quot;</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;ubuntu:precise&quot;</span><span class="p">)</span>
<span class="c1"># Start a container</span>
<span class="n">ubuntu_container</span> <span class="o">=</span> <span class="n">docker</span><span class="o">.</span><span class="n">Container</span><span class="p">(</span><span class="s2">&quot;ubuntuContainer&quot;</span><span class="p">,</span> <span class="n">image</span><span class="o">=</span><span class="n">ubuntu_remote_image</span><span class="o">.</span><span class="n">latest</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attach</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true attach to the container after its creation and waits the end of his execution.</p></li>
<li><p><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerCapabilitiesArgs'</em><em>]</em><em>]</em>) – See Capabilities below for details.</p></li>
<li><p><strong>command</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The command to use to start the
container. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span> <span class="pre">-f</span> <span class="pre">baz.conf</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;baz.conf&quot;]</span></code>.</p></li>
<li><p><strong>cpu_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. <code class="docutils literal notranslate"><span class="pre">0-1</span></code>.</p></li>
<li><p><strong>cpu_shares</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – CPU shares (relative weight) for the container.</p></li>
<li><p><strong>destroy_grace_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If defined will attempt to stop the container before destroying. Container will be destroyed after <code class="docutils literal notranslate"><span class="pre">n</span></code> seconds or on successful stop.</p></li>
<li><p><strong>devices</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerDeviceArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Devices below for details.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set of DNS servers.</p></li>
<li><p><strong>dns_opts</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set of DNS options used by the DNS provider(s), see <code class="docutils literal notranslate"><span class="pre">resolv.conf</span></code> documentation for valid list of options.</p></li>
<li><p><strong>dns_searches</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.</p></li>
<li><p><strong>domainname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name of the container.</p></li>
<li><p><strong>entrypoints</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span></code>
when starting a container, set the entrypoint to be
<code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;]</span></code>.</p></li>
<li><p><strong>envs</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Environment variables to set.</p></li>
<li><p><strong>group_adds</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Add additional groups to run as.</p></li>
<li><p><strong>healthcheck</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerHealthcheckArgs'</em><em>]</em><em>]</em>) – See Healthcheck below for details.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hostname of the container.</p></li>
<li><p><strong>hosts</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerHostArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Hostname to add.</p></li>
<li><p><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the image to back this container.
The easiest way to get this value is to use the <code class="docutils literal notranslate"><span class="pre">RemoteImage</span></code> resource
as is shown in the example above.</p></li>
<li><p><strong>ipc_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IPC sharing mode for the container. Possible values are: <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">shareable</span></code>, <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerLabelArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Adding labels.</p></li>
<li><p><strong>links</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set of links for link based
connectivity between containers that are running on the same host.</p></li>
<li><p><strong>log_driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The logging driver to use for the container.
Defaults to “json-file”.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>log_opts</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Key/value pairs to use as options for
the logging driver.</p></li>
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Save the container logs (<code class="docutils literal notranslate"><span class="pre">attach</span></code> must be enabled).</p></li>
<li><p><strong>max_retry_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum amount of times to an attempt
a restart when <code class="docutils literal notranslate"><span class="pre">restart</span></code> is set to “on-failure”</p></li>
<li><p><strong>memory</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The memory limit for the container in MBs.</p></li>
<li><p><strong>mounts</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerMountArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Mounts below for details.</p></li>
<li><p><strong>network_aliases</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Network aliases of the container for user-defined networks only. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p></li>
<li><p><strong>network_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network mode of the container.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Id of the networks in which the
container is. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p></li>
<li><p><strong>networks_advanced</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerNetworksAdvancedArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Networks Advanced below for details. If this block has priority to the deprecated <code class="docutils literal notranslate"><span class="pre">network_alias</span></code> and <code class="docutils literal notranslate"><span class="pre">network</span></code> properties.</p></li>
<li><p><strong>pid_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PID (Process) Namespace mode for the container. Either <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p></li>
<li><p><strong>ports</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerPortArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Ports below for details.</p></li>
<li><p><strong>privileged</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Run container in privileged mode.</p></li>
<li><p><strong>publish_all_ports</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Publish all ports of the container.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, this volume will be readonly.
Defaults to false.</p></li>
<li><p><strong>restart</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The restart policy for the container. Must be
one of “no”, “on-failure”, “always”, “unless-stopped”.</p></li>
<li><p><strong>shm_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of <code class="docutils literal notranslate"><span class="pre">/dev/shm</span></code> in MBs.</p></li>
<li><p><strong>start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, then the Docker container will be
started after creation. If false, then the container is only created.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>sysctls</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of kernel parameters (sysctls) to set in the container.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>tmpfs</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of container directories which should be replaced by <code class="docutils literal notranslate"><span class="pre">tmpfs</span> <span class="pre">mounts</span></code>, and their corresponding mount options.</p></li>
<li><p><strong>ulimits</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerUlimitArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Ulimits below for
details.</p></li>
<li><p><strong>uploads</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerUploadArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See File Upload below for details.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User used for run the first process. Format is
<code class="docutils literal notranslate"><span class="pre">user</span></code> or <code class="docutils literal notranslate"><span class="pre">user:group</span></code> which user and group can be passed literraly or
by name.</p></li>
<li><p><strong>userns_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the usernamespace mode for the container when usernamespace remapping option is enabled.</p></li>
<li><p><strong>volumes</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerVolumeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Volumes below for details.</p></li>
<li><p><strong>working_dir</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The working directory for commands to run in</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_docker.Container.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attach</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bridge</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capabilities</span><span class="p">:</span> <span class="n">Union[ContainerCapabilitiesArgs, Mapping[str, Any], Awaitable[Union[ContainerCapabilitiesArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">command</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_logs</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_set</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_shares</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destroy_grace_seconds</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerDeviceArgs, Mapping[str, Any], Awaitable[Union[ContainerDeviceArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerDeviceArgs, Mapping[str, Any], Awaitable[Union[ContainerDeviceArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_opts</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_searches</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domainname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entrypoints</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">envs</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exit_code</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_adds</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">healthcheck</span><span class="p">:</span> <span class="n">Union[ContainerHealthcheckArgs, Mapping[str, Any], Awaitable[Union[ContainerHealthcheckArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hosts</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerHostArgs, Mapping[str, Any], Awaitable[Union[ContainerHostArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerHostArgs, Mapping[str, Any], Awaitable[Union[ContainerHostArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_prefix_length</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipc_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerLabelArgs, Mapping[str, Any], Awaitable[Union[ContainerLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerLabelArgs, Mapping[str, Any], Awaitable[Union[ContainerLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">links</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_driver</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_opts</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_retry_count</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory_swap</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mounts</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerMountArgs, Mapping[str, Any], Awaitable[Union[ContainerMountArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerMountArgs, Mapping[str, Any], Awaitable[Union[ContainerMountArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">must_run</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_aliases</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_datas</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerNetworkDataArgs, Mapping[str, Any], Awaitable[Union[ContainerNetworkDataArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerNetworkDataArgs, Mapping[str, Any], Awaitable[Union[ContainerNetworkDataArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks_advanced</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerNetworksAdvancedArgs, Mapping[str, Any], Awaitable[Union[ContainerNetworksAdvancedArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerNetworksAdvancedArgs, Mapping[str, Any], Awaitable[Union[ContainerNetworksAdvancedArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pid_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerPortArgs, Mapping[str, Any], Awaitable[Union[ContainerPortArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerPortArgs, Mapping[str, Any], Awaitable[Union[ContainerPortArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileged</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">publish_all_ports</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restart</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rm</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shm_size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sysctls</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tmpfs</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ulimits</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerUlimitArgs, Mapping[str, Any], Awaitable[Union[ContainerUlimitArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerUlimitArgs, Mapping[str, Any], Awaitable[Union[ContainerUlimitArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uploads</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerUploadArgs, Mapping[str, Any], Awaitable[Union[ContainerUploadArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerUploadArgs, Mapping[str, Any], Awaitable[Union[ContainerUploadArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">userns_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volumes</span><span class="p">:</span> <span class="n">Union[List[Union[ContainerVolumeArgs, Mapping[str, Any], Awaitable[Union[ContainerVolumeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ContainerVolumeArgs, Mapping[str, Any], Awaitable[Union[ContainerVolumeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">working_dir</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_docker.container.Container<a class="headerlink" href="#pulumi_docker.Container.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Container resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attach</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true attach to the container after its creation and waits the end of his execution.</p></li>
<li><p><strong>bridge</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network bridge of the container as read from its NetworkSettings.</p></li>
<li><p><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerCapabilitiesArgs'</em><em>]</em><em>]</em>) – See Capabilities below for details.</p></li>
<li><p><strong>command</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The command to use to start the
container. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span> <span class="pre">-f</span> <span class="pre">baz.conf</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;baz.conf&quot;]</span></code>.</p></li>
<li><p><strong>container_logs</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The logs of the container if its execution is done (<code class="docutils literal notranslate"><span class="pre">attach</span></code> must be disabled).</p></li>
<li><p><strong>cpu_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. <code class="docutils literal notranslate"><span class="pre">0-1</span></code>.</p></li>
<li><p><strong>cpu_shares</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – CPU shares (relative weight) for the container.</p></li>
<li><p><strong>destroy_grace_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If defined will attempt to stop the container before destroying. Container will be destroyed after <code class="docutils literal notranslate"><span class="pre">n</span></code> seconds or on successful stop.</p></li>
<li><p><strong>devices</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerDeviceArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Devices below for details.</p></li>
<li><p><strong>dns</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set of DNS servers.</p></li>
<li><p><strong>dns_opts</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set of DNS options used by the DNS provider(s), see <code class="docutils literal notranslate"><span class="pre">resolv.conf</span></code> documentation for valid list of options.</p></li>
<li><p><strong>dns_searches</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.</p></li>
<li><p><strong>domainname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name of the container.</p></li>
<li><p><strong>entrypoints</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span></code>
when starting a container, set the entrypoint to be
<code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;]</span></code>.</p></li>
<li><p><strong>envs</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Environment variables to set.</p></li>
<li><p><strong>exit_code</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The exit code of the container if its execution is done (<code class="docutils literal notranslate"><span class="pre">must_run</span></code> must be disabled).</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The network gateway of the container as read from its
NetworkSettings.</p></li>
<li><p><strong>group_adds</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Add additional groups to run as.</p></li>
<li><p><strong>healthcheck</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerHealthcheckArgs'</em><em>]</em><em>]</em>) – See Healthcheck below for details.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Hostname of the container.</p></li>
<li><p><strong>hosts</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerHostArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Hostname to add.</p></li>
<li><p><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the image to back this container.
The easiest way to get this value is to use the <code class="docutils literal notranslate"><span class="pre">RemoteImage</span></code> resource
as is shown in the example above.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP address of the container’s first network it.</p></li>
<li><p><strong>ip_prefix_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP prefix length of the container as read from its
NetworkSettings.</p></li>
<li><p><strong>ipc_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IPC sharing mode for the container. Possible values are: <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">shareable</span></code>, <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerLabelArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Adding labels.</p></li>
<li><p><strong>links</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Set of links for link based
connectivity between containers that are running on the same host.</p></li>
<li><p><strong>log_driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The logging driver to use for the container.
Defaults to “json-file”.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>log_opts</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Key/value pairs to use as options for
the logging driver.</p></li>
<li><p><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Save the container logs (<code class="docutils literal notranslate"><span class="pre">attach</span></code> must be enabled).</p></li>
<li><p><strong>max_retry_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum amount of times to an attempt
a restart when <code class="docutils literal notranslate"><span class="pre">restart</span></code> is set to “on-failure”</p></li>
<li><p><strong>memory</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The memory limit for the container in MBs.</p></li>
<li><p><strong>mounts</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerMountArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Mounts below for details.</p></li>
<li><p><strong>network_aliases</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Network aliases of the container for user-defined networks only. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p></li>
<li><p><strong>network_datas</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerNetworkDataArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – (Map of a block) The IP addresses of the container on each
network. Key are the network names, values are the IP addresses.</p></li>
<li><p><strong>network_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network mode of the container.</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Id of the networks in which the
container is. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p></li>
<li><p><strong>networks_advanced</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerNetworksAdvancedArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Networks Advanced below for details. If this block has priority to the deprecated <code class="docutils literal notranslate"><span class="pre">network_alias</span></code> and <code class="docutils literal notranslate"><span class="pre">network</span></code> properties.</p></li>
<li><p><strong>pid_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PID (Process) Namespace mode for the container. Either <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p></li>
<li><p><strong>ports</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerPortArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Ports below for details.</p></li>
<li><p><strong>privileged</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Run container in privileged mode.</p></li>
<li><p><strong>publish_all_ports</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Publish all ports of the container.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, this volume will be readonly.
Defaults to false.</p></li>
<li><p><strong>restart</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The restart policy for the container. Must be
one of “no”, “on-failure”, “always”, “unless-stopped”.</p></li>
<li><p><strong>shm_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of <code class="docutils literal notranslate"><span class="pre">/dev/shm</span></code> in MBs.</p></li>
<li><p><strong>start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, then the Docker container will be
started after creation. If false, then the container is only created.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>sysctls</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of kernel parameters (sysctls) to set in the container.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>tmpfs</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of container directories which should be replaced by <code class="docutils literal notranslate"><span class="pre">tmpfs</span> <span class="pre">mounts</span></code>, and their corresponding mount options.</p></li>
<li><p><strong>ulimits</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerUlimitArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Ulimits below for
details.</p></li>
<li><p><strong>uploads</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerUploadArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See File Upload below for details.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User used for run the first process. Format is
<code class="docutils literal notranslate"><span class="pre">user</span></code> or <code class="docutils literal notranslate"><span class="pre">user:group</span></code> which user and group can be passed literraly or
by name.</p></li>
<li><p><strong>userns_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the usernamespace mode for the container when usernamespace remapping option is enabled.</p></li>
<li><p><strong>volumes</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ContainerVolumeArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Volumes below for details.</p></li>
<li><p><strong>working_dir</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The working directory for commands to run in</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.attach">
<em class="property">property </em><code class="sig-name descname">attach</code><a class="headerlink" href="#pulumi_docker.Container.attach" title="Permalink to this definition">¶</a></dt>
<dd><p>If true attach to the container after its creation and waits the end of his execution.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.bridge">
<em class="property">property </em><code class="sig-name descname">bridge</code><a class="headerlink" href="#pulumi_docker.Container.bridge" title="Permalink to this definition">¶</a></dt>
<dd><p>The network bridge of the container as read from its NetworkSettings.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.capabilities">
<em class="property">property </em><code class="sig-name descname">capabilities</code><a class="headerlink" href="#pulumi_docker.Container.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>See Capabilities below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.command">
<em class="property">property </em><code class="sig-name descname">command</code><a class="headerlink" href="#pulumi_docker.Container.command" title="Permalink to this definition">¶</a></dt>
<dd><p>The command to use to start the
container. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span> <span class="pre">-f</span> <span class="pre">baz.conf</span></code> set the
command to be <code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;,</span> <span class="pre">&quot;-f&quot;,</span> <span class="pre">&quot;baz.conf&quot;]</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.container_logs">
<em class="property">property </em><code class="sig-name descname">container_logs</code><a class="headerlink" href="#pulumi_docker.Container.container_logs" title="Permalink to this definition">¶</a></dt>
<dd><p>The logs of the container if its execution is done (<code class="docutils literal notranslate"><span class="pre">attach</span></code> must be disabled).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.cpu_set">
<em class="property">property </em><code class="sig-name descname">cpu_set</code><a class="headerlink" href="#pulumi_docker.Container.cpu_set" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. <code class="docutils literal notranslate"><span class="pre">0-1</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.cpu_shares">
<em class="property">property </em><code class="sig-name descname">cpu_shares</code><a class="headerlink" href="#pulumi_docker.Container.cpu_shares" title="Permalink to this definition">¶</a></dt>
<dd><p>CPU shares (relative weight) for the container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.destroy_grace_seconds">
<em class="property">property </em><code class="sig-name descname">destroy_grace_seconds</code><a class="headerlink" href="#pulumi_docker.Container.destroy_grace_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>If defined will attempt to stop the container before destroying. Container will be destroyed after <code class="docutils literal notranslate"><span class="pre">n</span></code> seconds or on successful stop.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.devices">
<em class="property">property </em><code class="sig-name descname">devices</code><a class="headerlink" href="#pulumi_docker.Container.devices" title="Permalink to this definition">¶</a></dt>
<dd><p>See Devices below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.dns">
<em class="property">property </em><code class="sig-name descname">dns</code><a class="headerlink" href="#pulumi_docker.Container.dns" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of DNS servers.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.dns_opts">
<em class="property">property </em><code class="sig-name descname">dns_opts</code><a class="headerlink" href="#pulumi_docker.Container.dns_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of DNS options used by the DNS provider(s), see <code class="docutils literal notranslate"><span class="pre">resolv.conf</span></code> documentation for valid list of options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.dns_searches">
<em class="property">property </em><code class="sig-name descname">dns_searches</code><a class="headerlink" href="#pulumi_docker.Container.dns_searches" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of DNS search domains that are used when bare unqualified hostnames are used inside of the container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.domainname">
<em class="property">property </em><code class="sig-name descname">domainname</code><a class="headerlink" href="#pulumi_docker.Container.domainname" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name of the container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.entrypoints">
<em class="property">property </em><code class="sig-name descname">entrypoints</code><a class="headerlink" href="#pulumi_docker.Container.entrypoints" title="Permalink to this definition">¶</a></dt>
<dd><p>The command to use as the
Entrypoint for the container. The Entrypoint allows you to configure a
container to run as an executable. For example, to run <code class="docutils literal notranslate"><span class="pre">/usr/bin/myprogram</span></code>
when starting a container, set the entrypoint to be
<code class="docutils literal notranslate"><span class="pre">[&quot;/usr/bin/myprogram&quot;]</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.envs">
<em class="property">property </em><code class="sig-name descname">envs</code><a class="headerlink" href="#pulumi_docker.Container.envs" title="Permalink to this definition">¶</a></dt>
<dd><p>Environment variables to set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.exit_code">
<em class="property">property </em><code class="sig-name descname">exit_code</code><a class="headerlink" href="#pulumi_docker.Container.exit_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The exit code of the container if its execution is done (<code class="docutils literal notranslate"><span class="pre">must_run</span></code> must be disabled).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.gateway">
<em class="property">property </em><code class="sig-name descname">gateway</code><a class="headerlink" href="#pulumi_docker.Container.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The network gateway of the container as read from its
NetworkSettings.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.group_adds">
<em class="property">property </em><code class="sig-name descname">group_adds</code><a class="headerlink" href="#pulumi_docker.Container.group_adds" title="Permalink to this definition">¶</a></dt>
<dd><p>Add additional groups to run as.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.healthcheck">
<em class="property">property </em><code class="sig-name descname">healthcheck</code><a class="headerlink" href="#pulumi_docker.Container.healthcheck" title="Permalink to this definition">¶</a></dt>
<dd><p>See Healthcheck below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_docker.Container.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>Hostname of the container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.hosts">
<em class="property">property </em><code class="sig-name descname">hosts</code><a class="headerlink" href="#pulumi_docker.Container.hosts" title="Permalink to this definition">¶</a></dt>
<dd><p>Hostname to add.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.image">
<em class="property">property </em><code class="sig-name descname">image</code><a class="headerlink" href="#pulumi_docker.Container.image" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the image to back this container.
The easiest way to get this value is to use the <code class="docutils literal notranslate"><span class="pre">RemoteImage</span></code> resource
as is shown in the example above.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.ip_address">
<em class="property">property </em><code class="sig-name descname">ip_address</code><a class="headerlink" href="#pulumi_docker.Container.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP address of the container’s first network it.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.ip_prefix_length">
<em class="property">property </em><code class="sig-name descname">ip_prefix_length</code><a class="headerlink" href="#pulumi_docker.Container.ip_prefix_length" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">network_data</span></code> instead. The IP prefix length of the container as read from its
NetworkSettings.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.ipc_mode">
<em class="property">property </em><code class="sig-name descname">ipc_mode</code><a class="headerlink" href="#pulumi_docker.Container.ipc_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>IPC sharing mode for the container. Possible values are: <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">shareable</span></code>, <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_docker.Container.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Adding labels.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.links">
<em class="property">property </em><code class="sig-name descname">links</code><a class="headerlink" href="#pulumi_docker.Container.links" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of links for link based
connectivity between containers that are running on the same host.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.log_driver">
<em class="property">property </em><code class="sig-name descname">log_driver</code><a class="headerlink" href="#pulumi_docker.Container.log_driver" title="Permalink to this definition">¶</a></dt>
<dd><p>The logging driver to use for the container.
Defaults to “json-file”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.log_opts">
<em class="property">property </em><code class="sig-name descname">log_opts</code><a class="headerlink" href="#pulumi_docker.Container.log_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/value pairs to use as options for
the logging driver.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.logs">
<em class="property">property </em><code class="sig-name descname">logs</code><a class="headerlink" href="#pulumi_docker.Container.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>Save the container logs (<code class="docutils literal notranslate"><span class="pre">attach</span></code> must be enabled).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.max_retry_count">
<em class="property">property </em><code class="sig-name descname">max_retry_count</code><a class="headerlink" href="#pulumi_docker.Container.max_retry_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of times to an attempt
a restart when <code class="docutils literal notranslate"><span class="pre">restart</span></code> is set to “on-failure”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.memory">
<em class="property">property </em><code class="sig-name descname">memory</code><a class="headerlink" href="#pulumi_docker.Container.memory" title="Permalink to this definition">¶</a></dt>
<dd><p>The memory limit for the container in MBs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.mounts">
<em class="property">property </em><code class="sig-name descname">mounts</code><a class="headerlink" href="#pulumi_docker.Container.mounts" title="Permalink to this definition">¶</a></dt>
<dd><p>See Mounts below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.network_aliases">
<em class="property">property </em><code class="sig-name descname">network_aliases</code><a class="headerlink" href="#pulumi_docker.Container.network_aliases" title="Permalink to this definition">¶</a></dt>
<dd><p>Network aliases of the container for user-defined networks only. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.network_datas">
<em class="property">property </em><code class="sig-name descname">network_datas</code><a class="headerlink" href="#pulumi_docker.Container.network_datas" title="Permalink to this definition">¶</a></dt>
<dd><p>(Map of a block) The IP addresses of the container on each
network. Key are the network names, values are the IP addresses.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.network_mode">
<em class="property">property </em><code class="sig-name descname">network_mode</code><a class="headerlink" href="#pulumi_docker.Container.network_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Network mode of the container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.networks">
<em class="property">property </em><code class="sig-name descname">networks</code><a class="headerlink" href="#pulumi_docker.Container.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the networks in which the
container is. <em>Deprecated:</em> use <code class="docutils literal notranslate"><span class="pre">networks_advanced</span></code> instead.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.networks_advanced">
<em class="property">property </em><code class="sig-name descname">networks_advanced</code><a class="headerlink" href="#pulumi_docker.Container.networks_advanced" title="Permalink to this definition">¶</a></dt>
<dd><p>See Networks Advanced below for details. If this block has priority to the deprecated <code class="docutils literal notranslate"><span class="pre">network_alias</span></code> and <code class="docutils literal notranslate"><span class="pre">network</span></code> properties.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.pid_mode">
<em class="property">property </em><code class="sig-name descname">pid_mode</code><a class="headerlink" href="#pulumi_docker.Container.pid_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The PID (Process) Namespace mode for the container. Either <code class="docutils literal notranslate"><span class="pre">container:&lt;name|id&gt;</span></code> or <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.ports">
<em class="property">property </em><code class="sig-name descname">ports</code><a class="headerlink" href="#pulumi_docker.Container.ports" title="Permalink to this definition">¶</a></dt>
<dd><p>See Ports below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.privileged">
<em class="property">property </em><code class="sig-name descname">privileged</code><a class="headerlink" href="#pulumi_docker.Container.privileged" title="Permalink to this definition">¶</a></dt>
<dd><p>Run container in privileged mode.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.publish_all_ports">
<em class="property">property </em><code class="sig-name descname">publish_all_ports</code><a class="headerlink" href="#pulumi_docker.Container.publish_all_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>Publish all ports of the container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.read_only">
<em class="property">property </em><code class="sig-name descname">read_only</code><a class="headerlink" href="#pulumi_docker.Container.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, this volume will be readonly.
Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.restart">
<em class="property">property </em><code class="sig-name descname">restart</code><a class="headerlink" href="#pulumi_docker.Container.restart" title="Permalink to this definition">¶</a></dt>
<dd><p>The restart policy for the container. Must be
one of “no”, “on-failure”, “always”, “unless-stopped”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.shm_size">
<em class="property">property </em><code class="sig-name descname">shm_size</code><a class="headerlink" href="#pulumi_docker.Container.shm_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of <code class="docutils literal notranslate"><span class="pre">/dev/shm</span></code> in MBs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.start">
<em class="property">property </em><code class="sig-name descname">start</code><a class="headerlink" href="#pulumi_docker.Container.start" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, then the Docker container will be
started after creation. If false, then the container is only created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.sysctls">
<em class="property">property </em><code class="sig-name descname">sysctls</code><a class="headerlink" href="#pulumi_docker.Container.sysctls" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of kernel parameters (sysctls) to set in the container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.tmpfs">
<em class="property">property </em><code class="sig-name descname">tmpfs</code><a class="headerlink" href="#pulumi_docker.Container.tmpfs" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of container directories which should be replaced by <code class="docutils literal notranslate"><span class="pre">tmpfs</span> <span class="pre">mounts</span></code>, and their corresponding mount options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.ulimits">
<em class="property">property </em><code class="sig-name descname">ulimits</code><a class="headerlink" href="#pulumi_docker.Container.ulimits" title="Permalink to this definition">¶</a></dt>
<dd><p>See Ulimits below for
details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.uploads">
<em class="property">property </em><code class="sig-name descname">uploads</code><a class="headerlink" href="#pulumi_docker.Container.uploads" title="Permalink to this definition">¶</a></dt>
<dd><p>See File Upload below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.user">
<em class="property">property </em><code class="sig-name descname">user</code><a class="headerlink" href="#pulumi_docker.Container.user" title="Permalink to this definition">¶</a></dt>
<dd><p>User used for run the first process. Format is
<code class="docutils literal notranslate"><span class="pre">user</span></code> or <code class="docutils literal notranslate"><span class="pre">user:group</span></code> which user and group can be passed literraly or
by name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.userns_mode">
<em class="property">property </em><code class="sig-name descname">userns_mode</code><a class="headerlink" href="#pulumi_docker.Container.userns_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the usernamespace mode for the container when usernamespace remapping option is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.volumes">
<em class="property">property </em><code class="sig-name descname">volumes</code><a class="headerlink" href="#pulumi_docker.Container.volumes" title="Permalink to this definition">¶</a></dt>
<dd><p>See Volumes below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Container.working_dir">
<em class="property">property </em><code class="sig-name descname">working_dir</code><a class="headerlink" href="#pulumi_docker.Container.working_dir" title="Permalink to this definition">¶</a></dt>
<dd><p>The working directory for commands to run in</p>
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

<dl class="py exception">
<dt id="pulumi_docker.Error">
<em class="property">exception </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Error</code><a class="headerlink" href="#pulumi_docker.Error" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_docker.GetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">GetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">driver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.GetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetwork.</p>
<dl class="py method">
<dt id="pulumi_docker.GetNetworkResult.driver">
<em class="property">property </em><code class="sig-name descname">driver</code><a class="headerlink" href="#pulumi_docker.GetNetworkResult.driver" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional, string) The driver of the Docker network. 
Possible values are <code class="docutils literal notranslate"><span class="pre">bridge</span></code>, <code class="docutils literal notranslate"><span class="pre">host</span></code>, <code class="docutils literal notranslate"><span class="pre">overlay</span></code>, <code class="docutils literal notranslate"><span class="pre">macvlan</span></code>.
See [docker docs][networkdocs] for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.GetNetworkResult.options">
<em class="property">property </em><code class="sig-name descname">options</code><a class="headerlink" href="#pulumi_docker.GetNetworkResult.options" title="Permalink to this definition">¶</a></dt>
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
<dl class="py method">
<dt id="pulumi_docker.GetRegistryImageResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_docker.GetRegistryImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_docker.Image">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">build</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">, </span>pulumi_docker.docker.DockerBuild<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">local_image_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry</span><span class="p">:</span> <span class="n">Union[pulumi_docker.image.ImageRegistry, Awaitable[pulumi_docker.image.ImageRegistry], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_push</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>A docker.Image resource represents a Docker image built locally which is published and made
available via a remote Docker registry.  This can be used to ensure that a Docker source
directory from a local deployment environment is built and pushed to a cloud-hosted Docker
registry as part of a Pulumi deployment, so that it can be referenced as an image input from
other cloud services that reference Docker images - including Kubernetes Pods, AWS ECS Tasks, and
Azure Container Instances.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>image_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The qualified image name that will be pushed to the remote registry.
Must be a supported image name for the target registry user.  This name can include a tag at the end.  If
provided all pushed image resources will contain that tag as well.
Either [imageName] or [localImageName] can have a tag.  However, if both have a tag, then
those tags must match.</p></li>
<li><p><strong>DockerBuild</strong><strong>] </strong><strong>build</strong> (<em>Union</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>,</em>) – The Docker build context, as a folder path or a detailed
DockerBuild object.</p></li>
<li><p><strong>local_image_name</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em>) – The docker image name to build locally before tagging with
imageName.  If not provided, it will be given the value of to [imageName].  This name can include a tag at
the end.  If provided all pushed image resources will contain that tag as well.
Either [imageName] or [localImageName] can have a tag.  However, if both have a tag, then
those tags must match.</p></li>
<li><p><strong>registry</strong> (<em>Optional</em><em>[</em><em>pulumi.Input</em><em>[</em><em>ImageRegistry</em><em>]</em><em>]</em>) – Credentials for the docker registry to push to.</p></li>
<li><p><strong>skip_push</strong> (<em>Optional</em><em>[</em><em>bool</em><em>]</em>) – Skip push flag.</p></li>
<li><p><strong>opts</strong> (<em>Optional</em><em>[</em><a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a><em>]</em>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_docker.Image.image_name">
<code class="sig-name descname">image_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Image.image_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique pinned image name on the remote repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Image.registry_server">
<code class="sig-name descname">registry_server</code><em class="property">: pulumi.Output[Optional[str]]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Image.registry_server" title="Permalink to this definition">¶</a></dt>
<dd><p>The server the image is located at.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_docker.Image.base_image_name">
<code class="sig-name descname">base_image_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_docker.Image.base_image_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The base image name that was built and pushed.  This does not include the id annotation, so
is not pinned to the specific build performed by this docker.Image.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_docker.LooseVersion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">LooseVersion</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">vstring</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.LooseVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Version numbering for anarchists and software realists.
Implements the standard interface for version number classes as
described above.  A version number consists of a series of numbers,
separated by either periods or strings of letters.  When comparing
version numbers, the numeric components will be compared
numerically, and the alphabetic components lexically.  The following
are all valid version numbers, in no particular order:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="mf">1.5</span><span class="o">.</span><span class="mi">1</span>
<span class="mf">1.5</span><span class="o">.</span><span class="mi">2</span><span class="n">b2</span>
<span class="mi">161</span>
<span class="mf">3.10</span><span class="n">a</span>
<span class="mf">8.02</span>
<span class="mf">3.4</span><span class="n">j</span>
<span class="mf">1996.07</span><span class="o">.</span><span class="mi">12</span>
<span class="mf">3.2</span><span class="o">.</span><span class="n">pl0</span>
<span class="mf">3.1</span><span class="o">.</span><span class="mf">1.6</span>
<span class="mi">2</span><span class="n">g6</span>
<span class="mi">11</span><span class="n">g</span>
<span class="mf">0.960923</span>
<span class="mf">2.2</span><span class="n">beta29</span>
<span class="mf">1.13</span><span class="o">++</span>
<span class="mf">5.5</span><span class="o">.</span><span class="n">kw</span>
<span class="mf">2.0</span><span class="n">b1pl0</span>
</pre></div>
</div>
<p>In fact, there is no such thing as an invalid version number under
this scheme; the rules for comparison are simple and predictable,
but may not always give the results you want (for some definition
of “want”).</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_docker.Network">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attachable</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_duplicate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ingress</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_configs</span><span class="p">:</span> <span class="n">Union[List[Union[NetworkIpamConfigArgs, Mapping[str, Any], Awaitable[Union[NetworkIpamConfigArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[NetworkIpamConfigArgs, Mapping[str, Any], Awaitable[Union[NetworkIpamConfigArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_driver</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[List[Union[NetworkLabelArgs, Mapping[str, Any], Awaitable[Union[NetworkLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[NetworkLabelArgs, Mapping[str, Any], Awaitable[Union[NetworkLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Network" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Docker Network. This can be used alongside
<a class="reference external" href="https://www.terraform.io/docs/providers/docker/r/container.html">docker_container</a>
to create virtual networks within the docker environment.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_docker</span> <span class="k">as</span> <span class="nn">docker</span>

<span class="c1"># Create a new docker network</span>
<span class="n">private_network</span> <span class="o">=</span> <span class="n">docker</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;privateNetwork&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<li><p><strong>ipam_configs</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NetworkIpamConfigArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See IPAM config below for
details.</p></li>
<li><p><strong>ipam_driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Driver used by the custom IP scheme of the
network.</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable IPv6 networking.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NetworkLabelArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Labels below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker network.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Network specific options to be used by
the drivers.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_docker.Network.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attachable</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check_duplicate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ingress</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_configs</span><span class="p">:</span> <span class="n">Union[List[Union[NetworkIpamConfigArgs, Mapping[str, Any], Awaitable[Union[NetworkIpamConfigArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[NetworkIpamConfigArgs, Mapping[str, Any], Awaitable[Union[NetworkIpamConfigArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipam_driver</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[List[Union[NetworkLabelArgs, Mapping[str, Any], Awaitable[Union[NetworkLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[NetworkLabelArgs, Mapping[str, Any], Awaitable[Union[NetworkLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_docker.network.Network<a class="headerlink" href="#pulumi_docker.Network.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Network resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<li><p><strong>ipam_configs</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NetworkIpamConfigArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See IPAM config below for
details.</p></li>
<li><p><strong>ipam_driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Driver used by the custom IP scheme of the
network.</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable IPv6 networking.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'NetworkLabelArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Labels below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker network.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Network specific options to be used by
the drivers.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.attachable">
<em class="property">property </em><code class="sig-name descname">attachable</code><a class="headerlink" href="#pulumi_docker.Network.attachable" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable manual container attachment to the network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.check_duplicate">
<em class="property">property </em><code class="sig-name descname">check_duplicate</code><a class="headerlink" href="#pulumi_docker.Network.check_duplicate" title="Permalink to this definition">¶</a></dt>
<dd><p>Requests daemon to check for networks
with same name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.driver">
<em class="property">property </em><code class="sig-name descname">driver</code><a class="headerlink" href="#pulumi_docker.Network.driver" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the network driver to use. Defaults to
<code class="docutils literal notranslate"><span class="pre">bridge</span></code> driver.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.ingress">
<em class="property">property </em><code class="sig-name descname">ingress</code><a class="headerlink" href="#pulumi_docker.Network.ingress" title="Permalink to this definition">¶</a></dt>
<dd><p>Create swarm routing-mesh network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.internal">
<em class="property">property </em><code class="sig-name descname">internal</code><a class="headerlink" href="#pulumi_docker.Network.internal" title="Permalink to this definition">¶</a></dt>
<dd><p>Restrict external access to the network.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.ipam_configs">
<em class="property">property </em><code class="sig-name descname">ipam_configs</code><a class="headerlink" href="#pulumi_docker.Network.ipam_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>See IPAM config below for
details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.ipam_driver">
<em class="property">property </em><code class="sig-name descname">ipam_driver</code><a class="headerlink" href="#pulumi_docker.Network.ipam_driver" title="Permalink to this definition">¶</a></dt>
<dd><p>Driver used by the custom IP scheme of the
network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.ipv6">
<em class="property">property </em><code class="sig-name descname">ipv6</code><a class="headerlink" href="#pulumi_docker.Network.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable IPv6 networking.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_docker.Network.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>See Labels below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_docker.Network.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Network.options">
<em class="property">property </em><code class="sig-name descname">options</code><a class="headerlink" href="#pulumi_docker.Network.options" title="Permalink to this definition">¶</a></dt>
<dd><p>Network specific options to be used by
the drivers.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_material</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert_material</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cert_path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_material</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_auth</span><span class="p">:</span> <span class="n">Union[List[Union[ProviderRegistryAuthArgs, Mapping[str, Any], Awaitable[Union[ProviderRegistryAuthArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ProviderRegistryAuthArgs, Mapping[str, Any], Awaitable[Union[ProviderRegistryAuthArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Provider" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">RemoteImage</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_locally</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_trigger</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_triggers</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.RemoteImage" title="Permalink to this definition">¶</a></dt>
<dd><p>Pulls a Docker image to a given Docker host from a Docker Registry.</p>
<p>This resource will <em>not</em> pull new layers of the image automatically unless used in
conjunction with <cite>``getRegistryImage`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/docker/d/registry_image.html">https://www.terraform.io/docs/providers/docker/d/registry_image.html</a>&gt;`_
data source to update the <code class="docutils literal notranslate"><span class="pre">pull_triggers</span></code> field.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_docker</span> <span class="k">as</span> <span class="nn">docker</span>

<span class="c1"># Find the latest Ubuntu precise image.</span>
<span class="n">ubuntu</span> <span class="o">=</span> <span class="n">docker</span><span class="o">.</span><span class="n">RemoteImage</span><span class="p">(</span><span class="s2">&quot;ubuntu&quot;</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;ubuntu:precise&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_docker</span> <span class="k">as</span> <span class="nn">docker</span>

<span class="n">ubuntu_registry_image</span> <span class="o">=</span> <span class="n">docker</span><span class="o">.</span><span class="n">get_registry_image</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;ubuntu:precise&quot;</span><span class="p">)</span>
<span class="n">ubuntu_remote_image</span> <span class="o">=</span> <span class="n">docker</span><span class="o">.</span><span class="n">RemoteImage</span><span class="p">(</span><span class="s2">&quot;ubuntuRemoteImage&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="n">ubuntu_registry_image</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">pull_triggers</span><span class="o">=</span><span class="p">[</span><span class="n">ubuntu_registry_image</span><span class="o">.</span><span class="n">sha256_digest</span><span class="p">])</span>
</pre></div>
</div>
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
<li><p><strong>pull_triggers</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of values which cause an
image pull when changed. This is used to store the image digest from the
registry when using the <code class="docutils literal notranslate"><span class="pre">getRegistryImage</span></code> <a class="reference external" href="https://www.terraform.io/docs/providers/docker/d/registry_image.html">data source</a>
to trigger an image update.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_docker.RemoteImage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_locally</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_trigger</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_triggers</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_docker.remote_image.RemoteImage<a class="headerlink" href="#pulumi_docker.RemoteImage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RemoteImage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>keep_locally</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, then the Docker image won’t be
deleted on destroy operation. If this is false, it will delete the image from
the docker local storage on destroy operation.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker image, including any tags or SHA256 repo digests.</p></li>
<li><p><strong>pull_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>Deprecated</strong>, use <code class="docutils literal notranslate"><span class="pre">pull_triggers</span></code> instead.</p></li>
<li><p><strong>pull_triggers</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>List of values which cause an
image pull when changed. This is used to store the image digest from the
registry when using the <code class="docutils literal notranslate"><span class="pre">getRegistryImage</span></code> <a class="reference external" href="https://www.terraform.io/docs/providers/docker/d/registry_image.html">data source</a>
to trigger an image update.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.RemoteImage.keep_locally">
<em class="property">property </em><code class="sig-name descname">keep_locally</code><a class="headerlink" href="#pulumi_docker.RemoteImage.keep_locally" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, then the Docker image won’t be
deleted on destroy operation. If this is false, it will delete the image from
the docker local storage on destroy operation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.RemoteImage.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_docker.RemoteImage.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker image, including any tags or SHA256 repo digests.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.RemoteImage.pull_trigger">
<em class="property">property </em><code class="sig-name descname">pull_trigger</code><a class="headerlink" href="#pulumi_docker.RemoteImage.pull_trigger" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>Deprecated</strong>, use <code class="docutils literal notranslate"><span class="pre">pull_triggers</span></code> instead.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.RemoteImage.pull_triggers">
<em class="property">property </em><code class="sig-name descname">pull_triggers</code><a class="headerlink" href="#pulumi_docker.RemoteImage.pull_triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of values which cause an
image pull when changed. This is used to store the image digest from the
registry when using the <code class="docutils literal notranslate"><span class="pre">getRegistryImage</span></code> <a class="reference external" href="https://www.terraform.io/docs/providers/docker/d/registry_image.html">data source</a>
to trigger an image update.</p>
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

<dl class="py exception">
<dt id="pulumi_docker.ResourceError">
<em class="property">exception </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">ResourceError</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">resource</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.Resource<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">hide_stack</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">False</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.ResourceError" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_docker.Secret">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Secret</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[List[Union[SecretLabelArgs, Mapping[str, Any], Awaitable[Union[SecretLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[SecretLabelArgs, Mapping[str, Any], Awaitable[Union[SecretLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Secret resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] data: The base64 encoded data of the secret.
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘SecretLabelArgs’]]]] labels: See Labels below for details.
:param pulumi.Input[str] name: The name of the Docker secret.</p>
<dl class="py method">
<dt id="pulumi_docker.Secret.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[List[Union[SecretLabelArgs, Mapping[str, Any], Awaitable[Union[SecretLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[SecretLabelArgs, Mapping[str, Any], Awaitable[Union[SecretLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_docker.secret.Secret<a class="headerlink" href="#pulumi_docker.Secret.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Secret resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64 encoded data of the secret.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SecretLabelArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Labels below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker secret.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Secret.data">
<em class="property">property </em><code class="sig-name descname">data</code><a class="headerlink" href="#pulumi_docker.Secret.data" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64 encoded data of the secret.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Secret.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_docker.Secret.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>See Labels below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Secret.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_docker.Secret.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker secret.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth</span><span class="p">:</span> <span class="n">Union[ServiceAuthArgs, Mapping[str, Any], Awaitable[Union[ServiceAuthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">converge_config</span><span class="p">:</span> <span class="n">Union[ServiceConvergeConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceConvergeConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_spec</span><span class="p">:</span> <span class="n">Union[ServiceEndpointSpecArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointSpecArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[List[Union[ServiceLabelArgs, Mapping[str, Any], Awaitable[Union[ServiceLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ServiceLabelArgs, Mapping[str, Any], Awaitable[Union[ServiceLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[ServiceModeArgs, Mapping[str, Any], Awaitable[Union[ServiceModeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rollback_config</span><span class="p">:</span> <span class="n">Union[ServiceRollbackConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceRollbackConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_spec</span><span class="p">:</span> <span class="n">Union[ServiceTaskSpecArgs, Mapping[str, Any], Awaitable[Union[ServiceTaskSpecArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_config</span><span class="p">:</span> <span class="n">Union[ServiceUpdateConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceUpdateConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Service resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[pulumi.InputType[‘ServiceAuthArgs’]] auth: See Auth below for details.
:param pulumi.Input[pulumi.InputType[‘ServiceConvergeConfigArgs’]] converge_config: See Converge Config below for details.
:param pulumi.Input[pulumi.InputType[‘ServiceEndpointSpecArgs’]] endpoint_spec: See EndpointSpec below for details.
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘ServiceLabelArgs’]]]] labels: See Labels below for details.
:param pulumi.Input[pulumi.InputType[‘ServiceModeArgs’]] mode: See Mode below for details.
:param pulumi.Input[str] name: The name of the Docker service.
:param pulumi.Input[pulumi.InputType[‘ServiceRollbackConfigArgs’]] rollback_config: See RollbackConfig below for details.
:param pulumi.Input[pulumi.InputType[‘ServiceTaskSpecArgs’]] task_spec: See TaskSpec below for details.
:param pulumi.Input[pulumi.InputType[‘ServiceUpdateConfigArgs’]] update_config: See UpdateConfig below for details.</p>
<dl class="py method">
<dt id="pulumi_docker.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth</span><span class="p">:</span> <span class="n">Union[ServiceAuthArgs, Mapping[str, Any], Awaitable[Union[ServiceAuthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">converge_config</span><span class="p">:</span> <span class="n">Union[ServiceConvergeConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceConvergeConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_spec</span><span class="p">:</span> <span class="n">Union[ServiceEndpointSpecArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointSpecArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[List[Union[ServiceLabelArgs, Mapping[str, Any], Awaitable[Union[ServiceLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ServiceLabelArgs, Mapping[str, Any], Awaitable[Union[ServiceLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[ServiceModeArgs, Mapping[str, Any], Awaitable[Union[ServiceModeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rollback_config</span><span class="p">:</span> <span class="n">Union[ServiceRollbackConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceRollbackConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_spec</span><span class="p">:</span> <span class="n">Union[ServiceTaskSpecArgs, Mapping[str, Any], Awaitable[Union[ServiceTaskSpecArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_config</span><span class="p">:</span> <span class="n">Union[ServiceUpdateConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceUpdateConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_docker.service.Service<a class="headerlink" href="#pulumi_docker.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceAuthArgs'</em><em>]</em><em>]</em>) – See Auth below for details.</p></li>
<li><p><strong>converge_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceConvergeConfigArgs'</em><em>]</em><em>]</em>) – See Converge Config below for details.</p></li>
<li><p><strong>endpoint_spec</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointSpecArgs'</em><em>]</em><em>]</em>) – See EndpointSpec below for details.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLabelArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Labels below for details.</p></li>
<li><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceModeArgs'</em><em>]</em><em>]</em>) – See Mode below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker service.</p></li>
<li><p><strong>rollback_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceRollbackConfigArgs'</em><em>]</em><em>]</em>) – See RollbackConfig below for details.</p></li>
<li><p><strong>task_spec</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceTaskSpecArgs'</em><em>]</em><em>]</em>) – See TaskSpec below for details.</p></li>
<li><p><strong>update_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceUpdateConfigArgs'</em><em>]</em><em>]</em>) – See UpdateConfig below for details.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.auth">
<em class="property">property </em><code class="sig-name descname">auth</code><a class="headerlink" href="#pulumi_docker.Service.auth" title="Permalink to this definition">¶</a></dt>
<dd><p>See Auth below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.converge_config">
<em class="property">property </em><code class="sig-name descname">converge_config</code><a class="headerlink" href="#pulumi_docker.Service.converge_config" title="Permalink to this definition">¶</a></dt>
<dd><p>See Converge Config below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.endpoint_spec">
<em class="property">property </em><code class="sig-name descname">endpoint_spec</code><a class="headerlink" href="#pulumi_docker.Service.endpoint_spec" title="Permalink to this definition">¶</a></dt>
<dd><p>See EndpointSpec below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_docker.Service.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>See Labels below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.mode">
<em class="property">property </em><code class="sig-name descname">mode</code><a class="headerlink" href="#pulumi_docker.Service.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>See Mode below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_docker.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.rollback_config">
<em class="property">property </em><code class="sig-name descname">rollback_config</code><a class="headerlink" href="#pulumi_docker.Service.rollback_config" title="Permalink to this definition">¶</a></dt>
<dd><p>See RollbackConfig below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.task_spec">
<em class="property">property </em><code class="sig-name descname">task_spec</code><a class="headerlink" href="#pulumi_docker.Service.task_spec" title="Permalink to this definition">¶</a></dt>
<dd><p>See TaskSpec below for details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Service.update_config">
<em class="property">property </em><code class="sig-name descname">update_config</code><a class="headerlink" href="#pulumi_docker.Service.update_config" title="Permalink to this definition">¶</a></dt>
<dd><p>See UpdateConfig below for details.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">ServiceConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.ServiceConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ServiceConfig resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] data: The base64 encoded data of the config.
:param pulumi.Input[str] name: The name of the Docker config.</p>
<dl class="py method">
<dt id="pulumi_docker.ServiceConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_docker.service_config.ServiceConfig<a class="headerlink" href="#pulumi_docker.ServiceConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64 encoded data of the config.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker config.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.ServiceConfig.data">
<em class="property">property </em><code class="sig-name descname">data</code><a class="headerlink" href="#pulumi_docker.ServiceConfig.data" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64 encoded data of the config.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.ServiceConfig.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_docker.ServiceConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker config.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver_opts</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[List[Union[VolumeLabelArgs, Mapping[str, Any], Awaitable[Union[VolumeLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[VolumeLabelArgs, Mapping[str, Any], Awaitable[Union[VolumeLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_docker.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and destroys a volume in Docker. This can be used alongside
<a class="reference external" href="https://www.terraform.io/docs/providers/docker/r/container.html">docker_container</a>
to prepare volumes that can be shared across containers.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_docker</span> <span class="k">as</span> <span class="nn">docker</span>

<span class="c1"># Creates a docker volume &quot;shared_volume&quot;.</span>
<span class="n">shared_volume</span> <span class="o">=</span> <span class="n">docker</span><span class="o">.</span><span class="n">Volume</span><span class="p">(</span><span class="s2">&quot;sharedVolume&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Driver type for the volume (defaults to local).</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>driver_opts</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Options specific to the driver.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'VolumeLabelArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – User-defined key/value metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker volume (generated if not
provided).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_docker.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">driver_opts</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[List[Union[VolumeLabelArgs, Mapping[str, Any], Awaitable[Union[VolumeLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[VolumeLabelArgs, Mapping[str, Any], Awaitable[Union[VolumeLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mountpoint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_docker.volume.Volume<a class="headerlink" href="#pulumi_docker.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>driver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Driver type for the volume (defaults to local).</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>driver_opts</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Options specific to the driver.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'VolumeLabelArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – User-defined key/value metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Docker volume (generated if not
provided).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Volume.driver">
<em class="property">property </em><code class="sig-name descname">driver</code><a class="headerlink" href="#pulumi_docker.Volume.driver" title="Permalink to this definition">¶</a></dt>
<dd><p>Driver type for the volume (defaults to local).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Volume.driver_opts">
<em class="property">property </em><code class="sig-name descname">driver_opts</code><a class="headerlink" href="#pulumi_docker.Volume.driver_opts" title="Permalink to this definition">¶</a></dt>
<dd><p>Options specific to the driver.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Volume.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_docker.Volume.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined key/value metadata.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_docker.Volume.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_docker.Volume.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Docker volume (generated if not
provided).</p>
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
<dt id="pulumi_docker.build_and_push_image">
<code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">build_and_push_image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">base_image_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">path_or_build</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>pulumi_docker.docker.DockerBuild<span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>pulumi_docker.docker.DockerBuild<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">repository_url</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">log_resource</span><span class="p">:</span> <span class="n">pulumi.resource.Resource</span></em>, <em class="sig-param"><span class="n">registry</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi_docker.docker.Registry<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">skip_push</span><span class="p">:</span> <span class="n">bool</span> <span class="o">=</span> <span class="default_value">False</span></em><span class="sig-paren">)</span> &#x2192; str<a class="headerlink" href="#pulumi_docker.build_and_push_image" title="Permalink to this definition">¶</a></dt>
<dd><p>build_and_push_image will build and push the Dockerfile and context from [pathOrBuild] into the
requested docker repo [repository_url].  It returns the unique target image name for the image in
the docker repository.  During preview this will build the image, and return the target image
name, without pushing. During a normal update, it will do the same, as well as tag and push the
image.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_docker.get_network">
<code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">get_network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_docker.get_network.AwaitableGetNetworkResult<a class="headerlink" href="#pulumi_docker.get_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Finds a specific docker network and returns information about it.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_docker</span> <span class="k">as</span> <span class="nn">docker</span>

<span class="n">main</span> <span class="o">=</span> <span class="n">docker</span><span class="o">.</span><span class="n">get_network</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;main&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">get_registry_image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_docker.get_registry_image.AwaitableGetRegistryImageResult<a class="headerlink" href="#pulumi_docker.get_registry_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Reads the image metadata from a Docker Registry. Used in conjunction with the
<a class="reference external" href="https://www.terraform.io/docs/providers/docker/r/image.html">docker_image</a> resource to keep an image up
to date on the latest available version of the tag.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_docker</span> <span class="k">as</span> <span class="nn">docker</span>

<span class="n">ubuntu_registry_image</span> <span class="o">=</span> <span class="n">docker</span><span class="o">.</span><span class="n">get_registry_image</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;ubuntu:precise&quot;</span><span class="p">)</span>
<span class="n">ubuntu_remote_image</span> <span class="o">=</span> <span class="n">docker</span><span class="o">.</span><span class="n">RemoteImage</span><span class="p">(</span><span class="s2">&quot;ubuntuRemoteImage&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="n">ubuntu_registry_image</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">pull_triggers</span><span class="o">=</span><span class="p">[</span><span class="n">ubuntu_registry_image</span><span class="o">.</span><span class="n">sha256_digest</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the Docker image, including any tags. e.g. <code class="docutils literal notranslate"><span class="pre">alpine:latest</span></code></p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_docker.random">
<code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">random</code><span class="sig-paren">(</span><span class="sig-paren">)</span> &#x2192; x in the interval [0, 1).<a class="headerlink" href="#pulumi_docker.random" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py function">
<dt id="pulumi_docker.run_command_that_can_fail">
<code class="sig-prename descclassname">pulumi_docker.</code><code class="sig-name descname">run_command_that_can_fail</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cmd_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">args</span><span class="p">:</span> <span class="n">Sequence<span class="p">[</span>str<span class="p">]</span></span></em>, <em class="sig-param"><span class="n">log_resource</span><span class="p">:</span> <span class="n">pulumi.resource.Resource</span></em>, <em class="sig-param"><span class="n">report_full_command_line</span><span class="p">:</span> <span class="n">bool</span></em>, <em class="sig-param"><span class="n">report_error_as_warning</span><span class="p">:</span> <span class="n">bool</span></em>, <em class="sig-param"><span class="n">stdin</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">env</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_docker.docker.CommandResult<a class="headerlink" href="#pulumi_docker.run_command_that_can_fail" title="Permalink to this definition">¶</a></dt>
<dd><p>Runs a CLI command in a child process, returning a future for the process’s exit. Both stdout
and stderr are redirected to process.stdout and process.stderr by default.</p>
<p>If the [stdin] argument is defined, its contents are piped into stdin for the child process.</p>
<p>[log_resource] is used to specify the resource to associate command output with. Stderr messages
are always sent (since they may contain important information about something that’s gone wrong).
Stdout messages will be logged ephemerally to this resource.  This lets the user know there is
progress, without having that dumped on them at the end.  If an error occurs though, the stdout
content will be printed.</p>
</dd></dl>

</div>
