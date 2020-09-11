---
title: Package pulumi_hcloud
title_tag: Package pulumi_hcloud | Python SDK
linktitle: pulumi_hcloud
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "hcloud" >}}

<div class="section" id="pulumi-hcloud">
<h1>Pulumi HCloud<a class="headerlink" href="#pulumi-hcloud" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-hcloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-hcloud/issues">pulumi/pulumi-hcloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-hcloud/issues">terraform-providers/terraform-provider-hcloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_hcloud"></span><dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetCertificateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetCertificateResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_valid_after</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_valid_before</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetDatacenterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetDatacenterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_server_type_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supported_server_type_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetDatacenterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetDatacentersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetDatacentersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetDatacentersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetFloatingIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetFloatingIpResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">home_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetFloatingIpResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprecated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">most_recent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">os_flavor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">os_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rapid_deploy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetLoadBalancerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetLoadBalancerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetLoadBalancerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetLocationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetLocationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">city</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latitude</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">longitude</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetLocationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetLocationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetLocationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">descriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetLocationsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetServerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backup_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iso</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rescue</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetServerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetSshKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetSshKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetSshKeysResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.AwaitableGetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">AwaitableGetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linux_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.AwaitableGetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.Certificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Clould Certificate to represent a TLS certificate in the Hetzner Cloud.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM encoded TLS certificate.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs) the
certificate should be created with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Certificate.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM encoded private key belonging to the certificate.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_names</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_valid_after</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_valid_before</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.certificate.Certificate<a class="headerlink" href="#pulumi_hcloud.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM encoded TLS certificate.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).</p></li>
<li><p><strong>domain_names</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – (list) Domains and subdomains covered by the certificate.</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) Fingerprint of the certificate.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs) the
certificate should be created with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Certificate.</p></li>
<li><p><strong>not_valid_after</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) Point in time when the Certificate stops being valid (in ISO-8601 format).</p></li>
<li><p><strong>not_valid_before</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) Point in time when the Certificate becomes valid (in ISO-8601 format).</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM encoded private key belonging to the certificate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Certificate.certificate">
<em class="property">property </em><code class="sig-name descname">certificate</code><a class="headerlink" href="#pulumi_hcloud.Certificate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM encoded TLS certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Certificate.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_hcloud.Certificate.created" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Certificate.domain_names">
<em class="property">property </em><code class="sig-name descname">domain_names</code><a class="headerlink" href="#pulumi_hcloud.Certificate.domain_names" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) Domains and subdomains covered by the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Certificate.fingerprint">
<em class="property">property </em><code class="sig-name descname">fingerprint</code><a class="headerlink" href="#pulumi_hcloud.Certificate.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Fingerprint of the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Certificate.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_hcloud.Certificate.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined labels (key-value pairs) the
certificate should be created with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Certificate.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Certificate.not_valid_after">
<em class="property">property </em><code class="sig-name descname">not_valid_after</code><a class="headerlink" href="#pulumi_hcloud.Certificate.not_valid_after" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Point in time when the Certificate stops being valid (in ISO-8601 format).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Certificate.not_valid_before">
<em class="property">property </em><code class="sig-name descname">not_valid_before</code><a class="headerlink" href="#pulumi_hcloud.Certificate.not_valid_before" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Point in time when the Certificate becomes valid (in ISO-8601 format).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Certificate.private_key">
<em class="property">property </em><code class="sig-name descname">private_key</code><a class="headerlink" href="#pulumi_hcloud.Certificate.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM encoded private key belonging to the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Certificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Certificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.FloatingIp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">FloatingIp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">home_location</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.FloatingIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Floating IP to represent a publicly-accessible static IP address that can be mapped to one of your servers.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">FloatingIp</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;ipv4&quot;</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the Floating IP.</p></li>
<li><p><strong>home_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Home location (routing is optimized for that location). Optional if server_id argument is passed.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs) should be created with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Floating IP.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Server to assign the Floating IP to.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the Floating IP. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> <code class="docutils literal notranslate"><span class="pre">ipv6</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">home_location</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_network</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.floating_ip.FloatingIp<a class="headerlink" href="#pulumi_hcloud.FloatingIp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FloatingIp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the Floating IP.</p></li>
<li><p><strong>home_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Home location (routing is optimized for that location). Optional if server_id argument is passed.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) IP Address of the Floating IP.</p></li>
<li><p><strong>ip_network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) IPv6 subnet. (Only set if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>)</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs) should be created with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Floating IP.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Server to assign the Floating IP to.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the Floating IP. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> <code class="docutils literal notranslate"><span class="pre">ipv6</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_hcloud.FloatingIp.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the Floating IP.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.home_location">
<em class="property">property </em><code class="sig-name descname">home_location</code><a class="headerlink" href="#pulumi_hcloud.FloatingIp.home_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Home location (routing is optimized for that location). Optional if server_id argument is passed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.ip_address">
<em class="property">property </em><code class="sig-name descname">ip_address</code><a class="headerlink" href="#pulumi_hcloud.FloatingIp.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) IP Address of the Floating IP.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.ip_network">
<em class="property">property </em><code class="sig-name descname">ip_network</code><a class="headerlink" href="#pulumi_hcloud.FloatingIp.ip_network" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) IPv6 subnet. (Only set if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_hcloud.FloatingIp.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined labels (key-value pairs) should be created with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.FloatingIp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Floating IP.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.server_id">
<em class="property">property </em><code class="sig-name descname">server_id</code><a class="headerlink" href="#pulumi_hcloud.FloatingIp.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Server to assign the Floating IP to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_hcloud.FloatingIp.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the Floating IP. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> <code class="docutils literal notranslate"><span class="pre">ipv6</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.FloatingIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.FloatingIp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.FloatingIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.FloatingIpAssignment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">FloatingIpAssignment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">floating_ip_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.FloatingIpAssignment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Floating IP Assignment to assign a Floating IP to a Hetzner Cloud Server. Deleting a Floating IP Assignment will unassign the Floating IP from the Server.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">,</span>
    <span class="n">datacenter</span><span class="o">=</span><span class="s2">&quot;fsn1-dc8&quot;</span><span class="p">)</span>
<span class="n">master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">FloatingIp</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;ipv4&quot;</span><span class="p">,</span>
    <span class="n">home_location</span><span class="o">=</span><span class="s2">&quot;nbg1&quot;</span><span class="p">)</span>
<span class="n">main</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">FloatingIpAssignment</span><span class="p">(</span><span class="s2">&quot;main&quot;</span><span class="p">,</span>
    <span class="n">floating_ip_id</span><span class="o">=</span><span class="n">master</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>floating_ip_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Floating IP.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Server to assign the Floating IP to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.FloatingIpAssignment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">floating_ip_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.floating_ip_assignment.FloatingIpAssignment<a class="headerlink" href="#pulumi_hcloud.FloatingIpAssignment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FloatingIpAssignment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>floating_ip_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Floating IP.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Server to assign the Floating IP to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIpAssignment.floating_ip_id">
<em class="property">property </em><code class="sig-name descname">floating_ip_id</code><a class="headerlink" href="#pulumi_hcloud.FloatingIpAssignment.floating_ip_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Floating IP.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIpAssignment.server_id">
<em class="property">property </em><code class="sig-name descname">server_id</code><a class="headerlink" href="#pulumi_hcloud.FloatingIpAssignment.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Server to assign the Floating IP to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.FloatingIpAssignment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.FloatingIpAssignment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.FloatingIpAssignment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.FloatingIpAssignment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.GetCertificateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetCertificateResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_valid_after</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_valid_before</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificate.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetCertificateResult.certificate">
<em class="property">property </em><code class="sig-name descname">certificate</code><a class="headerlink" href="#pulumi_hcloud.GetCertificateResult.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) PEM encoded TLS certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetCertificateResult.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_hcloud.GetCertificateResult.created" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetCertificateResult.domain_names">
<em class="property">property </em><code class="sig-name descname">domain_names</code><a class="headerlink" href="#pulumi_hcloud.GetCertificateResult.domain_names" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) Domains and subdomains covered by the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetCertificateResult.fingerprint">
<em class="property">property </em><code class="sig-name descname">fingerprint</code><a class="headerlink" href="#pulumi_hcloud.GetCertificateResult.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Fingerprint of the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetCertificateResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetCertificateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>(int) Unique ID of the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetCertificateResult.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_hcloud.GetCertificateResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>(map) User-defined labels (key-value pairs) assigned to the certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetCertificateResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.GetCertificateResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name of the Certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetCertificateResult.not_valid_after">
<em class="property">property </em><code class="sig-name descname">not_valid_after</code><a class="headerlink" href="#pulumi_hcloud.GetCertificateResult.not_valid_after" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Point in time when the Certificate stops being valid (in ISO-8601 format).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetCertificateResult.not_valid_before">
<em class="property">property </em><code class="sig-name descname">not_valid_before</code><a class="headerlink" href="#pulumi_hcloud.GetCertificateResult.not_valid_before" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Point in time when the Certificate becomes valid (in ISO-8601 format).</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetDatacenterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetDatacenterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_server_type_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supported_server_type_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetDatacenterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatacenter.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetDatacenterResult.available_server_type_ids">
<em class="property">property </em><code class="sig-name descname">available_server_type_ids</code><a class="headerlink" href="#pulumi_hcloud.GetDatacenterResult.available_server_type_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of available server types.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetDatacenterResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_hcloud.GetDatacenterResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Description of the datacenter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetDatacenterResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetDatacenterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>(int) Unique ID of the datacenter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetDatacenterResult.location">
<em class="property">property </em><code class="sig-name descname">location</code><a class="headerlink" href="#pulumi_hcloud.GetDatacenterResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>(map) Physical datacenter location.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetDatacenterResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.GetDatacenterResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name of the datacenter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetDatacenterResult.supported_server_type_ids">
<em class="property">property </em><code class="sig-name descname">supported_server_type_ids</code><a class="headerlink" href="#pulumi_hcloud.GetDatacenterResult.supported_server_type_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of server types supported by the datacenter.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetDatacentersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetDatacentersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetDatacentersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatacenters.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetDatacentersResult.datacenter_ids">
<em class="property">property </em><code class="sig-name descname">datacenter_ids</code><a class="headerlink" href="#pulumi_hcloud.GetDatacentersResult.datacenter_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of unique datacenter identifiers.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetDatacentersResult.descriptions">
<em class="property">property </em><code class="sig-name descname">descriptions</code><a class="headerlink" href="#pulumi_hcloud.GetDatacentersResult.descriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of all datacenter descriptions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetDatacentersResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetDatacentersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetDatacentersResult.names">
<em class="property">property </em><code class="sig-name descname">names</code><a class="headerlink" href="#pulumi_hcloud.GetDatacentersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of datacenter names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetFloatingIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetFloatingIpResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">home_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetFloatingIpResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFloatingIp.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetFloatingIpResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetFloatingIpResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>(int) Unique ID of the Floating IP.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetFloatingIpResult.ip_address">
<em class="property">property </em><code class="sig-name descname">ip_address</code><a class="headerlink" href="#pulumi_hcloud.GetFloatingIpResult.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) IP address of the Floating IP.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprecated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">most_recent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">os_flavor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">os_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rapid_deploy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetImageResult.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_hcloud.GetImageResult.created" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Date when the Image was created (in ISO-8601 format).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetImageResult.deprecated">
<em class="property">property </em><code class="sig-name descname">deprecated</code><a class="headerlink" href="#pulumi_hcloud.GetImageResult.deprecated" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Point in time when the image is considered to be deprecated (in ISO-8601 format).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetImageResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_hcloud.GetImageResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Description of the Image.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetImageResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>(int) Unique ID of the Image.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetImageResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.GetImageResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name of the Image, only present when the Image is of type <code class="docutils literal notranslate"><span class="pre">system</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetImageResult.os_flavor">
<em class="property">property </em><code class="sig-name descname">os_flavor</code><a class="headerlink" href="#pulumi_hcloud.GetImageResult.os_flavor" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Flavor of operating system contained in the image, could be <code class="docutils literal notranslate"><span class="pre">ubuntu</span></code>, <code class="docutils literal notranslate"><span class="pre">centos</span></code>, <code class="docutils literal notranslate"><span class="pre">debian</span></code>, <code class="docutils literal notranslate"><span class="pre">fedora</span></code> or <code class="docutils literal notranslate"><span class="pre">unknown</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetImageResult.os_version">
<em class="property">property </em><code class="sig-name descname">os_version</code><a class="headerlink" href="#pulumi_hcloud.GetImageResult.os_version" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Operating system version.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetImageResult.rapid_deploy">
<em class="property">property </em><code class="sig-name descname">rapid_deploy</code><a class="headerlink" href="#pulumi_hcloud.GetImageResult.rapid_deploy" title="Permalink to this definition">¶</a></dt>
<dd><p>(bool) Indicates that rapid deploy of the image is available.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetImageResult.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_hcloud.GetImageResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Type of the Image, could be <code class="docutils literal notranslate"><span class="pre">system</span></code>, <code class="docutils literal notranslate"><span class="pre">backup</span></code> or <code class="docutils literal notranslate"><span class="pre">snapshot</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetLoadBalancerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetLoadBalancerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLoadBalancer.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetLoadBalancerResult.algorithm">
<em class="property">property </em><code class="sig-name descname">algorithm</code><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) Configuration of the algorithm the Load Balancer use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLoadBalancerResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>(int) Unique ID of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLoadBalancerResult.ipv4">
<em class="property">property </em><code class="sig-name descname">ipv4</code><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult.ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) IPv4 Address of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLoadBalancerResult.ipv6">
<em class="property">property </em><code class="sig-name descname">ipv6</code><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) IPv4 Address of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLoadBalancerResult.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>(map) User-defined labels (key-value pairs) .</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLoadBalancerResult.load_balancer_type">
<em class="property">property </em><code class="sig-name descname">load_balancer_type</code><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult.load_balancer_type" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name of the Type of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLoadBalancerResult.location">
<em class="property">property </em><code class="sig-name descname">location</code><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name of the location the Load Balancer is in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLoadBalancerResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLoadBalancerResult.services">
<em class="property">property </em><code class="sig-name descname">services</code><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult.services" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of services a Load Balancer provides.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLoadBalancerResult.targets">
<em class="property">property </em><code class="sig-name descname">targets</code><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult.targets" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of targets of the Load Balancer.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetLocationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetLocationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">city</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latitude</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">longitude</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetLocationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLocation.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetLocationResult.city">
<em class="property">property </em><code class="sig-name descname">city</code><a class="headerlink" href="#pulumi_hcloud.GetLocationResult.city" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) City of the location.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLocationResult.country">
<em class="property">property </em><code class="sig-name descname">country</code><a class="headerlink" href="#pulumi_hcloud.GetLocationResult.country" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Country of the location.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLocationResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_hcloud.GetLocationResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Description of the location.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLocationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetLocationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>(int) Unique ID of the location.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLocationResult.latitude">
<em class="property">property </em><code class="sig-name descname">latitude</code><a class="headerlink" href="#pulumi_hcloud.GetLocationResult.latitude" title="Permalink to this definition">¶</a></dt>
<dd><p>(float) Latitude of the city.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLocationResult.longitude">
<em class="property">property </em><code class="sig-name descname">longitude</code><a class="headerlink" href="#pulumi_hcloud.GetLocationResult.longitude" title="Permalink to this definition">¶</a></dt>
<dd><p>(float) Longitude of the city.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLocationResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.GetLocationResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name of the location.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetLocationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetLocationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">descriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetLocationsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLocations.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetLocationsResult.descriptions">
<em class="property">property </em><code class="sig-name descname">descriptions</code><a class="headerlink" href="#pulumi_hcloud.GetLocationsResult.descriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of all location descriptions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLocationsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetLocationsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLocationsResult.location_ids">
<em class="property">property </em><code class="sig-name descname">location_ids</code><a class="headerlink" href="#pulumi_hcloud.GetLocationsResult.location_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of unique location identifiers.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetLocationsResult.names">
<em class="property">property </em><code class="sig-name descname">names</code><a class="headerlink" href="#pulumi_hcloud.GetLocationsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of location names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetwork.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetNetworkResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetNetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique ID of the Network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetNetworkResult.ip_range">
<em class="property">property </em><code class="sig-name descname">ip_range</code><a class="headerlink" href="#pulumi_hcloud.GetNetworkResult.ip_range" title="Permalink to this definition">¶</a></dt>
<dd><p>IPv4 prefix of the Network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetNetworkResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.GetNetworkResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Network.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetServerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backup_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iso</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rescue</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetServerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServer.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.backup_window">
<em class="property">property </em><code class="sig-name descname">backup_window</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The backup window of the server, if enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.backups">
<em class="property">property </em><code class="sig-name descname">backups</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.backups" title="Permalink to this definition">¶</a></dt>
<dd><p>(boolean) Whether backups are enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.datacenter">
<em class="property">property </em><code class="sig-name descname">datacenter</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The datacenter name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>(int) Unique ID of the server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.image">
<em class="property">property </em><code class="sig-name descname">image</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.image" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name or ID of the image the server was created from.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.ipv4_address">
<em class="property">property </em><code class="sig-name descname">ipv4_address</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.ipv4_address" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The IPv4 address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.ipv6_address">
<em class="property">property </em><code class="sig-name descname">ipv6_address</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.ipv6_address" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The first IPv6 address of the assigned network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.ipv6_network">
<em class="property">property </em><code class="sig-name descname">ipv6_network</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.ipv6_network" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The IPv6 network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.iso">
<em class="property">property </em><code class="sig-name descname">iso</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.iso" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) ID or Name of the mounted ISO image.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>(map) User-defined labels (key-value pairs)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.location">
<em class="property">property </em><code class="sig-name descname">location</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The location name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name of the server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.server_type">
<em class="property">property </em><code class="sig-name descname">server_type</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.server_type" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name of the server type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetServerResult.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_hcloud.GetServerResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The status of the server.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSshKey.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetSshKeyResult.fingerprint">
<em class="property">property </em><code class="sig-name descname">fingerprint</code><a class="headerlink" href="#pulumi_hcloud.GetSshKeyResult.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Fingerprint of the SSH Key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetSshKeyResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetSshKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>(int) Unique ID of the SSH Key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetSshKeyResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.GetSshKeyResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Name of the SSH Key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetSshKeyResult.public_key">
<em class="property">property </em><code class="sig-name descname">public_key</code><a class="headerlink" href="#pulumi_hcloud.GetSshKeyResult.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) Public Key of the SSH Key.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetSshKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetSshKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetSshKeysResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSshKeys.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetSshKeysResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetSshKeysResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetSshKeysResult.ssh_keys">
<em class="property">property </em><code class="sig-name descname">ssh_keys</code><a class="headerlink" href="#pulumi_hcloud.GetSshKeysResult.ssh_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>(list) List of all matches SSH keys. See <code class="docutils literal notranslate"><span class="pre">data.hcloud_ssh_key</span></code> for schema.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linux_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolume.</p>
<dl class="py method">
<dt id="pulumi_hcloud.GetVolumeResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_hcloud.GetVolumeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique ID of the volume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetVolumeResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.GetVolumeResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the volume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.GetVolumeResult.size">
<em class="property">property </em><code class="sig-name descname">size</code><a class="headerlink" href="#pulumi_hcloud.GetVolumeResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of the volume.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.LoadBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="p">:</span> <span class="n">Union[LoadBalancerAlgorithmArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerAlgorithmArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="p">:</span> <span class="n">Union[List[Union[LoadBalancerTargetArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerTargetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LoadBalancerTargetArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerTargetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Load Balancer to represent a Load Balancer in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">myserver</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;myserver&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;ubuntu-18.04&quot;</span><span class="p">)</span>
<span class="n">load_balancer</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancer</span><span class="p">(</span><span class="s2">&quot;loadBalancer&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_type</span><span class="o">=</span><span class="s2">&quot;lb11&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;nbg1&quot;</span><span class="p">,</span>
    <span class="n">targets</span><span class="o">=</span><span class="p">[</span><span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancerTargetArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;server&quot;</span><span class="p">,</span>
        <span class="n">server_id</span><span class="o">=</span><span class="n">myserver</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerAlgorithmArgs'</em><em>]</em><em>]</em>) – Configuration of the algorithm the Load Balancer use.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs) should be created with.</p></li>
<li><p><strong>load_balancer_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the Load Balancer.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the Load Balancer. Require when no network_zone is set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Load Balancer.</p></li>
<li><p><strong>network_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network Zone of the Load Balancer. Require when no location is set.</p></li>
<li><p><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerTargetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of targets of the Load Balancer.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="p">:</span> <span class="n">Union[LoadBalancerAlgorithmArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerAlgorithmArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_ip</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="p">:</span> <span class="n">Union[List[Union[LoadBalancerTargetArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerTargetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LoadBalancerTargetArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerTargetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.load_balancer.LoadBalancer<a class="headerlink" href="#pulumi_hcloud.LoadBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerAlgorithmArgs'</em><em>]</em><em>]</em>) – Configuration of the algorithm the Load Balancer use.</p></li>
<li><p><strong>ipv4</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) IPv4 Address of the Load Balancer.</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) IPv4 Address of the Load Balancer.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs) should be created with.</p></li>
<li><p><strong>load_balancer_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the Load Balancer.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the Load Balancer. Require when no network_zone is set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Load Balancer.</p></li>
<li><p><strong>network_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network Zone of the Load Balancer. Require when no location is set.</p></li>
<li><p><strong>targets</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerTargetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of targets of the Load Balancer.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.algorithm">
<em class="property">property </em><code class="sig-name descname">algorithm</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of the algorithm the Load Balancer use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.ipv4">
<em class="property">property </em><code class="sig-name descname">ipv4</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) IPv4 Address of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.ipv6">
<em class="property">property </em><code class="sig-name descname">ipv6</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) IPv4 Address of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined labels (key-value pairs) should be created with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.load_balancer_type">
<em class="property">property </em><code class="sig-name descname">load_balancer_type</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.load_balancer_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.location">
<em class="property">property </em><code class="sig-name descname">location</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of the Load Balancer. Require when no network_zone is set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.network_zone">
<em class="property">property </em><code class="sig-name descname">network_zone</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.network_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Network Zone of the Load Balancer. Require when no location is set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.targets">
<em class="property">property </em><code class="sig-name descname">targets</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.targets" title="Permalink to this definition">¶</a></dt>
<dd><p>List of targets of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.LoadBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.LoadBalancerNetwork">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">LoadBalancerNetwork</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_public_interface</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Load Balancer Network to represent a private network on a Load Balancer in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">lb1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancer</span><span class="p">(</span><span class="s2">&quot;lb1&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_type</span><span class="o">=</span><span class="s2">&quot;lb11&quot;</span><span class="p">,</span>
    <span class="n">network_zone</span><span class="o">=</span><span class="s2">&quot;eu-central&quot;</span><span class="p">)</span>
<span class="n">mynet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;mynet&quot;</span><span class="p">,</span> <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/8&quot;</span><span class="p">)</span>
<span class="n">foonet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">NetworkSubnet</span><span class="p">(</span><span class="s2">&quot;foonet&quot;</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;cloud&quot;</span><span class="p">,</span>
    <span class="n">network_zone</span><span class="o">=</span><span class="s2">&quot;eu-central&quot;</span><span class="p">,</span>
    <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.1.0/24&quot;</span><span class="p">)</span>
<span class="n">srvnetwork</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancerNetwork</span><span class="p">(</span><span class="s2">&quot;srvnetwork&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_id</span><span class="o">=</span><span class="n">lb1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">ip</span><span class="o">=</span><span class="s2">&quot;10.0.1.5&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable_public_interface</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the
Load Balancers public interface. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><strong>ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP to request to be assigned to this Load
Balancer. If you do not provide this then you will be auto assigned an
IP address.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Load Balancer.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the network which should be added
to the Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> is not set. Successful
creation of the resource depends on the existence of a subnet in the
Hetzner Cloud Backend. Using <code class="docutils literal notranslate"><span class="pre">network_id</span></code> will not create an explicit
dependency between the Load Balancer and the subnet. Therefore
<code class="docutils literal notranslate"><span class="pre">depends_on</span></code> may need to be used. Alternatively the <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code>
property can be used, which will create an explicit dependency between
<code class="docutils literal notranslate"><span class="pre">LoadBalancerNetwork</span></code> and the existence of a subnet.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the sub-network which should be
added to the Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">network_id</span></code> is not set.
<em>Note</em>: if the <code class="docutils literal notranslate"><span class="pre">ip</span></code> property is missing, the Load Balancer is
currently added to the last created subnet.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerNetwork.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_public_interface</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.load_balancer_network.LoadBalancerNetwork<a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerNetwork resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable_public_interface</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the
Load Balancers public interface. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><strong>ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP to request to be assigned to this Load
Balancer. If you do not provide this then you will be auto assigned an
IP address.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Load Balancer.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the network which should be added
to the Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> is not set. Successful
creation of the resource depends on the existence of a subnet in the
Hetzner Cloud Backend. Using <code class="docutils literal notranslate"><span class="pre">network_id</span></code> will not create an explicit
dependency between the Load Balancer and the subnet. Therefore
<code class="docutils literal notranslate"><span class="pre">depends_on</span></code> may need to be used. Alternatively the <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code>
property can be used, which will create an explicit dependency between
<code class="docutils literal notranslate"><span class="pre">LoadBalancerNetwork</span></code> and the existence of a subnet.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the sub-network which should be
added to the Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">network_id</span></code> is not set.
<em>Note</em>: if the <code class="docutils literal notranslate"><span class="pre">ip</span></code> property is missing, the Load Balancer is
currently added to the last created subnet.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerNetwork.enable_public_interface">
<em class="property">property </em><code class="sig-name descname">enable_public_interface</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork.enable_public_interface" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable the
Load Balancers public interface. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerNetwork.ip">
<em class="property">property </em><code class="sig-name descname">ip</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork.ip" title="Permalink to this definition">¶</a></dt>
<dd><p>IP to request to be assigned to this Load
Balancer. If you do not provide this then you will be auto assigned an
IP address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerNetwork.load_balancer_id">
<em class="property">property </em><code class="sig-name descname">load_balancer_id</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork.load_balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerNetwork.network_id">
<em class="property">property </em><code class="sig-name descname">network_id</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the network which should be added
to the Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> is not set. Successful
creation of the resource depends on the existence of a subnet in the
Hetzner Cloud Backend. Using <code class="docutils literal notranslate"><span class="pre">network_id</span></code> will not create an explicit
dependency between the Load Balancer and the subnet. Therefore
<code class="docutils literal notranslate"><span class="pre">depends_on</span></code> may need to be used. Alternatively the <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code>
property can be used, which will create an explicit dependency between
<code class="docutils literal notranslate"><span class="pre">LoadBalancerNetwork</span></code> and the existence of a subnet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerNetwork.subnet_id">
<em class="property">property </em><code class="sig-name descname">subnet_id</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the sub-network which should be
added to the Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">network_id</span></code> is not set.
<em>Note</em>: if the <code class="docutils literal notranslate"><span class="pre">ip</span></code> property is missing, the Load Balancer is
currently added to the last created subnet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerNetwork.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.LoadBalancerNetwork.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.LoadBalancerService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">LoadBalancerService</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="p">:</span> <span class="n">Union[LoadBalancerServiceHealthCheckArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerServiceHealthCheckArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http</span><span class="p">:</span> <span class="n">Union[LoadBalancerServiceHttpArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerServiceHttpArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listen_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxyprotocol</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService" title="Permalink to this definition">¶</a></dt>
<dd><p>Define services for Hetzner Cloud Load Balancers.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">load_balancer</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancer</span><span class="p">(</span><span class="s2">&quot;loadBalancer&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_type</span><span class="o">=</span><span class="s2">&quot;lb11&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;nbg1&quot;</span><span class="p">)</span>
<span class="n">load_balancer_service</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancerService</span><span class="p">(</span><span class="s2">&quot;loadBalancerService&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_id</span><span class="o">=</span><span class="n">hcloud_load_balancer</span><span class="p">[</span><span class="s2">&quot;test_load_balancer&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port the service connects to the targets on, required if protocol is <code class="docutils literal notranslate"><span class="pre">tcp</span></code>. Can be everything between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code>.</p></li>
<li><p><strong>health_check</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerServiceHealthCheckArgs'</em><em>]</em><em>]</em>) – List of health check configurations when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p></li>
<li><p><strong>http</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerServiceHttpArgs'</em><em>]</em><em>]</em>) – List of http configurations when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p></li>
<li><p><strong>listen_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port the service listen on, required if protocol is <code class="docutils literal notranslate"><span class="pre">tcp</span></code>. Can be everything between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code>. Must be unique per Load Balancer.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the load balancer this service belongs to.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Protocol of the service. <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code> or <code class="docutils literal notranslate"><span class="pre">tcp</span></code></p></li>
<li><p><strong>proxyprotocol</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable proxyprotocol.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="p">:</span> <span class="n">Union[LoadBalancerServiceHealthCheckArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerServiceHealthCheckArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http</span><span class="p">:</span> <span class="n">Union[LoadBalancerServiceHttpArgs, Mapping[str, Any], Awaitable[Union[LoadBalancerServiceHttpArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listen_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxyprotocol</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.load_balancer_service.LoadBalancerService<a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port the service connects to the targets on, required if protocol is <code class="docutils literal notranslate"><span class="pre">tcp</span></code>. Can be everything between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code>.</p></li>
<li><p><strong>health_check</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerServiceHealthCheckArgs'</em><em>]</em><em>]</em>) – List of health check configurations when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p></li>
<li><p><strong>http</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerServiceHttpArgs'</em><em>]</em><em>]</em>) – List of http configurations when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p></li>
<li><p><strong>listen_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port the service listen on, required if protocol is <code class="docutils literal notranslate"><span class="pre">tcp</span></code>. Can be everything between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code>. Must be unique per Load Balancer.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the load balancer this service belongs to.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Protocol of the service. <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code> or <code class="docutils literal notranslate"><span class="pre">tcp</span></code></p></li>
<li><p><strong>proxyprotocol</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable proxyprotocol.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerService.destination_port">
<em class="property">property </em><code class="sig-name descname">destination_port</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.destination_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port the service connects to the targets on, required if protocol is <code class="docutils literal notranslate"><span class="pre">tcp</span></code>. Can be everything between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerService.health_check">
<em class="property">property </em><code class="sig-name descname">health_check</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.health_check" title="Permalink to this definition">¶</a></dt>
<dd><p>List of health check configurations when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerService.http">
<em class="property">property </em><code class="sig-name descname">http</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.http" title="Permalink to this definition">¶</a></dt>
<dd><p>List of http configurations when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is <code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerService.listen_port">
<em class="property">property </em><code class="sig-name descname">listen_port</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.listen_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port the service listen on, required if protocol is <code class="docutils literal notranslate"><span class="pre">tcp</span></code>. Can be everything between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code>. Must be unique per Load Balancer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerService.load_balancer_id">
<em class="property">property </em><code class="sig-name descname">load_balancer_id</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.load_balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the load balancer this service belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerService.protocol">
<em class="property">property </em><code class="sig-name descname">protocol</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Protocol of the service. <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">https</span></code> or <code class="docutils literal notranslate"><span class="pre">tcp</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerService.proxyprotocol">
<em class="property">property </em><code class="sig-name descname">proxyprotocol</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.proxyprotocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable proxyprotocol.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.LoadBalancerService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.LoadBalancerTarget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">LoadBalancerTarget</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label_selector</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_private_ip</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds a target to a Hetzner Cloud Load Balancer.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">my_server</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;myServer&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;ubuntu-18.04&quot;</span><span class="p">)</span>
<span class="n">load_balancer</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancer</span><span class="p">(</span><span class="s2">&quot;loadBalancer&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_type</span><span class="o">=</span><span class="s2">&quot;lb11&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;nbg1&quot;</span><span class="p">)</span>
<span class="n">load_balancer_target</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancerTarget</span><span class="p">(</span><span class="s2">&quot;loadBalancerTarget&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;server&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_id</span><span class="o">=</span><span class="n">hcloud_load_balancer</span><span class="p">[</span><span class="s2">&quot;load_balcancer&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">my_server</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address for an IP Target. Required if
<code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">ip</span></code>.</p></li>
<li><p><strong>label_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Label Selector selecting targets
for this Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">label_selector</span></code>.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Load Balancer to which
the target gets attached.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the server which should be a
target for this Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">server</span></code></p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the target. Possible values
<code class="docutils literal notranslate"><span class="pre">server</span></code>, <code class="docutils literal notranslate"><span class="pre">label_selector</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code>.</p></li>
<li><p><strong>use_private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – use the private IP to connect to
Load Balancer targets. Only allowed if type is <code class="docutils literal notranslate"><span class="pre">server</span></code> or
<code class="docutils literal notranslate"><span class="pre">label_selector</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label_selector</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_private_ip</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.load_balancer_target.LoadBalancerTarget<a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address for an IP Target. Required if
<code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">ip</span></code>.</p></li>
<li><p><strong>label_selector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Label Selector selecting targets
for this Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">label_selector</span></code>.</p></li>
<li><p><strong>load_balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Load Balancer to which
the target gets attached.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the server which should be a
target for this Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">server</span></code></p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the target. Possible values
<code class="docutils literal notranslate"><span class="pre">server</span></code>, <code class="docutils literal notranslate"><span class="pre">label_selector</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code>.</p></li>
<li><p><strong>use_private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – use the private IP to connect to
Load Balancer targets. Only allowed if type is <code class="docutils literal notranslate"><span class="pre">server</span></code> or
<code class="docutils literal notranslate"><span class="pre">label_selector</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerTarget.ip">
<em class="property">property </em><code class="sig-name descname">ip</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget.ip" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address for an IP Target. Required if
<code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">ip</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerTarget.label_selector">
<em class="property">property </em><code class="sig-name descname">label_selector</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget.label_selector" title="Permalink to this definition">¶</a></dt>
<dd><p>Label Selector selecting targets
for this Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">label_selector</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerTarget.load_balancer_id">
<em class="property">property </em><code class="sig-name descname">load_balancer_id</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget.load_balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Load Balancer to which
the target gets attached.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerTarget.server_id">
<em class="property">property </em><code class="sig-name descname">server_id</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the server which should be a
target for this Load Balancer. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">server</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerTarget.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the target. Possible values
<code class="docutils literal notranslate"><span class="pre">server</span></code>, <code class="docutils literal notranslate"><span class="pre">label_selector</span></code>, <code class="docutils literal notranslate"><span class="pre">ip</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerTarget.use_private_ip">
<em class="property">property </em><code class="sig-name descname">use_private_ip</code><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget.use_private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>use the private IP to connect to
Load Balancer targets. Only allowed if type is <code class="docutils literal notranslate"><span class="pre">server</span></code> or
<code class="docutils literal notranslate"><span class="pre">label_selector</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerTarget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.LoadBalancerTarget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Network">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Network" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Network to represent a Network in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">priv_net</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;privNet&quot;</span><span class="p">,</span> <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.1.0/24&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP Range of the whole Network which must span all included subnets and route destinations. Must be one of the private ipv4 ranges of RFC1918.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs) should be created with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Network to create (must be unique per project).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.Network.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.network.Network<a class="headerlink" href="#pulumi_hcloud.Network.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Network resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP Range of the whole Network which must span all included subnets and route destinations. Must be one of the private ipv4 ranges of RFC1918.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs) should be created with.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Network to create (must be unique per project).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Network.ip_range">
<em class="property">property </em><code class="sig-name descname">ip_range</code><a class="headerlink" href="#pulumi_hcloud.Network.ip_range" title="Permalink to this definition">¶</a></dt>
<dd><p>IP Range of the whole Network which must span all included subnets and route destinations. Must be one of the private ipv4 ranges of RFC1918.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Network.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_hcloud.Network.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined labels (key-value pairs) should be created with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Network.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.Network.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Network to create (must be unique per project).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Network.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Network.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Network.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Network.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.NetworkRoute">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">NetworkRoute</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.NetworkRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Network Route to represent a Network route in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">mynet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;mynet&quot;</span><span class="p">,</span> <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/8&quot;</span><span class="p">)</span>
<span class="n">priv_net</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">NetworkRoute</span><span class="p">(</span><span class="s2">&quot;privNet&quot;</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">destination</span><span class="o">=</span><span class="s2">&quot;10.100.1.0/24&quot;</span><span class="p">,</span>
    <span class="n">gateway</span><span class="o">=</span><span class="s2">&quot;10.0.1.1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination network or host of this route. Must be a subnet of the ip_range of the Network. Must not overlap with an existing ip_range in any subnets or with any destinations in other routes or with the first ip of the networks ip_range or with 172.31.1.1.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Gateway for the route. Cannot be the first ip of the networks ip_range and also cannot be 172.31.1.1 as this IP is being used as a gateway for the public network interface of servers.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Network the route should be added to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.NetworkRoute.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.network_route.NetworkRoute<a class="headerlink" href="#pulumi_hcloud.NetworkRoute.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkRoute resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination network or host of this route. Must be a subnet of the ip_range of the Network. Must not overlap with an existing ip_range in any subnets or with any destinations in other routes or with the first ip of the networks ip_range or with 172.31.1.1.</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Gateway for the route. Cannot be the first ip of the networks ip_range and also cannot be 172.31.1.1 as this IP is being used as a gateway for the public network interface of servers.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Network the route should be added to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.NetworkRoute.destination">
<em class="property">property </em><code class="sig-name descname">destination</code><a class="headerlink" href="#pulumi_hcloud.NetworkRoute.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination network or host of this route. Must be a subnet of the ip_range of the Network. Must not overlap with an existing ip_range in any subnets or with any destinations in other routes or with the first ip of the networks ip_range or with 172.31.1.1.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.NetworkRoute.gateway">
<em class="property">property </em><code class="sig-name descname">gateway</code><a class="headerlink" href="#pulumi_hcloud.NetworkRoute.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Gateway for the route. Cannot be the first ip of the networks ip_range and also cannot be 172.31.1.1 as this IP is being used as a gateway for the public network interface of servers.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.NetworkRoute.network_id">
<em class="property">property </em><code class="sig-name descname">network_id</code><a class="headerlink" href="#pulumi_hcloud.NetworkRoute.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Network the route should be added to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.NetworkRoute.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.NetworkRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.NetworkRoute.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.NetworkRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.NetworkSubnet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">NetworkSubnet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.NetworkSubnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Network Subnet to represent a Subnet in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">mynet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;mynet&quot;</span><span class="p">,</span> <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/8&quot;</span><span class="p">)</span>
<span class="n">foonet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">NetworkSubnet</span><span class="p">(</span><span class="s2">&quot;foonet&quot;</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;cloud&quot;</span><span class="p">,</span>
    <span class="n">network_zone</span><span class="o">=</span><span class="s2">&quot;eu-central&quot;</span><span class="p">,</span>
    <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.1.0/24&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Range to allocate IPs from. Must be a subnet of the ip_range of the Network and must not overlap with any other subnets or with any destinations in routes.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Network the subnet should be added to.</p></li>
<li><p><strong>network_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of network zone.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of subnet. <code class="docutils literal notranslate"><span class="pre">server</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.NetworkSubnet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.network_subnet.NetworkSubnet<a class="headerlink" href="#pulumi_hcloud.NetworkSubnet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkSubnet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Range to allocate IPs from. Must be a subnet of the ip_range of the Network and must not overlap with any other subnets or with any destinations in routes.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Network the subnet should be added to.</p></li>
<li><p><strong>network_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of network zone.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of subnet. <code class="docutils literal notranslate"><span class="pre">server</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.NetworkSubnet.ip_range">
<em class="property">property </em><code class="sig-name descname">ip_range</code><a class="headerlink" href="#pulumi_hcloud.NetworkSubnet.ip_range" title="Permalink to this definition">¶</a></dt>
<dd><p>Range to allocate IPs from. Must be a subnet of the ip_range of the Network and must not overlap with any other subnets or with any destinations in routes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.NetworkSubnet.network_id">
<em class="property">property </em><code class="sig-name descname">network_id</code><a class="headerlink" href="#pulumi_hcloud.NetworkSubnet.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Network the subnet should be added to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.NetworkSubnet.network_zone">
<em class="property">property </em><code class="sig-name descname">network_zone</code><a class="headerlink" href="#pulumi_hcloud.NetworkSubnet.network_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of network zone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.NetworkSubnet.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_hcloud.NetworkSubnet.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of subnet. <code class="docutils literal notranslate"><span class="pre">server</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.NetworkSubnet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.NetworkSubnet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.NetworkSubnet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.NetworkSubnet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the hcloud package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API token to access the Hetzner cloud.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Rdns">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Rdns</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_ptr</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">floating_ip_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Rdns" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Reverse DNS Entry to create, modify and reset reverse dns entries for Hetzner Cloud Floating IPs or servers.</p>
<p>For servers:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Rdns</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">ip_address</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">ipv4_address</span><span class="p">,</span>
    <span class="n">dns_ptr</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>For Floating IPs:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">floating1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">FloatingIp</span><span class="p">(</span><span class="s2">&quot;floating1&quot;</span><span class="p">,</span>
    <span class="n">home_location</span><span class="o">=</span><span class="s2">&quot;nbg1&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;ipv4&quot;</span><span class="p">)</span>
<span class="n">floating_master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Rdns</span><span class="p">(</span><span class="s2">&quot;floatingMaster&quot;</span><span class="p">,</span>
    <span class="n">dns_ptr</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">floating_ip_id</span><span class="o">=</span><span class="n">floating1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">ip_address</span><span class="o">=</span><span class="n">floating1</span><span class="o">.</span><span class="n">ip_address</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_ptr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS address the <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> should resolve to.</p></li>
<li><p><strong>floating_ip_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Floating IP the <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> belongs to.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address that should point to <code class="docutils literal notranslate"><span class="pre">dns_ptr</span></code>.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The server the <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> belongs to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.Rdns.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_ptr</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">floating_ip_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.rdns.Rdns<a class="headerlink" href="#pulumi_hcloud.Rdns.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rdns resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_ptr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS address the <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> should resolve to.</p></li>
<li><p><strong>floating_ip_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Floating IP the <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> belongs to.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address that should point to <code class="docutils literal notranslate"><span class="pre">dns_ptr</span></code>.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The server the <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> belongs to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Rdns.dns_ptr">
<em class="property">property </em><code class="sig-name descname">dns_ptr</code><a class="headerlink" href="#pulumi_hcloud.Rdns.dns_ptr" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS address the <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> should resolve to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Rdns.floating_ip_id">
<em class="property">property </em><code class="sig-name descname">floating_ip_id</code><a class="headerlink" href="#pulumi_hcloud.Rdns.floating_ip_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Floating IP the <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Rdns.ip_address">
<em class="property">property </em><code class="sig-name descname">ip_address</code><a class="headerlink" href="#pulumi_hcloud.Rdns.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address that should point to <code class="docutils literal notranslate"><span class="pre">dns_ptr</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Rdns.server_id">
<em class="property">property </em><code class="sig-name descname">server_id</code><a class="headerlink" href="#pulumi_hcloud.Rdns.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The server the <code class="docutils literal notranslate"><span class="pre">ip_address</span></code> belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Rdns.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Rdns.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Rdns.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Rdns.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Server">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Server</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iso</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_disk</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rescue</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Server resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] backups: Enable or disable backups.
:param pulumi.Input[str] datacenter: The datacenter name to create the server in.
:param pulumi.Input[str] image: Name or ID of the image the server is created from.
:param pulumi.Input[str] iso: ID or Name of an ISO image to mount.
:param pulumi.Input[bool] keep_disk: If true, do not upgrade the disk. This allows downgrading the server type later.
:param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
:param pulumi.Input[str] location: The location name to create the server in. <code class="docutils literal notranslate"><span class="pre">nbg1</span></code>, <code class="docutils literal notranslate"><span class="pre">fsn1</span></code> or <code class="docutils literal notranslate"><span class="pre">hel1</span></code>
:param pulumi.Input[str] name: Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
:param pulumi.Input[str] rescue: Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. <code class="docutils literal notranslate"><span class="pre">linux64</span></code> <code class="docutils literal notranslate"><span class="pre">linux32</span></code> or <code class="docutils literal notranslate"><span class="pre">freebsd64</span></code>
:param pulumi.Input[str] server_type: Name of the server type this server should be created with.
:param pulumi.Input[List[pulumi.Input[str]]] ssh_keys: SSH key IDs or names which should be injected into the server at creation time
:param pulumi.Input[str] user_data: Cloud-Init user data to use during server creation</p>
<dl class="py method">
<dt id="pulumi_hcloud.Server.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_window</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_network</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iso</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_disk</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rescue</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.server.Server<a class="headerlink" href="#pulumi_hcloud.Server.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Server resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) The backup window of the server, if enabled.</p></li>
<li><p><strong>backups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable backups.</p></li>
<li><p><strong>datacenter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The datacenter name to create the server in.</p></li>
<li><p><strong>image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name or ID of the image the server is created from.</p></li>
<li><p><strong>ipv4_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) The IPv4 address.</p></li>
<li><p><strong>ipv6_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) The first IPv6 address of the assigned network.</p></li>
<li><p><strong>ipv6_network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) The IPv6 network.</p></li>
<li><p><strong>iso</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID or Name of an ISO image to mount.</p></li>
<li><p><strong>keep_disk</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, do not upgrade the disk. This allows downgrading the server type later.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs) should be created with.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location name to create the server in. <code class="docutils literal notranslate"><span class="pre">nbg1</span></code>, <code class="docutils literal notranslate"><span class="pre">fsn1</span></code> or <code class="docutils literal notranslate"><span class="pre">hel1</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).</p></li>
<li><p><strong>rescue</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. <code class="docutils literal notranslate"><span class="pre">linux64</span></code> <code class="docutils literal notranslate"><span class="pre">linux32</span></code> or <code class="docutils literal notranslate"><span class="pre">freebsd64</span></code></p></li>
<li><p><strong>server_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the server type this server should be created with.</p></li>
<li><p><strong>ssh_keys</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – SSH key IDs or names which should be injected into the server at creation time</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) The status of the server.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud-Init user data to use during server creation</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.backup_window">
<em class="property">property </em><code class="sig-name descname">backup_window</code><a class="headerlink" href="#pulumi_hcloud.Server.backup_window" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The backup window of the server, if enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.backups">
<em class="property">property </em><code class="sig-name descname">backups</code><a class="headerlink" href="#pulumi_hcloud.Server.backups" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable backups.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.datacenter">
<em class="property">property </em><code class="sig-name descname">datacenter</code><a class="headerlink" href="#pulumi_hcloud.Server.datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>The datacenter name to create the server in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.image">
<em class="property">property </em><code class="sig-name descname">image</code><a class="headerlink" href="#pulumi_hcloud.Server.image" title="Permalink to this definition">¶</a></dt>
<dd><p>Name or ID of the image the server is created from.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.ipv4_address">
<em class="property">property </em><code class="sig-name descname">ipv4_address</code><a class="headerlink" href="#pulumi_hcloud.Server.ipv4_address" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The IPv4 address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.ipv6_address">
<em class="property">property </em><code class="sig-name descname">ipv6_address</code><a class="headerlink" href="#pulumi_hcloud.Server.ipv6_address" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The first IPv6 address of the assigned network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.ipv6_network">
<em class="property">property </em><code class="sig-name descname">ipv6_network</code><a class="headerlink" href="#pulumi_hcloud.Server.ipv6_network" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The IPv6 network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.iso">
<em class="property">property </em><code class="sig-name descname">iso</code><a class="headerlink" href="#pulumi_hcloud.Server.iso" title="Permalink to this definition">¶</a></dt>
<dd><p>ID or Name of an ISO image to mount.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.keep_disk">
<em class="property">property </em><code class="sig-name descname">keep_disk</code><a class="headerlink" href="#pulumi_hcloud.Server.keep_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, do not upgrade the disk. This allows downgrading the server type later.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_hcloud.Server.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined labels (key-value pairs) should be created with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.location">
<em class="property">property </em><code class="sig-name descname">location</code><a class="headerlink" href="#pulumi_hcloud.Server.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location name to create the server in. <code class="docutils literal notranslate"><span class="pre">nbg1</span></code>, <code class="docutils literal notranslate"><span class="pre">fsn1</span></code> or <code class="docutils literal notranslate"><span class="pre">hel1</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.Server.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.rescue">
<em class="property">property </em><code class="sig-name descname">rescue</code><a class="headerlink" href="#pulumi_hcloud.Server.rescue" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. <code class="docutils literal notranslate"><span class="pre">linux64</span></code> <code class="docutils literal notranslate"><span class="pre">linux32</span></code> or <code class="docutils literal notranslate"><span class="pre">freebsd64</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.server_type">
<em class="property">property </em><code class="sig-name descname">server_type</code><a class="headerlink" href="#pulumi_hcloud.Server.server_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the server type this server should be created with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.ssh_keys">
<em class="property">property </em><code class="sig-name descname">ssh_keys</code><a class="headerlink" href="#pulumi_hcloud.Server.ssh_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>SSH key IDs or names which should be injected into the server at creation time</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_hcloud.Server.status" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The status of the server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.user_data">
<em class="property">property </em><code class="sig-name descname">user_data</code><a class="headerlink" href="#pulumi_hcloud.Server.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud-Init user data to use during server creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Server.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Server.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Server.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Server.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.ServerNetwork">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">ServerNetwork</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias_ips</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.ServerNetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Server Network to represent a private network on a server in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">mynet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;mynet&quot;</span><span class="p">,</span> <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/8&quot;</span><span class="p">)</span>
<span class="n">foonet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">NetworkSubnet</span><span class="p">(</span><span class="s2">&quot;foonet&quot;</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;cloud&quot;</span><span class="p">,</span>
    <span class="n">network_zone</span><span class="o">=</span><span class="s2">&quot;eu-central&quot;</span><span class="p">,</span>
    <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.1.0/24&quot;</span><span class="p">)</span>
<span class="n">srvnetwork</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">ServerNetwork</span><span class="p">(</span><span class="s2">&quot;srvnetwork&quot;</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">ip</span><span class="o">=</span><span class="s2">&quot;10.0.1.5&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alias_ips</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Additional IPs to be assigned
to this server.</p></li>
<li><p><strong>ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP to request to be assigned to this server.
If you do not provide this then you will be auto assigned an IP
address.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the network which should be added
to the server. Required if <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> is not set. Successful creation
of the resource depends on the existence of a subnet in the Hetzner
Cloud Backend. Using <code class="docutils literal notranslate"><span class="pre">network_id</span></code> will not create an explicit
dependency between server and subnet. Therefore <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> may need
to be used. Alternatively the <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> property can be used, which
will create an explicit dependency between <code class="docutils literal notranslate"><span class="pre">ServerNetwork</span></code> and
the existence of a subnet.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the server.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the sub-network which should be
added to the Server. Required if <code class="docutils literal notranslate"><span class="pre">network_id</span></code> is not set.
<em>Note</em>: if the <code class="docutils literal notranslate"><span class="pre">ip</span></code> property is missing, the Server is currently added
to the last created subnet.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.ServerNetwork.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias_ips</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mac_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.server_network.ServerNetwork<a class="headerlink" href="#pulumi_hcloud.ServerNetwork.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerNetwork resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alias_ips</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Additional IPs to be assigned
to this server.</p></li>
<li><p><strong>ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP to request to be assigned to this server.
If you do not provide this then you will be auto assigned an IP
address.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the network which should be added
to the server. Required if <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> is not set. Successful creation
of the resource depends on the existence of a subnet in the Hetzner
Cloud Backend. Using <code class="docutils literal notranslate"><span class="pre">network_id</span></code> will not create an explicit
dependency between server and subnet. Therefore <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> may need
to be used. Alternatively the <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> property can be used, which
will create an explicit dependency between <code class="docutils literal notranslate"><span class="pre">ServerNetwork</span></code> and
the existence of a subnet.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the server.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the sub-network which should be
added to the Server. Required if <code class="docutils literal notranslate"><span class="pre">network_id</span></code> is not set.
<em>Note</em>: if the <code class="docutils literal notranslate"><span class="pre">ip</span></code> property is missing, the Server is currently added
to the last created subnet.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.ServerNetwork.alias_ips">
<em class="property">property </em><code class="sig-name descname">alias_ips</code><a class="headerlink" href="#pulumi_hcloud.ServerNetwork.alias_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional IPs to be assigned
to this server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.ServerNetwork.ip">
<em class="property">property </em><code class="sig-name descname">ip</code><a class="headerlink" href="#pulumi_hcloud.ServerNetwork.ip" title="Permalink to this definition">¶</a></dt>
<dd><p>IP to request to be assigned to this server.
If you do not provide this then you will be auto assigned an IP
address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.ServerNetwork.network_id">
<em class="property">property </em><code class="sig-name descname">network_id</code><a class="headerlink" href="#pulumi_hcloud.ServerNetwork.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the network which should be added
to the server. Required if <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> is not set. Successful creation
of the resource depends on the existence of a subnet in the Hetzner
Cloud Backend. Using <code class="docutils literal notranslate"><span class="pre">network_id</span></code> will not create an explicit
dependency between server and subnet. Therefore <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> may need
to be used. Alternatively the <code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> property can be used, which
will create an explicit dependency between <code class="docutils literal notranslate"><span class="pre">ServerNetwork</span></code> and
the existence of a subnet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.ServerNetwork.server_id">
<em class="property">property </em><code class="sig-name descname">server_id</code><a class="headerlink" href="#pulumi_hcloud.ServerNetwork.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.ServerNetwork.subnet_id">
<em class="property">property </em><code class="sig-name descname">subnet_id</code><a class="headerlink" href="#pulumi_hcloud.ServerNetwork.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the sub-network which should be
added to the Server. Required if <code class="docutils literal notranslate"><span class="pre">network_id</span></code> is not set.
<em>Note</em>: if the <code class="docutils literal notranslate"><span class="pre">ip</span></code> property is missing, the Server is currently added
to the last created subnet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.ServerNetwork.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.ServerNetwork.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.ServerNetwork.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.ServerNetwork.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.SshKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud SSH key resource to manage SSH keys for server access.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="c1"># Create a new SSH key</span>
<span class="n">default</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">SshKey</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span> <span class="n">public_key</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;~/.ssh/id_rsa.pub&quot;</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – (map) User-defined labels (key-value pairs)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH key.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it can be read using the file interpolation function</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.ssh_key.SshKey<a class="headerlink" href="#pulumi_hcloud.SshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (string) The fingerprint of the SSH key</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – (map) User-defined labels (key-value pairs)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SSH key.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it can be read using the file interpolation function</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.SshKey.fingerprint">
<em class="property">property </em><code class="sig-name descname">fingerprint</code><a class="headerlink" href="#pulumi_hcloud.SshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>(string) The fingerprint of the SSH key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.SshKey.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_hcloud.SshKey.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>(map) User-defined labels (key-value pairs)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.SshKey.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.SshKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SSH key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.SshKey.public_key">
<em class="property">property </em><code class="sig-name descname">public_key</code><a class="headerlink" href="#pulumi_hcloud.SshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key. If this is a file, it can be read using the file interpolation function</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.SshKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.SshKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Volume">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automount</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud volume resource to manage volumes.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Volume</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">size</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">automount</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automount</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automount the volume upon attaching it (server_id must be provided).</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Format volume after creation. <code class="docutils literal notranslate"><span class="pre">xfs</span></code> or <code class="docutils literal notranslate"><span class="pre">ext4</span></code></p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs).</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the volume to create, optional if server_id argument is passed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the volume to create (must be unique per project).</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Server to attach the Volume to, optional if location argument is passed.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the volume (in GB).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automount</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linux_device</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.volume.Volume<a class="headerlink" href="#pulumi_hcloud.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automount</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automount the volume upon attaching it (server_id must be provided).</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Format volume after creation. <code class="docutils literal notranslate"><span class="pre">xfs</span></code> or <code class="docutils literal notranslate"><span class="pre">ext4</span></code></p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – User-defined labels (key-value pairs).</p></li>
<li><p><strong>linux_device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Device path on the file system for the Volume.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of the volume to create, optional if server_id argument is passed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the volume to create (must be unique per project).</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Server to attach the Volume to, optional if location argument is passed.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the volume (in GB).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Volume.automount">
<em class="property">property </em><code class="sig-name descname">automount</code><a class="headerlink" href="#pulumi_hcloud.Volume.automount" title="Permalink to this definition">¶</a></dt>
<dd><p>Automount the volume upon attaching it (server_id must be provided).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Volume.format">
<em class="property">property </em><code class="sig-name descname">format</code><a class="headerlink" href="#pulumi_hcloud.Volume.format" title="Permalink to this definition">¶</a></dt>
<dd><p>Format volume after creation. <code class="docutils literal notranslate"><span class="pre">xfs</span></code> or <code class="docutils literal notranslate"><span class="pre">ext4</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Volume.labels">
<em class="property">property </em><code class="sig-name descname">labels</code><a class="headerlink" href="#pulumi_hcloud.Volume.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined labels (key-value pairs).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Volume.linux_device">
<em class="property">property </em><code class="sig-name descname">linux_device</code><a class="headerlink" href="#pulumi_hcloud.Volume.linux_device" title="Permalink to this definition">¶</a></dt>
<dd><p>Device path on the file system for the Volume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Volume.location">
<em class="property">property </em><code class="sig-name descname">location</code><a class="headerlink" href="#pulumi_hcloud.Volume.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of the volume to create, optional if server_id argument is passed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Volume.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_hcloud.Volume.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the volume to create (must be unique per project).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Volume.server_id">
<em class="property">property </em><code class="sig-name descname">server_id</code><a class="headerlink" href="#pulumi_hcloud.Volume.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Server to attach the Volume to, optional if location argument is passed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Volume.size">
<em class="property">property </em><code class="sig-name descname">size</code><a class="headerlink" href="#pulumi_hcloud.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of the volume (in GB).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.Volume.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.Volume.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.VolumeAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">VolumeAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automount</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Volume attachment to attach a Volume to a Hetzner Cloud Server. Deleting a Volume Attachment will detach the Volume from the Server.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">,</span>
    <span class="n">datacenter</span><span class="o">=</span><span class="s2">&quot;nbg1-dc3&quot;</span><span class="p">)</span>
<span class="n">master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Volume</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;nbg1&quot;</span><span class="p">,</span>
    <span class="n">size</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>
<span class="n">main</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">VolumeAttachment</span><span class="p">(</span><span class="s2">&quot;main&quot;</span><span class="p">,</span>
    <span class="n">volume_id</span><span class="o">=</span><span class="n">master</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">automount</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automount</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automount the volume upon attaching it.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Server to attach the Volume to.</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Volume.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.VolumeAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automount</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.volume_attachment.VolumeAttachment<a class="headerlink" href="#pulumi_hcloud.VolumeAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VolumeAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automount</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automount the volume upon attaching it.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Server to attach the Volume to.</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the Volume.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.VolumeAttachment.automount">
<em class="property">property </em><code class="sig-name descname">automount</code><a class="headerlink" href="#pulumi_hcloud.VolumeAttachment.automount" title="Permalink to this definition">¶</a></dt>
<dd><p>Automount the volume upon attaching it.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.VolumeAttachment.server_id">
<em class="property">property </em><code class="sig-name descname">server_id</code><a class="headerlink" href="#pulumi_hcloud.VolumeAttachment.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Server to attach the Volume to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.VolumeAttachment.volume_id">
<em class="property">property </em><code class="sig-name descname">volume_id</code><a class="headerlink" href="#pulumi_hcloud.VolumeAttachment.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Volume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_hcloud.VolumeAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.VolumeAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.VolumeAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.VolumeAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_hcloud.get_certificate">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_certificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_certificate.AwaitableGetCertificateResult<a class="headerlink" href="#pulumi_hcloud.get_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Hetzner Cloud Certificate.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>float</em>) – ID of the certificate.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the certificate.</p></li>
<li><p><strong>with_selector</strong> (<em>str</em>) – <a class="reference external" href="https://docs.hetzner.cloud/#overview-label-selector">Label selector</a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_datacenter">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_datacenter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_datacenter.AwaitableGetDatacenterResult<a class="headerlink" href="#pulumi_hcloud.get_datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Hetzner Cloud Datacenter.
Use this resource to get detailed information about specific datacenter.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">ds1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_datacenter</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;fsn1-dc8&quot;</span><span class="p">)</span>
<span class="n">ds2</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_datacenter</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>float</em>) – ID of the datacenter.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the datacenter.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_datacenters">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_datacenters</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter_ids</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_datacenters.AwaitableGetDatacentersResult<a class="headerlink" href="#pulumi_hcloud.get_datacenters" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a list of available Hetzner Cloud Datacenters.
This resource may be useful to create highly available infrastructure, distributed across several datacenters.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">ds</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_datacenters</span><span class="p">()</span>
<span class="n">workers</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">)]:</span>
    <span class="n">workers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;workers-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
        <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx31&quot;</span><span class="p">,</span>
        <span class="n">datacenter</span><span class="o">=</span><span class="n">ds</span><span class="o">.</span><span class="n">names</span><span class="p">[</span><span class="nb">range</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">]]))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>datacenter_ids</strong> (<em>List</em><em>[</em><em>str</em><em>]</em>) – (list) List of unique datacenter identifiers.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_floating_ip">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_floating_ip</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_floating_ip.AwaitableGetFloatingIpResult<a class="headerlink" href="#pulumi_hcloud.get_floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a Hetzner Cloud Floating IP.</p>
<p>This resource can be useful when you need to determine a Floating IP ID based on the IP address.</p>
<p>Provides details about a Hetzner Cloud Floating IP.
This resource can be useful when you need to determine a Floating IP ID based on the IP address.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">ip1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_floating_ip</span><span class="p">(</span><span class="n">ip_address</span><span class="o">=</span><span class="s2">&quot;1.2.3.4&quot;</span><span class="p">)</span>
<span class="n">image2</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_floating_ip</span><span class="p">(</span><span class="n">with_selector</span><span class="o">=</span><span class="s2">&quot;key=value&quot;</span><span class="p">)</span>
<span class="n">main</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">var</span><span class="o">.</span><span class="n">counter</span><span class="p">)]:</span>
    <span class="n">main</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hcloud</span><span class="o">.</span><span class="n">FloatingIpAssignment</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;main-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">floating_ip_id</span><span class="o">=</span><span class="n">ip1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">server_id</span><span class="o">=</span><span class="n">hcloud_server</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>float</em>) – (int) Unique ID of the Floating IP.</p></li>
<li><p><strong>ip_address</strong> (<em>str</em>) – IP address of the Floating IP.</p></li>
<li><p><strong>with_selector</strong> (<em>str</em>) – <p><a class="reference external" href="https://docs.hetzner.cloud/#overview-label-selector">Label selector</a></p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_image">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">most_recent</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_image.AwaitableGetImageResult<a class="headerlink" href="#pulumi_hcloud.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>float</em>) – ID of the Image.</p></li>
<li><p><strong>most_recent</strong> (<em>bool</em>) – If more than one result is returned, use the most recent Image.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the Image.</p></li>
<li><p><strong>with_selector</strong> (<em>str</em>) – <p><a class="reference external" href="https://docs.hetzner.cloud/#overview-label-selector">Label selector</a></p>
</p></li>
<li><p><strong>with_statuses</strong> (<em>List</em><em>[</em><em>str</em><em>]</em>) – List only images with the specified status, could contain <code class="docutils literal notranslate"><span class="pre">creating</span></code> or <code class="docutils literal notranslate"><span class="pre">available</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_load_balancer">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_load_balancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_load_balancer.AwaitableGetLoadBalancerResult<a class="headerlink" href="#pulumi_hcloud.get_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Hetzner Cloud Server.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">lb1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_load_balancer</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;my-load-balancer&quot;</span><span class="p">)</span>
<span class="n">lb2</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_load_balancer</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="mi">123</span><span class="p">)</span>
<span class="n">lb3</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_load_balancer</span><span class="p">(</span><span class="n">with_selector</span><span class="o">=</span><span class="s2">&quot;key=value&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>float</em>) – ID of the Load Balancer.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the Load Balancer.</p></li>
<li><p><strong>with_selector</strong> (<em>str</em>) – Label Selector. For more information about possible values, visit the <a class="reference external" href="https://docs.hetzner.cloud/#overview-label-selector">Hetzner Cloud Documentation</a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_location">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_location</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_location.AwaitableGetLocationResult<a class="headerlink" href="#pulumi_hcloud.get_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Hetzner Cloud Location.
Use this resource to get detailed information about specific location.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">l1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_location</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;fsn1&quot;</span><span class="p">)</span>
<span class="n">l2</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_location</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>float</em>) – ID of the location.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the location.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_locations">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_locations</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">location_ids</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_locations.AwaitableGetLocationsResult<a class="headerlink" href="#pulumi_hcloud.get_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a list of available Hetzner Cloud Locations.
This resource may be useful to create highly available infrastructure, distributed across several locations.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">ds</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_locations</span><span class="p">()</span>
<span class="n">workers</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">)]:</span>
    <span class="n">workers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;workers-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
        <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx31&quot;</span><span class="p">,</span>
        <span class="n">location</span><span class="o">=</span><span class="n">ds</span><span class="o">.</span><span class="n">names</span><span class="p">[</span><span class="nb">range</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">]]))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>location_ids</strong> (<em>List</em><em>[</em><em>str</em><em>]</em>) – (list) List of unique location identifiers.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_network">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_network.AwaitableGetNetworkResult<a class="headerlink" href="#pulumi_hcloud.get_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>float</em>) – ID of the Network.</p></li>
<li><p><strong>ip_range</strong> (<em>str</em>) – IPv4 prefix of the Network.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the Network.</p></li>
<li><p><strong>with_selector</strong> (<em>str</em>) – <p>Label Selector. For more information about possible values, visit the <a class="reference external" href="https://docs.hetzner.cloud/#overview-label-selector">Hetzner Cloud Documentation</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_server">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_server</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_server.AwaitableGetServerResult<a class="headerlink" href="#pulumi_hcloud.get_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>float</em>) – ID of the server.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the server.</p></li>
<li><p><strong>with_selector</strong> (<em>str</em>) – <p>Label Selector. For more information about possible values, visit the <a class="reference external" href="https://docs.hetzner.cloud/#overview-label-selector">Hetzner Cloud Documentation</a>.</p>
</p></li>
<li><p><strong>with_statuses</strong> (<em>List</em><em>[</em><em>str</em><em>]</em>) – List only servers with the specified status, could contain <code class="docutils literal notranslate"><span class="pre">initializing</span></code>, <code class="docutils literal notranslate"><span class="pre">starting</span></code>, <code class="docutils literal notranslate"><span class="pre">running</span></code>, <code class="docutils literal notranslate"><span class="pre">stopping</span></code>, <code class="docutils literal notranslate"><span class="pre">off</span></code>, <code class="docutils literal notranslate"><span class="pre">deleting</span></code>, <code class="docutils literal notranslate"><span class="pre">rebuilding</span></code>, <code class="docutils literal notranslate"><span class="pre">migrating</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_ssh_key">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_ssh_key</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fingerprint</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_ssh_key.AwaitableGetSshKeyResult<a class="headerlink" href="#pulumi_hcloud.get_ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>fingerprint</strong> (<em>str</em>) – Fingerprint of the SSH Key.</p></li>
<li><p><strong>id</strong> (<em>float</em>) – ID of the SSH Key.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the SSH Key.</p></li>
<li><p><strong>with_selector</strong> (<em>str</em>) – <p><a class="reference external" href="https://docs.hetzner.cloud/#overview-label-selector">Label selector</a></p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_ssh_keys">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_ssh_keys</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">with_selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_ssh_keys.AwaitableGetSshKeysResult<a class="headerlink" href="#pulumi_hcloud.get_ssh_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>with_selector</strong> (<em>str</em>) – <p><a class="reference external" href="https://docs.hetzner.cloud/#overview-label-selector">Label selector</a></p>
</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_volume">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_hcloud.get_volume.AwaitableGetVolumeResult<a class="headerlink" href="#pulumi_hcloud.get_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>float</em>) – ID of the volume.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the volume.</p></li>
<li><p><strong>with_selector</strong> (<em>str</em>) – <p>Label Selector. For more information about possible values, visit the <a class="reference external" href="https://docs.hetzner.cloud/#overview-label-selector">Hetzner Cloud Documentation</a>.</p>
</p></li>
<li><p><strong>with_statuses</strong> (<em>List</em><em>[</em><em>str</em><em>]</em>) – List only volumes with the specified status, could contain <code class="docutils literal notranslate"><span class="pre">creating</span></code> or <code class="docutils literal notranslate"><span class="pre">available</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
