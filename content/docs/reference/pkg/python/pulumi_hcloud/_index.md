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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Clould Certificate to represent a TLS certificate in the Hetzner Cloud.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_valid_after</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">not_valid_before</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">FloatingIp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">home_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.FloatingIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Floating IP to represent a publicly-accessible static IP address that can be mapped to one of your servers.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">FloatingIp</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;ipv4&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.FloatingIp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">home_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.FloatingIp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FloatingIp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">FloatingIpAssignment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">floating_ip_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.FloatingIpAssignment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Floating IP Assignment to assign a Floating IP to a Hetzner Cloud Server. Deleting a Floating IP Assignment will unassign the Floating IP from the Server.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">datacenter</span><span class="o">=</span><span class="s2">&quot;fsn1-dc8&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">FloatingIp</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">home_location</span><span class="o">=</span><span class="s2">&quot;nbg1&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;ipv4&quot;</span><span class="p">)</span>
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
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.FloatingIpAssignment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">floating_ip_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.FloatingIpAssignment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FloatingIpAssignment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetDatacenterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetDatacenterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_server_type_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supported_server_type_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetDatacenterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatacenter.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetDatacentersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetDatacentersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetDatacentersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatacenters.</p>
<dl class="py attribute">
<dt id="pulumi_hcloud.GetDatacentersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_hcloud.GetDatacentersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetFloatingIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetFloatingIpResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">home_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetFloatingIpResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFloatingIp.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deprecated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">most_recent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">os_flavor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">os_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rapid_deploy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetLoadBalancerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetLoadBalancerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetLoadBalancerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLoadBalancer.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetLocationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetLocationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">city</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latitude</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">longitude</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetLocationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLocation.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetLocationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetLocationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">descriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetLocationsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLocations.</p>
<dl class="py attribute">
<dt id="pulumi_hcloud.GetLocationsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_hcloud.GetLocationsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetwork.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetServerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backup_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iso</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rescue</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetServerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServer.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSshKey.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetSshKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetSshKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetSshKeysResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSshKeys.</p>
<dl class="py attribute">
<dt id="pulumi_hcloud.GetSshKeysResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_hcloud.GetSshKeysResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.GetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">GetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linux_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.GetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolume.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_hcloud.LoadBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Load Balancer to represent a Load Balancer in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">myserver</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;myserver&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;ubuntu-18.04&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">load_balancer</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancer</span><span class="p">(</span><span class="s2">&quot;loadBalancer&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_type</span><span class="o">=</span><span class="s2">&quot;lb11&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;nbg1&quot;</span><span class="p">,</span>
    <span class="n">targets</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;server_id&quot;</span><span class="p">:</span> <span class="n">myserver</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;server&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>algorithm</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">server_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use_private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>algorithm</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>targets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">server_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use_private_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">LoadBalancerNetwork</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_public_interface</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Load Balancer Network to represent a private network on a Load Balancer in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">lb1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancer</span><span class="p">(</span><span class="s2">&quot;lb1&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_type</span><span class="o">=</span><span class="s2">&quot;lb11&quot;</span><span class="p">,</span>
    <span class="n">network_zone</span><span class="o">=</span><span class="s2">&quot;eu-central&quot;</span><span class="p">)</span>
<span class="n">mynet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;mynet&quot;</span><span class="p">,</span> <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/8&quot;</span><span class="p">)</span>
<span class="n">foonet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">NetworkSubnet</span><span class="p">(</span><span class="s2">&quot;foonet&quot;</span><span class="p">,</span>
    <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.1.0/24&quot;</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">network_zone</span><span class="o">=</span><span class="s2">&quot;eu-central&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;cloud&quot;</span><span class="p">)</span>
<span class="n">srvnetwork</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancerNetwork</span><span class="p">(</span><span class="s2">&quot;srvnetwork&quot;</span><span class="p">,</span>
    <span class="n">ip</span><span class="o">=</span><span class="s2">&quot;10.0.1.5&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_id</span><span class="o">=</span><span class="n">lb1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerNetwork.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_public_interface</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerNetwork.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerNetwork resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">LoadBalancerService</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listen_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxyprotocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService" title="Permalink to this definition">¶</a></dt>
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
</ul>
</dd>
</dl>
<p>The <strong>health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">http</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>http</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectHttp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stickySessions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listen_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxyprotocol</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">http</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">response</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>http</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectHttp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stickySessions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">LoadBalancerTarget</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds a target to a Hetzner Cloud Load Balancer.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">my_server</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;myServer&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;ubuntu-18.04&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">load_balancer</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancer</span><span class="p">(</span><span class="s2">&quot;loadBalancer&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_type</span><span class="o">=</span><span class="s2">&quot;lb11&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;nbg1&quot;</span><span class="p">)</span>
<span class="n">load_balancer_target</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">LoadBalancerTarget</span><span class="p">(</span><span class="s2">&quot;loadBalancerTarget&quot;</span><span class="p">,</span>
    <span class="n">load_balancer_id</span><span class="o">=</span><span class="n">hcloud_load_balancer</span><span class="p">[</span><span class="s2">&quot;load_balcancer&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">my_server</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;server&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.LoadBalancerTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_private_ip</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.LoadBalancerTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancerTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Network" title="Permalink to this definition">¶</a></dt>
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
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.Network.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Network.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Network resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">NetworkRoute</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.NetworkRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Network Route to represent a Network route in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">mynet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;mynet&quot;</span><span class="p">,</span> <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/8&quot;</span><span class="p">)</span>
<span class="n">priv_net</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">NetworkRoute</span><span class="p">(</span><span class="s2">&quot;privNet&quot;</span><span class="p">,</span>
    <span class="n">destination</span><span class="o">=</span><span class="s2">&quot;10.100.1.0/24&quot;</span><span class="p">,</span>
    <span class="n">gateway</span><span class="o">=</span><span class="s2">&quot;10.0.1.1&quot;</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.NetworkRoute.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.NetworkRoute.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkRoute resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">NetworkSubnet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.NetworkSubnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Network Subnet to represent a Subnet in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">mynet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;mynet&quot;</span><span class="p">,</span> <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/8&quot;</span><span class="p">)</span>
<span class="n">foonet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">NetworkSubnet</span><span class="p">(</span><span class="s2">&quot;foonet&quot;</span><span class="p">,</span>
    <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.1.0/24&quot;</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">network_zone</span><span class="o">=</span><span class="s2">&quot;eu-central&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;cloud&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.NetworkSubnet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.NetworkSubnet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkSubnet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Provider" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Rdns</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_ptr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">floating_ip_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Rdns" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Reverse DNS Entry to create, modify and reset reverse dns entries for Hetzner Cloud Floating IPs or servers.</p>
<p>For servers:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Rdns</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">dns_ptr</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">ip_address</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">ipv4_address</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
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
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.Rdns.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_ptr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">floating_ip_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Rdns.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rdns resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Server</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iso</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_disk</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rescue</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Server resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_hcloud.Server.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iso</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_disk</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rescue</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Server.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Server resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">ServerNetwork</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.ServerNetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Server Network to represent a private network on a server in the Hetzner Cloud.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">mynet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;mynet&quot;</span><span class="p">,</span> <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.0.0/8&quot;</span><span class="p">)</span>
<span class="n">foonet</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">NetworkSubnet</span><span class="p">(</span><span class="s2">&quot;foonet&quot;</span><span class="p">,</span>
    <span class="n">ip_range</span><span class="o">=</span><span class="s2">&quot;10.0.1.0/24&quot;</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">network_zone</span><span class="o">=</span><span class="s2">&quot;eu-central&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;cloud&quot;</span><span class="p">)</span>
<span class="n">srvnetwork</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">ServerNetwork</span><span class="p">(</span><span class="s2">&quot;srvnetwork&quot;</span><span class="p">,</span>
    <span class="n">ip</span><span class="o">=</span><span class="s2">&quot;10.0.1.5&quot;</span><span class="p">,</span>
    <span class="n">network_id</span><span class="o">=</span><span class="n">mynet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.ServerNetwork.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mac_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.ServerNetwork.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerNetwork resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.SshKey" title="Permalink to this definition">¶</a></dt>
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
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.SshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud volume resource to manage volumes.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Volume</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">automount</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">size</span><span class="o">=</span><span class="mi">50</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linux_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">VolumeAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Hetzner Cloud Volume attachment to attach a Volume to a Hetzner Cloud Server. Deleting a Volume Attachment will detach the Volume from the Server.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">node1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;node1&quot;</span><span class="p">,</span>
    <span class="n">datacenter</span><span class="o">=</span><span class="s2">&quot;nbg1-dc3&quot;</span><span class="p">,</span>
    <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
    <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx11&quot;</span><span class="p">)</span>
<span class="n">master</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">Volume</span><span class="p">(</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;nbg1&quot;</span><span class="p">,</span>
    <span class="n">size</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>
<span class="n">main</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">VolumeAttachment</span><span class="p">(</span><span class="s2">&quot;main&quot;</span><span class="p">,</span>
    <span class="n">automount</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">node1</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">volume_id</span><span class="o">=</span><span class="n">master</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_hcloud.VolumeAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">automount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.VolumeAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VolumeAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
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
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_certificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Hetzner Cloud Certificate.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_datacenter">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_datacenter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Hetzner Cloud Datacenter.
Use this resource to get detailed information about specific datacenter.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">ds1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_datacenter</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;fsn1-dc8&quot;</span><span class="p">)</span>
<span class="n">ds2</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_datacenter</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_datacenters">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_datacenters</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_datacenters" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a list of available Hetzner Cloud Datacenters.
This resource may be useful to create highly available infrastructure, distributed across several datacenters.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">ds</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_datacenters</span><span class="p">()</span>
<span class="n">workers</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">)]:</span>
    <span class="n">workers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;workers-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">datacenter</span><span class="o">=</span><span class="n">ds</span><span class="o">.</span><span class="n">names</span><span class="p">[</span><span class="nb">range</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">]],</span>
        <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
        <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx31&quot;</span><span class="p">))</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_floating_ip">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_floating_ip</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_floating_ip" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_image">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">most_recent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_load_balancer">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_load_balancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_load_balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Hetzner Cloud Server.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">lb1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_load_balancer</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;my-load-balancer&quot;</span><span class="p">)</span>
<span class="n">lb2</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_load_balancer</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;123&quot;</span><span class="p">)</span>
<span class="n">lb3</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_load_balancer</span><span class="p">(</span><span class="n">with_selector</span><span class="o">=</span><span class="s2">&quot;key=value&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_location">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_location</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific Hetzner Cloud Location.
Use this resource to get detailed information about specific location.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">l1</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_location</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;fsn1&quot;</span><span class="p">)</span>
<span class="n">l2</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_location</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_locations">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_locations</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">location_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a list of available Hetzner Cloud Locations.
This resource may be useful to create highly available infrastructure, distributed across several locations.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_hcloud</span> <span class="k">as</span> <span class="nn">hcloud</span>

<span class="n">ds</span> <span class="o">=</span> <span class="n">hcloud</span><span class="o">.</span><span class="n">get_locations</span><span class="p">()</span>
<span class="n">workers</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">)]:</span>
    <span class="n">workers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hcloud</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;workers-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">image</span><span class="o">=</span><span class="s2">&quot;debian-9&quot;</span><span class="p">,</span>
        <span class="n">location</span><span class="o">=</span><span class="n">ds</span><span class="o">.</span><span class="n">names</span><span class="p">[</span><span class="nb">range</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">]],</span>
        <span class="n">server_type</span><span class="o">=</span><span class="s2">&quot;cx31&quot;</span><span class="p">))</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_network">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_server">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_server</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_ssh_key">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_ssh_key</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_ssh_keys">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_ssh_keys</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_ssh_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_hcloud.get_volume">
<code class="sig-prename descclassname">pulumi_hcloud.</code><code class="sig-name descname">get_volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_selector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_statuses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_hcloud.get_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
