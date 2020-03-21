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
<span class="target" id="module-pulumi_spotinst.gcp"></span><dl class="class">
<dt id="pulumi_spotinst.gcp.Elastigroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.gcp.</code><code class="sig-name descname">Elastigroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">backend_services=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">disks=None</em>, <em class="sig-param">draining_timeout=None</em>, <em class="sig-param">fallback_to_ondemand=None</em>, <em class="sig-param">gpu=None</em>, <em class="sig-param">health_check_grace_period=None</em>, <em class="sig-param">health_check_type=None</em>, <em class="sig-param">instance_types_customs=None</em>, <em class="sig-param">instance_types_ondemand=None</em>, <em class="sig-param">instance_types_preemptibles=None</em>, <em class="sig-param">integration_docker_swarm=None</em>, <em class="sig-param">integration_gke=None</em>, <em class="sig-param">ip_forwarding=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">metadatas=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">ondemand_count=None</em>, <em class="sig-param">preemptible_percentage=None</em>, <em class="sig-param">scaling_down_policies=None</em>, <em class="sig-param">scaling_up_policies=None</em>, <em class="sig-param">scheduled_tasks=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">shutdown_script=None</em>, <em class="sig-param">startup_script=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">unhealthy_duration=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst elastigroup GCP resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/elastigroup_gcp.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/elastigroup_gcp.html.markdown</a>.</p>
</div></blockquote>
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
<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>List of availability zones for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The region your GCP group will be created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired number of instances the group should have at any time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.draining_timeout">
<code class="sig-name descname">draining_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.draining_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (seconds) the instance is allowed to run after it is detached from the group. This is to allow the instance time to drain all the current TCP connections before terminating it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.fallback_to_ondemand">
<code class="sig-name descname">fallback_to_ondemand</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.fallback_to_ondemand" title="Permalink to this definition">¶</a></dt>
<dd><p>Activate fallback-to-on-demand. When provisioning an instance, if no Preemptible market is available, fallback-to-on-demand will provision an On-Demand instance to maintain the group capacity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.instance_types_customs">
<code class="sig-name descname">instance_types_customs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.instance_types_customs" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines a set of custom instance types. Required if instance_types_preemptible and instance_types_ondemand are not set.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">memoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The memory (in GiB) in the custom instance types. GCP has a number of limitations on accepted memory values.For more information, see the GCP documentation (here.)[<a class="reference external" href="https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications">https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#specifications</a>]</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.instance_types_ondemand">
<code class="sig-name descname">instance_types_ondemand</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.instance_types_ondemand" title="Permalink to this definition">¶</a></dt>
<dd><p>The regular VM instance type to use for mixed-type groups and when falling back to on-demand. Required if instance_types_preemptible is not set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.instance_types_preemptibles">
<code class="sig-name descname">instance_types_preemptibles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.instance_types_preemptibles" title="Permalink to this definition">¶</a></dt>
<dd><p>The preemptible VMs instance type. To maximize cost savings and market availability, select as many types as possible. Required if instance_types_ondemand is not set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of objects with key-value pairs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Labels key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Labels value.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.max_size">
<code class="sig-name descname">max_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of instances the group should have at any time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.metadatas">
<code class="sig-name descname">metadatas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.metadatas" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of objects with key-value pairs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Labels key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Labels value.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.min_size">
<code class="sig-name descname">min_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of instances the group should have at any time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The group name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.preemptible_percentage">
<code class="sig-name descname">preemptible_percentage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.preemptible_percentage" title="Permalink to this definition">¶</a></dt>
<dd><p>Percentage of Preemptible VMs to spin up from the “desired_capacity”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.service_account">
<code class="sig-name descname">service_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The email of the service account in which the group instances will be launched.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.shutdown_script">
<code class="sig-name descname">shutdown_script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.shutdown_script" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-encoded shutdown script that executes prior to instance termination, for more information please see: <a class="reference external" href="https://api.spotinst.com/integration-docs/elastigroup/concepts/compute-concepts/shutdown-scripts/">Shutdown Script</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.startup_script">
<code class="sig-name descname">startup_script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.startup_script" title="Permalink to this definition">¶</a></dt>
<dd><p>Create and run your own startup scripts on your virtual machines to perform automated tasks every time your instance boots up.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.subnets">
<code class="sig-name descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of regions and subnets.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region for the group of subnets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The names of the subnets in the region.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.gcp.Elastigroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags to mark created instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.gcp.Elastigroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_healing=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">backend_services=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">disks=None</em>, <em class="sig-param">draining_timeout=None</em>, <em class="sig-param">fallback_to_ondemand=None</em>, <em class="sig-param">gpu=None</em>, <em class="sig-param">health_check_grace_period=None</em>, <em class="sig-param">health_check_type=None</em>, <em class="sig-param">instance_types_customs=None</em>, <em class="sig-param">instance_types_ondemand=None</em>, <em class="sig-param">instance_types_preemptibles=None</em>, <em class="sig-param">integration_docker_swarm=None</em>, <em class="sig-param">integration_gke=None</em>, <em class="sig-param">ip_forwarding=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">metadatas=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">ondemand_count=None</em>, <em class="sig-param">preemptible_percentage=None</em>, <em class="sig-param">scaling_down_policies=None</em>, <em class="sig-param">scaling_up_policies=None</em>, <em class="sig-param">scheduled_tasks=None</em>, <em class="sig-param">service_account=None</em>, <em class="sig-param">shutdown_script=None</em>, <em class="sig-param">startup_script=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">unhealthy_duration=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_spotinst.gcp.Elastigroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.gcp.Elastigroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.gcp.Elastigroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
