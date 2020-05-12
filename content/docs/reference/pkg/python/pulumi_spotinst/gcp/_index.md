---
title: Module gcp
title_tag: Module gcp | Package pulumi_spotinst | Python SDK
linktitle: gcp
notitle: true
---

<div class="section" id="gcp">
<h1>gcp<a class="headerlink" href="#gcp" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-spotinst/issues">pulumi/pulumi-spotinst repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/issues">terraform-providers/terraform-provider-spotinst repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_spotinst.gcp"></span><dl class="py class">
<dt id="pulumi_spotinst.gcp.Elastigroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.gcp.</code><code class="sig-name descname">Elastigroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draining_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_to_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_grace_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_customs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_preemptibles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_docker_swarm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_gke</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_forwarding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadatas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ondemand_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preemptible_percentage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shutdown_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">startup_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unhealthy_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst elastigroup GCP resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">gcp</span><span class="o">.</span><span class="n">Elastigroup</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">availability_zones</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;asia-east1-c&quot;</span><span class="p">,</span>
        <span class="s2">&quot;us-central1-a&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">backend_services_config</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;ports&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;portName&quot;</span><span class="p">:</span> <span class="s2">&quot;port-name&quot;</span><span class="p">,</span>
            <span class="s2">&quot;ports&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="mi">8000</span><span class="p">,</span>
                <span class="mi">6000</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">}],</span>
        <span class="s2">&quot;serviceName&quot;</span><span class="p">:</span> <span class="s2">&quot;spotinst-elb-backend-service&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;spotinst gcp group&quot;</span><span class="p">,</span>
    <span class="n">desired_capacity</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">disks</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;autoDelete&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;boot&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;deviceName&quot;</span><span class="p">:</span> <span class="s2">&quot;device&quot;</span><span class="p">,</span>
        <span class="s2">&quot;initializeParams&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;diskSizeGb&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
            <span class="s2">&quot;diskType&quot;</span><span class="p">:</span> <span class="s2">&quot;pd-standard&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sourceImage&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
        <span class="p">}],</span>
        <span class="s2">&quot;interface&quot;</span><span class="p">:</span> <span class="s2">&quot;SCSI&quot;</span><span class="p">,</span>
        <span class="s2">&quot;mode&quot;</span><span class="p">:</span> <span class="s2">&quot;READ_WRITE&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;PERSISTENT&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">draining_timeout</span><span class="o">=</span><span class="mi">180</span><span class="p">,</span>
    <span class="n">fallback_to_ondemand</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">instance_types_customs</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;memoryGiB&quot;</span><span class="p">:</span> <span class="mf">7.5</span><span class="p">,</span>
        <span class="s2">&quot;vCPU&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">instance_types_ondemand</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;n1-standard-1&quot;</span><span class="p">],</span>
    <span class="n">instance_types_preemptibles</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;n1-standard-1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;n1-standard-2&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">labels</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;test_key&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;test_value&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">max_size</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">min_size</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">network_interfaces</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;network&quot;</span><span class="p">:</span> <span class="s2">&quot;spot-network&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">preemptible_percentage</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span>
    <span class="n">scaling</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;up&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;action&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;adjustment&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
                <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;adjustment&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
            <span class="s2">&quot;cooldown&quot;</span><span class="p">:</span> <span class="mi">300</span><span class="p">,</span>
            <span class="s2">&quot;dimensions&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;storage_type&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;pd-ssd&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
            <span class="s2">&quot;evaluationPeriods&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
            <span class="s2">&quot;metricName&quot;</span><span class="p">:</span> <span class="s2">&quot;instance/disk/read_ops_count&quot;</span><span class="p">,</span>
            <span class="s2">&quot;namespace&quot;</span><span class="p">:</span> <span class="s2">&quot;compute&quot;</span><span class="p">,</span>
            <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;gte&quot;</span><span class="p">,</span>
            <span class="s2">&quot;period&quot;</span><span class="p">:</span> <span class="mi">300</span><span class="p">,</span>
            <span class="s2">&quot;policyName&quot;</span><span class="p">:</span> <span class="s2">&quot;scale_up_1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;source&quot;</span><span class="p">:</span> <span class="s2">&quot;stackdriver&quot;</span><span class="p">,</span>
            <span class="s2">&quot;statistic&quot;</span><span class="p">:</span> <span class="s2">&quot;average&quot;</span><span class="p">,</span>
            <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="mi">10000</span><span class="p">,</span>
            <span class="s2">&quot;unit&quot;</span><span class="p">:</span> <span class="s2">&quot;percent&quot;</span><span class="p">,</span>
        <span class="p">}],</span>
    <span class="p">}],</span>
    <span class="n">service_account</span><span class="o">=</span><span class="s2">&quot;example@myProject.iam.gservicecct.com&quot;</span><span class="p">,</span>
    <span class="n">startup_script</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="n">subnets</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;region&quot;</span><span class="p">:</span> <span class="s2">&quot;asia-east1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;subnetNames&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;http&quot;</span><span class="p">,</span>
        <span class="s2">&quot;https&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">gpu</span></code> - (Optional) Defines the GPU configuration.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Required) The type of GPU instance. Valid values: <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-v100</span></code>, <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-p100</span></code>, <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> - (Required) The number of GPUs. Must be 0, 2, 4, 6, 8.</p></li>
</ul>
</li>
</ul>
<p>Usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="health-check"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backend_services</span></code> - (Optional) Describes the backend service configurations.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">service_name</span></code> - (Required) The name of the backend service.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location_type</span></code> - (Optional) Sets which location the backend services will be active. Valid values: <code class="docutils literal notranslate"><span class="pre">regional</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> - (Optional) Use when <code class="docutils literal notranslate"><span class="pre">location_type</span></code> is “regional”. Set the traffic for the backend service to either between the instances in the vpc or to traffic from the internet. Valid values: <code class="docutils literal notranslate"><span class="pre">INTERNAL</span></code>, <code class="docutils literal notranslate"><span class="pre">EXTERNAL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">named_port</span></code> - (Optional) Describes a named port and a list of ports.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port_name</span></code> - (Required) The name of the port.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> - (Required) A list of ports.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>Usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="disks"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disks</span></code> - (Optional) Array of disks associated with this instance. Persistent disks must be created before you can assign them.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">auto_delete</span></code> - (Optional) Specifies whether the disk will be auto-deleted when the instance is deleted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">boot</span></code> - (Optional) Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device_name</span></code> - (Optional) Specifies a unique device name of your choice.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">SCSI</span></code>) Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">READ_WRITE</span></code>) The mode in which to attach this disk, either READ_WRITE or READ_ONLY.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source</span></code> - (Optional) Specifies a valid partial or full URL to an existing Persistent Disk resource. This field is only applicable for persistent disks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">PERSISTENT</span></code>) Specifies the type of disk, either SCRATCH or PERSISTENT.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialize_params</span></code> - (Optional) Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> - (Optional) Specifies disk size in gigabytes. Must be in increments of 2.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_type</span></code> - (Optional, Default” <code class="docutils literal notranslate"><span class="pre">pd-standard</span></code>) Specifies the disk type to use to create the instance. Valid values: pd-ssd, local-ssd.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_image</span></code> - (Optional) A source image used to create the disk. You can provide a private (custom) image, and Compute Engine will use the corresponding image from your project.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>Usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="network-interface"></a></span></p>
<p>Each of the <code class="docutils literal notranslate"><span class="pre">network_interface</span></code> attributes controls a portion of the GCP
Instance’s “Network Interfaces”. It’s a good idea to familiarize yourself with <a class="reference external" href="https://cloud.google.com/vpc/docs/multiple-interfaces-concepts">GCP’s Network
Interfaces docs</a>
to understand the implications of using these attributes.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">network_interface</span></code> - (Required, minimum 1) Array of objects representing the network configuration for the elastigroup.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> - (Required) Network resource for this group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">access_configs</span></code> - (Optional) Array of configurations.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Optional) Name of this access configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Optional) Array of configurations for this interface. Currently, only ONE_TO_ONE_NAT is supported.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="scaling-policy"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">scaling_up_policy</span></code> - (Optional) Contains scaling policies for scaling the Elastigroup up.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaling_down_policy</span></code> - (Optional) Contains scaling policies for scaling the Elastigroup down.</p></li>
</ul>
<p>Each <code class="docutils literal notranslate"><span class="pre">scaling_*_policy</span></code> supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">policy_name</span></code> - (Optional) Name of scaling policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> - (Optional) Metric to monitor. Valid values: “Percentage CPU”, “Network In”, “Network Out”, “Disk Read Bytes”, “Disk Write Bytes”, “Disk Write Operations/Sec”, “Disk Read Operations/Sec”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> - (Optional) Statistic by which to evaluate the selected metric. Valid values: “AVERAGE”, “SAMPLE_COUNT”, “SUM”, “MINIMUM”, “MAXIMUM”, “PERCENTILE”, “COUNT”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> - (Optional) The value at which the scaling action is triggered.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> - (Optional) Amount of time (seconds) for which the threshold must be met in order to trigger the scaling action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluation_periods</span></code> - (Optional) Number of consecutive periods in which the threshold must be met in order to trigger a scaling action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> - (Optional) Time (seconds) to wait after a scaling action before resuming monitoring.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> - (Optional) The operator used to evaluate the threshold against the current metric value. Valid values: “gt” (greater than), “get” (greater-than or equal), “lt” (less than), “lte” (less than or equal).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> - (Optional) Scaling action to take when the policy is triggered.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Optional) Type of scaling action to take when the scaling policy is triggered. Valid values: “adjustment”, “setMinTarget”, “updateCapacity”, “percentageAdjustment”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> - (Optional) Value to which the action type will be adjusted. Required if using “numeric” or “percentageAdjustment” action types.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> - (Optional) A list of dimensions describing qualities of the metric.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The dimension name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - (Required) The dimension value.</p></li>
</ul>
</li>
</ul>
<p>Usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="third-party-integrations"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">integration_docker_swarm</span></code> - (Optional) Describes the <a class="reference external" href="https://api.spotinst.com/integration-docs/elastigroup/container-management/docker-swarm/docker-swarm-integration/">Docker Swarm</a> integration.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">master_host</span></code> - (Required) IP or FQDN of one of your swarm managers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_port</span></code> - (Required) Network port used by your swarm.</p></li>
</ul>
</li>
</ul>
<p>Usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="scheduled-task"></a></span></p>
<p>Each <code class="docutils literal notranslate"><span class="pre">scheduled_task</span></code> supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">task_type</span></code> - (Required) The task type to run. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;setCapacity&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cron_expression</span></code> - (Optional) A valid cron expression. The cron is running in UTC time zone and is in <a class="reference external" href="https://en.wikipedia.org/wiki/Cron">Unix cron format</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">is_enabled</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>) Setting the task to being enabled or disabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_capacity</span></code> - (Optional) The desired number of instances the group should have.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_capacity</span></code> - (Optional) The minimum number of instances the group should have.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_capacity</span></code> - (Optional) The maximum number of instances the group should have.</p></li>
</ul>
<p>Usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of availability zones for the group.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region your GCP group will be created in.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired number of instances the group should have at any time.</p></li>
<li><p><strong>draining_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (seconds) the instance is allowed to run after it is detached from the group. This is to allow the instance time to drain all the current TCP connections before terminating it.</p></li>
<li><p><strong>fallback_to_ondemand</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Activate fallback-to-on-demand. When provisioning an instance, if no Preemptible market is available, fallback-to-on-demand will provision an On-Demand instance to maintain the group capacity.</p></li>
<li><p><strong>instance_types_customs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Defines a set of custom instance types. Required if instance_types_preemptible and instance_types_ondemand are not set.</p></li>
<li><p><strong>instance_types_ondemand</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The regular VM instance type to use for mixed-type groups and when falling back to on-demand. Required if instance_types_preemptible is not set.</p></li>
<li><p><strong>instance_types_preemptibles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The preemptible VMs instance type. To maximize cost savings and market availability, select as many types as possible. Required if instance_types_ondemand is not set.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of objects with key-value pairs.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of instances the group should have at any time.</p></li>
<li><p><strong>metadatas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of objects with key-value pairs.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of instances the group should have at any time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group name.</p></li>
<li><p><strong>preemptible_percentage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Percentage of Preemptible VMs to spin up from the “desired_capacity”.</p></li>
<li><p><strong>service_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email of the service account in which the group instances will be launched.</p></li>
<li><p><strong>shutdown_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-encoded shutdown script that executes prior to instance termination, for more information please see: <a class="reference external" href="https://api.spotinst.com/integration-docs/elastigroup/concepts/compute-concepts/shutdown-scripts/">Shutdown Script</a></p></li>
<li><p><strong>startup_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Create and run your own startup scripts on your virtual machines to perform automated tasks every time your instance boots up.</p></li>
<li><p><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of regions and subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags to mark created instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backend_services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">locationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">memoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The memory (in GiB) in the custom instance types. GCP has a number of limitations on accepted memory values.For more information, see the GCP documentation (here.)[<a class="reference external" href="https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications">https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications</a>]</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels value.</p></li>
</ul>
<p>The <strong>metadatas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels value.</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels value.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels value.</p></li>
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
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>subnets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region for the group of subnets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The names of the subnets in the region.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of availability zones for the group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The region your GCP group will be created in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.draining_timeout">
<code class="sig-name descname">draining_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.draining_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (seconds) the instance is allowed to run after it is detached from the group. This is to allow the instance time to drain all the current TCP connections before terminating it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.fallback_to_ondemand">
<code class="sig-name descname">fallback_to_ondemand</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.fallback_to_ondemand" title="Permalink to this definition">¶</a></dt>
<dd><p>Activate fallback-to-on-demand. When provisioning an instance, if no Preemptible market is available, fallback-to-on-demand will provision an On-Demand instance to maintain the group capacity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.instance_types_customs">
<code class="sig-name descname">instance_types_customs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.instance_types_customs" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines a set of custom instance types. Required if instance_types_preemptible and instance_types_ondemand are not set.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">memoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The memory (in GiB) in the custom instance types. GCP has a number of limitations on accepted memory values.For more information, see the GCP documentation (here.)[<a class="reference external" href="https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications">https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications</a>]</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.instance_types_ondemand">
<code class="sig-name descname">instance_types_ondemand</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.instance_types_ondemand" title="Permalink to this definition">¶</a></dt>
<dd><p>The regular VM instance type to use for mixed-type groups and when falling back to on-demand. Required if instance_types_preemptible is not set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.instance_types_preemptibles">
<code class="sig-name descname">instance_types_preemptibles</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.instance_types_preemptibles" title="Permalink to this definition">¶</a></dt>
<dd><p>The preemptible VMs instance type. To maximize cost savings and market availability, select as many types as possible. Required if instance_types_ondemand is not set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of objects with key-value pairs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Labels key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Labels value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.max_size">
<code class="sig-name descname">max_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.metadatas">
<code class="sig-name descname">metadatas</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.metadatas" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of objects with key-value pairs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Labels key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Labels value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.min_size">
<code class="sig-name descname">min_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The group name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.preemptible_percentage">
<code class="sig-name descname">preemptible_percentage</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.preemptible_percentage" title="Permalink to this definition">¶</a></dt>
<dd><p>Percentage of Preemptible VMs to spin up from the “desired_capacity”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.service_account">
<code class="sig-name descname">service_account</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of the service account in which the group instances will be launched.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.shutdown_script">
<code class="sig-name descname">shutdown_script</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.shutdown_script" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-encoded shutdown script that executes prior to instance termination, for more information please see: <a class="reference external" href="https://api.spotinst.com/integration-docs/elastigroup/concepts/compute-concepts/shutdown-scripts/">Shutdown Script</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.startup_script">
<code class="sig-name descname">startup_script</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.startup_script" title="Permalink to this definition">¶</a></dt>
<dd><p>Create and run your own startup scripts on your virtual machines to perform automated tasks every time your instance boots up.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.subnets">
<code class="sig-name descname">subnets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regions and subnets.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region for the group of subnets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The names of the subnets in the region.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags to mark created instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.gcp.Elastigroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_healing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draining_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fallback_to_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_grace_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_customs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_ondemand</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types_preemptibles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_docker_swarm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_gke</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_forwarding</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metadatas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ondemand_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preemptible_percentage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shutdown_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">startup_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unhealthy_duration</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Elastigroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of availability zones for the group.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region your GCP group will be created in.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired number of instances the group should have at any time.</p></li>
<li><p><strong>draining_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (seconds) the instance is allowed to run after it is detached from the group. This is to allow the instance time to drain all the current TCP connections before terminating it.</p></li>
<li><p><strong>fallback_to_ondemand</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Activate fallback-to-on-demand. When provisioning an instance, if no Preemptible market is available, fallback-to-on-demand will provision an On-Demand instance to maintain the group capacity.</p></li>
<li><p><strong>instance_types_customs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Defines a set of custom instance types. Required if instance_types_preemptible and instance_types_ondemand are not set.</p></li>
<li><p><strong>instance_types_ondemand</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The regular VM instance type to use for mixed-type groups and when falling back to on-demand. Required if instance_types_preemptible is not set.</p></li>
<li><p><strong>instance_types_preemptibles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The preemptible VMs instance type. To maximize cost savings and market availability, select as many types as possible. Required if instance_types_ondemand is not set.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of objects with key-value pairs.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of instances the group should have at any time.</p></li>
<li><p><strong>metadatas</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of objects with key-value pairs.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of instances the group should have at any time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group name.</p></li>
<li><p><strong>preemptible_percentage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Percentage of Preemptible VMs to spin up from the “desired_capacity”.</p></li>
<li><p><strong>service_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email of the service account in which the group instances will be launched.</p></li>
<li><p><strong>shutdown_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The Base64-encoded shutdown script that executes prior to instance termination, for more information please see: <a class="reference external" href="https://api.spotinst.com/integration-docs/elastigroup/concepts/compute-concepts/shutdown-scripts/">Shutdown Script</a></p>
</p></li>
<li><p><strong>startup_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Create and run your own startup scripts on your virtual machines to perform automated tasks every time your instance boots up.</p></li>
<li><p><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of regions and subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags to mark created instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backend_services</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">locationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namedPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">memoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The memory (in GiB) in the custom instance types. GCP has a number of limitations on accepted memory values.For more information, see the GCP documentation (here.)[<a class="reference external" href="https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications">https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications</a>]</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels value.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>labels</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels value.</p></li>
</ul>
<p>The <strong>metadatas</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels value.</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels value.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Labels value.</p></li>
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
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>subnets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region for the group of subnets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The names of the subnets in the region.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.gcp.Elastigroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gcp.Elastigroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
