---
title: Module ecs
title_tag: Module ecs | Package pulumi_spotinst | Python SDK
linktitle: ecs
notitle: true
---

<div class="section" id="ecs">
<h1>ecs<a class="headerlink" href="#ecs" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-spotinst/issues">pulumi/pulumi-spotinst repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/issues">terraform-providers/terraform-provider-spotinst repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_spotinst.ecs"></span><dl class="class">
<dt id="pulumi_spotinst.ecs.Ocean">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.ecs.</code><code class="sig-name descname">Ocean</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">associate_public_ip_address=None</em>, <em class="sig-param">autoscaler=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">draining_timeout=None</em>, <em class="sig-param">ebs_optimized=None</em>, <em class="sig-param">iam_instance_profile=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">key_pair=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">monitoring=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">update_policy=None</em>, <em class="sig-param">user_data=None</em>, <em class="sig-param">utilize_reserved_instances=None</em>, <em class="sig-param">whitelists=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Ocean ECS resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>associate_public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Configure public IP address allocation.</p></li>
<li><p><strong>autoscaler</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the Ocean ECS autoscaler.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ocean cluster name.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of instances to launch and maintain in the cluster.</p></li>
<li><p><strong>draining_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance profile iam role.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the image used to launch the instances.</p></li>
<li><p><strong>key_pair</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key pair to attach the instances.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The upper limit of instances the cluster can scale up to.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The lower limit of instances the cluster can scale down to.</p></li>
<li><p><strong>monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ocean cluster name.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region the cluster will run in.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more security group ids.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds tags to instances launched in an Ocean cluster.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded MIME user data to make available to the instances.</p></li>
<li><p><strong>whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Instance types allowed in the Ocean cluster.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaler</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Cooldown period between scaling actions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">down</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Auto Scaling scale down operations.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxScaleDownPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Would represent the maximum % to scale-down. Number between 1-100</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Spare resource capacity management enabling fast assignment of tasks without waiting for new resources to launch.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the number of CPUs to allocate the headroom. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the amount of memory (MB) to allocate the headroom.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of units to retain as headroom, where each unit has the defined headroom CPU and memory.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">isAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Automatically configure and optimize headroom resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the Ocean ECS autoscaler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optionally set upper and lower bounds on the resource usage of the cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxMemoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum memory in GiB units that can be allocated to the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum cpu in vCPU units that can be allocated to the cluster.</p></li>
</ul>
</li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value.</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rollConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_ecs.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_ecs.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.associate_public_ip_address">
<code class="sig-name descname">associate_public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.associate_public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Configure public IP address allocation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.autoscaler">
<code class="sig-name descname">autoscaler</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.autoscaler" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the Ocean ECS autoscaler.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Cooldown period between scaling actions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">down</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Auto Scaling scale down operations.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxScaleDownPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Would represent the maximum % to scale-down. Number between 1-100</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headroom</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Spare resource capacity management enabling fast assignment of tasks without waiting for new resources to launch.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the number of CPUs to allocate the headroom. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Optionally configure the amount of memory (MB) to allocate the headroom.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of units to retain as headroom, where each unit has the defined headroom CPU and memory.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">isAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Automatically configure and optimize headroom resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enable the Ocean ECS autoscaler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Optionally set upper and lower bounds on the resource usage of the cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxMemoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum memory in GiB units that can be allocated to the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum cpu in vCPU units that can be allocated to the cluster.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The ocean cluster name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances to launch and maintain in the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.draining_timeout">
<code class="sig-name descname">draining_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.draining_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.ebs_optimized">
<code class="sig-name descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.iam_instance_profile">
<code class="sig-name descname">iam_instance_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance profile iam role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the image used to launch the instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.key_pair">
<code class="sig-name descname">key_pair</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.key_pair" title="Permalink to this definition">¶</a></dt>
<dd><p>The key pair to attach the instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.max_size">
<code class="sig-name descname">max_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The upper limit of instances the cluster can scale up to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.min_size">
<code class="sig-name descname">min_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The lower limit of instances the cluster can scale down to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.monitoring">
<code class="sig-name descname">monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ocean cluster name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region the cluster will run in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more security group ids.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Optionally adds tags to instances launched in an Ocean cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag value.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.user_data">
<code class="sig-name descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded MIME user data to make available to the instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.Ocean.whitelists">
<code class="sig-name descname">whitelists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance types allowed in the Ocean cluster.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.ecs.Ocean.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">associate_public_ip_address=None</em>, <em class="sig-param">autoscaler=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">draining_timeout=None</em>, <em class="sig-param">ebs_optimized=None</em>, <em class="sig-param">iam_instance_profile=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">key_pair=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">monitoring=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">subnet_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">update_policy=None</em>, <em class="sig-param">user_data=None</em>, <em class="sig-param">utilize_reserved_instances=None</em>, <em class="sig-param">whitelists=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Ocean resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>associate_public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Configure public IP address allocation.</p></li>
<li><p><strong>autoscaler</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the Ocean ECS autoscaler.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ocean cluster name.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of instances to launch and maintain in the cluster.</p></li>
<li><p><strong>draining_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance profile iam role.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the image used to launch the instances.</p></li>
<li><p><strong>key_pair</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key pair to attach the instances.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The upper limit of instances the cluster can scale up to.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The lower limit of instances the cluster can scale down to.</p></li>
<li><p><strong>monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ocean cluster name.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region the cluster will run in.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more security group ids.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds tags to instances launched in an Ocean cluster.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded MIME user data to make available to the instances.</p></li>
<li><p><strong>whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Instance types allowed in the Ocean cluster.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaler</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Cooldown period between scaling actions.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">down</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Auto Scaling scale down operations.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxScaleDownPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Would represent the maximum % to scale-down. Number between 1-100</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headroom</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Spare resource capacity management enabling fast assignment of tasks without waiting for new resources to launch.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cpuPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the number of CPUs to allocate the headroom. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memoryPerUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Optionally configure the amount of memory (MB) to allocate the headroom.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numOfUnits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of units to retain as headroom, where each unit has the defined headroom CPU and memory.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">isAutoConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Automatically configure and optimize headroom resources.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the Ocean ECS autoscaler.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Optionally set upper and lower bounds on the resource usage of the cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxMemoryGib</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum memory in GiB units that can be allocated to the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum cpu in vCPU units that can be allocated to the cluster.</p></li>
</ul>
</li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag value.</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rollConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_ecs.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_ecs.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.ecs.Ocean.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.ecs.Ocean.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.ecs.Ocean.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.ecs.</code><code class="sig-name descname">OceanLaunchSpec</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">iam_instance_profile=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ocean_id=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">user_data=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a custom Spotinst Ocean ECS Launch Spec resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds labels to instances launched in an Ocean cluster.</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN or name of an IAM instance profile to associate with launched instances.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the image used to launch the instances.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ocean Launch Specification name.</p></li>
<li><p><strong>ocean_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ocean cluster ID .</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more security group ids.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded MIME user data to make available to the instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The label key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The label value.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_ecs_launch_spec.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_ecs_launch_spec.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec.attributes">
<code class="sig-name descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Optionally adds labels to instances launched in an Ocean cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The label key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The label value.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec.iam_instance_profile">
<code class="sig-name descname">iam_instance_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec.iam_instance_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN or name of an IAM instance profile to associate with launched instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the image used to launch the instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ocean Launch Specification name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec.ocean_id">
<code class="sig-name descname">ocean_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec.ocean_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ocean cluster ID .</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more security group ids.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec.user_data">
<code class="sig-name descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded MIME user data to make available to the instances.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">attributes=None</em>, <em class="sig-param">iam_instance_profile=None</em>, <em class="sig-param">image_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">ocean_id=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">user_data=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OceanLaunchSpec resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optionally adds labels to instances launched in an Ocean cluster.</p></li>
<li><p><strong>iam_instance_profile</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN or name of an IAM instance profile to associate with launched instances.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the image used to launch the instances.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ocean Launch Specification name.</p></li>
<li><p><strong>ocean_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ocean cluster ID .</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more security group ids.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded MIME user data to make available to the instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The label key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The label value.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_ecs_launch_spec.html.markdown">https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_ecs_launch_spec.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.ecs.OceanLaunchSpec.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.ecs.OceanLaunchSpec.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
