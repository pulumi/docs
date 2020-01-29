---
title: Module gke
title_tag: Module gke | Package pulumi_spotinst | Python SDK
linktitle: gke
notitle: true
---

<div class="section" id="gke">
<h1>gke<a class="headerlink" href="#gke" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-spotinst/issues">pulumi/pulumi-spotinst repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/issues">terraform-providers/terraform-provider-spotinst repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_spotinst.gke"></span><dl class="class">
<dt id="pulumi_spotinst.gke.Elastigroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.gke.</code><code class="sig-name descname">Elastigroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_services=None</em>, <em class="sig-param">cluster_id=None</em>, <em class="sig-param">cluster_zone_name=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">disks=None</em>, <em class="sig-param">draining_timeout=None</em>, <em class="sig-param">fallback_to_ondemand=None</em>, <em class="sig-param">gpu=None</em>, <em class="sig-param">instance_types_customs=None</em>, <em class="sig-param">instance_types_ondemand=None</em>, <em class="sig-param">instance_types_preemptibles=None</em>, <em class="sig-param">integration_docker_swarm=None</em>, <em class="sig-param">integration_gke=None</em>, <em class="sig-param">ip_forwarding=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">metadatas=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">node_image=None</em>, <em class="sig-param">ondemand_count=None</em>, <em class="sig-param">preemptible_percentage=None</em>, <em class="sig-param">scaling_down_policies=None</em>, <em class="sig-param">scaling_up_policies=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">shutdown_script=None</em>, <em class="sig-param">startup_script=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Elastigroup GKE resource. Please see <a class="reference external" href="https://api.spotinst.com/elastigroup-for-google-cloud/tutorials/import-a-gke-cluster-as-an-elastigroup/">Importing a GKE cluster</a> for detailed information.</p>
<p>The following parameters are created remotely and imported. The diffs have been suppressed in order to maintain plan legibility. You may update the values of these
imported parameters by defining them in your template with your desired new value (including null values).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backend_services</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location_type</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">named_port</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port_name</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code></p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_forwarding</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fallback_to_od</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_name</span></code></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the GKE cluster you wish to import.</p></li>
<li><p><strong>cluster_zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone where the cluster is hosted.</p></li>
<li><p><strong>node_image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image that will be used for the node VMs. Possible values: COS, UBUNTU.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backend_services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">locationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">boot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initializeParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">diskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>gpu</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>instance_types_customs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">memoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>integration_docker_swarm</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">masterHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>integration_gke</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpdate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleLabels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the GKE cluster you wish to import.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>metadatas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">aliasIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ipCidrRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_down_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_up_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/elastigroup_gke.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/elastigroup_gke.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_spotinst.gke.Elastigroup.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the GKE cluster you wish to import.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.Elastigroup.cluster_zone_name">
<code class="sig-name descname">cluster_zone_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.cluster_zone_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone where the cluster is hosted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.Elastigroup.node_image">
<code class="sig-name descname">node_image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.node_image" title="Permalink to this definition">¶</a></dt>
<dd><p>The image that will be used for the node VMs. Possible values: COS, UBUNTU.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.gke.Elastigroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_services=None</em>, <em class="sig-param">cluster_id=None</em>, <em class="sig-param">cluster_zone_name=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">disks=None</em>, <em class="sig-param">draining_timeout=None</em>, <em class="sig-param">fallback_to_ondemand=None</em>, <em class="sig-param">gpu=None</em>, <em class="sig-param">instance_types_customs=None</em>, <em class="sig-param">instance_types_ondemand=None</em>, <em class="sig-param">instance_types_preemptibles=None</em>, <em class="sig-param">integration_docker_swarm=None</em>, <em class="sig-param">integration_gke=None</em>, <em class="sig-param">ip_forwarding=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">metadatas=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">node_image=None</em>, <em class="sig-param">ondemand_count=None</em>, <em class="sig-param">preemptible_percentage=None</em>, <em class="sig-param">scaling_down_policies=None</em>, <em class="sig-param">scaling_up_policies=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">shutdown_script=None</em>, <em class="sig-param">startup_script=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Elastigroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the GKE cluster you wish to import.</p></li>
<li><p><strong>cluster_zone_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone where the cluster is hosted.</p></li>
<li><p><strong>node_image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The image that will be used for the node VMs. Possible values: COS, UBUNTU.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backend_services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">locationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">boot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initializeParams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">diskSizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>gpu</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>instance_types_customs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">memoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>integration_docker_swarm</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">masterHost</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>integration_gke</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpdate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleCooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleDown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleHeadroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleIsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaleLabels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the GKE cluster you wish to import.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>metadatas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">aliasIpRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ipCidrRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetworkRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_down_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_up_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/elastigroup_gke.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/elastigroup_gke.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.gke.Elastigroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.Elastigroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanImport">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.gke.</code><code class="sig-name descname">OceanImport</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_services=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">whitelists=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Ocean GKE import resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Describes the backend service configurations.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GKE cluster name.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of instances to launch and maintain in the cluster.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone the master cluster is located in.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The upper limit of instances the cluster can scale up to.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The lower limit of instances the cluster can scale down to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backend_services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">locationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets which location the backend services will be active. Valid values: <code class="docutils literal notranslate"><span class="pre">regional</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of ports.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Use when <code class="docutils literal notranslate"><span class="pre">location_type</span></code> is <code class="docutils literal notranslate"><span class="pre">regional</span></code>. Set the traffic for the backend service to either between the instances in the vpc or to traffic from the internet. Valid values: <code class="docutils literal notranslate"><span class="pre">INTERNAL</span></code>, <code class="docutils literal notranslate"><span class="pre">EXTERNAL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the backend service.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_import.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_import.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanImport.backend_services">
<code class="sig-name descname">backend_services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.backend_services" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the backend service configurations.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">locationType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sets which location the backend services will be active. Valid values: <code class="docutils literal notranslate"><span class="pre">regional</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of ports.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Use when <code class="docutils literal notranslate"><span class="pre">location_type</span></code> is <code class="docutils literal notranslate"><span class="pre">regional</span></code>. Set the traffic for the backend service to either between the instances in the vpc or to traffic from the internet. Valid values: <code class="docutils literal notranslate"><span class="pre">INTERNAL</span></code>, <code class="docutils literal notranslate"><span class="pre">EXTERNAL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the backend service.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanImport.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The GKE cluster name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanImport.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances to launch and maintain in the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanImport.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone the master cluster is located in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanImport.max_size">
<code class="sig-name descname">max_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The upper limit of instances the cluster can scale up to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanImport.min_size">
<code class="sig-name descname">min_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The lower limit of instances the cluster can scale down to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.gke.OceanImport.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_services=None</em>, <em class="sig-param">cluster_controller_id=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">whitelists=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OceanImport resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Describes the backend service configurations.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GKE cluster name.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of instances to launch and maintain in the cluster.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone the master cluster is located in.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The upper limit of instances the cluster can scale up to.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The lower limit of instances the cluster can scale down to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backend_services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">locationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets which location the backend services will be active. Valid values: <code class="docutils literal notranslate"><span class="pre">regional</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of ports.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Use when <code class="docutils literal notranslate"><span class="pre">location_type</span></code> is <code class="docutils literal notranslate"><span class="pre">regional</span></code>. Set the traffic for the backend service to either between the instances in the vpc or to traffic from the internet. Valid values: <code class="docutils literal notranslate"><span class="pre">INTERNAL</span></code>, <code class="docutils literal notranslate"><span class="pre">EXTERNAL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the backend service.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_import.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_import.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.gke.OceanImport.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanImport.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanLaunchSpec">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.gke.</code><code class="sig-name descname">OceanLaunchSpec</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscale_headrooms=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">metadatas=None</em>, <em class="sig-param">ocean_id=None</em>, <em class="sig-param">source_image=None</em>, <em class="sig-param">taints=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a custom Spotinst Ocean GKE Launch Spec resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscale_headrooms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set custom headroom per launch spec. provide list of headrooms object.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Cluster’s labels.</p></li>
<li><p><strong>metadatas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Cluster’s metadata.</p></li>
<li><p><strong>ocean_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ocean cluster ID required for launchSpec create.</p></li>
<li><p><strong>source_image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Image URL.</p></li>
<li><p><strong>taints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Cluster’s taints.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscale_headrooms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the number of CPUs to allocate for each headroom unit. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the number of GPUS to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the amount of memory (MB) to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of units to retain as headroom, where each unit has the defined headroom CPU, memory and GPU.</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>metadatas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>taints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_launch_spec.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_launch_spec.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.autoscale_headrooms">
<code class="sig-name descname">autoscale_headrooms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.autoscale_headrooms" title="Permalink to this definition">¶</a></dt>
<dd><p>Set custom headroom per launch spec. provide list of headrooms object.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the number of CPUs to allocate for each headroom unit. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the number of GPUS to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the amount of memory (MB) to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of units to retain as headroom, where each unit has the defined headroom CPU, memory and GPU.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster’s labels.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.metadatas">
<code class="sig-name descname">metadatas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.metadatas" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster’s metadata.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.ocean_id">
<code class="sig-name descname">ocean_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.ocean_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ocean cluster ID required for launchSpec create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.source_image">
<code class="sig-name descname">source_image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.source_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Image URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.taints">
<code class="sig-name descname">taints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.taints" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster’s taints.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscale_headrooms=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">metadatas=None</em>, <em class="sig-param">ocean_id=None</em>, <em class="sig-param">source_image=None</em>, <em class="sig-param">taints=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OceanLaunchSpec resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscale_headrooms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Set custom headroom per launch spec. provide list of headrooms object.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Cluster’s labels.</p></li>
<li><p><strong>metadatas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Cluster’s metadata.</p></li>
<li><p><strong>ocean_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ocean cluster ID required for launchSpec create.</p></li>
<li><p><strong>source_image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Image URL.</p></li>
<li><p><strong>taints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Cluster’s taints.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscale_headrooms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the number of CPUs to allocate for each headroom unit. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the number of GPUS to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the amount of memory (MB) to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of units to retain as headroom, where each unit has the defined headroom CPU, memory and GPU.</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>metadatas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>taints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_launch_spec.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_launch_spec.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.gke.</code><code class="sig-name descname">OceanLaunchSpecImport</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">node_pool_name=None</em>, <em class="sig-param">ocean_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a custom Spotinst Ocean GKE Launch Spec Import resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>node_pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The node pool you wish to use in your launchSpec.</p></li>
<li><p><strong>ocean_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ocean cluster ID required for launchSpec create.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_launch_spec_import.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_launch_spec_import.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport.node_pool_name">
<code class="sig-name descname">node_pool_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport.node_pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The node pool you wish to use in your launchSpec.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport.ocean_id">
<code class="sig-name descname">ocean_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport.ocean_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ocean cluster ID required for launchSpec create.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">node_pool_name=None</em>, <em class="sig-param">ocean_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OceanLaunchSpecImport resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>node_pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The node pool you wish to use in your launchSpec.</p></li>
<li><p><strong>ocean_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ocean cluster ID required for launchSpec create.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_launch_spec_import.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_gke_launch_spec_import.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
