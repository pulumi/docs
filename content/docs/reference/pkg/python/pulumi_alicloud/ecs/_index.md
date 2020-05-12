---
title: Module ecs
title_tag: Module ecs | Package pulumi_alicloud | Python SDK
linktitle: ecs
notitle: true
---

<div class="section" id="ecs">
<h1>ecs<a class="headerlink" href="#ecs" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.ecs"></span><dl class="py class">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AutoProvisioningGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_provisioning_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_provisioning_group_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_target_capacity_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">excess_capacity_termination_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_template_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_template_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_template_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_spot_price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_as_you_go_allocation_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_as_you_go_target_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_allocation_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_instance_interruption_behavior</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_instance_pools_to_use_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_target_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terminate_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terminate_instances_with_expiration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">total_target_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_from</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_until</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a ECS auto provisioning group resource which is a solution that uses preemptive instances and pay_as_you_go instances to rapidly deploy clusters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.79.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">name</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;auto_provisioning_group&quot;</span>
<span class="n">default_zones</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="n">available_disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_efficiency&quot;</span><span class="p">,</span>
    <span class="n">available_resource_creation</span><span class="o">=</span><span class="s2">&quot;VSwitch&quot;</span><span class="p">)</span>
<span class="n">default_network</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;defaultNetwork&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.16.0.0/16&quot;</span><span class="p">)</span>
<span class="n">default_switch</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Switch</span><span class="p">(</span><span class="s2">&quot;defaultSwitch&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="n">default_zones</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.16.0.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">default_network</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_security_group</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="s2">&quot;defaultSecurityGroup&quot;</span><span class="p">,</span> <span class="n">vpc_id</span><span class="o">=</span><span class="n">default_network</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_images</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_images</span><span class="p">(</span><span class="n">most_recent</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;^ubuntu_18.*64&quot;</span><span class="p">,</span>
    <span class="n">owners</span><span class="o">=</span><span class="s2">&quot;system&quot;</span><span class="p">)</span>
<span class="n">template</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">LaunchTemplate</span><span class="p">(</span><span class="s2">&quot;template&quot;</span><span class="p">,</span>
    <span class="n">image_id</span><span class="o">=</span><span class="n">default_images</span><span class="o">.</span><span class="n">images</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="s2">&quot;ecs.n1.tiny&quot;</span><span class="p">,</span>
    <span class="n">security_group_id</span><span class="o">=</span><span class="n">default_security_group</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_auto_provisioning_group</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">AutoProvisioningGroup</span><span class="p">(</span><span class="s2">&quot;defaultAutoProvisioningGroup&quot;</span><span class="p">,</span>
    <span class="n">launch_template_configs</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="s2">&quot;ecs.n1.small&quot;</span><span class="p">,</span>
        <span class="s2">&quot;vswitchId&quot;</span><span class="p">:</span> <span class="n">default_switch</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">launch_template_id</span><span class="o">=</span><span class="n">template</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">pay_as_you_go_target_capacity</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="n">spot_target_capacity</span><span class="o">=</span><span class="s2">&quot;2&quot;</span><span class="p">,</span>
    <span class="n">total_target_capacity</span><span class="o">=</span><span class="s2">&quot;4&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The config mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> - (Optional) The instance type of the Nth extended configurations of the launch template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_price</span></code> - (Required) The maximum price of the instance type specified in the Nth extended configurations of the launch template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> - (Required) The ID of the VSwitch in the Nth extended configurations of the launch template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weighted_capacity</span></code> - (Optional) The weight of the instance type specified in the Nth extended configurations of the launch template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> - (Optional) The priority of the instance type specified in the Nth extended configurations of the launch template. A value of 0 indicates the highest priority.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_target_capacity_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of supplemental instances. When the total value of <cite>PayAsYouGoTargetCapacity</cite> and <cite>SpotTargetCapacity</cite> is smaller than the value of TotalTargetCapacity, the auto provisioning group will create instances of the specified type to meet the capacity requirements. Valid values:<cite>PayAsYouGo</cite>: Pay-as-you-go instances; <cite>Spot</cite>: Preemptible instances, Default value: <code class="docutils literal notranslate"><span class="pre">Spot</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the auto provisioning group.</p></li>
<li><p><strong>excess_capacity_termination_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shutdown policy for excess preemptible instances followed when the capacity of the auto provisioning group exceeds the target capacity. Valid values: <code class="docutils literal notranslate"><span class="pre">no-termination</span></code> and <code class="docutils literal notranslate"><span class="pre">termination</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">no-termination</span></code>.</p></li>
<li><p><strong>launch_template_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – DataDisk mappings to attach to ecs instance. See Block config below for details.</p></li>
<li><p><strong>launch_template_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance launch template associated with the auto provisioning group.</p></li>
<li><p><strong>launch_template_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the instance launch template associated with the auto provisioning group.</p></li>
<li><p><strong>max_spot_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The global maximum price for preemptible instances in the auto provisioning group. If both the <code class="docutils literal notranslate"><span class="pre">MaxSpotPrice</span></code> and <code class="docutils literal notranslate"><span class="pre">LaunchTemplateConfig.N.MaxPrice</span></code> parameters are specified, the maximum price is the lower value of the two.</p></li>
<li><p><strong>pay_as_you_go_allocation_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scale-out policy for pay-as-you-go instances. Valid values: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code> and <code class="docutils literal notranslate"><span class="pre">prioritized</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>.</p></li>
<li><p><strong>pay_as_you_go_target_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target capacity of pay-as-you-go instances in the auto provisioning group.</p></li>
<li><p><strong>spot_allocation_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scale-out policy for preemptible instances. Valid values:<cite>lowest-price</cite> and <code class="docutils literal notranslate"><span class="pre">diversified</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>.</p></li>
<li><p><strong>spot_instance_interruption_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default behavior after preemptible instances are shut down. Value values: <code class="docutils literal notranslate"><span class="pre">stop</span></code> and <code class="docutils literal notranslate"><span class="pre">terminate</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">stop</span></code>.</p></li>
<li><p><strong>spot_instance_pools_to_use_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This parameter takes effect when the <code class="docutils literal notranslate"><span class="pre">SpotAllocationStrategy</span></code> parameter is set to <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>. The auto provisioning group selects instance types of the lowest cost to create instances.</p></li>
<li><p><strong>spot_target_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target capacity of preemptible instances in the auto provisioning group.</p></li>
<li><p><strong>terminate_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to release instances of the auto provisioning group. Valid values:<cite>false</cite> and <code class="docutils literal notranslate"><span class="pre">true</span></code>, default value: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>terminate_instances_with_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The shutdown policy for preemptible instances when the auto provisioning group expires. Valid values: <code class="docutils literal notranslate"><span class="pre">false</span></code> and <code class="docutils literal notranslate"><span class="pre">true</span></code>, default value: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>total_target_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The total target capacity of the auto provisioning group. The target capacity consists of the following three parts:PayAsYouGoTargetCapacity,SpotTargetCapacity and the supplemental capacity besides PayAsYouGoTargetCapacity and SpotTargetCapacity.</p></li>
<li><p><strong>valid_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the auto provisioning group is started. The period of time between this point in time and the point in time specified by the <code class="docutils literal notranslate"><span class="pre">valid_until</span></code> parameter is the effective time period of the auto provisioning group.By default, an auto provisioning group is immediately started after creation.</p></li>
<li><p><strong>valid_until</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the auto provisioning group expires. The period of time between this point in time and the point in time specified by the <code class="docutils literal notranslate"><span class="pre">valid_from</span></code> parameter is the effective time period of the auto provisioning group.By default, an auto provisioning group never expires.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>launch_template_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPrice</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.default_target_capacity_type">
<code class="sig-name descname">default_target_capacity_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.default_target_capacity_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of supplemental instances. When the total value of <code class="docutils literal notranslate"><span class="pre">PayAsYouGoTargetCapacity</span></code> and <code class="docutils literal notranslate"><span class="pre">SpotTargetCapacity</span></code> is smaller than the value of TotalTargetCapacity, the auto provisioning group will create instances of the specified type to meet the capacity requirements. Valid values:<cite>PayAsYouGo</cite>: Pay-as-you-go instances; <cite>Spot</cite>: Preemptible instances, Default value: <code class="docutils literal notranslate"><span class="pre">Spot</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the auto provisioning group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.excess_capacity_termination_policy">
<code class="sig-name descname">excess_capacity_termination_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.excess_capacity_termination_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The shutdown policy for excess preemptible instances followed when the capacity of the auto provisioning group exceeds the target capacity. Valid values: <code class="docutils literal notranslate"><span class="pre">no-termination</span></code> and <code class="docutils literal notranslate"><span class="pre">termination</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">no-termination</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.launch_template_configs">
<code class="sig-name descname">launch_template_configs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.launch_template_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>DataDisk mappings to attach to ecs instance. See Block config below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPrice</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.launch_template_id">
<code class="sig-name descname">launch_template_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.launch_template_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the instance launch template associated with the auto provisioning group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.launch_template_version">
<code class="sig-name descname">launch_template_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.launch_template_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the instance launch template associated with the auto provisioning group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.max_spot_price">
<code class="sig-name descname">max_spot_price</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.max_spot_price" title="Permalink to this definition">¶</a></dt>
<dd><p>The global maximum price for preemptible instances in the auto provisioning group. If both the <code class="docutils literal notranslate"><span class="pre">MaxSpotPrice</span></code> and <code class="docutils literal notranslate"><span class="pre">LaunchTemplateConfig.N.MaxPrice</span></code> parameters are specified, the maximum price is the lower value of the two.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.pay_as_you_go_allocation_strategy">
<code class="sig-name descname">pay_as_you_go_allocation_strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.pay_as_you_go_allocation_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>The scale-out policy for pay-as-you-go instances. Valid values: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code> and <code class="docutils literal notranslate"><span class="pre">prioritized</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.pay_as_you_go_target_capacity">
<code class="sig-name descname">pay_as_you_go_target_capacity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.pay_as_you_go_target_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The target capacity of pay-as-you-go instances in the auto provisioning group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.spot_allocation_strategy">
<code class="sig-name descname">spot_allocation_strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.spot_allocation_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>The scale-out policy for preemptible instances. Valid values:<code class="docutils literal notranslate"><span class="pre">lowest-price</span></code> and <code class="docutils literal notranslate"><span class="pre">diversified</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.spot_instance_interruption_behavior">
<code class="sig-name descname">spot_instance_interruption_behavior</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.spot_instance_interruption_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The default behavior after preemptible instances are shut down. Value values: <code class="docutils literal notranslate"><span class="pre">stop</span></code> and <code class="docutils literal notranslate"><span class="pre">terminate</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">stop</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.spot_instance_pools_to_use_count">
<code class="sig-name descname">spot_instance_pools_to_use_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.spot_instance_pools_to_use_count" title="Permalink to this definition">¶</a></dt>
<dd><p>This parameter takes effect when the <code class="docutils literal notranslate"><span class="pre">SpotAllocationStrategy</span></code> parameter is set to <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>. The auto provisioning group selects instance types of the lowest cost to create instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.spot_target_capacity">
<code class="sig-name descname">spot_target_capacity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.spot_target_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The target capacity of preemptible instances in the auto provisioning group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.terminate_instances">
<code class="sig-name descname">terminate_instances</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.terminate_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to release instances of the auto provisioning group. Valid values:<code class="docutils literal notranslate"><span class="pre">false</span></code> and <code class="docutils literal notranslate"><span class="pre">true</span></code>, default value: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.terminate_instances_with_expiration">
<code class="sig-name descname">terminate_instances_with_expiration</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.terminate_instances_with_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>The shutdown policy for preemptible instances when the auto provisioning group expires. Valid values: <code class="docutils literal notranslate"><span class="pre">false</span></code> and <code class="docutils literal notranslate"><span class="pre">true</span></code>, default value: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.total_target_capacity">
<code class="sig-name descname">total_target_capacity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.total_target_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The total target capacity of the auto provisioning group. The target capacity consists of the following three parts:PayAsYouGoTargetCapacity,SpotTargetCapacity and the supplemental capacity besides PayAsYouGoTargetCapacity and SpotTargetCapacity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.valid_from">
<code class="sig-name descname">valid_from</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.valid_from" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the auto provisioning group is started. The period of time between this point in time and the point in time specified by the <code class="docutils literal notranslate"><span class="pre">valid_until</span></code> parameter is the effective time period of the auto provisioning group.By default, an auto provisioning group is immediately started after creation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.valid_until">
<code class="sig-name descname">valid_until</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.valid_until" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the auto provisioning group expires. The period of time between this point in time and the point in time specified by the <code class="docutils literal notranslate"><span class="pre">valid_from</span></code> parameter is the effective time period of the auto provisioning group.By default, an auto provisioning group never expires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_provisioning_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_provisioning_group_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_target_capacity_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">excess_capacity_termination_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_template_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_template_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_template_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_spot_price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_as_you_go_allocation_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_as_you_go_target_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_allocation_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_instance_interruption_behavior</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_instance_pools_to_use_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_target_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terminate_instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terminate_instances_with_expiration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">total_target_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_from</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_until</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AutoProvisioningGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_target_capacity_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of supplemental instances. When the total value of <cite>PayAsYouGoTargetCapacity</cite> and <cite>SpotTargetCapacity</cite> is smaller than the value of TotalTargetCapacity, the auto provisioning group will create instances of the specified type to meet the capacity requirements. Valid values:<cite>PayAsYouGo</cite>: Pay-as-you-go instances; <cite>Spot</cite>: Preemptible instances, Default value: <code class="docutils literal notranslate"><span class="pre">Spot</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the auto provisioning group.</p></li>
<li><p><strong>excess_capacity_termination_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shutdown policy for excess preemptible instances followed when the capacity of the auto provisioning group exceeds the target capacity. Valid values: <code class="docutils literal notranslate"><span class="pre">no-termination</span></code> and <code class="docutils literal notranslate"><span class="pre">termination</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">no-termination</span></code>.</p></li>
<li><p><strong>launch_template_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – DataDisk mappings to attach to ecs instance. See Block config below for details.</p></li>
<li><p><strong>launch_template_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the instance launch template associated with the auto provisioning group.</p></li>
<li><p><strong>launch_template_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the instance launch template associated with the auto provisioning group.</p></li>
<li><p><strong>max_spot_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The global maximum price for preemptible instances in the auto provisioning group. If both the <code class="docutils literal notranslate"><span class="pre">MaxSpotPrice</span></code> and <code class="docutils literal notranslate"><span class="pre">LaunchTemplateConfig.N.MaxPrice</span></code> parameters are specified, the maximum price is the lower value of the two.</p></li>
<li><p><strong>pay_as_you_go_allocation_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scale-out policy for pay-as-you-go instances. Valid values: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code> and <code class="docutils literal notranslate"><span class="pre">prioritized</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>.</p></li>
<li><p><strong>pay_as_you_go_target_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target capacity of pay-as-you-go instances in the auto provisioning group.</p></li>
<li><p><strong>spot_allocation_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scale-out policy for preemptible instances. Valid values:<cite>lowest-price</cite> and <code class="docutils literal notranslate"><span class="pre">diversified</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>.</p></li>
<li><p><strong>spot_instance_interruption_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default behavior after preemptible instances are shut down. Value values: <code class="docutils literal notranslate"><span class="pre">stop</span></code> and <code class="docutils literal notranslate"><span class="pre">terminate</span></code>,Default value: <code class="docutils literal notranslate"><span class="pre">stop</span></code>.</p></li>
<li><p><strong>spot_instance_pools_to_use_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This parameter takes effect when the <code class="docutils literal notranslate"><span class="pre">SpotAllocationStrategy</span></code> parameter is set to <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>. The auto provisioning group selects instance types of the lowest cost to create instances.</p></li>
<li><p><strong>spot_target_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target capacity of preemptible instances in the auto provisioning group.</p></li>
<li><p><strong>terminate_instances</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to release instances of the auto provisioning group. Valid values:<cite>false</cite> and <code class="docutils literal notranslate"><span class="pre">true</span></code>, default value: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>terminate_instances_with_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The shutdown policy for preemptible instances when the auto provisioning group expires. Valid values: <code class="docutils literal notranslate"><span class="pre">false</span></code> and <code class="docutils literal notranslate"><span class="pre">true</span></code>, default value: <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>total_target_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The total target capacity of the auto provisioning group. The target capacity consists of the following three parts:PayAsYouGoTargetCapacity,SpotTargetCapacity and the supplemental capacity besides PayAsYouGoTargetCapacity and SpotTargetCapacity.</p></li>
<li><p><strong>valid_from</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the auto provisioning group is started. The period of time between this point in time and the point in time specified by the <code class="docutils literal notranslate"><span class="pre">valid_until</span></code> parameter is the effective time period of the auto provisioning group.By default, an auto provisioning group is immediately started after creation.</p></li>
<li><p><strong>valid_until</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the auto provisioning group expires. The period of time between this point in time and the point in time specified by the <code class="docutils literal notranslate"><span class="pre">valid_from</span></code> parameter is the effective time period of the auto provisioning group.By default, an auto provisioning group never expires.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>launch_template_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPrice</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.AutoProvisioningGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AutoProvisioningGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.AwaitableGetDisksResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetDisksResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetDisksResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.AwaitableGetEipsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetEipsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">eips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">in_use</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetEipsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.AwaitableGetImagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetImagesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">most_recent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetImagesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.AwaitableGetInstanceTypeFamiliesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetInstanceTypeFamiliesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">families</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">generation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetInstanceTypeFamiliesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.AwaitableGetInstanceTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetInstanceTypesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_core_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eni_amount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpu_amount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpu_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_node_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorted_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetInstanceTypesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.AwaitableGetKeyPairsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetKeyPairsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">finger_print</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_pairs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetKeyPairsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.AwaitableGetNetworkInterfacesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetNetworkInterfacesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetNetworkInterfacesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.AwaitableGetSecurityGroupRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetSecurityGroupRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">direction</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_desc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nic_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetSecurityGroupRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.AwaitableGetSecurityGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetSecurityGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetSecurityGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.AwaitableGetSnapshotsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">AwaitableGetSnapshotsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">disk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshots</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_disk_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.AwaitableGetSnapshotsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.CopyImage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">CopyImage</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.CopyImage" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a CopyImage resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_alicloud.ecs.CopyImage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.CopyImage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CopyImage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.CopyImage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.CopyImage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.CopyImage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.CopyImage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.Disk">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">Disk</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_auto_snapshot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_with_instance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_auto_snapshot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Disk" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Disk resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] availability_zone: The Zone to create the disk in.
:param pulumi.Input[str] category: Category of the disk. Valid values are <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.
:param pulumi.Input[bool] delete_auto_snapshot: Indicates whether the automatic snapshot is deleted when the disk is released. Default value: false.
:param pulumi.Input[bool] delete_with_instance: Indicates whether the disk is released together with the instance: Default value: false.
:param pulumi.Input[str] description: Description of the disk. This description can have a string of 2 to 256 characters, It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.
:param pulumi.Input[bool] enable_auto_snapshot: Indicates whether to apply a created automatic snapshot policy to the disk. Default value: false.
:param pulumi.Input[bool] encrypted: If true, the disk will be encrypted, conflict with <code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code>.
:param pulumi.Input[str] name: Name of the ECS disk. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”_”, and must not begin or end with a hyphen, and must not begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.
:param pulumi.Input[str] resource_group_id: The Id of resource group which the disk belongs.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>&gt; **NOTE:** Disk category `cloud` has been outdated and it only can be used none I/O Optimized ECS instances. Recommend `cloud_efficiency` and `cloud_ssd` disk.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the disk in GiBs. When resize the disk, the new size must be greater than the former value, or you would get an error <code class="docutils literal notranslate"><span class="pre">InvalidDiskSize.TooSmall</span></code>.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A snapshot to base the disk off of. If the disk size required by snapshot is greater than <code class="docutils literal notranslate"><span class="pre">size</span></code>, the <code class="docutils literal notranslate"><span class="pre">size</span></code> will be ignored, conflict with <code class="docutils literal notranslate"><span class="pre">encrypted</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to create the disk in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.category">
<code class="sig-name descname">category</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.category" title="Permalink to this definition">¶</a></dt>
<dd><p>Category of the disk. Valid values are <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.delete_auto_snapshot">
<code class="sig-name descname">delete_auto_snapshot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.delete_auto_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the automatic snapshot is deleted when the disk is released. Default value: false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.delete_with_instance">
<code class="sig-name descname">delete_with_instance</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.delete_with_instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the disk is released together with the instance: Default value: false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the disk. This description can have a string of 2 to 256 characters, It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.enable_auto_snapshot">
<code class="sig-name descname">enable_auto_snapshot</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.enable_auto_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether to apply a created automatic snapshot policy to the disk. Default value: false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.encrypted">
<code class="sig-name descname">encrypted</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the disk will be encrypted, conflict with <code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the ECS disk. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”_”, and must not begin or end with a hyphen, and must not begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the disk belongs.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Disk category <code class="docutils literal notranslate"><span class="pre">cloud</span></code> has been outdated and it only can be used none I/O Optimized ECS instances. Recommend <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> disk.</p>
</div></blockquote>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.size">
<code class="sig-name descname">size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the disk in GiBs. When resize the disk, the new size must be greater than the former value, or you would get an error <code class="docutils literal notranslate"><span class="pre">InvalidDiskSize.TooSmall</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A snapshot to base the disk off of. If the disk size required by snapshot is greater than <code class="docutils literal notranslate"><span class="pre">size</span></code>, the <code class="docutils literal notranslate"><span class="pre">size</span></code> will be ignored, conflict with <code class="docutils literal notranslate"><span class="pre">encrypted</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The disk status.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Disk.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.Disk.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_auto_snapshot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_with_instance</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_auto_snapshot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Disk resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to create the disk in.</p></li>
<li><p><strong>category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Category of the disk. Valid values are <code class="docutils literal notranslate"><span class="pre">cloud</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>delete_auto_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the automatic snapshot is deleted when the disk is released. Default value: false.</p></li>
<li><p><strong>delete_with_instance</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the disk is released together with the instance: Default value: false.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the disk. This description can have a string of 2 to 256 characters, It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p></li>
<li><p><strong>enable_auto_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to apply a created automatic snapshot policy to the disk. Default value: false.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the disk will be encrypted, conflict with <code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the ECS disk. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”_”, and must not begin or end with a hyphen, and must not begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the disk belongs.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>&gt; **NOTE:** Disk category `cloud` has been outdated and it only can be used none I/O Optimized ECS instances. Recommend `cloud_efficiency` and `cloud_ssd` disk.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the disk in GiBs. When resize the disk, the new size must be greater than the former value, or you would get an error <code class="docutils literal notranslate"><span class="pre">InvalidDiskSize.TooSmall</span></code>.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A snapshot to base the disk off of. If the disk size required by snapshot is greater than <code class="docutils literal notranslate"><span class="pre">size</span></code>, the <code class="docutils literal notranslate"><span class="pre">size</span></code> will be ignored, conflict with <code class="docutils literal notranslate"><span class="pre">encrypted</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The disk status.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.Disk.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.Disk.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Disk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.DiskAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">DiskAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.DiskAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a DiskAttachment resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] device_name: The device name has been deprecated, and when attaching disk, it will be allocated automatically by system according to default order from /dev/xvdb to /dev/xvdz.
:param pulumi.Input[str] disk_id: ID of the Disk to be attached.
:param pulumi.Input[str] instance_id: ID of the Instance to attach to.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.DiskAttachment.device_name">
<code class="sig-name descname">device_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.DiskAttachment.device_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The device name has been deprecated, and when attaching disk, it will be allocated automatically by system according to default order from /dev/xvdb to /dev/xvdz.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.DiskAttachment.disk_id">
<code class="sig-name descname">disk_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.DiskAttachment.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Disk to be attached.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.DiskAttachment.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.DiskAttachment.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Instance to attach to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.DiskAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.DiskAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DiskAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device name has been deprecated, and when attaching disk, it will be allocated automatically by system according to default order from /dev/xvdb to /dev/xvdz.</p></li>
<li><p><strong>disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Disk to be attached.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Instance to attach to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.DiskAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.DiskAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.DiskAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.DiskAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.Eip">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">Eip</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">isp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Eip" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Eip resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] bandwidth: Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). If this value is not specified, then automatically sets it to 5 Mbps.
:param pulumi.Input[str] description: Description of the EIP instance, This description can have a string of 2 to 256 characters, It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.
:param pulumi.Input[str] instance_charge_type: Elastic IP instance charge type. Valid values are “PrePaid” and “PostPaid”. Default to “PostPaid”.
:param pulumi.Input[str] internet_charge_type: Internet charge type of the EIP, Valid values are <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>, <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>. From version <code class="docutils literal notranslate"><span class="pre">1.7.1</span></code>, default to <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. It is only PayByBandwidth when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is PrePaid.
:param pulumi.Input[str] isp: The line type of the Elastic IP instance. Default to <code class="docutils literal notranslate"><span class="pre">BGP</span></code>. Other type of the isp need to open a whitelist.
:param pulumi.Input[str] name: The name of the EIP instance. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”_”, and must not begin or end with a hyphen, and must not begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.
:param pulumi.Input[float] period: The duration that you will buy the resource, in month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>.</p>
<blockquote>
<div><p>Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify “period” and you can do that via web console.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the eip belongs.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.bandwidth">
<code class="sig-name descname">bandwidth</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). If this value is not specified, then automatically sets it to 5 Mbps.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the EIP instance, This description can have a string of 2 to 256 characters, It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic IP instance charge type. Valid values are “PrePaid” and “PostPaid”. Default to “PostPaid”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.internet_charge_type">
<code class="sig-name descname">internet_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.internet_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Internet charge type of the EIP, Valid values are <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>, <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>. From version <code class="docutils literal notranslate"><span class="pre">1.7.1</span></code>, default to <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. It is only PayByBandwidth when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is PrePaid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.ip_address">
<code class="sig-name descname">ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The elastic ip address</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.isp">
<code class="sig-name descname">isp</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.isp" title="Permalink to this definition">¶</a></dt>
<dd><p>The line type of the Elastic IP instance. Default to <code class="docutils literal notranslate"><span class="pre">BGP</span></code>. Other type of the isp need to open a whitelist.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the EIP instance. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”_”, and must not begin or end with a hyphen, and must not begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy the resource, in month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>.
Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify “period” and you can do that via web console.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the eip belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The EIP current status.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Eip.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.Eip.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">isp</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Eip resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). If this value is not specified, then automatically sets it to 5 Mbps.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the EIP instance, This description can have a string of 2 to 256 characters, It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elastic IP instance charge type. Valid values are “PrePaid” and “PostPaid”. Default to “PostPaid”.</p></li>
<li><p><strong>internet_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet charge type of the EIP, Valid values are <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>, <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>. From version <code class="docutils literal notranslate"><span class="pre">1.7.1</span></code>, default to <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. It is only PayByBandwidth when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is PrePaid.</p></li>
<li><p><strong>ip*address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The elastic ip address</p>
</p></li>
<li><p><strong>isp</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The line type of the Elastic IP instance. Default to <code class="docutils literal notranslate"><span class="pre">BGP</span></code>. Other type of the isp need to open a whitelist.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the EIP instance. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as “-“,”.”,”<a href="#id3"><span class="problematic" id="id4">*</span></a>”, and must not begin or end with a hyphen, and must not begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy the resource, in month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>.
Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify “period” and you can do that via web console.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the eip belongs.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EIP current status.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.Eip.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.Eip.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Eip.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.EipAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">EipAssociation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allocation_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.EipAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a EipAssociation resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] allocation_id: The allocation EIP ID.
:param pulumi.Input[str] instance_id: The ID of the ECS or SLB instance or Nat Gateway.
:param pulumi.Input[str] instance_type: The type of cloud product that the eip instance to bind.
:param pulumi.Input[str] private_ip_address: The private IP address in the network segment of the vswitch which has been assigned.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.EipAssociation.allocation_id">
<code class="sig-name descname">allocation_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.EipAssociation.allocation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The allocation EIP ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.EipAssociation.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.EipAssociation.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the ECS or SLB instance or Nat Gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.EipAssociation.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.EipAssociation.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of cloud product that the eip instance to bind.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.EipAssociation.private_ip_address">
<code class="sig-name descname">private_ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.EipAssociation.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP address in the network segment of the vswitch which has been assigned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.EipAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allocation_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip_address</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.EipAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EipAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The allocation EIP ID.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the ECS or SLB instance or Nat Gateway.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of cloud product that the eip instance to bind.</p></li>
<li><p><strong>private_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private IP address in the network segment of the vswitch which has been assigned.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.EipAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.EipAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.EipAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.EipAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.GetDisksResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetDisksResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetDisksResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDisks.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetDisksResult.category">
<code class="sig-name descname">category</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetDisksResult.category" title="Permalink to this definition">¶</a></dt>
<dd><p>Disk category. Possible values: <code class="docutils literal notranslate"><span class="pre">cloud</span></code> (basic cloud disk), <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code> (ultra cloud disk), <code class="docutils literal notranslate"><span class="pre">ephemeral_ssd</span></code> (local SSD cloud disk), <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> (SSD cloud disk), and <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code> (ESSD cloud disk).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetDisksResult.disks">
<code class="sig-name descname">disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetDisksResult.disks" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of disks. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetDisksResult.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetDisksResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicate whether the disk is encrypted or not. Possible values: <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetDisksResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetDisksResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetDisksResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetDisksResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the related instance. It is <code class="docutils literal notranslate"><span class="pre">null</span></code> unless the <code class="docutils literal notranslate"><span class="pre">status</span></code> is <code class="docutils literal notranslate"><span class="pre">In_use</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetDisksResult.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetDisksResult.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetDisksResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetDisksResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the disk.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetDisksResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetDisksResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Disk type. Possible values: <code class="docutils literal notranslate"><span class="pre">system</span></code> and <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.GetEipsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetEipsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">eips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">in_use</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetEipsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEips.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetEipsResult.eips">
<code class="sig-name descname">eips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetEipsResult.eips" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of EIPs. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetEipsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetEipsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetEipsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetEipsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) A list of EIP IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetEipsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetEipsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) A list of EIP names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetEipsResult.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetEipsResult.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the eips belongs.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.GetImagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetImagesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">most_recent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetImagesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImages.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetImagesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetImagesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetImagesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetImagesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of image IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetImagesResult.images">
<code class="sig-name descname">images</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetImagesResult.images" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of images. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.GetInstanceTypeFamiliesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetInstanceTypeFamiliesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">families</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">generation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypeFamiliesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceTypeFamilies.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstanceTypeFamiliesResult.generation">
<code class="sig-name descname">generation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypeFamiliesResult.generation" title="Permalink to this definition">¶</a></dt>
<dd><p>The generation of the instance type family.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstanceTypeFamiliesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypeFamiliesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstanceTypeFamiliesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypeFamiliesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance type family IDs.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.GetInstanceTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetInstanceTypesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_core_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eni_amount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpu_amount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpu_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_node_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorted_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceTypes.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstanceTypesResult.cpu_core_count">
<code class="sig-name descname">cpu_core_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypesResult.cpu_core_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of CPU cores.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstanceTypesResult.eni_amount">
<code class="sig-name descname">eni_amount</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypesResult.eni_amount" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of network interfaces that an instance type can be attached to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstanceTypesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstanceTypesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance type IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstanceTypesResult.instance_types">
<code class="sig-name descname">instance_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypesResult.instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of image types. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstanceTypesResult.memory_size">
<code class="sig-name descname">memory_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstanceTypesResult.memory_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of memory, measured in GB.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Availability zone the instance belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ECS instance IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.image_id">
<code class="sig-name descname">image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Image ID the instance is using.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instances. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instances names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.ram_role_name">
<code class="sig-name descname">ram_role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.ram_role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ram role name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance current status.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the ECS instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VPC the instance belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetInstancesResult.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetInstancesResult.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VSwitch the instance belongs to.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.GetKeyPairsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetKeyPairsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">finger_print</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_pairs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetKeyPairsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKeyPairs.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetKeyPairsResult.finger_print">
<code class="sig-name descname">finger_print</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetKeyPairsResult.finger_print" title="Permalink to this definition">¶</a></dt>
<dd><p>Finger print of the key pair.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetKeyPairsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetKeyPairsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetKeyPairsResult.key_pairs">
<code class="sig-name descname">key_pairs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetKeyPairsResult.key_pairs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of key pairs. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetKeyPairsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetKeyPairsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of key pair names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetKeyPairsResult.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetKeyPairsResult.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetKeyPairsResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetKeyPairsResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional, Available in v1.66.0+) A mapping of tags to assign to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.GetNetworkInterfacesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetNetworkInterfacesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetNetworkInterfacesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkInterfaces.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetNetworkInterfacesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetNetworkInterfacesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetNetworkInterfacesResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetNetworkInterfacesResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the instance that the ENI is attached to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetNetworkInterfacesResult.interfaces">
<code class="sig-name descname">interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetNetworkInterfacesResult.interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of ENIs. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetNetworkInterfacesResult.private_ip">
<code class="sig-name descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetNetworkInterfacesResult.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Primary private IP of the ENI.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetNetworkInterfacesResult.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetNetworkInterfacesResult.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetNetworkInterfacesResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetNetworkInterfacesResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the ENI.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetNetworkInterfacesResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetNetworkInterfacesResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VPC that the ENI belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetNetworkInterfacesResult.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetNetworkInterfacesResult.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VSwitch that the ENI is linked to.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetSecurityGroupRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">direction</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_desc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nic_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecurityGroupRules.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupRulesResult.direction">
<code class="sig-name descname">direction</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupRulesResult.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>Authorization direction, <code class="docutils literal notranslate"><span class="pre">ingress</span></code> or <code class="docutils literal notranslate"><span class="pre">egress</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupRulesResult.group_desc">
<code class="sig-name descname">group_desc</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupRulesResult.group_desc" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the security group that owns the rules.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupRulesResult.group_name">
<code class="sig-name descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupRulesResult.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the security group that owns the rules.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupRulesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupRulesResult.ip_protocol">
<code class="sig-name descname">ip_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupRulesResult.ip_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol. Can be <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>, <code class="docutils literal notranslate"><span class="pre">icmp</span></code>, <code class="docutils literal notranslate"><span class="pre">gre</span></code> or <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupRulesResult.nic_type">
<code class="sig-name descname">nic_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupRulesResult.nic_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Network type, <code class="docutils literal notranslate"><span class="pre">internet</span></code> or <code class="docutils literal notranslate"><span class="pre">intranet</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupRulesResult.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupRulesResult.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Authorization policy. Can be either <code class="docutils literal notranslate"><span class="pre">accept</span></code> or <code class="docutils literal notranslate"><span class="pre">drop</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupRulesResult.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupRulesResult.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group rules. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetSecurityGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecurityGroups.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Security Groups. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Security Group IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Security Group names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupsResult.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupsResult.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the security_group belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupsResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupsResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the ECS instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSecurityGroupsResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSecurityGroupsResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC that owns the security group.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.GetSnapshotsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">GetSnapshotsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">disk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshots</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_disk_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.GetSnapshotsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshots.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSnapshotsResult.encrypted">
<code class="sig-name descname">encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSnapshotsResult.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the snapshot is encrypted or not.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSnapshotsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSnapshotsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSnapshotsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSnapshotsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of snapshot IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSnapshotsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSnapshotsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of snapshots names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSnapshotsResult.snapshots">
<code class="sig-name descname">snapshots</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSnapshotsResult.snapshots" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of snapshots. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSnapshotsResult.source_disk_type">
<code class="sig-name descname">source_disk_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSnapshotsResult.source_disk_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Source disk attribute. Value range:</p>
<ul class="simple">
<li><p>System</p></li>
<li><p>Data</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSnapshotsResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSnapshotsResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot status. Value range:</p>
<ul class="simple">
<li><p>progressing</p></li>
<li><p>accomplished</p></li>
<li><p>failed</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSnapshotsResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSnapshotsResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.GetSnapshotsResult.usage">
<code class="sig-name descname">usage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.GetSnapshotsResult.usage" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the snapshots are used to create resources or not. Value range:</p>
<ul class="simple">
<li><p>image</p></li>
<li><p>disk</p></li>
<li><p>image_disk</p></li>
<li><p>none</p></li>
</ul>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ecs.Image">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">Image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">architecture</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_device_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a custom image. You can then use a custom image to create ECS instances (RunInstances) or change the system disk for an existing instance (ReplaceSystemDisk).</p>
<blockquote>
<div><p><strong>NOTE:</strong>  If you want to create a template from an ECS instance, you can specify the instance ID (InstanceId) to create a custom image. You must make sure that the status of the specified instance is Running or Stopped. After a successful invocation, each disk of the specified instance has a new snapshot created.</p>
<p><strong>NOTE:</strong>  If you want to create a custom image based on the system disk of your ECS instance, you can specify one of the system disk snapshots (SnapshotId) to create a custom image. However, the specified snapshot cannot be created on or before July 15, 2013.</p>
<p><strong>NOTE:</strong>  If you want to combine snapshots of multiple disks into an image template, you can specify DiskDeviceMapping to create a custom image.</p>
<p><strong>NOTE:</strong>  Available in 1.64.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">Image</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">architecture</span><span class="o">=</span><span class="s2">&quot;x86_64&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;test-image&quot;</span><span class="p">,</span>
    <span class="n">image_name</span><span class="o">=</span><span class="s2">&quot;test-image&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="s2">&quot;i-bp1g6zv0ce8oghu7k***&quot;</span><span class="p">,</span>
    <span class="n">platform</span><span class="o">=</span><span class="s2">&quot;CentOS&quot;</span><span class="p">,</span>
    <span class="n">resource_group_id</span><span class="o">=</span><span class="s2">&quot;rg-bp67acfmxazb4ph***&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;FinanceDept&quot;</span><span class="p">:</span> <span class="s2">&quot;FinanceDeptJoshua&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>architecture</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the architecture of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">i386</span></code> , Default is <code class="docutils literal notranslate"><span class="pre">x86_64</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the image. It must be 2 to 256 characters in length and must not start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value: null.</p></li>
<li><p><strong>disk_device_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Description of the system with disks and snapshots under the image.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to force delete the custom image, Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
- false：Verifies that the image is not currently in use by any other instances before deleting the image.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>image*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a> is not allowed). It can contain digits, colons (:), underscores (<a href="#id7"><span class="problematic" id="id8">*</span></a>), or hyphens (-). Default value: null.</p>
</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance ID.</p></li>
<li><p><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the operating system platform of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">CentOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Ubuntu</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">OpenSUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">RedHat</span></code>, <code class="docutils literal notranslate"><span class="pre">Debian</span></code>, <code class="docutils literal notranslate"><span class="pre">CoreOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Aliyun</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2003</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2008</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2012</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">7</span></code>, Default is <code class="docutils literal notranslate"><span class="pre">Others</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Customized</span> <span class="pre">Linux</span></code>.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the enterprise resource group to which a custom image belongs</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a snapshot that is used to create a combined custom image.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The tag value of an image. The value of N ranges from 1 to 20.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>disk_device_mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of a disk in the combined custom image. Value range: /dev/xvda to /dev/xvdz.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of a disk in the combined custom image. If you specify this parameter, you can use a data disk snapshot as the data source of a system disk for creating an image. If it is not specified, the disk type is determined by the corresponding snapshot. Valid values: <code class="docutils literal notranslate"><span class="pre">system</span></code>, <code class="docutils literal notranslate"><span class="pre">data</span></code>,</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of a disk in the combined custom image, in GiB. Value range: 5 to 2000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a snapshot that is used to create a combined custom image.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Image.architecture">
<code class="sig-name descname">architecture</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Image.architecture" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the architecture of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">i386</span></code> , Default is <code class="docutils literal notranslate"><span class="pre">x86_64</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Image.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Image.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the image. It must be 2 to 256 characters in length and must not start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value: null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Image.disk_device_mappings">
<code class="sig-name descname">disk_device_mappings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Image.disk_device_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the system with disks and snapshots under the image.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of a disk in the combined custom image. Value range: /dev/xvda to /dev/xvdz.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the type of a disk in the combined custom image. If you specify this parameter, you can use a data disk snapshot as the data source of a system disk for creating an image. If it is not specified, the disk type is determined by the corresponding snapshot. Valid values: <code class="docutils literal notranslate"><span class="pre">system</span></code>, <code class="docutils literal notranslate"><span class="pre">data</span></code>,</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the size of a disk in the combined custom image, in GiB. Value range: 5 to 2000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies a snapshot that is used to create a combined custom image.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Image.force">
<code class="sig-name descname">force</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Image.force" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether to force delete the custom image, Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
<ul class="simple">
<li><p>true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.</p></li>
<li><p>false：Verifies that the image is not currently in use by any other instances before deleting the image.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Image.image_name">
<code class="sig-name descname">image_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Image.image_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a> is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Image.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Image.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Image.platform">
<code class="sig-name descname">platform</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Image.platform" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the operating system platform of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">CentOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Ubuntu</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">OpenSUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">RedHat</span></code>, <code class="docutils literal notranslate"><span class="pre">Debian</span></code>, <code class="docutils literal notranslate"><span class="pre">CoreOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Aliyun</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2003</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2008</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2012</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">7</span></code>, Default is <code class="docutils literal notranslate"><span class="pre">Others</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Customized</span> <span class="pre">Linux</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Image.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Image.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the enterprise resource group to which a custom image belongs</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Image.snapshot_id">
<code class="sig-name descname">snapshot_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Image.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a snapshot that is used to create a combined custom image.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Image.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Image.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tag value of an image. The value of N ranges from 1 to 20.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.Image.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">architecture</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_device_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Image.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Image resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>architecture</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the architecture of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">i386</span></code> , Default is <code class="docutils literal notranslate"><span class="pre">x86_64</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the image. It must be 2 to 256 characters in length and must not start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value: null.</p></li>
<li><p><strong>disk_device_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Description of the system with disks and snapshots under the image.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to force delete the custom image, Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
- false：Verifies that the image is not currently in use by any other instances before deleting the image.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>image*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a> is not allowed). It can contain digits, colons (:), underscores (<a href="#id11"><span class="problematic" id="id12">*</span></a>), or hyphens (-). Default value: null.</p>
</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance ID.</p></li>
<li><p><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the operating system platform of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">CentOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Ubuntu</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">OpenSUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">RedHat</span></code>, <code class="docutils literal notranslate"><span class="pre">Debian</span></code>, <code class="docutils literal notranslate"><span class="pre">CoreOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Aliyun</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2003</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2008</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2012</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">7</span></code>, Default is <code class="docutils literal notranslate"><span class="pre">Others</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Customized</span> <span class="pre">Linux</span></code>.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the enterprise resource group to which a custom image belongs</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a snapshot that is used to create a combined custom image.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The tag value of an image. The value of N ranges from 1 to 20.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>disk_device_mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of a disk in the combined custom image. Value range: /dev/xvda to /dev/xvdz.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of a disk in the combined custom image. If you specify this parameter, you can use a data disk snapshot as the data source of a system disk for creating an image. If it is not specified, the disk type is determined by the corresponding snapshot. Valid values: <code class="docutils literal notranslate"><span class="pre">system</span></code>, <code class="docutils literal notranslate"><span class="pre">data</span></code>,</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of a disk in the combined custom image, in GiB. Value range: 5 to 2000.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies a snapshot that is used to create a combined custom image.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.Image.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Image.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.Image.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Image.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.ImageCopy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">ImageCopy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy" title="Permalink to this definition">¶</a></dt>
<dd><p>Copies a custom image from one region to another. You can use copied images to perform operations in the target region, such as creating instances (RunInstances) and replacing system disks (ReplaceSystemDisk).</p>
<blockquote>
<div><p><strong>NOTE:</strong> You can only copy the custom image when it is in the Available state.</p>
<p><strong>NOTE:</strong> You can only copy the image belonging to your Alibaba Cloud account. Images cannot be copied from one account to another.</p>
<p><strong>NOTE:</strong> If the copying is not completed, you cannot call DeleteImage to delete the image but you can call CancelCopyImage to cancel the copying.</p>
<p><strong>NOTE:</strong> Available in 1.66.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">ImageCopy</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;test-image&quot;</span><span class="p">,</span>
    <span class="n">image_name</span><span class="o">=</span><span class="s2">&quot;test-image&quot;</span><span class="p">,</span>
    <span class="n">source_image_id</span><span class="o">=</span><span class="s2">&quot;m-bp1gxyhdswlsn18tu***&quot;</span><span class="p">,</span>
    <span class="n">source_region_id</span><span class="o">=</span><span class="s2">&quot;cn-hangzhou&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;FinanceDept&quot;</span><span class="p">:</span> <span class="s2">&quot;FinanceDeptJoshua&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the image. It must be 2 to 256 characters in length and must not start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value: null.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to encrypt the image.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to force delete the custom image, Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
- false：Verifies that the image is not currently in use by any other instances before deleting the image.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>image*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a> is not allowed). It can contain digits, colons (:), underscores (<a href="#id15"><span class="problematic" id="id16">*</span></a>), or hyphens (-). Default value: null.</p>
</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key ID used to encrypt the image.</p></li>
<li><p><strong>source_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source image ID.</p></li>
<li><p><strong>source_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the region to which the source custom image belongs. You can call <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25609.htm">DescribeRegions</a> to view the latest regions of Alibaba Cloud.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The tag value of an image. The value of N ranges from 1 to 20.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageCopy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the image. It must be 2 to 256 characters in length and must not start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value: null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageCopy.encrypted">
<code class="sig-name descname">encrypted</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether to encrypt the image.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageCopy.force">
<code class="sig-name descname">force</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.force" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether to force delete the custom image, Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
<ul class="simple">
<li><p>true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.</p></li>
<li><p>false：Verifies that the image is not currently in use by any other instances before deleting the image.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageCopy.image_name">
<code class="sig-name descname">image_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.image_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a> is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageCopy.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Key ID used to encrypt the image.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageCopy.source_image_id">
<code class="sig-name descname">source_image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.source_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The source image ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageCopy.source_region_id">
<code class="sig-name descname">source_region_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.source_region_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the region to which the source custom image belongs. You can call <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25609.htm">DescribeRegions</a> to view the latest regions of Alibaba Cloud.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageCopy.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tag value of an image. The value of N ranges from 1 to 20.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.ImageCopy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_region_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ImageCopy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the image. It must be 2 to 256 characters in length and must not start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value: null.</p></li>
<li><p><strong>encrypted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to encrypt the image.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to force delete the custom image, Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
- false：Verifies that the image is not currently in use by any other instances before deleting the image.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>image*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a> is not allowed). It can contain digits, colons (:), underscores (<a href="#id20"><span class="problematic" id="id21">*</span></a>), or hyphens (-). Default value: null.</p>
</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key ID used to encrypt the image.</p></li>
<li><p><strong>source_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source image ID.</p></li>
<li><p><strong>source_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ID of the region to which the source custom image belongs. You can call <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25609.htm">DescribeRegions</a> to view the latest regions of Alibaba Cloud.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The tag value of an image. The value of N ranges from 1 to 20.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.ImageCopy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.ImageCopy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageCopy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.ImageExport">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">ImageExport</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oss_bucket</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oss_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageExport" title="Permalink to this definition">¶</a></dt>
<dd><p>Export a custom image to the OSS bucket in the same region as the custom image.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If you create an ECS instance using a mirror image and create a system disk snapshot again, exporting a custom image created from the system disk snapshot is not supported.</p>
<p><strong>NOTE:</strong> Support for exporting custom images that include data disk snapshot information in the image. The number of data disks cannot exceed 4 and the maximum capacity of a single data disk cannot exceed 500 GiB.</p>
<p><strong>NOTE:</strong> Before exporting the image, you must authorize the cloud server ECS official service account to write OSS permissions through RAM.</p>
<p><strong>NOTE:</strong> Available in 1.68.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">ImageExport</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">image_id</span><span class="o">=</span><span class="s2">&quot;m-bp1gxy***&quot;</span><span class="p">,</span>
    <span class="n">oss_bucket</span><span class="o">=</span><span class="s2">&quot;ecsimageexportconfig&quot;</span><span class="p">,</span>
    <span class="n">oss_prefix</span><span class="o">=</span><span class="s2">&quot;ecsExport&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source image ID.</p></li>
<li><p><strong>oss_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Save the exported OSS bucket.</p></li>
<li><p><strong>oss_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix of your OSS Object. It can be composed of numbers or letters, and the character length is 1 ~ 30.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageExport.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageExport.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The source image ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageExport.oss_bucket">
<code class="sig-name descname">oss_bucket</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageExport.oss_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Save the exported OSS bucket.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageExport.oss_prefix">
<code class="sig-name descname">oss_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageExport.oss_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The prefix of your OSS Object. It can be composed of numbers or letters, and the character length is 1 ~ 30.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.ImageExport.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oss_bucket</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oss_prefix</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageExport.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ImageExport resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source image ID.</p></li>
<li><p><strong>oss_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Save the exported OSS bucket.</p></li>
<li><p><strong>oss_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix of your OSS Object. It can be composed of numbers or letters, and the character length is 1 ~ 30.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.ImageExport.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageExport.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.ImageExport.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageExport.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.ImageImport">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">ImageImport</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">architecture</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_device_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">os_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageImport" title="Permalink to this definition">¶</a></dt>
<dd><p>Import a copy of your local on-premise file to ECS, and appear as a custom replacement in the corresponding domain.</p>
<blockquote>
<div><p><strong>NOTE:</strong> You must upload the image file to the object storage OSS in advance.</p>
<p><strong>NOTE:</strong> The region where the image is imported must be the same region as the OSS bucket where the image file is uploaded.</p>
<p><strong>NOTE:</strong> Available in 1.69.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">this</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">ImageImport</span><span class="p">(</span><span class="s2">&quot;this&quot;</span><span class="p">,</span>
    <span class="n">architecture</span><span class="o">=</span><span class="s2">&quot;x86_64&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;test import image&quot;</span><span class="p">,</span>
    <span class="n">disk_device_mappings</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;diskImageSize&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
        <span class="s2">&quot;ossBucket&quot;</span><span class="p">:</span> <span class="s2">&quot;testimportimage&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ossObject&quot;</span><span class="p">:</span> <span class="s2">&quot;root.img&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">image_name</span><span class="o">=</span><span class="s2">&quot;test-import-image&quot;</span><span class="p">,</span>
    <span class="n">license_type</span><span class="o">=</span><span class="s2">&quot;Auto&quot;</span><span class="p">,</span>
    <span class="n">os_type</span><span class="o">=</span><span class="s2">&quot;linux&quot;</span><span class="p">,</span>
    <span class="n">platform</span><span class="o">=</span><span class="s2">&quot;Ubuntu&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>architecture</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the architecture of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">i386</span></code> , Default is <code class="docutils literal notranslate"><span class="pre">x86_64</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the image. The length is 2 to 256 English or Chinese characters, and cannot begin with http: // and https: //.</p></li>
<li><p><strong>disk_device_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Description of the system with disks and snapshots under the image.</p></li>
<li><p><strong>image*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The image name. The length is 2 ~ 128 English or Chinese characters. Must start with a capital letter or Chinese, and cannot start with http: // and https: //. Can contain numbers, colons (:), underscores (<a href="#id25"><span class="problematic" id="id26">*</span></a>), or hyphens (-).</p>
</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operating system platform type. Valid values: <code class="docutils literal notranslate"><span class="pre">windows</span></code>, Default is <code class="docutils literal notranslate"><span class="pre">linux</span></code>.</p></li>
<li><p><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the operating system platform of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">CentOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Ubuntu</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">OpenSUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">Debian</span></code>, <code class="docutils literal notranslate"><span class="pre">CoreOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2003</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2008</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2012</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">7</span></code>, Default is <code class="docutils literal notranslate"><span class="pre">Others</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Customized</span> <span class="pre">Linux</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>disk_device_mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of a disk in the combined custom image. If you specify this parameter, you can use a data disk snapshot as the data source of a system disk for creating an image. If it is not specified, the disk type is determined by the corresponding snapshot. Valid values: <code class="docutils literal notranslate"><span class="pre">system</span></code>, <code class="docutils literal notranslate"><span class="pre">data</span></code>,</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskImageSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Resolution size. You must ensure that the system disk space ≥ file system space. Ranges: When n = 1, the system disk: 5 ~ 500GiB, When n = 2 ~ 17, that is, data disk: 5 ~ 1000GiB, When temporary is introduced, the system automatically detects the size, which is subject to the detection result.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Image format. Value range: When the <code class="docutils literal notranslate"><span class="pre">RAW</span></code>, <code class="docutils literal notranslate"><span class="pre">VHD</span></code>, <code class="docutils literal notranslate"><span class="pre">qcow2</span></code> is imported into the image, the system automatically detects the image format, whichever comes first.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oss_bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Save the exported OSS bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ossObject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageImport.architecture">
<code class="sig-name descname">architecture</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageImport.architecture" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the architecture of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">i386</span></code> , Default is <code class="docutils literal notranslate"><span class="pre">x86_64</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageImport.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageImport.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the image. The length is 2 to 256 English or Chinese characters, and cannot begin with http: // and https: //.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageImport.disk_device_mappings">
<code class="sig-name descname">disk_device_mappings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageImport.disk_device_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the system with disks and snapshots under the image.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the type of a disk in the combined custom image. If you specify this parameter, you can use a data disk snapshot as the data source of a system disk for creating an image. If it is not specified, the disk type is determined by the corresponding snapshot. Valid values: <code class="docutils literal notranslate"><span class="pre">system</span></code>, <code class="docutils literal notranslate"><span class="pre">data</span></code>,</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskImageSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Resolution size. You must ensure that the system disk space ≥ file system space. Ranges: When n = 1, the system disk: 5 ~ 500GiB, When n = 2 ~ 17, that is, data disk: 5 ~ 1000GiB, When temporary is introduced, the system automatically detects the size, which is subject to the detection result.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Image format. Value range: When the <code class="docutils literal notranslate"><span class="pre">RAW</span></code>, <code class="docutils literal notranslate"><span class="pre">VHD</span></code>, <code class="docutils literal notranslate"><span class="pre">qcow2</span></code> is imported into the image, the system automatically detects the image format, whichever comes first.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oss_bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Save the exported OSS bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ossObject</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageImport.image_name">
<code class="sig-name descname">image_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageImport.image_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The image name. The length is 2 ~ 128 English or Chinese characters. Must start with a capital letter or Chinese, and cannot start with http: // and https: //. Can contain numbers, colons (:), underscores (_), or hyphens (-).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageImport.os_type">
<code class="sig-name descname">os_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageImport.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Operating system platform type. Valid values: <code class="docutils literal notranslate"><span class="pre">windows</span></code>, Default is <code class="docutils literal notranslate"><span class="pre">linux</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageImport.platform">
<code class="sig-name descname">platform</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageImport.platform" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the operating system platform of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">CentOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Ubuntu</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">OpenSUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">Debian</span></code>, <code class="docutils literal notranslate"><span class="pre">CoreOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2003</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2008</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2012</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">7</span></code>, Default is <code class="docutils literal notranslate"><span class="pre">Others</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Customized</span> <span class="pre">Linux</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.ImageImport.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">architecture</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_device_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">os_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageImport.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ImageImport resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>architecture</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the architecture of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">i386</span></code> , Default is <code class="docutils literal notranslate"><span class="pre">x86_64</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the image. The length is 2 to 256 English or Chinese characters, and cannot begin with http: // and https: //.</p></li>
<li><p><strong>disk_device_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Description of the system with disks and snapshots under the image.</p></li>
<li><p><strong>image*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The image name. The length is 2 ~ 128 English or Chinese characters. Must start with a capital letter or Chinese, and cannot start with http: // and https: //. Can contain numbers, colons (:), underscores (<a href="#id29"><span class="problematic" id="id30">*</span></a>), or hyphens (-).</p>
</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operating system platform type. Valid values: <code class="docutils literal notranslate"><span class="pre">windows</span></code>, Default is <code class="docutils literal notranslate"><span class="pre">linux</span></code>.</p></li>
<li><p><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the operating system platform of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: <code class="docutils literal notranslate"><span class="pre">CentOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Ubuntu</span></code>, <code class="docutils literal notranslate"><span class="pre">SUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">OpenSUSE</span></code>, <code class="docutils literal notranslate"><span class="pre">Debian</span></code>, <code class="docutils literal notranslate"><span class="pre">CoreOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2003</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2008</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">Server</span> <span class="pre">2012</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows</span> <span class="pre">7</span></code>, Default is <code class="docutils literal notranslate"><span class="pre">Others</span> <span class="pre">Linux</span></code>, <code class="docutils literal notranslate"><span class="pre">Customized</span> <span class="pre">Linux</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>disk_device_mappings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of a disk in the combined custom image. If you specify this parameter, you can use a data disk snapshot as the data source of a system disk for creating an image. If it is not specified, the disk type is determined by the corresponding snapshot. Valid values: <code class="docutils literal notranslate"><span class="pre">system</span></code>, <code class="docutils literal notranslate"><span class="pre">data</span></code>,</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskImageSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Resolution size. You must ensure that the system disk space ≥ file system space. Ranges: When n = 1, the system disk: 5 ~ 500GiB, When n = 2 ~ 17, that is, data disk: 5 ~ 1000GiB, When temporary is introduced, the system automatically detects the size, which is subject to the detection result.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Image format. Value range: When the <code class="docutils literal notranslate"><span class="pre">RAW</span></code>, <code class="docutils literal notranslate"><span class="pre">VHD</span></code>, <code class="docutils literal notranslate"><span class="pre">qcow2</span></code> is imported into the image, the system automatically detects the image format, whichever comes first.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oss_bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Save the exported OSS bucket.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ossObject</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.ImageImport.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageImport.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.ImageImport.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageImport.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.ImageSharePermission">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">ImageSharePermission</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageSharePermission" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage image sharing permissions. You can share your custom image to other Alibaba Cloud users. The user can use the shared custom image to create ECS instances or replace the system disk of the instance.</p>
<blockquote>
<div><p><strong>NOTE:</strong> You can only share your own custom images to other Alibaba Cloud users.</p>
<p><strong>NOTE:</strong> Each custom image can be shared with up to 50 Alibaba Cloud accounts. You can submit a ticket to share with more users.</p>
<p><strong>NOTE:</strong> After creating an ECS instance using a shared image, once the custom image owner releases the image sharing relationship or deletes the custom image, the instance cannot initialize the system disk.</p>
<p><strong>NOTE:</strong> Available in 1.68.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">ImageSharePermission</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;1234567890&quot;</span><span class="p">,</span>
    <span class="n">image_id</span><span class="o">=</span><span class="s2">&quot;m-bp1gxyh***&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alibaba Cloud Account ID. It is used to share images.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source image ID.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageSharePermission.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageSharePermission.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Alibaba Cloud Account ID. It is used to share images.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ImageSharePermission.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ImageSharePermission.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The source image ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.ImageSharePermission.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageSharePermission.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ImageSharePermission resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alibaba Cloud Account ID. It is used to share images.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source image ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.ImageSharePermission.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageSharePermission.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.ImageSharePermission.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ImageSharePermission.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allocate_public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_release_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credit_specification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dry_run</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_in</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_out</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">io_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renewal_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_enhancement_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_price_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_auto_snapshot_policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Instance resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] allocate_public_ip: It has been deprecated from version “1.7.0”. Setting “internet_max_bandwidth_out” larger than 0 can allocate a public ip address for an instance.
:param pulumi.Input[str] auto_release_time: The automatic release time of the <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> instance.</p>
<blockquote>
<div><p>The time follows the ISO 8601 standard and is in UTC time. Format: yyyy-MM-ddTHH:mm:ssZ. It must be at least half an hour later than the current time and less than 3 years since the current time.
Set it to null can cancel automatic release attribute and the ECS instance will not be released automatically.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Auto renewal period of an instance, in the unit of month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to 1. Valid value:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- [1, 2, 3, 6, 12] when `period_unit` in &quot;Month&quot;
- [1, 2, 3] when `period_unit` in &quot;Week&quot;
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to start the instance in. It is ignored and will be computed when set <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>.</p></li>
<li><p><strong>credit_specification</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Performance mode of the t5 burstable instance. Valid values: ‘Standard’, ‘Unlimited’.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of data disks created with instance.</p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether enable the deletion protection or not.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">true</span><span class="p">:</span> <span class="n">Enable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
<span class="o">-</span> <span class="n">false</span><span class="p">:</span> <span class="n">Disable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the data disk.</p></li>
<li><p><strong>dry_run</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to send a dry-run request. Default to false.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- true: Only a dry-run request is sent and no instance is created. The system checks whether the required parameters are set, and validates the request format, service permissions, and available ECS instances. If the validation fails, the corresponding error code is returned. If the validation succeeds, the `DryRunOperation` error code is returned.
- false: A request is sent. If the validation succeeds, the instance is created.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If it is true, the “PrePaid” instance will be change to “PostPaid” and then deleted forcibly.
However, because of changing instance charge type has CPU core count quota limitation, so strongly recommand that “Don’t modify instance charge type frequentlly in one month”.</p></li>
<li><p><strong>host*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Host name of the ECS, which is a string of at least two characters. “hostname” cannot start or end with “.” or “-“. In addition, two or more consecutive “.” or “-“ symbols are not allowed. On Windows, the host name can contain a maximum of 15 characters, which can be a combination of uppercase/lowercase letters, numerals, and “-“. The host name cannot contain dots (“.”) or contain only numeric characters. When it is changed, the instance will reboot to make the change take effect.
On other OSs such as Linux, the host name can contain a maximum of 30 characters, which can be segments separated by dots (“.”), where each segment can contain uppercase/lowercase letters, numerals, or “<a href="#id33"><span class="problematic" id="id34">*</span></a>“. When it is changed, the instance will reboot to make the change take effect.</p>
</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Image to use for the instance. ECS instance’s image can be replaced via changing ‘image_id’. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>include_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to change instance disks charge type when changing instance charge type.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, The default is <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance to start. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>internet_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet charge type of the instance, Valid values are <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>, <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. At present, ‘PrePaid’ instance cannot change the value to “PayByBandwidth” from “PayByTraffic”.</p></li>
<li><p><strong>internet_max_bandwidth_in</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). Value range: [1, 200]. If this value is not specified, then automatically sets it to 200 Mbps.</p></li>
<li><p><strong>internet_max_bandwidth_out</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum outgoing bandwidth to the public network, measured in Mbps (Mega bit per second). Value range:  [0, 100]. Default to 0 Mbps.</p></li>
<li><p><strong>io_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.</p></li>
<li><p><strong>is_outdated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use outdated instance type. Default to false.</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to an instance. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating an instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password to an instance is a string of 8 to 30 characters. It must contain uppercase/lowercase letters and numerals, but cannot contain special symbols. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy the resource, in month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to 1. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- [1-9, 12, 24, 36, 48, 60] when `period_unit` in &quot;Month&quot;
- [1-3] when `period_unit` in &quot;Week&quot;
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The duration unit that you will buy the resource. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is ‘PrePaid’. Valid value: [“Week”, “Month”]. Default to “Month”.</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance private IP address can be specified when you creating new instance. It is valid when <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>renewal_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to renew an ECS instance automatically or not. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to “Normal”. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `AutoRenewal`: Enable auto renewal.
- `Normal`: Disable auto renewal.
- `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the instance belongs.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance RAM role name. The name is provided and maintained by RAM. You can use <code class="docutils literal notranslate"><span class="pre">ram.Role</span></code> to create a new one.</p></li>
<li><p><strong>security_enhancement_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security enhancement strategy.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Active</span><span class="p">:</span> <span class="n">Enable</span> <span class="n">security</span> <span class="n">enhancement</span> <span class="n">strategy</span><span class="p">,</span> <span class="n">it</span> <span class="n">only</span> <span class="n">works</span> <span class="n">on</span> <span class="n">system</span> <span class="n">images</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Deactive</span><span class="p">:</span> <span class="n">Disable</span> <span class="n">security</span> <span class="n">enhancement</span> <span class="n">strategy</span><span class="p">,</span> <span class="n">it</span> <span class="n">works</span> <span class="n">on</span> <span class="nb">all</span> <span class="n">images</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group ids to associate with.</p></li>
<li><p><strong>spot_price_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The hourly price threshold of a instance, and it takes effect only when parameter ‘spot_strategy’ is ‘SpotWithPriceLimit’. Three decimals is allowed at most.</p></li>
<li><p><strong>spot_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The spot strategy of a Pay-As-You-Go instance, and it takes effect only when parameter <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is ‘PostPaid’. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">NoSpot</span><span class="p">:</span> <span class="n">A</span> <span class="n">regular</span> <span class="n">Pay</span><span class="o">-</span><span class="n">As</span><span class="o">-</span><span class="n">You</span><span class="o">-</span><span class="n">Go</span> <span class="n">instance</span><span class="o">.</span>
<span class="o">-</span> <span class="n">SpotWithPriceLimit</span><span class="p">:</span> <span class="n">A</span> <span class="n">price</span> <span class="n">threshold</span> <span class="k">for</span> <span class="n">a</span> <span class="n">spot</span> <span class="n">instance</span>
<span class="o">-</span> <span class="n">SpotAsPriceGo</span><span class="p">:</span> <span class="n">A</span> <span class="n">price</span> <span class="n">that</span> <span class="ow">is</span> <span class="n">based</span> <span class="n">on</span> <span class="n">the</span> <span class="n">highest</span> <span class="n">Pay</span><span class="o">-</span><span class="n">As</span><span class="o">-</span><span class="n">You</span><span class="o">-</span><span class="n">Go</span> <span class="n">instance</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>system_disk_auto_snapshot_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the automatic snapshot policy applied to the system disk.</p></li>
<li><p><strong>system_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">ephemeral_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud</span></code>. <code class="docutils literal notranslate"><span class="pre">cloud</span></code> only is used to some none I/O optimized instance. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>system_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the system disk, measured in GiB. Value range: [20, 500]. The specified value must be equal to or greater than max{20, Imagesize}. Default value: max{40, ImageSize}. ECS instance’s system disk can be reset when replacing system disk. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-defined data to customize the startup behaviors of an ECS instance and to pass data into an ECS instance. From version 1.60.0, it can be update in-place. If updated, the instance will reboot to make the change take effect. Note: Not all of changes will take effect and it depends on <a class="reference external" href="https://cloudinit.readthedocs.io/en/latest/topics/modules.html">cloud-init module type</a>.</p></li>
<li><p><strong>volume_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the devices created by the instance at launch time.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual switch ID to launch in VPC. This parameter must be set unless you can create classic network instances. When it is changed, the instance will reboot to make the change take effect.</p>
</dd>
</dl>
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the automatic snapshot policy applied to the system disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The category of the disk:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud</span></code>: The general cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>: The efficiency cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>: The SSD cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>: The ESSD cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ephemeral_ssd</span></code>: The local SSD disk.
Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_with_instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Delete this data disk when the instance is destroyed. It only works on cloud, cloud_efficiency, cloud_essd, cloud_ssd disk. If the category of this data disk was ephemeral_ssd, please don’t set this param.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - -(Optional, Bool, ForceNew) Encrypted the data in this disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the data disk.</p>
<ul>
<li><p>cloud：[5, 2000]</p></li>
<li><p>cloud_efficiency：[20, 32768]</p></li>
<li><p>cloud_ssd：[20, 32768]</p></li>
<li><p>cloud_essd：[20, 32768]</p></li>
<li><p>ephemeral_ssd: [5, 800]</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The snapshot ID used to initialize the data disk. If the size specified by snapshot is greater that the size of the disk, use the size specified by snapshot as the size of the data disk.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.allocate_public_ip">
<code class="sig-name descname">allocate_public_ip</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.allocate_public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from version “1.7.0”. Setting “internet_max_bandwidth_out” larger than 0 can allocate a public ip address for an instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.auto_release_time">
<code class="sig-name descname">auto_release_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.auto_release_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The automatic release time of the <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> instance. 
The time follows the ISO 8601 standard and is in UTC time. Format: yyyy-MM-ddTHH:mm:ssZ. It must be at least half an hour later than the current time and less than 3 years since the current time.
Set it to null can cancel automatic release attribute and the ECS instance will not be released automatically.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.auto_renew_period">
<code class="sig-name descname">auto_renew_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Auto renewal period of an instance, in the unit of month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to 1. Valid value:</p>
<ul class="simple">
<li><p>[1, 2, 3, 6, 12] when <code class="docutils literal notranslate"><span class="pre">period_unit</span></code> in “Month”</p></li>
<li><p>[1, 2, 3] when <code class="docutils literal notranslate"><span class="pre">period_unit</span></code> in “Week”</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to start the instance in. It is ignored and will be computed when set <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.credit_specification">
<code class="sig-name descname">credit_specification</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.credit_specification" title="Permalink to this definition">¶</a></dt>
<dd><p>Performance mode of the t5 burstable instance. Valid values: ‘Standard’, ‘Unlimited’.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.data_disks">
<code class="sig-name descname">data_disks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of data disks created with instance.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the automatic snapshot policy applied to the system disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The category of the disk:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud</span></code>: The general cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>: The efficiency cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>: The SSD cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>: The ESSD cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ephemeral_ssd</span></code>: The local SSD disk.
Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_with_instance</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Delete this data disk when the instance is destroyed. It only works on cloud, cloud_efficiency, cloud_essd, cloud_ssd disk. If the category of this data disk was ephemeral_ssd, please don’t set this param.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - -(Optional, Bool, ForceNew) Encrypted the data in this disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the data disk.</p>
<ul>
<li><p>cloud：[5, 2000]</p></li>
<li><p>cloud_efficiency：[20, 32768]</p></li>
<li><p>cloud_ssd：[20, 32768]</p></li>
<li><p>cloud_essd：[20, 32768]</p></li>
<li><p>ephemeral_ssd: [5, 800]</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The snapshot ID used to initialize the data disk. If the size specified by snapshot is greater that the size of the disk, use the size specified by snapshot as the size of the data disk.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.deletion_protection">
<code class="sig-name descname">deletion_protection</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether enable the deletion protection or not.</p>
<ul class="simple">
<li><p>true: Enable deletion protection.</p></li>
<li><p>false: Disable deletion protection.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the data disk.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.dry_run">
<code class="sig-name descname">dry_run</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.dry_run" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to send a dry-run request. Default to false.</p>
<ul class="simple">
<li><p>true: Only a dry-run request is sent and no instance is created. The system checks whether the required parameters are set, and validates the request format, service permissions, and available ECS instances. If the validation fails, the corresponding error code is returned. If the validation succeeds, the <code class="docutils literal notranslate"><span class="pre">DryRunOperation</span></code> error code is returned.</p></li>
<li><p>false: A request is sent. If the validation succeeds, the instance is created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.force_delete">
<code class="sig-name descname">force_delete</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>If it is true, the “PrePaid” instance will be change to “PostPaid” and then deleted forcibly.
However, because of changing instance charge type has CPU core count quota limitation, so strongly recommand that “Don’t modify instance charge type frequentlly in one month”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.host_name">
<code class="sig-name descname">host_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Host name of the ECS, which is a string of at least two characters. “hostname” cannot start or end with “.” or “-“. In addition, two or more consecutive “.” or “-“ symbols are not allowed. On Windows, the host name can contain a maximum of 15 characters, which can be a combination of uppercase/lowercase letters, numerals, and “-“. The host name cannot contain dots (“.”) or contain only numeric characters. When it is changed, the instance will reboot to make the change take effect.
On other OSs such as Linux, the host name can contain a maximum of 30 characters, which can be segments separated by dots (“.”), where each segment can contain uppercase/lowercase letters, numerals, or “_“. When it is changed, the instance will reboot to make the change take effect.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Image to use for the instance. ECS instance’s image can be replaced via changing ‘image_id’. When it is changed, the instance will reboot to make the change take effect.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.include_data_disks">
<code class="sig-name descname">include_data_disks</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.include_data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to change instance disks charge type when changing instance charge type.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, The default is <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of instance to start. When it is changed, the instance will reboot to make the change take effect.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.internet_charge_type">
<code class="sig-name descname">internet_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.internet_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Internet charge type of the instance, Valid values are <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>, <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. At present, ‘PrePaid’ instance cannot change the value to “PayByBandwidth” from “PayByTraffic”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.internet_max_bandwidth_in">
<code class="sig-name descname">internet_max_bandwidth_in</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.internet_max_bandwidth_in" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). Value range: [1, 200]. If this value is not specified, then automatically sets it to 200 Mbps.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.internet_max_bandwidth_out">
<code class="sig-name descname">internet_max_bandwidth_out</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.internet_max_bandwidth_out" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum outgoing bandwidth to the public network, measured in Mbps (Mega bit per second). Value range:  [0, 100]. Default to 0 Mbps.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.io_optimized">
<code class="sig-name descname">io_optimized</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.io_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.is_outdated">
<code class="sig-name descname">is_outdated</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.is_outdated" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use outdated instance type. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.key_name">
<code class="sig-name descname">key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to an instance. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored. When it is changed, the instance will reboot to make the change take effect.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating an instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set. When it is changed, the instance will reboot to make the change take effect.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password to an instance is a string of 8 to 30 characters. It must contain uppercase/lowercase letters and numerals, but cannot contain special symbols. When it is changed, the instance will reboot to make the change take effect.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy the resource, in month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to 1. Valid values:</p>
<ul class="simple">
<li><p>[1-9, 12, 24, 36, 48, 60] when <code class="docutils literal notranslate"><span class="pre">period_unit</span></code> in “Month”</p></li>
<li><p>[1-3] when <code class="docutils literal notranslate"><span class="pre">period_unit</span></code> in “Week”</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.period_unit">
<code class="sig-name descname">period_unit</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.period_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration unit that you will buy the resource. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is ‘PrePaid’. Valid value: [“Week”, “Month”]. Default to “Month”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.private_ip">
<code class="sig-name descname">private_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance private IP address can be specified when you creating new instance. It is valid when <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified. When it is changed, the instance will reboot to make the change take effect.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.public_ip">
<code class="sig-name descname">public_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance public ip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.renewal_status">
<code class="sig-name descname">renewal_status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.renewal_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to renew an ECS instance automatically or not. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to “Normal”. Valid values:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">AutoRenewal</span></code>: Enable auto renewal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">Normal</span></code>: Disable auto renewal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">NotRenewal</span></code>: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the instance belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.role_name">
<code class="sig-name descname">role_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance RAM role name. The name is provided and maintained by RAM. You can use <code class="docutils literal notranslate"><span class="pre">ram.Role</span></code> to create a new one.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.security_enhancement_strategy">
<code class="sig-name descname">security_enhancement_strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.security_enhancement_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>The security enhancement strategy.</p>
<ul class="simple">
<li><p>Active: Enable security enhancement strategy, it only works on system images.</p></li>
<li><p>Deactive: Disable security enhancement strategy, it works on all images.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.security_groups">
<code class="sig-name descname">security_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group ids to associate with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.spot_price_limit">
<code class="sig-name descname">spot_price_limit</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.spot_price_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The hourly price threshold of a instance, and it takes effect only when parameter ‘spot_strategy’ is ‘SpotWithPriceLimit’. Three decimals is allowed at most.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.spot_strategy">
<code class="sig-name descname">spot_strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.spot_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>The spot strategy of a Pay-As-You-Go instance, and it takes effect only when parameter <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is ‘PostPaid’. Value range:</p>
<ul class="simple">
<li><p>NoSpot: A regular Pay-As-You-Go instance.</p></li>
<li><p>SpotWithPriceLimit: A price threshold for a spot instance</p></li>
<li><p>SpotAsPriceGo: A price that is based on the highest Pay-As-You-Go instance</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance status.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.system_disk_auto_snapshot_policy_id">
<code class="sig-name descname">system_disk_auto_snapshot_policy_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.system_disk_auto_snapshot_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the automatic snapshot policy applied to the system disk.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.system_disk_category">
<code class="sig-name descname">system_disk_category</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.system_disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">ephemeral_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud</span></code>. <code class="docutils literal notranslate"><span class="pre">cloud</span></code> only is used to some none I/O optimized instance. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.system_disk_size">
<code class="sig-name descname">system_disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.system_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of the system disk, measured in GiB. Value range: [20, 500]. The specified value must be equal to or greater than max{20, Imagesize}. Default value: max{40, ImageSize}. ECS instance’s system disk can be reset when replacing system disk. When it is changed, the instance will reboot to make the change take effect.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
<ul class="simple">
<li><p>Key: It can be up to 64 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It cannot be a null string.</p></li>
<li><p>Value: It can be up to 128 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It can be a null string.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.user_data">
<code class="sig-name descname">user_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined data to customize the startup behaviors of an ECS instance and to pass data into an ECS instance. From version 1.60.0, it can be update in-place. If updated, the instance will reboot to make the change take effect. Note: Not all of changes will take effect and it depends on <a class="reference external" href="https://cloudinit.readthedocs.io/en/latest/topics/modules.html">cloud-init module type</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.volume_tags">
<code class="sig-name descname">volume_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.volume_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the devices created by the instance at launch time.</p>
<ul class="simple">
<li><p>Key: It can be up to 64 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It cannot be a null string.</p></li>
<li><p>Value: It can be up to 128 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It can be a null string.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Instance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual switch ID to launch in VPC. This parameter must be set unless you can create classic network instances. When it is changed, the instance will reboot to make the change take effect.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allocate_public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_release_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credit_specification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dry_run</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_in</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_out</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">io_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renewal_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_enhancement_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_price_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_auto_snapshot_policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocate_public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It has been deprecated from version “1.7.0”. Setting “internet_max_bandwidth_out” larger than 0 can allocate a public ip address for an instance.</p></li>
<li><p><strong>auto_release_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The automatic release time of the <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> instance. 
The time follows the ISO 8601 standard and is in UTC time. Format: yyyy-MM-ddTHH:mm:ssZ. It must be at least half an hour later than the current time and less than 3 years since the current time.
Set it to null can cancel automatic release attribute and the ECS instance will not be released automatically.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Auto renewal period of an instance, in the unit of month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to 1. Valid value:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- [1, 2, 3, 6, 12] when `period_unit` in &quot;Month&quot;
- [1, 2, 3] when `period_unit` in &quot;Week&quot;
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to start the instance in. It is ignored and will be computed when set <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code>.</p></li>
<li><p><strong>credit_specification</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Performance mode of the t5 burstable instance. Valid values: ‘Standard’, ‘Unlimited’.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of data disks created with instance.</p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether enable the deletion protection or not.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">true</span><span class="p">:</span> <span class="n">Enable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
<span class="o">-</span> <span class="n">false</span><span class="p">:</span> <span class="n">Disable</span> <span class="n">deletion</span> <span class="n">protection</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the data disk.</p></li>
<li><p><strong>dry_run</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to send a dry-run request. Default to false.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- true: Only a dry-run request is sent and no instance is created. The system checks whether the required parameters are set, and validates the request format, service permissions, and available ECS instances. If the validation fails, the corresponding error code is returned. If the validation succeeds, the `DryRunOperation` error code is returned.
- false: A request is sent. If the validation succeeds, the instance is created.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If it is true, the “PrePaid” instance will be change to “PostPaid” and then deleted forcibly.
However, because of changing instance charge type has CPU core count quota limitation, so strongly recommand that “Don’t modify instance charge type frequentlly in one month”.</p></li>
<li><p><strong>host*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Host name of the ECS, which is a string of at least two characters. “hostname” cannot start or end with “.” or “-“. In addition, two or more consecutive “.” or “-“ symbols are not allowed. On Windows, the host name can contain a maximum of 15 characters, which can be a combination of uppercase/lowercase letters, numerals, and “-“. The host name cannot contain dots (“.”) or contain only numeric characters. When it is changed, the instance will reboot to make the change take effect.
On other OSs such as Linux, the host name can contain a maximum of 30 characters, which can be segments separated by dots (“.”), where each segment can contain uppercase/lowercase letters, numerals, or “<a href="#id39"><span class="problematic" id="id40">*</span></a>“. When it is changed, the instance will reboot to make the change take effect.</p>
</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Image to use for the instance. ECS instance’s image can be replaced via changing ‘image_id’. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>include_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to change instance disks charge type when changing instance charge type.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, The default is <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance to start. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>internet_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet charge type of the instance, Valid values are <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>, <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">PayByTraffic</span></code>. At present, ‘PrePaid’ instance cannot change the value to “PayByBandwidth” from “PayByTraffic”.</p></li>
<li><p><strong>internet_max_bandwidth_in</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). Value range: [1, 200]. If this value is not specified, then automatically sets it to 200 Mbps.</p></li>
<li><p><strong>internet_max_bandwidth_out</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum outgoing bandwidth to the public network, measured in Mbps (Mega bit per second). Value range:  [0, 100]. Default to 0 Mbps.</p></li>
<li><p><strong>io_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.</p></li>
<li><p><strong>is_outdated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use outdated instance type. Default to false.</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to an instance. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating an instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set. When it is changed, the instance will reboot to make the change take effect.</p>
</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password to an instance is a string of 8 to 30 characters. It must contain uppercase/lowercase letters and numerals, but cannot contain special symbols. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy the resource, in month. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to 1. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- [1-9, 12, 24, 36, 48, 60] when `period_unit` in &quot;Month&quot;
- [1-3] when `period_unit` in &quot;Week&quot;
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The duration unit that you will buy the resource. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is ‘PrePaid’. Valid value: [“Week”, “Month”]. Default to “Month”.</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance private IP address can be specified when you creating new instance. It is valid when <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance public ip.</p></li>
<li><p><strong>renewal_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to renew an ECS instance automatically or not. It is valid when <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Default to “Normal”. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `AutoRenewal`: Enable auto renewal.
- `Normal`: Disable auto renewal.
- `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the instance belongs.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance RAM role name. The name is provided and maintained by RAM. You can use <code class="docutils literal notranslate"><span class="pre">ram.Role</span></code> to create a new one.</p></li>
<li><p><strong>security_enhancement_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security enhancement strategy.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Active</span><span class="p">:</span> <span class="n">Enable</span> <span class="n">security</span> <span class="n">enhancement</span> <span class="n">strategy</span><span class="p">,</span> <span class="n">it</span> <span class="n">only</span> <span class="n">works</span> <span class="n">on</span> <span class="n">system</span> <span class="n">images</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Deactive</span><span class="p">:</span> <span class="n">Disable</span> <span class="n">security</span> <span class="n">enhancement</span> <span class="n">strategy</span><span class="p">,</span> <span class="n">it</span> <span class="n">works</span> <span class="n">on</span> <span class="nb">all</span> <span class="n">images</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group ids to associate with.</p></li>
<li><p><strong>spot_price_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The hourly price threshold of a instance, and it takes effect only when parameter ‘spot_strategy’ is ‘SpotWithPriceLimit’. Three decimals is allowed at most.</p></li>
<li><p><strong>spot_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The spot strategy of a Pay-As-You-Go instance, and it takes effect only when parameter <code class="docutils literal notranslate"><span class="pre">instance_charge_type</span></code> is ‘PostPaid’. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">NoSpot</span><span class="p">:</span> <span class="n">A</span> <span class="n">regular</span> <span class="n">Pay</span><span class="o">-</span><span class="n">As</span><span class="o">-</span><span class="n">You</span><span class="o">-</span><span class="n">Go</span> <span class="n">instance</span><span class="o">.</span>
<span class="o">-</span> <span class="n">SpotWithPriceLimit</span><span class="p">:</span> <span class="n">A</span> <span class="n">price</span> <span class="n">threshold</span> <span class="k">for</span> <span class="n">a</span> <span class="n">spot</span> <span class="n">instance</span>
<span class="o">-</span> <span class="n">SpotAsPriceGo</span><span class="p">:</span> <span class="n">A</span> <span class="n">price</span> <span class="n">that</span> <span class="ow">is</span> <span class="n">based</span> <span class="n">on</span> <span class="n">the</span> <span class="n">highest</span> <span class="n">Pay</span><span class="o">-</span><span class="n">As</span><span class="o">-</span><span class="n">You</span><span class="o">-</span><span class="n">Go</span> <span class="n">instance</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance status.</p></li>
<li><p><strong>system_disk_auto_snapshot_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the automatic snapshot policy applied to the system disk.</p></li>
<li><p><strong>system_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">ephemeral_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud</span></code>. <code class="docutils literal notranslate"><span class="pre">cloud</span></code> only is used to some none I/O optimized instance. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
<li><p><strong>system_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the system disk, measured in GiB. Value range: [20, 500]. The specified value must be equal to or greater than max{20, Imagesize}. Default value: max{40, ImageSize}. ECS instance’s system disk can be reset when replacing system disk. When it is changed, the instance will reboot to make the change take effect.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>User-defined data to customize the startup behaviors of an ECS instance and to pass data into an ECS instance. From version 1.60.0, it can be update in-place. If updated, the instance will reboot to make the change take effect. Note: Not all of changes will take effect and it depends on <a class="reference external" href="https://cloudinit.readthedocs.io/en/latest/topics/modules.html">cloud-init module type</a>.</p>
</p></li>
<li><p><strong>volume_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the devices created by the instance at launch time.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual switch ID to launch in VPC. This parameter must be set unless you can create classic network instances. When it is changed, the instance will reboot to make the change take effect.</p>
</dd>
</dl>
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the automatic snapshot policy applied to the system disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The category of the disk:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud</span></code>: The general cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>: The efficiency cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>: The SSD cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code>: The ESSD cloud disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ephemeral_ssd</span></code>: The local SSD disk.
Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_with_instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Delete this data disk when the instance is destroyed. It only works on cloud, cloud_efficiency, cloud_essd, cloud_ssd disk. If the category of this data disk was ephemeral_ssd, please don’t set this param.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - -(Optional, Bool, ForceNew) Encrypted the data in this disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the data disk.</p>
<ul>
<li><p>cloud：[5, 2000]</p></li>
<li><p>cloud_efficiency：[20, 32768]</p></li>
<li><p>cloud_ssd：[20, 32768]</p></li>
<li><p>cloud_essd：[20, 32768]</p></li>
<li><p>ephemeral_ssd: [5, 800]</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The snapshot ID used to initialize the data disk. If the size specified by snapshot is greater that the size of the disk, use the size specified by snapshot as the size of the data disk.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.KeyPair">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">KeyPair</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPair" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KeyPair resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] key_file: The name of file to save your new key pair’s private key. Strongly suggest you to specified it when you creating key pair, otherwise, you wouldn’t get its private key ever.
:param pulumi.Input[str] key_name: The key pair’s name. It is the only in one Alicloud account.
:param pulumi.Input[str] public_key: You can import an existing public key and using Alicloud key pair to manage it.
:param pulumi.Input[str] resource_group_id: The Id of resource group which the key pair belongs.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.KeyPair.key_file">
<code class="sig-name descname">key_file</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPair.key_file" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of file to save your new key pair’s private key. Strongly suggest you to specified it when you creating key pair, otherwise, you wouldn’t get its private key ever.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.KeyPair.key_name">
<code class="sig-name descname">key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPair.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The key pair’s name. It is the only in one Alicloud account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.KeyPair.public_key">
<code class="sig-name descname">public_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPair.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>You can import an existing public key and using Alicloud key pair to manage it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.KeyPair.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPair.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the key pair belongs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.KeyPair.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">finger_print</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPair.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KeyPair resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of file to save your new key pair’s private key. Strongly suggest you to specified it when you creating key pair, otherwise, you wouldn’t get its private key ever.</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key pair’s name. It is the only in one Alicloud account.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – You can import an existing public key and using Alicloud key pair to manage it.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the key pair belongs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.KeyPair.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPair.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.KeyPair.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPair.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.KeyPairAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">KeyPairAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPairAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a key pair attachment resource to bind key pair for several ECS instances.</p>
<blockquote>
<div><p><strong>NOTE:</strong> After the key pair is attached with sone instances, there instances must be rebooted to make the key pair affect.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="n">available_disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_ssd&quot;</span><span class="p">,</span>
    <span class="n">available_resource_creation</span><span class="o">=</span><span class="s2">&quot;VSwitch&quot;</span><span class="p">)</span>
<span class="nb">type</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_instance_types</span><span class="p">(</span><span class="n">availability_zone</span><span class="o">=</span><span class="n">default</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">cpu_core_count</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">memory_size</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="n">images</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_images</span><span class="p">(</span><span class="n">most_recent</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;^ubuntu_18.*64&quot;</span><span class="p">,</span>
    <span class="n">owners</span><span class="o">=</span><span class="s2">&quot;system&quot;</span><span class="p">)</span>
<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">name</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;keyPairAttachmentName&quot;</span>
<span class="n">vpc</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;vpc&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;10.1.0.0/21&quot;</span><span class="p">)</span>
<span class="n">vswitch</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Switch</span><span class="p">(</span><span class="s2">&quot;vswitch&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="n">default</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;10.1.1.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="s2">&quot;group&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;New security group&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">instance</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">)]:</span>
    <span class="n">instance</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;instance-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">image_id</span><span class="o">=</span><span class="n">images</span><span class="o">.</span><span class="n">images</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
        <span class="n">instance_name</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">instance_type</span><span class="o">=</span><span class="nb">type</span><span class="o">.</span><span class="n">instance_types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="n">internet_charge_type</span><span class="o">=</span><span class="s2">&quot;PayByTraffic&quot;</span><span class="p">,</span>
        <span class="n">internet_max_bandwidth_out</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">password</span><span class="o">=</span><span class="s2">&quot;Test12345&quot;</span><span class="p">,</span>
        <span class="n">security_groups</span><span class="o">=</span><span class="p">[</span><span class="n">group</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
        <span class="n">system_disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_ssd&quot;</span><span class="p">,</span>
        <span class="n">vswitch_id</span><span class="o">=</span><span class="n">vswitch</span><span class="o">.</span><span class="n">id</span><span class="p">))</span>
<span class="n">pair</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">KeyPair</span><span class="p">(</span><span class="s2">&quot;pair&quot;</span><span class="p">,</span> <span class="n">key_name</span><span class="o">=</span><span class="n">name</span><span class="p">)</span>
<span class="n">attachment</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">KeyPairAttachment</span><span class="p">(</span><span class="s2">&quot;attachment&quot;</span><span class="p">,</span>
    <span class="n">instance_ids</span><span class="o">=</span><span class="p">[</span><span class="n">__item</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">instance</span><span class="p">],</span>
    <span class="n">key_name</span><span class="o">=</span><span class="n">pair</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set it to true and it will reboot instances which attached with the key pair to make key pair affect immediately.</p></li>
<li><p><strong>instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of ECS instance’s IDs.</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of key pair used to bind.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.KeyPairAttachment.force">
<code class="sig-name descname">force</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPairAttachment.force" title="Permalink to this definition">¶</a></dt>
<dd><p>Set it to true and it will reboot instances which attached with the key pair to make key pair affect immediately.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.KeyPairAttachment.instance_ids">
<code class="sig-name descname">instance_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPairAttachment.instance_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of ECS instance’s IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.KeyPairAttachment.key_name">
<code class="sig-name descname">key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPairAttachment.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of key pair used to bind.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.KeyPairAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPairAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KeyPairAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set it to true and it will reboot instances which attached with the key pair to make key pair affect immediately.</p></li>
<li><p><strong>instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of ECS instance’s IDs.</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of key pair used to bind.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.KeyPairAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPairAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.KeyPairAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.KeyPairAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.LaunchTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">LaunchTemplate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_release_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_owner_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_in</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_out</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">io_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_pair_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_enhancement_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_price_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">userdata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ECS Launch Template resource.</p>
<p>For information about Launch Template and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/73916.html">Launch Template</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">images</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_images</span><span class="p">(</span><span class="n">owners</span><span class="o">=</span><span class="s2">&quot;system&quot;</span><span class="p">)</span>
<span class="n">instances</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_instances</span><span class="p">()</span>
<span class="n">template</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">LaunchTemplate</span><span class="p">(</span><span class="s2">&quot;template&quot;</span><span class="p">,</span>
    <span class="n">data_disks</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;test1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;disk1&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;test2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;disk2&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;test1&quot;</span><span class="p">,</span>
    <span class="n">host_name</span><span class="o">=</span><span class="s2">&quot;tf-test-host&quot;</span><span class="p">,</span>
    <span class="n">image_id</span><span class="o">=</span><span class="n">images</span><span class="o">.</span><span class="n">images</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PrePaid&quot;</span><span class="p">,</span>
    <span class="n">instance_name</span><span class="o">=</span><span class="s2">&quot;tf-instance-name&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="n">instances</span><span class="o">.</span><span class="n">instances</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;instance_type&quot;</span><span class="p">],</span>
    <span class="n">internet_charge_type</span><span class="o">=</span><span class="s2">&quot;PayByBandwidth&quot;</span><span class="p">,</span>
    <span class="n">internet_max_bandwidth_in</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">internet_max_bandwidth_out</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">io_optimized</span><span class="o">=</span><span class="s2">&quot;none&quot;</span><span class="p">,</span>
    <span class="n">key_pair_name</span><span class="o">=</span><span class="s2">&quot;test-key-pair&quot;</span><span class="p">,</span>
    <span class="n">network_interfaces</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;hello1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;eth0&quot;</span><span class="p">,</span>
        <span class="s2">&quot;primaryIp&quot;</span><span class="p">:</span> <span class="s2">&quot;10.0.0.2&quot;</span><span class="p">,</span>
        <span class="s2">&quot;securityGroupId&quot;</span><span class="p">:</span> <span class="s2">&quot;xxxx&quot;</span><span class="p">,</span>
        <span class="s2">&quot;vswitchId&quot;</span><span class="p">:</span> <span class="s2">&quot;xxxxxxx&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">network_type</span><span class="o">=</span><span class="s2">&quot;vpc&quot;</span><span class="p">,</span>
    <span class="n">ram_role_name</span><span class="o">=</span><span class="s2">&quot;xxxxx&quot;</span><span class="p">,</span>
    <span class="n">resource_group_id</span><span class="o">=</span><span class="s2">&quot;rg-zkdfjahg9zxncv0&quot;</span><span class="p">,</span>
    <span class="n">security_enhancement_strategy</span><span class="o">=</span><span class="s2">&quot;Active&quot;</span><span class="p">,</span>
    <span class="n">security_group_id</span><span class="o">=</span><span class="s2">&quot;sg-zxcvj0lasdf102350asdf9a&quot;</span><span class="p">,</span>
    <span class="n">spot_price_limit</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">spot_strategy</span><span class="o">=</span><span class="s2">&quot;SpotWithPriceLimit&quot;</span><span class="p">,</span>
    <span class="n">system_disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_ssd&quot;</span><span class="p">,</span>
    <span class="n">system_disk_description</span><span class="o">=</span><span class="s2">&quot;test disk&quot;</span><span class="p">,</span>
    <span class="n">system_disk_name</span><span class="o">=</span><span class="s2">&quot;hello&quot;</span><span class="p">,</span>
    <span class="n">system_disk_size</span><span class="o">=</span><span class="mi">40</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;tag1&quot;</span><span class="p">:</span> <span class="s2">&quot;hello&quot;</span><span class="p">,</span>
        <span class="s2">&quot;tag2&quot;</span><span class="p">:</span> <span class="s2">&quot;world&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">userdata</span><span class="o">=</span><span class="s2">&quot;xxxxxxxxxxxxxx&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="s2">&quot;vpc-asdfnbg0as8dfk1nb2&quot;</span><span class="p">,</span>
    <span class="n">vswitch_id</span><span class="o">=</span><span class="s2">&quot;sw-ljkngaksdjfj0nnasdf&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;beijing-a&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_release_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance auto release time. The time is presented using the ISO8601 standard and in UTC time. The format is  YYYY-MM-DDTHH:MM:SSZ.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of data disks created with instance.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the data disk.</p></li>
<li><p><strong>host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance host name.It cannot start or end with a period (.) or a hyphen (-) and it cannot have two or more consecutive periods (.) or hyphens (-).For Windows: The host name can be [2, 15] characters in length. It can contain A-Z, a-z, numbers, periods (.), and hyphens (-). It cannot only contain numbers. For other operating systems: The host name can be [2, 64] characters in length. It can be segments separated by periods (.). It can contain A-Z, a-z, numbers, and hyphens (-).</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Image ID.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Billing methods. Optional values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">PrePaid</span><span class="p">:</span> <span class="n">Monthly</span><span class="p">,</span> <span class="ow">or</span> <span class="n">annual</span> <span class="n">subscription</span><span class="o">.</span> <span class="n">Make</span> <span class="n">sure</span> <span class="n">that</span> <span class="n">your</span> <span class="n">registered</span> <span class="n">credit</span> <span class="n">card</span> <span class="ow">is</span> <span class="n">invalid</span> <span class="ow">or</span> <span class="n">you</span> <span class="n">have</span> <span class="n">insufficient</span> <span class="n">balance</span> <span class="ow">in</span> <span class="n">your</span> <span class="n">PayPal</span> <span class="n">account</span><span class="o">.</span> <span class="n">Otherwise</span><span class="p">,</span> <span class="n">InvalidPayMethod</span> <span class="n">error</span> <span class="n">may</span> <span class="n">occur</span><span class="o">.</span>
<span class="o">-</span> <span class="n">PostPaid</span><span class="p">:</span> <span class="n">Pay</span><span class="o">-</span><span class="n">As</span><span class="o">-</span><span class="n">You</span><span class="o">-</span><span class="n">Go</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the instance. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (<a href="#id45"><span class="problematic" id="id46">*</span></a>), and hyphens (-).</p>
</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance type. For more information, call resource_alicloud_instances to obtain the latest instance type list.</p></li>
<li><p><strong>internet_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet bandwidth billing method. Optional values: PayByTraffic.</p></li>
<li><p><strong>internet_max_bandwidth_in</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum inbound bandwidth from the Internet network, measured in Mbit/s. Value range: [1, 200].</p></li>
<li><p><strong>internet_max_bandwidth_out</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum outbound bandwidth from the Internet, its unit of measurement is Mbit/s. Value range: [0, 100].</p></li>
<li><p><strong>io_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether it is an I/O-optimized instance or not. Optional values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">none</span>
<span class="o">-</span> <span class="n">optimized</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key_pair_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the key pair.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Ignore</span> <span class="n">this</span> <span class="n">parameter</span> <span class="k">for</span> <span class="n">Windows</span> <span class="n">instances</span><span class="o">.</span> <span class="n">It</span> <span class="ow">is</span> <span class="n">null</span> <span class="n">by</span> <span class="n">default</span><span class="o">.</span> <span class="n">Even</span> <span class="k">if</span> <span class="n">you</span> <span class="n">enter</span> <span class="n">this</span> <span class="n">parameter</span><span class="p">,</span> <span class="n">only</span> <span class="n">the</span>  <span class="n">Password</span> <span class="n">content</span> <span class="ow">is</span> <span class="n">used</span><span class="o">.</span>
<span class="o">-</span> <span class="n">The</span> <span class="n">password</span> <span class="n">logon</span> <span class="n">method</span> <span class="k">for</span> <span class="n">Linux</span> <span class="n">instances</span> <span class="ow">is</span> <span class="nb">set</span> <span class="n">to</span> <span class="n">forbidden</span> <span class="n">upon</span> <span class="n">initialization</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the data disk.</p></li>
<li><p><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The list of network interfaces created with instance.</p></li>
<li><p><strong>network_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network type of the instance. Value options: Classic | VPC.</p></li>
<li><p><strong>ram_role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RAM role name of the instance. You can use the RAM API ListRoles to query instance RAM role names.</p></li>
<li><p><strong>security_enhancement_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether or not to activate the security enhancement feature and install network security software free of charge. Optional values: Active | Deactive.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security group ID must be one in the same VPC.</p></li>
<li><p><strong>spot_price_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – -(Optional)        Sets the maximum hourly instance price. Supports up to three decimal places.</p></li>
<li><p><strong>spot_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The spot strategy for a Pay-As-You-Go instance. This parameter is valid and required only when InstanceChargeType is set to PostPaid. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">NoSpot</span><span class="p">:</span> <span class="n">Normal</span> <span class="n">Pay</span><span class="o">-</span><span class="n">As</span><span class="o">-</span><span class="n">You</span><span class="o">-</span><span class="n">Go</span> <span class="n">instance</span><span class="o">.</span>
<span class="o">-</span> <span class="n">SpotWithPriceLimit</span><span class="p">:</span> <span class="n">Sets</span> <span class="n">the</span> <span class="n">maximum</span> <span class="n">price</span> <span class="k">for</span> <span class="n">a</span> <span class="n">spot</span> <span class="n">instance</span><span class="o">.</span>
<span class="o">-</span> <span class="n">SpotAsPriceGo</span><span class="p">:</span> <span class="n">The</span> <span class="n">system</span> <span class="n">automatically</span> <span class="n">calculates</span> <span class="n">the</span> <span class="n">price</span><span class="o">.</span> <span class="n">The</span> <span class="n">maximum</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">the</span> <span class="n">Pay</span><span class="o">-</span><span class="n">As</span><span class="o">-</span><span class="n">You</span><span class="o">-</span><span class="n">Go</span> <span class="n">price</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>system_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The category of the system disk. System disk type. Optional values:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">cloud</span><span class="p">:</span> <span class="n">Basic</span> <span class="n">cloud</span> <span class="n">disk</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_efficiency</span><span class="p">:</span> <span class="n">Ultra</span> <span class="n">cloud</span> <span class="n">disk</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_ssd</span><span class="p">:</span> <span class="n">SSD</span> <span class="n">cloud</span> <span class="n">Disks</span><span class="o">.</span>
<span class="o">-</span> <span class="n">ephemeral_ssd</span><span class="p">:</span> <span class="n">local</span> <span class="n">SSD</span> <span class="n">Disks</span>
<span class="o">-</span> <span class="n">cloud_essd</span><span class="p">:</span> <span class="n">ESSD</span> <span class="n">cloud</span> <span class="n">Disks</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>system_disk_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – System disk description. It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>system_disk*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>System disk name. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (<a href="#id49"><span class="problematic" id="id50">*</span></a>), and hyphens (-).</p>
</p></li>
<li><p><strong>system_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the system disk, measured in GB. Value range: [20, 500].</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>userdata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User data of the instance, which is Base64-encoded. Size of the raw data cannot exceed 16 KB.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID of the instance.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The category of the disk:</p>
<ul>
<li><p>cloud: Basic cloud disk.</p></li>
<li><p>cloud_efficiency: Ultra cloud disk.</p></li>
<li><p>cloud_ssd: SSD cloud Disks.</p></li>
<li><p>ephemeral_ssd: local SSD Disks</p></li>
<li><p>cloud_essd: ESSD cloud Disks.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_with_instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Delete this data disk when the instance is destroyed. It only works on cloud, cloud_efficiency, cloud_ssd and cloud_essd disk. If the category of this data disk was ephemeral_ssd, please don’t set this param.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - -(Optional, Bool) Encrypted the data in this disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the data disk.</p>
<ul>
<li><p>cloud：[5, 2000]</p></li>
<li><p>cloud_efficiency：[20, 32768]</p></li>
<li><p>cloud_ssd：[20, 32768]</p></li>
<li><p>cloud_essd：[20, 32768]</p></li>
<li><p>ephemeral_ssd: [5, 800]</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The snapshot ID used to initialize the data disk. If the size specified by snapshot is greater that the size of the disk, use the size specified by snapshot as the size of the data disk.</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primaryIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The primary private IP address of the ENI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The security group ID must be one in the same VPC.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.auto_release_time">
<code class="sig-name descname">auto_release_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.auto_release_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance auto release time. The time is presented using the ISO8601 standard and in UTC time. The format is  YYYY-MM-DDTHH:MM:SSZ.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.data_disks">
<code class="sig-name descname">data_disks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of data disks created with instance.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The category of the disk:</p>
<ul>
<li><p>cloud: Basic cloud disk.</p></li>
<li><p>cloud_efficiency: Ultra cloud disk.</p></li>
<li><p>cloud_ssd: SSD cloud Disks.</p></li>
<li><p>ephemeral_ssd: local SSD Disks</p></li>
<li><p>cloud_essd: ESSD cloud Disks.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_with_instance</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Delete this data disk when the instance is destroyed. It only works on cloud, cloud_efficiency, cloud_ssd and cloud_essd disk. If the category of this data disk was ephemeral_ssd, please don’t set this param.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - -(Optional, Bool) Encrypted the data in this disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the data disk.</p>
<ul>
<li><p>cloud：[5, 2000]</p></li>
<li><p>cloud_efficiency：[20, 32768]</p></li>
<li><p>cloud_ssd：[20, 32768]</p></li>
<li><p>cloud_essd：[20, 32768]</p></li>
<li><p>ephemeral_ssd: [5, 800]</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The snapshot ID used to initialize the data disk. If the size specified by snapshot is greater that the size of the disk, use the size specified by snapshot as the size of the data disk.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the data disk.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.host_name">
<code class="sig-name descname">host_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance host name.It cannot start or end with a period (.) or a hyphen (-) and it cannot have two or more consecutive periods (.) or hyphens (-).For Windows: The host name can be [2, 15] characters in length. It can contain A-Z, a-z, numbers, periods (.), and hyphens (-). It cannot only contain numbers. For other operating systems: The host name can be [2, 64] characters in length. It can be segments separated by periods (.). It can contain A-Z, a-z, numbers, and hyphens (-).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Image ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Billing methods. Optional values:</p>
<ul class="simple">
<li><p>PrePaid: Monthly, or annual subscription. Make sure that your registered credit card is invalid or you have insufficient balance in your PayPal account. Otherwise, InvalidPayMethod error may occur.</p></li>
<li><p>PostPaid: Pay-As-You-Go.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.instance_name">
<code class="sig-name descname">instance_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (_), and hyphens (-).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance type. For more information, call resource_alicloud_instances to obtain the latest instance type list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.internet_charge_type">
<code class="sig-name descname">internet_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.internet_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Internet bandwidth billing method. Optional values: PayByTraffic.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.internet_max_bandwidth_in">
<code class="sig-name descname">internet_max_bandwidth_in</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.internet_max_bandwidth_in" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum inbound bandwidth from the Internet network, measured in Mbit/s. Value range: [1, 200].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.internet_max_bandwidth_out">
<code class="sig-name descname">internet_max_bandwidth_out</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.internet_max_bandwidth_out" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum outbound bandwidth from the Internet, its unit of measurement is Mbit/s. Value range: [0, 100].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.io_optimized">
<code class="sig-name descname">io_optimized</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.io_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether it is an I/O-optimized instance or not. Optional values:</p>
<ul class="simple">
<li><p>none</p></li>
<li><p>optimized</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.key_pair_name">
<code class="sig-name descname">key_pair_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.key_pair_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the key pair.</p>
<ul class="simple">
<li><p>Ignore this parameter for Windows instances. It is null by default. Even if you enter this parameter, only the  Password content is used.</p></li>
<li><p>The password logon method for Linux instances is set to forbidden upon initialization.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the data disk.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.network_interfaces">
<code class="sig-name descname">network_interfaces</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of network interfaces created with instance.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primaryIp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The primary private IP address of the ENI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The security group ID must be one in the same VPC.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.network_type">
<code class="sig-name descname">network_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.network_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Network type of the instance. Value options: Classic | VPC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.ram_role_name">
<code class="sig-name descname">ram_role_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.ram_role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The RAM role name of the instance. You can use the RAM API ListRoles to query instance RAM role names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.security_enhancement_strategy">
<code class="sig-name descname">security_enhancement_strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.security_enhancement_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to activate the security enhancement feature and install network security software free of charge. Optional values: Active | Deactive.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The security group ID must be one in the same VPC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.spot_price_limit">
<code class="sig-name descname">spot_price_limit</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.spot_price_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>-(Optional)         Sets the maximum hourly instance price. Supports up to three decimal places.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.spot_strategy">
<code class="sig-name descname">spot_strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.spot_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>The spot strategy for a Pay-As-You-Go instance. This parameter is valid and required only when InstanceChargeType is set to PostPaid. Value range:</p>
<ul class="simple">
<li><p>NoSpot: Normal Pay-As-You-Go instance.</p></li>
<li><p>SpotWithPriceLimit: Sets the maximum price for a spot instance.</p></li>
<li><p>SpotAsPriceGo: The system automatically calculates the price. The maximum value is the Pay-As-You-Go price.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.system_disk_category">
<code class="sig-name descname">system_disk_category</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.system_disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>The category of the system disk. System disk type. Optional values:</p>
<ul class="simple">
<li><p>cloud: Basic cloud disk.</p></li>
<li><p>cloud_efficiency: Ultra cloud disk.</p></li>
<li><p>cloud_ssd: SSD cloud Disks.</p></li>
<li><p>ephemeral_ssd: local SSD Disks</p></li>
<li><p>cloud_essd: ESSD cloud Disks.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.system_disk_description">
<code class="sig-name descname">system_disk_description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.system_disk_description" title="Permalink to this definition">¶</a></dt>
<dd><p>System disk description. It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.system_disk_name">
<code class="sig-name descname">system_disk_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.system_disk_name" title="Permalink to this definition">¶</a></dt>
<dd><p>System disk name. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (_), and hyphens (-).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.system_disk_size">
<code class="sig-name descname">system_disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.system_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of the system disk, measured in GB. Value range: [20, 500].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
<ul class="simple">
<li><p>Key: It can be up to 64 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It cannot be a null string.</p></li>
<li><p>Value: It can be up to 128 characters in length. It cannot begin with “aliyun”, “acs:”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It can be a null string.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.userdata">
<code class="sig-name descname">userdata</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.userdata" title="Permalink to this definition">¶</a></dt>
<dd><p>User data of the instance, which is Base64-encoded. Size of the raw data cannot exceed 16 KB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone ID of the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_release_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_owner_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_in</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_out</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">io_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_pair_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_interfaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_enhancement_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_price_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">userdata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LaunchTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_release_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance auto release time. The time is presented using the ISO8601 standard and in UTC time. The format is  YYYY-MM-DDTHH:MM:SSZ.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of data disks created with instance.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the data disk.</p></li>
<li><p><strong>host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance host name.It cannot start or end with a period (.) or a hyphen (-) and it cannot have two or more consecutive periods (.) or hyphens (-).For Windows: The host name can be [2, 15] characters in length. It can contain A-Z, a-z, numbers, periods (.), and hyphens (-). It cannot only contain numbers. For other operating systems: The host name can be [2, 64] characters in length. It can be segments separated by periods (.). It can contain A-Z, a-z, numbers, and hyphens (-).</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Image ID.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Billing methods. Optional values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">PrePaid</span><span class="p">:</span> <span class="n">Monthly</span><span class="p">,</span> <span class="ow">or</span> <span class="n">annual</span> <span class="n">subscription</span><span class="o">.</span> <span class="n">Make</span> <span class="n">sure</span> <span class="n">that</span> <span class="n">your</span> <span class="n">registered</span> <span class="n">credit</span> <span class="n">card</span> <span class="ow">is</span> <span class="n">invalid</span> <span class="ow">or</span> <span class="n">you</span> <span class="n">have</span> <span class="n">insufficient</span> <span class="n">balance</span> <span class="ow">in</span> <span class="n">your</span> <span class="n">PayPal</span> <span class="n">account</span><span class="o">.</span> <span class="n">Otherwise</span><span class="p">,</span> <span class="n">InvalidPayMethod</span> <span class="n">error</span> <span class="n">may</span> <span class="n">occur</span><span class="o">.</span>
<span class="o">-</span> <span class="n">PostPaid</span><span class="p">:</span> <span class="n">Pay</span><span class="o">-</span><span class="n">As</span><span class="o">-</span><span class="n">You</span><span class="o">-</span><span class="n">Go</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the instance. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (<a href="#id53"><span class="problematic" id="id54">*</span></a>), and hyphens (-).</p>
</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance type. For more information, call resource_alicloud_instances to obtain the latest instance type list.</p></li>
<li><p><strong>internet_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Internet bandwidth billing method. Optional values: PayByTraffic.</p></li>
<li><p><strong>internet_max_bandwidth_in</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum inbound bandwidth from the Internet network, measured in Mbit/s. Value range: [1, 200].</p></li>
<li><p><strong>internet_max_bandwidth_out</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum outbound bandwidth from the Internet, its unit of measurement is Mbit/s. Value range: [0, 100].</p></li>
<li><p><strong>io_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether it is an I/O-optimized instance or not. Optional values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">none</span>
<span class="o">-</span> <span class="n">optimized</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key_pair_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the key pair.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Ignore</span> <span class="n">this</span> <span class="n">parameter</span> <span class="k">for</span> <span class="n">Windows</span> <span class="n">instances</span><span class="o">.</span> <span class="n">It</span> <span class="ow">is</span> <span class="n">null</span> <span class="n">by</span> <span class="n">default</span><span class="o">.</span> <span class="n">Even</span> <span class="k">if</span> <span class="n">you</span> <span class="n">enter</span> <span class="n">this</span> <span class="n">parameter</span><span class="p">,</span> <span class="n">only</span> <span class="n">the</span>  <span class="n">Password</span> <span class="n">content</span> <span class="ow">is</span> <span class="n">used</span><span class="o">.</span>
<span class="o">-</span> <span class="n">The</span> <span class="n">password</span> <span class="n">logon</span> <span class="n">method</span> <span class="k">for</span> <span class="n">Linux</span> <span class="n">instances</span> <span class="ow">is</span> <span class="nb">set</span> <span class="n">to</span> <span class="n">forbidden</span> <span class="n">upon</span> <span class="n">initialization</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the data disk.</p></li>
<li><p><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The list of network interfaces created with instance.</p></li>
<li><p><strong>network_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network type of the instance. Value options: Classic | VPC.</p></li>
<li><p><strong>ram_role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RAM role name of the instance. You can use the RAM API ListRoles to query instance RAM role names.</p></li>
<li><p><strong>security_enhancement_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether or not to activate the security enhancement feature and install network security software free of charge. Optional values: Active | Deactive.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security group ID must be one in the same VPC.</p></li>
<li><p><strong>spot_price_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – -(Optional)        Sets the maximum hourly instance price. Supports up to three decimal places.</p></li>
<li><p><strong>spot_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The spot strategy for a Pay-As-You-Go instance. This parameter is valid and required only when InstanceChargeType is set to PostPaid. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">NoSpot</span><span class="p">:</span> <span class="n">Normal</span> <span class="n">Pay</span><span class="o">-</span><span class="n">As</span><span class="o">-</span><span class="n">You</span><span class="o">-</span><span class="n">Go</span> <span class="n">instance</span><span class="o">.</span>
<span class="o">-</span> <span class="n">SpotWithPriceLimit</span><span class="p">:</span> <span class="n">Sets</span> <span class="n">the</span> <span class="n">maximum</span> <span class="n">price</span> <span class="k">for</span> <span class="n">a</span> <span class="n">spot</span> <span class="n">instance</span><span class="o">.</span>
<span class="o">-</span> <span class="n">SpotAsPriceGo</span><span class="p">:</span> <span class="n">The</span> <span class="n">system</span> <span class="n">automatically</span> <span class="n">calculates</span> <span class="n">the</span> <span class="n">price</span><span class="o">.</span> <span class="n">The</span> <span class="n">maximum</span> <span class="n">value</span> <span class="ow">is</span> <span class="n">the</span> <span class="n">Pay</span><span class="o">-</span><span class="n">As</span><span class="o">-</span><span class="n">You</span><span class="o">-</span><span class="n">Go</span> <span class="n">price</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>system_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The category of the system disk. System disk type. Optional values:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">cloud</span><span class="p">:</span> <span class="n">Basic</span> <span class="n">cloud</span> <span class="n">disk</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_efficiency</span><span class="p">:</span> <span class="n">Ultra</span> <span class="n">cloud</span> <span class="n">disk</span><span class="o">.</span>
<span class="o">-</span> <span class="n">cloud_ssd</span><span class="p">:</span> <span class="n">SSD</span> <span class="n">cloud</span> <span class="n">Disks</span><span class="o">.</span>
<span class="o">-</span> <span class="n">ephemeral_ssd</span><span class="p">:</span> <span class="n">local</span> <span class="n">SSD</span> <span class="n">Disks</span>
<span class="o">-</span> <span class="n">cloud_essd</span><span class="p">:</span> <span class="n">ESSD</span> <span class="n">cloud</span> <span class="n">Disks</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>system_disk_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – System disk description. It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>system_disk*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>System disk name. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (<a href="#id57"><span class="problematic" id="id58">*</span></a>), and hyphens (-).</p>
</p></li>
<li><p><strong>system_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of the system disk, measured in GB. Value range: [20, 500].</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;acs:&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>userdata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User data of the instance, which is Base64-encoded. Size of the raw data cannot exceed 16 KB.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone ID of the instance.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The category of the disk:</p>
<ul>
<li><p>cloud: Basic cloud disk.</p></li>
<li><p>cloud_efficiency: Ultra cloud disk.</p></li>
<li><p>cloud_ssd: SSD cloud Disks.</p></li>
<li><p>ephemeral_ssd: local SSD Disks</p></li>
<li><p>cloud_essd: ESSD cloud Disks.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_with_instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Delete this data disk when the instance is destroyed. It only works on cloud, cloud_efficiency, cloud_ssd and cloud_essd disk. If the category of this data disk was ephemeral_ssd, please don’t set this param.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - -(Optional, Bool) Encrypted the data in this disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the data disk.</p>
<ul>
<li><p>cloud：[5, 2000]</p></li>
<li><p>cloud_efficiency：[20, 32768]</p></li>
<li><p>cloud_ssd：[20, 32768]</p></li>
<li><p>cloud_essd：[20, 32768]</p></li>
<li><p>ephemeral_ssd: [5, 800]</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The snapshot ID used to initialize the data disk. If the size specified by snapshot is greater that the size of the disk, use the size specified by snapshot as the size of the data disk.</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primaryIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The primary private IP address of the ENI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The security group ID must be one in the same VPC.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.LaunchTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.LaunchTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.LaunchTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.ReservedInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">ReservedInstance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_amount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offering_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Reserved Instance resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.65.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">ReservedInstance</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="s2">&quot;ecs.g6.large&quot;</span><span class="p">,</span>
    <span class="n">instance_amount</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="n">period_unit</span><span class="o">=</span><span class="s2">&quot;Year&quot;</span><span class="p">,</span>
    <span class="n">offering_type</span><span class="o">=</span><span class="s2">&quot;All Upfront&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;ReservedInstance&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;cn-shanghai-g&quot;</span><span class="p">,</span>
    <span class="n">scope</span><span class="o">=</span><span class="s2">&quot;Zone&quot;</span><span class="p">,</span>
    <span class="n">period</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the RI. 2 to 256 English or Chinese characters. It cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>instance_amount</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of instances allocated to an RI (An RI is a coupon that includes one or more allocated instances.).</p></li>
<li><p><strong>instance*type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Instance type of the RI. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25378.html">Instance type families</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RI. The name must be a string of 2 to 128 characters in length and can contain letters, numbers, colons (:), underscores (<a href="#id61"><span class="problematic" id="id62">*</span></a>), and hyphens. It must start with a letter. It cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>offering_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Payment type of the RI. Optional values: <cite>No Upfront</cite>: No upfront payment is required., <cite>Partial Upfront</cite>: A portion of upfront payment is required.<code class="docutils literal notranslate"><span class="pre">All</span> <span class="pre">Upfront</span></code>: Full upfront payment is required.</p></li>
<li><p><strong>period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Term unit. Optional value: Year.</p></li>
<li><p><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operating system type of the image used by the instance. Optional values: <code class="docutils literal notranslate"><span class="pre">Windows</span></code>, <code class="docutils literal notranslate"><span class="pre">Linux</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Linux</span></code>.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource group ID.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Scope of the RI. Optional values: <cite>Region</cite>: region-level, <cite>Zone</cite>: zone-level. Default is <code class="docutils literal notranslate"><span class="pre">Region</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the zone to which the RI belongs. When Scope is set to Zone, this parameter is required. For information about the zone list, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25610.html">DescribeZones</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ReservedInstance.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the RI. 2 to 256 English or Chinese characters. It cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ReservedInstance.instance_amount">
<code class="sig-name descname">instance_amount</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.instance_amount" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of instances allocated to an RI (An RI is a coupon that includes one or more allocated instances.).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ReservedInstance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance type of the RI. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25378.html">Instance type families</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ReservedInstance.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the RI. The name must be a string of 2 to 128 characters in length and can contain letters, numbers, colons (:), underscores (_), and hyphens. It must start with a letter. It cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ReservedInstance.offering_type">
<code class="sig-name descname">offering_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.offering_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Payment type of the RI. Optional values: <cite>No Upfront</cite>: No upfront payment is required., <cite>Partial Upfront</cite>: A portion of upfront payment is required.<code class="docutils literal notranslate"><span class="pre">All</span> <span class="pre">Upfront</span></code>: Full upfront payment is required.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ReservedInstance.period_unit">
<code class="sig-name descname">period_unit</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.period_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>Term unit. Optional value: Year.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ReservedInstance.platform">
<code class="sig-name descname">platform</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system type of the image used by the instance. Optional values: <code class="docutils literal notranslate"><span class="pre">Windows</span></code>, <code class="docutils literal notranslate"><span class="pre">Linux</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Linux</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ReservedInstance.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource group ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ReservedInstance.scope">
<code class="sig-name descname">scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Scope of the RI. Optional values: <cite>Region</cite>: region-level, <cite>Zone</cite>: zone-level. Default is <code class="docutils literal notranslate"><span class="pre">Region</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.ReservedInstance.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the zone to which the RI belongs. When Scope is set to Zone, this parameter is required. For information about the zone list, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25610.html">DescribeZones</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.ReservedInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_amount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offering_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReservedInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the RI. 2 to 256 English or Chinese characters. It cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>instance_amount</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of instances allocated to an RI (An RI is a coupon that includes one or more allocated instances.).</p></li>
<li><p><strong>instance*type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Instance type of the RI. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25378.html">Instance type families</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the RI. The name must be a string of 2 to 128 characters in length and can contain letters, numbers, colons (:), underscores (<a href="#id68"><span class="problematic" id="id69">*</span></a>), and hyphens. It must start with a letter. It cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>offering_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Payment type of the RI. Optional values: <cite>No Upfront</cite>: No upfront payment is required., <cite>Partial Upfront</cite>: A portion of upfront payment is required.<code class="docutils literal notranslate"><span class="pre">All</span> <span class="pre">Upfront</span></code>: Full upfront payment is required.</p></li>
<li><p><strong>period_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Term unit. Optional value: Year.</p></li>
<li><p><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operating system type of the image used by the instance. Optional values: <code class="docutils literal notranslate"><span class="pre">Windows</span></code>, <code class="docutils literal notranslate"><span class="pre">Linux</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">Linux</span></code>.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource group ID.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Scope of the RI. Optional values: <cite>Region</cite>: region-level, <cite>Zone</cite>: zone-level. Default is <code class="docutils literal notranslate"><span class="pre">Region</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>ID of the zone to which the RI belongs. When Scope is set to Zone, this parameter is required. For information about the zone list, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25610.html">DescribeZones</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.ReservedInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.ReservedInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.ReservedInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.SecurityGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">SecurityGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inner_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inner_access_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecurityGroup resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The security group description. Defaults to null.
:param pulumi.Input[bool] inner_access: Field ‘inner_access’ has been deprecated from provider version 1.55.3. Use ‘inner_access_policy’ replaces it.
:param pulumi.Input[str] inner_access_policy: Whether to allow both machines to access each other on all ports in the same security group. Valid values: [“Accept”, “Drop”]
:param pulumi.Input[str] name: The name of the security group. Defaults to null.
:param pulumi.Input[str] resource_group_id: The Id of resource group which the security_group belongs.
:param pulumi.Input[str] security_group_type: The type of the security group. Valid values:</p>
<blockquote>
<div><p><code class="docutils literal notranslate"><span class="pre">normal</span></code>: basic security group.
<code class="docutils literal notranslate"><span class="pre">enterprise</span></code>: advanced security group For more information.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The security group description. Defaults to null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroup.inner_access">
<code class="sig-name descname">inner_access</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.inner_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Field ‘inner_access’ has been deprecated from provider version 1.55.3. Use ‘inner_access_policy’ replaces it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroup.inner_access_policy">
<code class="sig-name descname">inner_access_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.inner_access_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to allow both machines to access each other on all ports in the same security group. Valid values: [“Accept”, “Drop”]</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the security group. Defaults to null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroup.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the security_group belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroup.security_group_type">
<code class="sig-name descname">security_group_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.security_group_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the security group. Valid values:
<code class="docutils literal notranslate"><span class="pre">normal</span></code>: basic security group.
<code class="docutils literal notranslate"><span class="pre">enterprise</span></code>: advanced security group For more information.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroup.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.SecurityGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inner_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inner_access_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security group description. Defaults to null.</p></li>
<li><p><strong>inner_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Field ‘inner_access’ has been deprecated from provider version 1.55.3. Use ‘inner_access_policy’ replaces it.</p></li>
<li><p><strong>inner_access_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether to allow both machines to access each other on all ports in the same security group. Valid values: [“Accept”, “Drop”]</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security group. Defaults to null.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the security_group belongs.</p></li>
<li><p><strong>security_group_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the security group. Valid values:
<code class="docutils literal notranslate"><span class="pre">normal</span></code>: basic security group.
<code class="docutils literal notranslate"><span class="pre">enterprise</span></code>: advanced security group For more information.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.SecurityGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.SecurityGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.SecurityGroupRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">SecurityGroupRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nic_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_range</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_group_owner_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecurityGroupRule resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cidr_ip: The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.
:param pulumi.Input[str] description: The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.
:param pulumi.Input[str] ip_protocol: The protocol. Can be <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>, <code class="docutils literal notranslate"><span class="pre">icmp</span></code>, <code class="docutils literal notranslate"><span class="pre">gre</span></code> or <code class="docutils literal notranslate"><span class="pre">all</span></code>.
:param pulumi.Input[str] nic_type: Network type, can be either <code class="docutils literal notranslate"><span class="pre">internet</span></code> or <code class="docutils literal notranslate"><span class="pre">intranet</span></code>, the default value is <code class="docutils literal notranslate"><span class="pre">internet</span></code>.
:param pulumi.Input[str] policy: Authorization policy, can be either <code class="docutils literal notranslate"><span class="pre">accept</span></code> or <code class="docutils literal notranslate"><span class="pre">drop</span></code>, the default value is <code class="docutils literal notranslate"><span class="pre">accept</span></code>.
:param pulumi.Input[str] port_range: The range of port numbers relevant to the IP protocol. Default to “-1/-1”. When the protocol is tcp or udp, each side port number range from 1 to 65535 and ‘-1/-1’ will be invalid.</p>
<blockquote>
<div><p>For example, <code class="docutils literal notranslate"><span class="pre">1/200</span></code> means that the range of the port numbers is 1-200. Other protocols’ ‘port_range’ can only be “-1/-1”, and other values will be invalid.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Authorization policy priority, with parameter values: <code class="docutils literal notranslate"><span class="pre">1-100</span></code>, default value: 1.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security group to apply this rule to.</p></li>
<li><p><strong>source_group_owner_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if <code class="docutils literal notranslate"><span class="pre">cidr_ip</span></code> has already been set.</p></li>
<li><p><strong>source_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target security group ID within the same region. If this field is specified, the <code class="docutils literal notranslate"><span class="pre">nic_type</span></code> can only select <code class="docutils literal notranslate"><span class="pre">intranet</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of rule being created. Valid options are <code class="docutils literal notranslate"><span class="pre">ingress</span></code> (inbound) or <code class="docutils literal notranslate"><span class="pre">egress</span></code> (outbound).</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.cidr_ip">
<code class="sig-name descname">cidr_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.cidr_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.ip_protocol">
<code class="sig-name descname">ip_protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.ip_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol. Can be <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>, <code class="docutils literal notranslate"><span class="pre">icmp</span></code>, <code class="docutils literal notranslate"><span class="pre">gre</span></code> or <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.nic_type">
<code class="sig-name descname">nic_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.nic_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Network type, can be either <code class="docutils literal notranslate"><span class="pre">internet</span></code> or <code class="docutils literal notranslate"><span class="pre">intranet</span></code>, the default value is <code class="docutils literal notranslate"><span class="pre">internet</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Authorization policy, can be either <code class="docutils literal notranslate"><span class="pre">accept</span></code> or <code class="docutils literal notranslate"><span class="pre">drop</span></code>, the default value is <code class="docutils literal notranslate"><span class="pre">accept</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.port_range">
<code class="sig-name descname">port_range</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>The range of port numbers relevant to the IP protocol. Default to “-1/-1”. When the protocol is tcp or udp, each side port number range from 1 to 65535 and ‘-1/-1’ will be invalid.
For example, <code class="docutils literal notranslate"><span class="pre">1/200</span></code> means that the range of the port numbers is 1-200. Other protocols’ ‘port_range’ can only be “-1/-1”, and other values will be invalid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Authorization policy priority, with parameter values: <code class="docutils literal notranslate"><span class="pre">1-100</span></code>, default value: 1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The security group to apply this rule to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.source_group_owner_account">
<code class="sig-name descname">source_group_owner_account</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.source_group_owner_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if <code class="docutils literal notranslate"><span class="pre">cidr_ip</span></code> has already been set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.source_security_group_id">
<code class="sig-name descname">source_security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.source_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The target security group ID within the same region. If this field is specified, the <code class="docutils literal notranslate"><span class="pre">nic_type</span></code> can only select <code class="docutils literal notranslate"><span class="pre">intranet</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of rule being created. Valid options are <code class="docutils literal notranslate"><span class="pre">ingress</span></code> (inbound) or <code class="docutils literal notranslate"><span class="pre">egress</span></code> (outbound).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nic_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_range</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_group_owner_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityGroupRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.</p></li>
<li><p><strong>ip_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol. Can be <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>, <code class="docutils literal notranslate"><span class="pre">icmp</span></code>, <code class="docutils literal notranslate"><span class="pre">gre</span></code> or <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>nic_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network type, can be either <code class="docutils literal notranslate"><span class="pre">internet</span></code> or <code class="docutils literal notranslate"><span class="pre">intranet</span></code>, the default value is <code class="docutils literal notranslate"><span class="pre">internet</span></code>.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authorization policy, can be either <code class="docutils literal notranslate"><span class="pre">accept</span></code> or <code class="docutils literal notranslate"><span class="pre">drop</span></code>, the default value is <code class="docutils literal notranslate"><span class="pre">accept</span></code>.</p></li>
<li><p><strong>port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The range of port numbers relevant to the IP protocol. Default to “-1/-1”. When the protocol is tcp or udp, each side port number range from 1 to 65535 and ‘-1/-1’ will be invalid.
For example, <code class="docutils literal notranslate"><span class="pre">1/200</span></code> means that the range of the port numbers is 1-200. Other protocols’ ‘port_range’ can only be “-1/-1”, and other values will be invalid.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Authorization policy priority, with parameter values: <code class="docutils literal notranslate"><span class="pre">1-100</span></code>, default value: 1.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security group to apply this rule to.</p></li>
<li><p><strong>source_group_owner_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if <code class="docutils literal notranslate"><span class="pre">cidr_ip</span></code> has already been set.</p></li>
<li><p><strong>source_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target security group ID within the same region. If this field is specified, the <code class="docutils literal notranslate"><span class="pre">nic_type</span></code> can only select <code class="docutils literal notranslate"><span class="pre">intranet</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of rule being created. Valid options are <code class="docutils literal notranslate"><span class="pre">ingress</span></code> (inbound) or <code class="docutils literal notranslate"><span class="pre">egress</span></code> (outbound).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.SecurityGroupRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SecurityGroupRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.Snapshot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">Snapshot</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ECS snapshot resource.</p>
<p>For information about snapshot and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25460.html">Snapshot</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">snapshot</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">Snapshot</span><span class="p">(</span><span class="s2">&quot;snapshot&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;this snapshot is created for testing&quot;</span><span class="p">,</span>
    <span class="n">disk_id</span><span class="o">=</span><span class="n">alicloud_disk_attachment</span><span class="p">[</span><span class="s2">&quot;instance-attachment&quot;</span><span class="p">][</span><span class="s2">&quot;disk_id&quot;</span><span class="p">],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;version&quot;</span><span class="p">:</span> <span class="s2">&quot;1.2&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the snapshot. This description can have a string of 2 to 256 characters, It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p></li>
<li><p><strong>disk*id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The source disk ID.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the snapshot. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as “-“, “.”, “<a href="#id73"><span class="problematic" id="id74">*</span></a>”, and must not begin or end with a hyphen, and must not begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Snapshot.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Snapshot.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the snapshot. This description can have a string of 2 to 256 characters, It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Snapshot.disk_id">
<code class="sig-name descname">disk_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Snapshot.disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The source disk ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Snapshot.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Snapshot.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the snapshot. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as “-“, “.”, “_”, and must not begin or end with a hyphen, and must not begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.Snapshot.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.Snapshot.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.Snapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Snapshot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Snapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the snapshot. This description can have a string of 2 to 256 characters, It cannot begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p></li>
<li><p><strong>disk*id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The source disk ID.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the snapshot. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as “-“, “.”, “<a href="#id77"><span class="problematic" id="id78">*</span></a>”, and must not begin or end with a hyphen, and must not begin with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. Default value is null.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.Snapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Snapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.Snapshot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.Snapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.SnapshotPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">SnapshotPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repeat_weekdays</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_points</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SnapshotPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ECS snapshot policy resource.</p>
<p>For information about snapshot policy and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25460.html">Snapshot</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.42.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">sp</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">SnapshotPolicy</span><span class="p">(</span><span class="s2">&quot;sp&quot;</span><span class="p">,</span>
    <span class="n">repeat_weekdays</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;2&quot;</span><span class="p">,</span>
        <span class="s2">&quot;3&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">retention_days</span><span class="o">=-</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">time_points</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;22&quot;</span><span class="p">,</span>
        <span class="s2">&quot;23&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The snapshot policy name.</p></li>
<li><p><strong>repeat_weekdays</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- A maximum of seven time points can be selected.
- The format is  an JSON array of [&quot;1&quot;, &quot;2&quot;, … &quot;7&quot;]  and the time points are separated by commas (,).
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The snapshot retention time, and the unit of measurement is day. Optional values:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span> <span class="n">The</span> <span class="n">automatic</span> <span class="n">snapshots</span> <span class="n">are</span> <span class="n">retained</span> <span class="n">permanently</span><span class="o">.</span>
<span class="o">-</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">65536</span><span class="p">]:</span> <span class="n">The</span> <span class="n">number</span> <span class="n">of</span> <span class="n">days</span> <span class="n">retained</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>time_points</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- A maximum of 24 time points can be selected.
- The format is  an JSON array of [&quot;0&quot;, &quot;1&quot;, … &quot;23&quot;] and the time points are separated by commas (,).
</pre></div>
</div>
<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SnapshotPolicy.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SnapshotPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot policy name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SnapshotPolicy.repeat_weekdays">
<code class="sig-name descname">repeat_weekdays</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SnapshotPolicy.repeat_weekdays" title="Permalink to this definition">¶</a></dt>
<dd><p>The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.</p>
<ul class="simple">
<li><p>A maximum of seven time points can be selected.</p></li>
<li><p>The format is  an JSON array of [“1”, “2”, … “7”]  and the time points are separated by commas (,).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SnapshotPolicy.retention_days">
<code class="sig-name descname">retention_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SnapshotPolicy.retention_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The snapshot retention time, and the unit of measurement is day. Optional values:</p>
<ul class="simple">
<li><p>-1: The automatic snapshots are retained permanently.</p></li>
<li><p>[1, 65536]: The number of days retained.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ecs.SnapshotPolicy.time_points">
<code class="sig-name descname">time_points</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ecs.SnapshotPolicy.time_points" title="Permalink to this definition">¶</a></dt>
<dd><p>The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.</p>
<ul class="simple">
<li><p>A maximum of 24 time points can be selected.</p></li>
<li><p>The format is  an JSON array of [“0”, “1”, … “23”] and the time points are separated by commas (,).</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.SnapshotPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repeat_weekdays</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_points</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SnapshotPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SnapshotPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The snapshot policy name.</p></li>
<li><p><strong>repeat_weekdays</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- A maximum of seven time points can be selected.
- The format is  an JSON array of [&quot;1&quot;, &quot;2&quot;, … &quot;7&quot;]  and the time points are separated by commas (,).
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The snapshot retention time, and the unit of measurement is day. Optional values:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span> <span class="n">The</span> <span class="n">automatic</span> <span class="n">snapshots</span> <span class="n">are</span> <span class="n">retained</span> <span class="n">permanently</span><span class="o">.</span>
<span class="o">-</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">65536</span><span class="p">]:</span> <span class="n">The</span> <span class="n">number</span> <span class="n">of</span> <span class="n">days</span> <span class="n">retained</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>time_points</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- A maximum of 24 time points can be selected.
- The format is  an JSON array of [&quot;0&quot;, &quot;1&quot;, … &quot;23&quot;] and the time points are separated by commas (,).
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ecs.SnapshotPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SnapshotPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.SnapshotPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.SnapshotPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ecs.get_disks">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_disks</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the disks of the current Alibaba Cloud user.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">disks_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_disks</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;sample_disk&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstDiskId&quot;</span><span class="p">,</span> <span class="n">disks_ds</span><span class="o">.</span><span class="n">disks</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>category</strong> (<em>str</em>) – Disk category. Possible values: <code class="docutils literal notranslate"><span class="pre">cloud</span></code> (basic cloud disk), <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code> (ultra cloud disk), <code class="docutils literal notranslate"><span class="pre">ephemeral_ssd</span></code> (local SSD cloud disk), <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code> (SSD cloud disk), and <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code> (ESSD cloud disk).</p></li>
<li><p><strong>encrypted</strong> (<em>str</em>) – Indicate whether the disk is encrypted or not. Possible values: <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of disks IDs.</p></li>
<li><p><strong>instance_id</strong> (<em>str</em>) – Filter the results by the specified ECS instance ID.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by disk name.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group which the disk belongs.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags assigned to the disks. It must be in the format:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```
data &quot;ecs.getDisks&quot; &quot;disks_ds&quot; {
tags = {
tagKey1 = &quot;tagValue1&quot;,
tagKey2 = &quot;tagValue2&quot;
}
}
```
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>type</strong> (<em>str</em>) – Disk type. Possible values: <code class="docutils literal notranslate"><span class="pre">system</span></code> and <code class="docutils literal notranslate"><span class="pre">data</span></code>.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ecs.get_eips">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_eips</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">in_use</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_eips" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of EIPs (Elastic IP address) owned by an Alibaba Cloud account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">eips_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_eips</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstEipId&quot;</span><span class="p">,</span> <span class="n">eips_ds</span><span class="o">.</span><span class="n">eips</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of EIP IDs.</p></li>
<li><p><strong>in_use</strong> (<em>bool</em>) – Deprecated since the version 1.8.0 of this provider.</p></li>
<li><p><strong>ip_addresses</strong> (<em>list</em>) – A list of EIP public IP addresses.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group which the eips belongs.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ecs.get_images">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_images</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">most_recent</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owners</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_images" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides available image resources. It contains user’s private images, system images provided by Alibaba Cloud, 
other public images and the ones available on the image market.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">images_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_images</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;^centos_6&quot;</span><span class="p">,</span>
    <span class="n">owners</span><span class="o">=</span><span class="s2">&quot;system&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstImageId&quot;</span><span class="p">,</span> <span class="n">images_ds</span><span class="o">.</span><span class="n">images</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>most_recent</strong> (<em>bool</em>) – If more than one result are returned, select the most recent one.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter resulting images by name.</p></li>
<li><p><strong>owners</strong> (<em>str</em>) – Filter results by a specific image owner. Valid items are <code class="docutils literal notranslate"><span class="pre">system</span></code>, <code class="docutils literal notranslate"><span class="pre">self</span></code>, <code class="docutils literal notranslate"><span class="pre">others</span></code>, <code class="docutils literal notranslate"><span class="pre">marketplace</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ecs.get_instance_type_families">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_instance_type_families</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">generation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_instance_type_families" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the ECS instance type families of Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.54.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>generation</strong> (<em>str</em>) – <p>The generation of the instance type family, Valid values: <code class="docutils literal notranslate"><span class="pre">ecs-1</span></code>, <code class="docutils literal notranslate"><span class="pre">ecs-2</span></code>, <code class="docutils literal notranslate"><span class="pre">ecs-3</span></code> and <code class="docutils literal notranslate"><span class="pre">ecs-4</span></code>. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25378.htm">Instance type families</a>.</p>
</p></li>
<li><p><strong>instance_charge_type</strong> (<em>str</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>spot_strategy</strong> (<em>str</em>) – Filter the results by ECS spot type. Valid values: <code class="docutils literal notranslate"><span class="pre">NoSpot</span></code>, <code class="docutils literal notranslate"><span class="pre">SpotWithPriceLimit</span></code> and <code class="docutils literal notranslate"><span class="pre">SpotAsPriceGo</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">NoSpot</span></code>.</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The Zone to launch the instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ecs.get_instance_types">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_instance_types</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_core_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eni_amount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpu_amount</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpu_spec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_node_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memory_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorted_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the ECS instance types of Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> By default, only the upgraded instance types are returned. If you want to get outdated instance types, you must set <code class="docutils literal notranslate"><span class="pre">is_outdated</span></code> to true.</p>
<p><strong>NOTE:</strong> If one instance type is sold out, it will not be exported.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">types_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_instance_types</span><span class="p">(</span><span class="n">cpu_core_count</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">memory_size</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<span class="n">instance</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;instance&quot;</span><span class="p">,</span> <span class="n">instance_type</span><span class="o">=</span><span class="n">types_ds</span><span class="o">.</span><span class="n">instance_types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>availability_zone</strong> (<em>str</em>) – The zone where instance types are supported.</p></li>
<li><p><strong>cpu_core_count</strong> (<em>float</em>) – Filter the results to a specific number of cpu cores.</p></li>
<li><p><strong>eni_amount</strong> (<em>float</em>) – Filter the result whose network interface number is no more than <code class="docutils literal notranslate"><span class="pre">eni_amount</span></code>.</p></li>
<li><p><strong>gpu_amount</strong> (<em>float</em>) – The GPU amount of an instance type.</p></li>
<li><p><strong>gpu_spec</strong> (<em>str</em>) – The GPU spec of an instance type.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>str</em>) – Filter the results by charge type. Valid values: <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> and <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>instance_type_family</strong> (<em>str</em>) – Filter the results based on their family name. For example: ‘ecs.n4’.</p></li>
<li><p><strong>is_outdated</strong> (<em>bool</em>) – If true, outdated instance types are included in the results. Default to false.</p></li>
<li><p><strong>memory_size</strong> (<em>float</em>) – Filter the results to a specific memory size in GB.</p></li>
<li><p><strong>network_type</strong> (<em>str</em>) – Filter the results by network type. Valid values: <code class="docutils literal notranslate"><span class="pre">Classic</span></code> and <code class="docutils literal notranslate"><span class="pre">Vpc</span></code>.</p></li>
<li><p><strong>spot_strategy</strong> (<em>str</em>) – Filter the results by ECS spot type. Valid values: <code class="docutils literal notranslate"><span class="pre">NoSpot</span></code>, <code class="docutils literal notranslate"><span class="pre">SpotWithPriceLimit</span></code> and <code class="docutils literal notranslate"><span class="pre">SpotAsPriceGo</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">NoSpot</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ecs.get_instances">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>The Instances data source list ECS instance resources according to their ID, name regex, image id, status and other fields.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">instances_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_instances</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;web_server&quot;</span><span class="p">,</span>
    <span class="n">status</span><span class="o">=</span><span class="s2">&quot;Running&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstInstanceId&quot;</span><span class="p">,</span> <span class="n">instances_ds</span><span class="o">.</span><span class="n">instances</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;instanceIds&quot;</span><span class="p">,</span> <span class="n">instances_ds</span><span class="o">.</span><span class="n">ids</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>availability_zone</strong> (<em>str</em>) – Availability zone where instances are located.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of ECS instance IDs.</p></li>
<li><p><strong>image_id</strong> (<em>str</em>) – The image ID of some ECS instance used.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by instance name.</p></li>
<li><p><strong>ram_role_name</strong> (<em>str</em>) – The RAM role name which the instance attaches.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group which the instance belongs.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – Instance status. Valid values: “Creating”, “Starting”, “Running”, “Stopping” and “Stopped”. If undefined, all statuses are considered.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags assigned to the ECS instances. It must be in the format:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```
data &quot;ecs.getInstances&quot; &quot;taggedInstances&quot; {
tags = {
tagKey1 = &quot;tagValue1&quot;,
tagKey2 = &quot;tagValue2&quot;
}
}
```
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vpc_id</strong> (<em>str</em>) – ID of the VPC linked to the instances.</p></li>
<li><p><strong>vswitch_id</strong> (<em>str</em>) – ID of the VSwitch linked to the instances.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ecs.get_key_pairs">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_key_pairs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">finger_print</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_key_pairs" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of key pairs in an Alibaba Cloud account according to the specified filters.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="c1"># Declare the data source</span>
<span class="n">default_key_pair</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">KeyPair</span><span class="p">(</span><span class="s2">&quot;defaultKeyPair&quot;</span><span class="p">,</span> <span class="n">key_name</span><span class="o">=</span><span class="s2">&quot;keyPairDatasource&quot;</span><span class="p">)</span>
<span class="n">default_key_pairs</span> <span class="o">=</span> <span class="n">default_key_pair</span><span class="o">.</span><span class="n">key_name</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">key_name</span><span class="p">:</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_key_pairs</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="n">key_name</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>finger_print</strong> (<em>bool</em>) – A finger print used to retrieve specified key pair.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of key pair IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to apply to the resulting key pairs.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group which the key pair belongs.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ecs.get_network_interfaces">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_network_interfaces</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of elastic network interfaces according to the specified filters in an Alibaba Cloud account.</p>
<p>For information about elastic network interface and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/58496.html">Elastic Network Interface</a></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">name</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;networkInterfacesName&quot;</span>
<span class="n">vpc</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;vpc&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;192.168.0.0/24&quot;</span><span class="p">)</span>
<span class="n">default_zones</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="n">available_resource_creation</span><span class="o">=</span><span class="s2">&quot;VSwitch&quot;</span><span class="p">)</span>
<span class="n">vswitch</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Switch</span><span class="p">(</span><span class="s2">&quot;vswitch&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="n">default_zones</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;192.168.0.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="s2">&quot;group&quot;</span><span class="p">,</span> <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">interface</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">NetworkInterface</span><span class="p">(</span><span class="s2">&quot;interface&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Basic test&quot;</span><span class="p">,</span>
    <span class="n">private_ip</span><span class="o">=</span><span class="s2">&quot;192.168.0.2&quot;</span><span class="p">,</span>
    <span class="n">security_groups</span><span class="o">=</span><span class="p">[</span><span class="n">group</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;TF-VER&quot;</span><span class="p">:</span> <span class="s2">&quot;0.11.3&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">vswitch_id</span><span class="o">=</span><span class="n">vswitch</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">instance</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;instance&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="n">default_zones</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">image_id</span><span class="o">=</span><span class="s2">&quot;centos_7_04_64_20G_alibase_201701015.vhd&quot;</span><span class="p">,</span>
    <span class="n">instance_name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="s2">&quot;ecs.e3.xlarge&quot;</span><span class="p">,</span>
    <span class="n">internet_max_bandwidth_out</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
    <span class="n">security_groups</span><span class="o">=</span><span class="p">[</span><span class="n">group</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">system_disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_efficiency&quot;</span><span class="p">,</span>
    <span class="n">vswitch_id</span><span class="o">=</span><span class="n">vswitch</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">attachment</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">NetworkInterfaceAttachment</span><span class="p">(</span><span class="s2">&quot;attachment&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">instance</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">network_interface_id</span><span class="o">=</span><span class="n">interface</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_network_interfaces</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">attachment</span><span class="o">.</span><span class="n">network_interface_id</span><span class="p">,</span> <span class="n">instance</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="n">group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="n">vpc</span><span class="o">.</span><span class="n">id</span><span class="p">,</span> <span class="n">vswitch</span><span class="o">.</span><span class="n">id</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">network_interface_id</span><span class="p">,</span> <span class="n">instanceId</span><span class="p">,</span> <span class="n">groupId</span><span class="p">,</span> <span class="n">vpcId</span><span class="p">,</span> <span class="n">vswitchId</span><span class="p">:</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_network_interfaces</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="n">network_interface_id</span><span class="p">],</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">instance_id</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;tf-testAccNetworkInterfacesBasic</span><span class="si">%d</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="n">private_ip</span><span class="o">=</span><span class="s2">&quot;192.168.0.2&quot;</span><span class="p">,</span>
    <span class="n">security_group_id</span><span class="o">=</span><span class="n">group_id</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;TF-VER&quot;</span><span class="p">:</span> <span class="s2">&quot;0.11.3&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;Secondary&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc_id</span><span class="p">,</span>
    <span class="n">vswitch_id</span><span class="o">=</span><span class="n">vswitch_id</span><span class="p">))</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;eni0Name&quot;</span><span class="p">,</span> <span class="n">default_network_interfaces</span><span class="o">.</span><span class="n">interfaces</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ids</span></code> - (Optional)  A list of ENI IDs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name_regex</span></code> - (Optional) A regex string to filter results by ENI name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> - (Optional) The VPC ID linked to ENIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> - (Optional) The VSwitch ID linked to ENIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip</span></code> - (Optional) The primary private IP address of the ENI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_id</span></code> - (Optional) The security group ID linked to ENIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Optional) The name of the ENIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Optional) The type of ENIs, Only support for “Primary” or “Secondary”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> - (Optional) The ECS instance ID that the ENI is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> - (Optional) A map of tags assigned to ENIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">output_file</span></code> - (Optional) The name of output file that saves the filter results.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_id</span></code> - (Optional, ForceNew, Available in 1.57.0+) The Id of resource group which the network interface belongs.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance_id</strong> (<em>str</em>) – ID of the instance that the ENI is attached to.</p></li>
<li><p><strong>private_ip</strong> (<em>str</em>) – Primary private IP of the ENI.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags assigned to the ENI.</p></li>
<li><p><strong>vpc_id</strong> (<em>str</em>) – ID of the VPC that the ENI belongs to.</p></li>
<li><p><strong>vswitch_id</strong> (<em>str</em>) – ID of the VSwitch that the ENI is linked to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ecs.get_security_group_rules">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_security_group_rules</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">direction</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nic_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_security_group_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">ecs.getSecurityGroupRules</span></code> data source provides a collection of security permissions of a specific security group.
Each collection item represents a single <code class="docutils literal notranslate"><span class="pre">ingress</span></code> or <code class="docutils literal notranslate"><span class="pre">egress</span></code> permission rule.
The ID of the security group can be provided via a variable or the result from the other data source <code class="docutils literal notranslate"><span class="pre">ecs.getSecurityGroups</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">security_group_id</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">require_object</span><span class="p">(</span><span class="s2">&quot;securityGroupId&quot;</span><span class="p">)</span>
<span class="n">groups_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_security_groups</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;api&quot;</span><span class="p">)</span>
<span class="n">ingress_rules_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_security_group_rules</span><span class="p">(</span><span class="n">direction</span><span class="o">=</span><span class="s2">&quot;ingress&quot;</span><span class="p">,</span>
    <span class="n">group_id</span><span class="o">=</span><span class="n">groups_ds</span><span class="o">.</span><span class="n">groups</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">ip_protocol</span><span class="o">=</span><span class="s2">&quot;TCP&quot;</span><span class="p">,</span>
    <span class="n">nic_type</span><span class="o">=</span><span class="s2">&quot;internet&quot;</span><span class="p">)</span>
<span class="c1"># Pass port_range to the backend service</span>
<span class="n">backend</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;backend&quot;</span><span class="p">,</span> <span class="n">user_data</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;config_service.sh --portrange=</span><span class="si">{</span><span class="n">ingress_rules_ds</span><span class="o">.</span><span class="n">rules</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s1">&#39;port_range&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>direction</strong> (<em>str</em>) – Authorization direction. Valid values are: <code class="docutils literal notranslate"><span class="pre">ingress</span></code> or <code class="docutils literal notranslate"><span class="pre">egress</span></code>.</p></li>
<li><p><strong>group_id</strong> (<em>str</em>) – The ID of the security group that owns the rules.</p></li>
<li><p><strong>ip_protocol</strong> (<em>str</em>) – The IP protocol. Valid values are: <code class="docutils literal notranslate"><span class="pre">tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">udp</span></code>, <code class="docutils literal notranslate"><span class="pre">icmp</span></code>, <code class="docutils literal notranslate"><span class="pre">gre</span></code> and <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>nic_type</strong> (<em>str</em>) – Refers to the network type. Can be either <code class="docutils literal notranslate"><span class="pre">internet</span></code> or <code class="docutils literal notranslate"><span class="pre">intranet</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">internet</span></code>.</p></li>
<li><p><strong>policy</strong> (<em>str</em>) – Authorization policy. Can be either <code class="docutils literal notranslate"><span class="pre">accept</span></code> or <code class="docutils literal notranslate"><span class="pre">drop</span></code>. The default value is <code class="docutils literal notranslate"><span class="pre">accept</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ecs.get_security_groups">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_security_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of Security Groups in an Alibaba Cloud account according to the specified filters.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">sec_groups_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_security_groups</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;^web-&quot;</span><span class="p">,</span>
    <span class="n">output_file</span><span class="o">=</span><span class="s2">&quot;web_access.json&quot;</span><span class="p">)</span>
<span class="c1"># In conjunction with a VPC</span>
<span class="n">primary_vpc_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;primaryVpcDs&quot;</span><span class="p">)</span>
<span class="n">primary_sec_groups_ds</span> <span class="o">=</span> <span class="n">primary_vpc_ds</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_security_groups</span><span class="p">(</span><span class="n">vpc_id</span><span class="o">=</span><span class="nb">id</span><span class="p">))</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstGroupId&quot;</span><span class="p">,</span> <span class="n">primary_sec_groups_ds</span><span class="o">.</span><span class="n">groups</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of Security Group IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter the resulting security groups by their names.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group which the security_group belongs.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags assigned to the ECS instances. It must be in the format:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```
data &quot;ecs.getSecurityGroups&quot; &quot;taggedSecurityGroups&quot; {
tags = {
tagKey1 = &quot;tagValue1&quot;,
tagKey2 = &quot;tagValue2&quot;
}
}
```
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>vpc_id</strong> (<em>str</em>) – Used to retrieve security groups that belong to the specified VPC ID.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ecs.get_snapshots">
<code class="sig-prename descclassname">pulumi_alicloud.ecs.</code><code class="sig-name descname">get_snapshots</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">disk_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_disk_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ecs.get_snapshots" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of snapshot according to the specified filters in an Alibaba Cloud account.</p>
<p>For information about snapshot and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/25460.html">Snapshot</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.40.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">snapshots</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_snapshots</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;s-123456890abcdef&quot;</span><span class="p">],</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;tf-testAcc-snapshot&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> - (Optional) The specified instance ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_id</span></code> - (Optional) The specified disk ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> - (Optional) Queries the encrypted snapshots. Optional values:</p>
<ul class="simple">
<li><p>true: Encrypted snapshots.</p></li>
<li><p>false: No encryption attribute limit.</p></li>
</ul>
<p>Default value: false.</p>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ids</span></code> - (Optional)  A list of snapshot IDs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name_regex</span></code> - (Optional) A regex string to filter results by snapshot name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> - (Optional) The specified snapshot status.</p>
<ul class="simple">
<li><p>The snapshot status. Optional values:</p></li>
<li><p>progressing: The snapshots are being created.</p></li>
<li><p>accomplished: The snapshots are ready to use.</p></li>
<li><p>failed: The snapshot creation failed.</p></li>
<li><p>all: All status.</p></li>
</ul>
<p>Default value: all.</p>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Optional) The snapshot category. Optional values:</p>
<ul class="simple">
<li><p>auto: Auto snapshots.</p></li>
<li><p>user: Manual snapshots.</p></li>
<li><p>all: Auto and manual snapshots.</p></li>
</ul>
<p>Default value: all.</p>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_disk_type</span></code> - (Optional) The type of source disk:</p>
<ul class="simple">
<li><p>System: The snapshots are created for system disks.</p></li>
<li><p>Data: The snapshots are created for data disks.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> - (Optional) The usage of the snapshot:</p>
<ul class="simple">
<li><p>image: The snapshots are used to create custom images.</p></li>
<li><p>disk: The snapshots are used to CreateDisk.</p></li>
<li><p>mage_disk: The snapshots are used to create custom images and data disks.</p></li>
<li><p>none: The snapshots are not used yet.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> - (Optional) A map of tags assigned to snapshots.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">output_file</span></code> - (Optional) The name of output file that saves the filter results.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>encrypted</strong> (<em>bool</em>) – Whether the snapshot is encrypted or not.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of snapshot IDs.</p></li>
<li><p><strong>source_disk_type</strong> (<em>str</em>) – Source disk attribute. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">System</span>
<span class="o">*</span> <span class="n">Data</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>status</strong> (<em>str</em>) – The snapshot status. Value range:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">progressing</span>
<span class="o">*</span> <span class="n">accomplished</span>
<span class="o">*</span> <span class="n">failed</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags assigned to the snapshot.</p></li>
<li><p><strong>usage</strong> (<em>str</em>) – Whether the snapshots are used to create resources or not. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">image</span>
<span class="o">*</span> <span class="n">disk</span>
<span class="o">*</span> <span class="n">image_disk</span>
<span class="o">*</span> <span class="n">none</span>
</pre></div>
</div>
</dd></dl>

</div>
