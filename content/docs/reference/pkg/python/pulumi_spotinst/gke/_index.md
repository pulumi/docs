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
<span class="target" id="module-pulumi_spotinst.gke"></span><dl class="py class">
<dt id="pulumi_spotinst.gke.Elastigroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.gke.</code><code class="sig-name descname">Elastigroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_zone_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draining_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_to_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_customs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_preemptibles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_docker_swarm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_gke</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_forwarding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadatas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ondemand_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preemptible_percentage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shutdown_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">startup_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Elastigroup GKE resource. Please see <a class="reference external" href="https://api.spotinst.com/elastigroup-for-google-cloud/tutorials/import-a-gke-cluster-as-an-elastigroup/">Importing a GKE cluster</a> for detailed information.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">example_gke_elastigroup</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">gke</span><span class="o">.</span><span class="n">Elastigroup</span><span class="p">(</span><span class="s2">&quot;example-gke-elastigroup&quot;</span><span class="p">,</span>
    <span class="n">backend_services</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;locationType&quot;</span><span class="p">:</span> <span class="s2">&quot;global&quot;</span><span class="p">,</span>
        <span class="s2">&quot;namedPorts&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
            <span class="s2">&quot;ports&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="mi">80</span><span class="p">,</span>
                <span class="mi">8080</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">}],</span>
        <span class="s2">&quot;serviceName&quot;</span><span class="p">:</span> <span class="s2">&quot;backend-service&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">cluster_zone_name</span><span class="o">=</span><span class="s2">&quot;us-central1-a&quot;</span><span class="p">,</span>
    <span class="n">desired_capacity</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">instance_types_ondemand</span><span class="o">=</span><span class="s2">&quot;n1-standard-1&quot;</span><span class="p">,</span>
    <span class="n">instance_types_preemptibles</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;n1-standard-1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;n1-standard-2&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">integration_gke</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;autoscaleCooldown&quot;</span><span class="p">:</span> <span class="mi">300</span><span class="p">,</span>
        <span class="s2">&quot;autoscaleDown&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;evaluationPeriods&quot;</span><span class="p">:</span> <span class="mi">300</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;autoscaleHeadroom&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;cpuPerUnit&quot;</span><span class="p">:</span> <span class="mi">1024</span><span class="p">,</span>
            <span class="s2">&quot;memoryPerUnit&quot;</span><span class="p">:</span> <span class="mi">512</span><span class="p">,</span>
            <span class="s2">&quot;numOfUnits&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;autoscaleIsAutoConfig&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="s2">&quot;autoscaleIsEnabled&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;autoscaleLabels&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;label_key&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;label_value&quot;</span><span class="p">,</span>
        <span class="p">}],</span>
        <span class="s2">&quot;clusterId&quot;</span><span class="p">:</span> <span class="s2">&quot;example-cluster-id&quot;</span><span class="p">,</span>
        <span class="s2">&quot;location&quot;</span><span class="p">:</span> <span class="s2">&quot;us-central1-a&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">max_size</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">min_size</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">node_image</span><span class="o">=</span><span class="s2">&quot;COS&quot;</span><span class="p">,</span>
    <span class="n">preemptible_percentage</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">integration_gke</span></code> - (Required) Describes the GKE integration.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> - (Optional) The location of your GKE cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> - (Optional) The GKE cluster ID you wish to import.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_is_enabled</span></code> -  (Optional, Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>) Specifies whether the auto scaling feature is enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_is_autoconfig</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>) Enabling the automatic auto-scaler functionality. For more information please see: .</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_cooldown</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">300</span></code>) The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_headroom</span></code> - (Optional) Headroom for the cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpu_per_unit</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>) Cpu units for compute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory_per_unit</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>) RAM units for compute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">num_of_units</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>) Amount of units for compute.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_down</span></code> - (Optional) Enabling scale down.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluation_periods</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">5</span></code>) Amount of cooldown evaluation periods for scale down.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscale_labels</span></code> - (Optional) Labels to assign to the resource.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> - (Optional) The label name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - (Optional) The label value.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>Usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="diff-suppressed-parameters"></a></span></p>
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
<dl class="py attribute">
<dt id="pulumi_spotinst.gke.Elastigroup.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the GKE cluster you wish to import.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.Elastigroup.cluster_zone_name">
<code class="sig-name descname">cluster_zone_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.cluster_zone_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone where the cluster is hosted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.Elastigroup.node_image">
<code class="sig-name descname">node_image</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.node_image" title="Permalink to this definition">¶</a></dt>
<dd><p>The image that will be used for the node VMs. Possible values: COS, UBUNTU.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.gke.Elastigroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_zone_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draining_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_to_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_customs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_preemptibles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_docker_swarm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_gke</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_forwarding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadatas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ondemand_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preemptible_percentage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shutdown_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">startup_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.gke.Elastigroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.Elastigroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.Elastigroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanImport">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.gke.</code><code class="sig-name descname">OceanImport</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscaler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">whitelists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Ocean GKE import resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">gke</span><span class="o">.</span><span class="n">OceanImport</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">backend_services</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;locationType&quot;</span><span class="p">:</span> <span class="s2">&quot;regional&quot;</span><span class="p">,</span>
        <span class="s2">&quot;namedPorts&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
            <span class="s2">&quot;ports&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="mi">80</span><span class="p">,</span>
                <span class="mi">8080</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">}],</span>
        <span class="s2">&quot;scheme&quot;</span><span class="p">:</span> <span class="s2">&quot;INTERNAL&quot;</span><span class="p">,</span>
        <span class="s2">&quot;serviceName&quot;</span><span class="p">:</span> <span class="s2">&quot;example-backend-service&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="s2">&quot;example-cluster-name&quot;</span><span class="p">,</span>
    <span class="n">desired_capacity</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-central1-a&quot;</span><span class="p">,</span>
    <span class="n">max_size</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">min_size</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">whitelists</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;n1-standard-1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;n1-standard-2&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scheduled_task</span></code> - (Optional) Set scheduling object.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">shutdown_hours</span></code> - (Optional) Set shutdown hours for cluster object.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">is_enabled</span></code> - (Optional)  Flag to enable / disable the shutdown hours.
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Example</span><span class="p">:</span> <span class="kc">True</span>
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_windows</span></code> - (Required) Set time windows for shutdown hours. specify a list of ‘timeWindows’ with at least one time window Each string is in the format of - ddd:hh:mm-ddd:hh:mm ddd = day of week = Sun | Mon | Tue | Wed | Thu | Fri | Sat hh = hour 24 = 0 -23 mm = minute = 0 - 59. Time windows should not overlap. required on cluster.scheduling.isEnabled = True. API Times are in UTC
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Example</span><span class="p">:</span> <span class="n">Fri</span><span class="p">:</span><span class="mi">15</span><span class="p">:</span><span class="mi">30</span><span class="o">-</span><span class="n">Wed</span><span class="p">:</span><span class="mi">14</span><span class="p">:</span><span class="mi">30</span>
</pre></div>
</div>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tasks</span></code> - (Optional) The scheduling tasks for the cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">is_enabled</span></code> - (Required)  Describes whether the task is enabled. When true the task should run when false it should not run. Required for cluster.scheduling.tasks object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cron_expression</span></code> - (Required) A valid cron expression. For example : ” * * * * * “.The cron is running in UTC time zone and is in Unix cron format Cron Expression Validator Script. Only one of ‘frequency’ or ‘cronExpression’ should be used at a time. Required for cluster.scheduling.tasks object
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Example</span><span class="p">:</span> <span class="mi">0</span> <span class="mi">1</span> <span class="o">*</span> <span class="o">*</span> <span class="o">*</span>
</pre></div>
</div>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">task_type</span></code> - (Required) Valid values: “clusterRoll”. Required for cluster.scheduling.tasks object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batch_size_percentage</span></code> - (Optional)  Value in % to set size of batch in roll. Valid values are 0-100
.. code-block:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">Example</span><span class="p">:</span> <span class="mf">20.</span>
</pre></div>
</div>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="autoscaler"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaler</span></code> - (Optional) The Ocean Kubernetes Autoscaler object.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">is_enabled</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>) Enable the Ocean Kubernetes Autoscaler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">is_auto_config</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>) Automatically configure and optimize headroom resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">auto_headroom_percentage</span></code> - Optionally set the auto headroom percentage, set a number between 0-200 to control the headroom % from the cluster. Relevant when isAutoConfig=true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">null</span></code>) Cooldown period between scaling actions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headroom</span></code> - (Optional) Spare resource capacity management enabling fast assignment of Pods without waiting for new resources to launch.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpu_per_unit</span></code> - (Optional) Optionally configure the number of CPUs to allocate the headroom. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory_per_unit</span></code> - (Optional) Optionally configure the amount of memory (MiB) to allocate the headroom.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpu_per_unit</span></code> - (Optional) How much GPU allocate for headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">num_of_units</span></code> - (Optional) The number of units to retain as headroom, where each unit has the defined headroom CPU and memory.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">down</span></code> - (Optional) Auto Scaling scale down operations.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluation_periods</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">null</span></code>) The number of evaluation periods that should accumulate before a scale down action takes place.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_scale_down_percentage</span></code> - (Optional) Would represent the maximum % to scale-down. Number between 1-100.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_limits</span></code> - (Optional) Optionally set upper and lower bounds on the resource usage of the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_vcpu</span></code> - (Optional) The maximum cpu in vCpu units that can be allocated to the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_memory_gib</span></code> - (Optional) The maximum memory in GiB units that can be allocated to the cluster.</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
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
<p>The <strong>autoscaler</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoHeadroomPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">down</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxScaleDownPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">isAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxMemoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
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
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shutdownHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tasks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanImport.backend_services">
<code class="sig-name descname">backend_services</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.backend_services" title="Permalink to this definition">¶</a></dt>
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

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanImport.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The GKE cluster name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanImport.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances to launch and maintain in the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanImport.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone the master cluster is located in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanImport.max_size">
<code class="sig-name descname">max_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The upper limit of instances the cluster can scale up to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanImport.min_size">
<code class="sig-name descname">min_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The lower limit of instances the cluster can scale down to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.gke.OceanImport.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscaler</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_controller_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">whitelists</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.get" title="Permalink to this definition">¶</a></dt>
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
<p>The <strong>autoscaler</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoHeadroomPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">down</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxScaleDownPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">isAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxMemoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
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
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">shutdownHours</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeWindows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tasks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.gke.OceanImport.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanImport.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanImport.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanLaunchSpec">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.gke.</code><code class="sig-name descname">OceanLaunchSpec</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscale_headrooms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadatas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ocean_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">taints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a custom Spotinst Ocean GKE Launch Spec resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">gke</span><span class="o">.</span><span class="n">OceanLaunchSpec</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">autoscale_headrooms</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;cpuPerUnit&quot;</span><span class="p">:</span> <span class="mi">1000</span><span class="p">,</span>
        <span class="s2">&quot;gpuPerUnit&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
        <span class="s2">&quot;memoryPerUnit&quot;</span><span class="p">:</span> <span class="mi">2048</span><span class="p">,</span>
        <span class="s2">&quot;numOfUnits&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">labels</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;labelKey&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;labelVal&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">metadatas</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;gci-update-strategy&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;update_disabled&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">ocean_id</span><span class="o">=</span><span class="s2">&quot;o-123456&quot;</span><span class="p">,</span>
    <span class="n">source_image</span><span class="o">=</span><span class="s2">&quot;image&quot;</span><span class="p">,</span>
    <span class="n">taints</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;effect&quot;</span><span class="p">:</span> <span class="s2">&quot;taintEffect&quot;</span><span class="p">,</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;taintKey&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;taintVal&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
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
<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.autoscale_headrooms">
<code class="sig-name descname">autoscale_headrooms</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.autoscale_headrooms" title="Permalink to this definition">¶</a></dt>
<dd><p>Set custom headroom per launch spec. provide list of headrooms object.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the number of CPUs to allocate for each headroom unit. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the number of GPUS to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the amount of memory (MB) to allocate for each headroom unit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of units to retain as headroom, where each unit has the defined headroom CPU, memory and GPU.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster’s labels.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.metadatas">
<code class="sig-name descname">metadatas</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.metadatas" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster’s metadata.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.ocean_id">
<code class="sig-name descname">ocean_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.ocean_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ocean cluster ID required for launchSpec create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.source_image">
<code class="sig-name descname">source_image</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.source_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Image URL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.taints">
<code class="sig-name descname">taints</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.taints" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster’s taints.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscale_headrooms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadatas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ocean_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_image</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">taints</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanLaunchSpec.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpec.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.gke.</code><code class="sig-name descname">OceanLaunchSpecImport</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_pool_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ocean_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a custom Spotinst Ocean GKE Launch Spec Import resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">gke</span><span class="o">.</span><span class="n">OceanLaunchSpecImport</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">node_pool_name</span><span class="o">=</span><span class="s2">&quot;default-pool&quot;</span><span class="p">,</span>
    <span class="n">ocean_id</span><span class="o">=</span><span class="s2">&quot;o-123456&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport.node_pool_name">
<code class="sig-name descname">node_pool_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport.node_pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The node pool you wish to use in your launchSpec.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport.ocean_id">
<code class="sig-name descname">ocean_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport.ocean_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ocean cluster ID required for launchSpec create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_pool_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ocean_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gke.OceanLaunchSpecImport.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gke.OceanLaunchSpecImport.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
