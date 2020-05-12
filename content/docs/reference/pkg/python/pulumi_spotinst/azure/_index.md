---
title: Module azure
title_tag: Module azure | Package pulumi_spotinst | Python SDK
linktitle: azure
notitle: true
---

<div class="section" id="azure">
<h1>azure<a class="headerlink" href="#azure" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-spotinst/issues">pulumi/pulumi-spotinst repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/issues">terraform-providers/terraform-provider-spotinst repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_spotinst.azure"></span><dl class="py class">
<dt id="pulumi_spotinst.azure.Elastigroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.azure.</code><code class="sig-name descname">Elastigroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_kubernetes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_multai_runtime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">low_priority_sizes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_service_identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">od_sizes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shutdown_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst elastigroup Azure resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">test_azure_group</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">azure</span><span class="o">.</span><span class="n">Elastigroup</span><span class="p">(</span><span class="s2">&quot;testAzureGroup&quot;</span><span class="p">,</span>
    <span class="n">desired_capacity</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">health_check</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;autoHealing&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;gracePeriod&quot;</span><span class="p">:</span> <span class="mi">120</span><span class="p">,</span>
        <span class="s2">&quot;healthCheckType&quot;</span><span class="p">:</span> <span class="s2">&quot;INSTANCE_STATE&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">images</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;marketplace&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;offer&quot;</span><span class="p">:</span> <span class="s2">&quot;UbuntuServer&quot;</span><span class="p">,</span>
            <span class="s2">&quot;publisher&quot;</span><span class="p">:</span> <span class="s2">&quot;Canonical&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sku&quot;</span><span class="p">:</span> <span class="s2">&quot;16.04-LTS&quot;</span><span class="p">,</span>
        <span class="p">}],</span>
    <span class="p">}],</span>
    <span class="n">load_balancers</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;autoWeight&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;balancerId&quot;</span><span class="p">:</span> <span class="s2">&quot;lb-1ee2e3q&quot;</span><span class="p">,</span>
        <span class="s2">&quot;targetSetId&quot;</span><span class="p">:</span> <span class="s2">&quot;ts-3eq&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;MULTAI_TARGET_SET&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">login</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;sshPublicKey&quot;</span><span class="p">:</span> <span class="s2">&quot;33a2s1f3g5a1df5g1ad3f2g1adfg56dfg==&quot;</span><span class="p">,</span>
        <span class="s2">&quot;userName&quot;</span><span class="p">:</span> <span class="s2">&quot;admin&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">low_priority_sizes</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;standard_a1_v1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;standard_a1_v2&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">managed_service_identities</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;example-identity&quot;</span><span class="p">,</span>
        <span class="s2">&quot;resourceGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;spotinst-azure&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">max_size</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">min_size</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">network</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;assignPublicIp&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;resourceGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;subnetResourceGroup&quot;</span><span class="p">,</span>
        <span class="s2">&quot;subnetName&quot;</span><span class="p">:</span> <span class="s2">&quot;my-subnet-name&quot;</span><span class="p">,</span>
        <span class="s2">&quot;virtualNetworkName&quot;</span><span class="p">:</span> <span class="s2">&quot;vname&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">od_sizes</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;standard_a1_v1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;standard_a1_v2&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">product</span><span class="o">=</span><span class="s2">&quot;Linux&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;eastus&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;spotinst-azure&quot;</span><span class="p">,</span>
    <span class="n">scaling_down_policies</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;actionType&quot;</span><span class="p">:</span> <span class="s2">&quot;adjustment&quot;</span><span class="p">,</span>
        <span class="s2">&quot;adjustment&quot;</span><span class="p">:</span> <span class="s2">&quot;MIN(5,10)&quot;</span><span class="p">,</span>
        <span class="s2">&quot;cooldown&quot;</span><span class="p">:</span> <span class="mi">60</span><span class="p">,</span>
        <span class="s2">&quot;dimensions&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;name-1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;value-1&quot;</span><span class="p">,</span>
        <span class="p">}],</span>
        <span class="s2">&quot;evaluationPeriods&quot;</span><span class="p">:</span> <span class="s2">&quot;10&quot;</span><span class="p">,</span>
        <span class="s2">&quot;metricName&quot;</span><span class="p">:</span> <span class="s2">&quot;CPUUtilization&quot;</span><span class="p">,</span>
        <span class="s2">&quot;namespace&quot;</span><span class="p">:</span> <span class="s2">&quot;Microsoft.Compute&quot;</span><span class="p">,</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;gt&quot;</span><span class="p">,</span>
        <span class="s2">&quot;period&quot;</span><span class="p">:</span> <span class="s2">&quot;60&quot;</span><span class="p">,</span>
        <span class="s2">&quot;policyName&quot;</span><span class="p">:</span> <span class="s2">&quot;policy-name&quot;</span><span class="p">,</span>
        <span class="s2">&quot;statistic&quot;</span><span class="p">:</span> <span class="s2">&quot;average&quot;</span><span class="p">,</span>
        <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
        <span class="s2">&quot;unit&quot;</span><span class="p">:</span> <span class="s2">&quot;percent&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">scaling_up_policies</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;actionType&quot;</span><span class="p">:</span> <span class="s2">&quot;setMinTarget&quot;</span><span class="p">,</span>
        <span class="s2">&quot;cooldown&quot;</span><span class="p">:</span> <span class="mi">60</span><span class="p">,</span>
        <span class="s2">&quot;dimensions&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;resourceName&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;resource-name&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="p">{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;resourceGroupName&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;resource-group-name&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">],</span>
        <span class="s2">&quot;evaluationPeriods&quot;</span><span class="p">:</span> <span class="s2">&quot;10&quot;</span><span class="p">,</span>
        <span class="s2">&quot;metricName&quot;</span><span class="p">:</span> <span class="s2">&quot;CPUUtilization&quot;</span><span class="p">,</span>
        <span class="s2">&quot;minTargetCapacity&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="s2">&quot;namespace&quot;</span><span class="p">:</span> <span class="s2">&quot;Microsoft.Compute&quot;</span><span class="p">,</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;gt&quot;</span><span class="p">,</span>
        <span class="s2">&quot;period&quot;</span><span class="p">:</span> <span class="s2">&quot;60&quot;</span><span class="p">,</span>
        <span class="s2">&quot;policyName&quot;</span><span class="p">:</span> <span class="s2">&quot;policy-name&quot;</span><span class="p">,</span>
        <span class="s2">&quot;statistic&quot;</span><span class="p">:</span> <span class="s2">&quot;average&quot;</span><span class="p">,</span>
        <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
        <span class="s2">&quot;unit&quot;</span><span class="p">:</span> <span class="s2">&quot;percent&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">scheduled_tasks</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;adjustment&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
        <span class="s2">&quot;adjustmentPercentage&quot;</span><span class="p">:</span> <span class="mi">50</span><span class="p">,</span>
        <span class="s2">&quot;batchSizePercentage&quot;</span><span class="p">:</span> <span class="mi">33</span><span class="p">,</span>
        <span class="s2">&quot;cronExpression&quot;</span><span class="p">:</span> <span class="s2">&quot;* * * * *&quot;</span><span class="p">,</span>
        <span class="s2">&quot;gracePeriod&quot;</span><span class="p">:</span> <span class="mi">300</span><span class="p">,</span>
        <span class="s2">&quot;isEnabled&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;scaleMaxCapacity&quot;</span><span class="p">:</span> <span class="mi">8</span><span class="p">,</span>
        <span class="s2">&quot;scaleMinCapacity&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
        <span class="s2">&quot;scaleTargetCapacity&quot;</span><span class="p">:</span> <span class="mi">6</span><span class="p">,</span>
        <span class="s2">&quot;taskType&quot;</span><span class="p">:</span> <span class="s2">&quot;scale&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">shutdown_script</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="n">strategy</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;drainingTimeout&quot;</span><span class="p">:</span> <span class="mi">300</span><span class="p">,</span>
        <span class="s2">&quot;odCount&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">user_data</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">load_balancers</span></code> - (Required) Describes a set of one or more classic load balancer target groups and/or Multai load balancer target sets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Required) The resource type. Valid values: CLASSIC, TARGET_GROUP, MULTAI_TARGET_SET.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">balancer_id</span></code> - (Required) The balancer ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_set_id</span></code> - (Required) The scale set ID associated with the load balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">auto_weight</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>)</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="image"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> - (Required) Image of a VM. An image is a template for creating new VMs. Choose from Azure image catalogue (marketplace) or use a custom image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> - (Optional) Image publisher. Required if resource_group_name is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> - (Optional) Name of the image to use. Required if publisher is specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> - (Optional) Image’s Stock Keeping Unit, which is the specific version of the image. Required if publisher is specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> - (Optional) Name of Resource Group for custom image. Required if publisher not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image_name</span></code> - (Optional) Name of the custom image. Required if resource_group_name is specified.</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="health-check"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">health_check</span></code> - (Optional) Describes the health check configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> - (Optional) Health check used to validate VM health. Valid values: “INSTANCE_STATE”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> - (Optional) Period of time (seconds) to wait for VM to reach healthiness before monitoring for unhealthiness.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">auto_healing</span></code> - (Optional) Enable auto-healing of unhealthy VMs.</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="network"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> - (Required) Defines the Virtual Network and Subnet for your Elastigroup.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_name</span></code> - (Required) Name of Vnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_name</span></code> - (Required) ID of subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> - (Required) Vnet Resource Group Name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">assign_public_up</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">false</span></code>) Assign a public IP to each VM in the Elastigroup.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">additional_ip_configs</span></code> - (Optional) Array of additional IP configuration objects.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The IP configuration name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_version</span></code> - (Optional) Available from Azure Api-Version 2017-03-30 onwards, it represents whether the specific ipconfiguration is IPv4 or IPv6. Valid values: <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>, <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>.</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="login"></a></span></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="login"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">login</span></code> - (Required) Describes the login configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_name</span></code> - (Required) Set admin access for accessing your VMs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssh_public_key</span></code> - (Optional) SSH for admin access to Linux VMs. Required for Linux product types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> - (Optional) Password for admin access to Windows VMs. Required for Windows product types.</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="scaling-policy"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">scheduled_task</span></code> - (Optional) Describes the configuration of one or more scheduled tasks.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">is_enabled</span></code> - (Optional, Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>) Describes whether the task is enabled. When true the task should run when false it should not run.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cron_expression</span></code> - (Required) A valid cron expression (<code class="docutils literal notranslate"><span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span></code>). The cron is running in UTC time zone and is in Unix cron format Cron Expression Validator Script.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">task_type</span></code> - (Required) The task type to run. Valid Values: <code class="docutils literal notranslate"><span class="pre">backup_ami</span></code>, <code class="docutils literal notranslate"><span class="pre">scale</span></code>, <code class="docutils literal notranslate"><span class="pre">scaleUp</span></code>, <code class="docutils literal notranslate"><span class="pre">roll</span></code>, <code class="docutils literal notranslate"><span class="pre">statefulUpdateCapacity</span></code>, <code class="docutils literal notranslate"><span class="pre">statefulRecycle</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale_min_capacity</span></code> - (Optional) The min capacity of the group. Should be used when choosing ‘task_type’ of ‘scale’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale_max_capacity</span></code> - (Optional) The max capacity of the group. Required when ‘task_type’ is ‘scale’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale_target_capacity</span></code> - (Optional) The target capacity of the group. Should be used when choosing ‘task_type’ of ‘scale’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> - (Optional) The number of instances to add/remove to/from the target capacity when scale is needed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment_percentage</span></code> - (Optional) The percent of instances to add/remove to/from the target capacity when scale is needed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batch_size_percentage</span></code> - (Optional) The percentage size of each batch in the scheduled deployment roll. Required when the ‘task_type’ is ‘roll’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> - (Optional) The time to allow instances to become healthy.</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="update-policy"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">update_policy</span></code> - (Optional)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">should_roll</span></code> - (Required) Sets the enablement of the roll option.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roll_config</span></code> - (Required) While used, you can control whether the group should perform a deployment after an update to the configuration.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batch_size_percentage</span></code> - (Required) Sets the percentage of the instances to deploy in each batch.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> - (Optional) Sets the health check type to use. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;INSTANCE_STATE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;NONE&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> - (Optional) Sets the grace period for new instances to become healthy.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p><span class="raw-html-m2r"><a id="third-party-integrations"></a></span></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">integration_kubernetes</span></code> - (Optional) Describes the <a class="reference external" href="https://kubernetes.io/">Kubernetes</a> integration.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_identifier</span></code> - (Required) The cluster ID.</p></li>
</ul>
</li>
</ul>
<p>Usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">integration_multai_runtime</span></code> - (Optional) Describes the <a class="reference external" href="https://spotinst.com/">Multai Runtime</a> integration.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deployment_id</span></code> - (Optional) The deployment id you want to get</p></li>
</ul>
</li>
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
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired number of instances the group should have at any time.</p></li>
<li><p><strong>low_priority_sizes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Available Low-Priority sizes.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of instances the group should have at any time.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of instances the group should have at any time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the managed identity.</p></li>
<li><p><strong>od_sizes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Available On-Demand sizes</p></li>
<li><p><strong>product</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region your Azure group will be created in.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Resource Group that the user-assigned managed identity resides in.</p></li>
<li><p><strong>shutdown_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shutdown script for the group. Value should be passed as a string encoded at Base64 only.</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the deployment strategy.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded MIME user data to make available to the instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auto_healing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>images</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">imageName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Resource Group that the user-assigned managed identity resides in.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">marketplaces</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>integration_kubernetes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_multai_runtime</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deployment_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>load_balancers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">balancer_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>login</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshPublicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>managed_service_identities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the managed identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Resource Group that the user-assigned managed identity resides in.</p></li>
</ul>
<p>The <strong>network</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalIpConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the managed identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">assignPublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Resource Group that the user-assigned managed identity resides in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_down_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the managed identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_up_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the managed identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustmentPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMaxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMinCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>strategy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">draining_timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Time (seconds) to allow the instance to be drained from incoming TCP connections and detached from MLB before terminating it during a scale-down operation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lowPriorityPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percentage of Low Priority instances to maintain. Required if <code class="docutils literal notranslate"><span class="pre">od_count</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">odCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of On-Demand instances to maintain. Required if low_priority_percentage is not specified.</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rollConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.low_priority_sizes">
<code class="sig-name descname">low_priority_sizes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.low_priority_sizes" title="Permalink to this definition">¶</a></dt>
<dd><p>Available Low-Priority sizes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.max_size">
<code class="sig-name descname">max_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.min_size">
<code class="sig-name descname">min_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of instances the group should have at any time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the managed identity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.od_sizes">
<code class="sig-name descname">od_sizes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.od_sizes" title="Permalink to this definition">¶</a></dt>
<dd><p>Available On-Demand sizes</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.product">
<code class="sig-name descname">product</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.product" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region your Azure group will be created in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Resource Group that the user-assigned managed identity resides in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.shutdown_script">
<code class="sig-name descname">shutdown_script</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.shutdown_script" title="Permalink to this definition">¶</a></dt>
<dd><p>Shutdown script for the group. Value should be passed as a string encoded at Base64 only.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.strategy">
<code class="sig-name descname">strategy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the deployment strategy.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">draining_timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Time (seconds) to allow the instance to be drained from incoming TCP connections and detached from MLB before terminating it during a scale-down operation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lowPriorityPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Percentage of Low Priority instances to maintain. Required if <code class="docutils literal notranslate"><span class="pre">od_count</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">odCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of On-Demand instances to maintain. Required if low_priority_percentage is not specified.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.azure.Elastigroup.user_data">
<code class="sig-name descname">user_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded MIME user data to make available to the instances.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.azure.Elastigroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_kubernetes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_multai_runtime</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">low_priority_sizes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_service_identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">od_sizes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_down_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_up_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_tasks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shutdown_script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Elastigroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired number of instances the group should have at any time.</p></li>
<li><p><strong>low_priority_sizes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Available Low-Priority sizes.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of instances the group should have at any time.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of instances the group should have at any time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the managed identity.</p></li>
<li><p><strong>od_sizes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Available On-Demand sizes</p></li>
<li><p><strong>product</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation system type. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;Linux&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Windows&quot;</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region your Azure group will be created in.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Resource Group that the user-assigned managed identity resides in.</p></li>
<li><p><strong>shutdown_script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Shutdown script for the group. Value should be passed as a string encoded at Base64 only.</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the deployment strategy.</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64-encoded MIME user data to make available to the instances.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auto_healing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>images</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">imageName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Resource Group that the user-assigned managed identity resides in.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">marketplaces</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>integration_kubernetes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIdentifier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>integration_multai_runtime</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deployment_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>load_balancers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">balancer_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>login</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshPublicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>managed_service_identities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the managed identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Resource Group that the user-assigned managed identity resides in.</p></li>
</ul>
<p>The <strong>network</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalIpConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the managed identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">assignPublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_group_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Resource Group that the user-assigned managed identity resides in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworkName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_down_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the managed identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scaling_up_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cooldown</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the managed identity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationPeriods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>scheduled_tasks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adjustmentPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cronExpression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMaxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleMinCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaleTargetCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>strategy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">draining_timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Time (seconds) to allow the instance to be drained from incoming TCP connections and detached from MLB before terminating it during a scale-down operation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lowPriorityPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percentage of Low Priority instances to maintain. Required if <code class="docutils literal notranslate"><span class="pre">od_count</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">odCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of On-Demand instances to maintain. Required if low_priority_percentage is not specified.</p></li>
</ul>
<p>The <strong>update_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rollConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batchSizePercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">grace_period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_check_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">shouldRoll</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.azure.Elastigroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.azure.Elastigroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.azure.Elastigroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
