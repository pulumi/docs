---
title: Module emr
title_tag: Module emr | Package pulumi_alicloud | Python SDK
linktitle: emr
notitle: true
---

<div class="section" id="emr">
<h1>emr<a class="headerlink" href="#emr" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.emr"></span><dl class="py class">
<dt id="pulumi_alicloud.emr.AwaitableGetDiskTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">AwaitableGetDiskTypesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.AwaitableGetDiskTypesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.emr.AwaitableGetInstanceTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">AwaitableGetInstanceTypesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_local_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_node_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.AwaitableGetInstanceTypesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.emr.AwaitableGetMainVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">AwaitableGetMainVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">emr_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">main_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.AwaitableGetMainVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.emr.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deposit_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eas_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">emr_ver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">high_availability_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_open_public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_pair_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_pwd</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">option_software_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">related_cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_local_metadb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_emr_ecs_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a EMR Cluster resource. With this you can create, read, and release  EMR Cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.57.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default_main_versions</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_main_versions</span><span class="p">()</span>
<span class="n">default_instance_types</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_instance_types</span><span class="p">(</span><span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;InstanceType&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">support_local_storage</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">support_node_types</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;MASTER&quot;</span><span class="p">,</span>
        <span class="s2">&quot;CORE&quot;</span><span class="p">,</span>
        <span class="s2">&quot;TASK&quot;</span><span class="p">,</span>
    <span class="p">])</span>
<span class="n">data_disk</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_disk_types</span><span class="p">(</span><span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;DataDisk&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">])</span>
<span class="n">system_disk</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_disk_types</span><span class="p">(</span><span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;SystemDisk&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">])</span>
<span class="n">vpc</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">var</span><span class="o">.</span><span class="n">vpc_id</span> <span class="o">==</span>  <span class="k">else</span> <span class="mi">0</span> <span class="o">==</span> <span class="kc">True</span><span class="p">)]:</span>
    <span class="n">vpc</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;vpc-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_cidr&quot;</span><span class="p">]))</span>
<span class="n">default_security_group</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">var</span><span class="o">.</span><span class="n">security_group_id</span> <span class="o">==</span>  <span class="k">else</span> <span class="mi">0</span> <span class="o">==</span> <span class="kc">True</span><span class="p">)]:</span>
    <span class="n">default_security_group</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;defaultSecurityGroup-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span> <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]))</span>
<span class="c1"># VSwitch Resource for Module</span>
<span class="n">vswitch</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">var</span><span class="o">.</span><span class="n">vswitch_id</span> <span class="o">==</span>  <span class="k">else</span> <span class="mi">0</span> <span class="o">==</span> <span class="kc">True</span><span class="p">)]:</span>
    <span class="n">vswitch</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Switch</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;vswitch-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">availability_zone</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;availability_zone&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;availability_zone&quot;</span><span class="p">],</span>
        <span class="n">cidr_block</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;vswitch_cidr&quot;</span><span class="p">],</span>
        <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]))</span>
<span class="c1"># Ram role Resource for Module</span>
<span class="n">default_role</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ram</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;defaultRole&quot;</span><span class="p">,</span>
    <span class="n">document</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;    {</span>
<span class="s2">        &quot;Statement&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">            &quot;Action&quot;: &quot;sts:AssumeRole&quot;,</span>
<span class="s2">            &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">            &quot;Principal&quot;: {</span>
<span class="s2">            &quot;Service&quot;: [</span>
<span class="s2">                &quot;emr.aliyuncs.com&quot;, </span>
<span class="s2">                &quot;ecs.aliyuncs.com&quot;</span>
<span class="s2">            ]</span>
<span class="s2">            }</span>
<span class="s2">        }</span>
<span class="s2">        ],</span>
<span class="s2">        &quot;Version&quot;: &quot;1&quot;</span>
<span class="s2">    }</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;this is a role test.&quot;</span><span class="p">,</span>
    <span class="n">force</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">default_cluster</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;defaultCluster&quot;</span><span class="p">,</span>
    <span class="n">emr_ver</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;emrVersion&quot;</span><span class="p">],</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">host_group</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;hostGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;master_group&quot;</span><span class="p">,</span>
            <span class="s2">&quot;hostGroupType&quot;</span><span class="p">:</span> <span class="s2">&quot;MASTER&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nodeCount&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskType&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskCapacity&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
            <span class="s2">&quot;diskCount&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sysDiskType&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;sysDiskCapacity&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;hostGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;core_group&quot;</span><span class="p">,</span>
            <span class="s2">&quot;hostGroupType&quot;</span><span class="p">:</span> <span class="s2">&quot;CORE&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nodeCount&quot;</span><span class="p">:</span> <span class="s2">&quot;3&quot;</span><span class="p">,</span>
            <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskType&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskCapacity&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
            <span class="s2">&quot;diskCount&quot;</span><span class="p">:</span> <span class="s2">&quot;4&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sysDiskType&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;sysDiskCapacity&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;hostGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;task_group&quot;</span><span class="p">,</span>
            <span class="s2">&quot;hostGroupType&quot;</span><span class="p">:</span> <span class="s2">&quot;TASK&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nodeCount&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskType&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskCapacity&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
            <span class="s2">&quot;diskCount&quot;</span><span class="p">:</span> <span class="s2">&quot;4&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sysDiskType&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;sysDiskCapacity&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">high_availability_enable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">],</span>
    <span class="n">security_group_id</span><span class="o">=</span><span class="n">default_security_group</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;security_group_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;security_group_id&quot;</span><span class="p">],</span>
    <span class="n">is_open_public_ip</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">vswitch_id</span><span class="o">=</span><span class="n">vswitch</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vswitch_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vswitch_id&quot;</span><span class="p">],</span>
    <span class="n">user_defined_emr_ecs_role</span><span class="o">=</span><span class="n">default_role</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">ssh_enable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">master_pwd</span><span class="o">=</span><span class="s2">&quot;ABCtest1234!&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default_main_versions</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_main_versions</span><span class="p">()</span>
<span class="n">default_instance_types</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_instance_types</span><span class="p">(</span><span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;InstanceType&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">support_local_storage</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">support_node_types</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;MASTER&quot;</span><span class="p">,</span>
        <span class="s2">&quot;CORE&quot;</span><span class="p">,</span>
        <span class="s2">&quot;TASK&quot;</span><span class="p">,</span>
    <span class="p">])</span>
<span class="n">data_disk</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_disk_types</span><span class="p">(</span><span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;DataDisk&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">])</span>
<span class="n">system_disk</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_disk_types</span><span class="p">(</span><span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;SystemDisk&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">])</span>
<span class="n">vpc</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">var</span><span class="o">.</span><span class="n">vpc_id</span> <span class="o">==</span>  <span class="k">else</span> <span class="mi">0</span> <span class="o">==</span> <span class="kc">True</span><span class="p">)]:</span>
    <span class="n">vpc</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;vpc-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_cidr&quot;</span><span class="p">]))</span>
<span class="n">default_security_group</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">var</span><span class="o">.</span><span class="n">security_group_id</span> <span class="o">==</span>  <span class="k">else</span> <span class="mi">0</span> <span class="o">==</span> <span class="kc">True</span><span class="p">)]:</span>
    <span class="n">default_security_group</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;defaultSecurityGroup-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span> <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]))</span>
<span class="c1"># VSwitch Resource for Module</span>
<span class="n">vswitch</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">var</span><span class="o">.</span><span class="n">vswitch_id</span> <span class="o">==</span>  <span class="k">else</span> <span class="mi">0</span> <span class="o">==</span> <span class="kc">True</span><span class="p">)]:</span>
    <span class="n">vswitch</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Switch</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;vswitch-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">availability_zone</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;availability_zone&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;availability_zone&quot;</span><span class="p">],</span>
        <span class="n">cidr_block</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;vswitch_cidr&quot;</span><span class="p">],</span>
        <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]))</span>
<span class="c1"># Ram role Resource for Module</span>
<span class="n">default_role</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ram</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;defaultRole&quot;</span><span class="p">,</span>
    <span class="n">document</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;    {</span>
<span class="s2">        &quot;Statement&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">            &quot;Action&quot;: &quot;sts:AssumeRole&quot;,</span>
<span class="s2">            &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">            &quot;Principal&quot;: {</span>
<span class="s2">            &quot;Service&quot;: [</span>
<span class="s2">                &quot;emr.aliyuncs.com&quot;, </span>
<span class="s2">                &quot;ecs.aliyuncs.com&quot;</span>
<span class="s2">            ]</span>
<span class="s2">            }</span>
<span class="s2">        }</span>
<span class="s2">        ],</span>
<span class="s2">        &quot;Version&quot;: &quot;1&quot;</span>
<span class="s2">    }</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;this is a role test.&quot;</span><span class="p">,</span>
    <span class="n">force</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">default_cluster</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;defaultCluster&quot;</span><span class="p">,</span>
    <span class="n">emr_ver</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;emrVersion&quot;</span><span class="p">],</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">host_group</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;hostGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;master_group&quot;</span><span class="p">,</span>
            <span class="s2">&quot;hostGroupType&quot;</span><span class="p">:</span> <span class="s2">&quot;MASTER&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nodeCount&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskType&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskCapacity&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
            <span class="s2">&quot;diskCount&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sysDiskType&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;sysDiskCapacity&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;hostGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;core_group&quot;</span><span class="p">,</span>
            <span class="s2">&quot;hostGroupType&quot;</span><span class="p">:</span> <span class="s2">&quot;CORE&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nodeCount&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskType&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskCapacity&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
            <span class="s2">&quot;diskCount&quot;</span><span class="p">:</span> <span class="s2">&quot;4&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sysDiskType&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;sysDiskCapacity&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;hostGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;task_group&quot;</span><span class="p">,</span>
            <span class="s2">&quot;hostGroupType&quot;</span><span class="p">:</span> <span class="s2">&quot;TASK&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nodeCount&quot;</span><span class="p">:</span> <span class="s2">&quot;4&quot;</span><span class="p">,</span>
            <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskType&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskCapacity&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
            <span class="s2">&quot;diskCount&quot;</span><span class="p">:</span> <span class="s2">&quot;4&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sysDiskType&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;sysDiskCapacity&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">high_availability_enable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">],</span>
    <span class="n">security_group_id</span><span class="o">=</span><span class="n">default_security_group</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;security_group_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;security_group_id&quot;</span><span class="p">],</span>
    <span class="n">is_open_public_ip</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">vswitch_id</span><span class="o">=</span><span class="n">vswitch</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vswitch_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vswitch_id&quot;</span><span class="p">],</span>
    <span class="n">user_defined_emr_ecs_role</span><span class="o">=</span><span class="n">default_role</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">ssh_enable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">master_pwd</span><span class="o">=</span><span class="s2">&quot;ABCtest1234!&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default_main_versions</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_main_versions</span><span class="p">()</span>
<span class="n">default_instance_types</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_instance_types</span><span class="p">(</span><span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;InstanceType&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">support_local_storage</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">support_node_types</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;MASTER&quot;</span><span class="p">,</span>
        <span class="s2">&quot;CORE&quot;</span><span class="p">,</span>
        <span class="s2">&quot;TASK&quot;</span><span class="p">,</span>
    <span class="p">])</span>
<span class="n">data_disk</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_disk_types</span><span class="p">(</span><span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;DataDisk&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">])</span>
<span class="n">system_disk</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_disk_types</span><span class="p">(</span><span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;SystemDisk&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">])</span>
<span class="n">vpc</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">var</span><span class="o">.</span><span class="n">vpc_id</span> <span class="o">==</span>  <span class="k">else</span> <span class="mi">0</span> <span class="o">==</span> <span class="kc">True</span><span class="p">)]:</span>
    <span class="n">vpc</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;vpc-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_cidr&quot;</span><span class="p">]))</span>
<span class="n">default_security_group</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">var</span><span class="o">.</span><span class="n">security_group_id</span> <span class="o">==</span>  <span class="k">else</span> <span class="mi">0</span> <span class="o">==</span> <span class="kc">True</span><span class="p">)]:</span>
    <span class="n">default_security_group</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;defaultSecurityGroup-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span> <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]))</span>
<span class="c1"># VSwitch Resource for Module</span>
<span class="n">vswitch</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">var</span><span class="o">.</span><span class="n">vswitch_id</span> <span class="o">==</span>  <span class="k">else</span> <span class="mi">0</span> <span class="o">==</span> <span class="kc">True</span><span class="p">)]:</span>
    <span class="n">vswitch</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Switch</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;vswitch-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">availability_zone</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;availability_zone&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;availability_zone&quot;</span><span class="p">],</span>
        <span class="n">cidr_block</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;vswitch_cidr&quot;</span><span class="p">],</span>
        <span class="n">vpc_id</span><span class="o">=</span><span class="n">vpc</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">]))</span>
<span class="c1"># Ram role Resource for Module</span>
<span class="n">default_role</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ram</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;defaultRole&quot;</span><span class="p">,</span>
    <span class="n">document</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;    {</span>
<span class="s2">        &quot;Statement&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">            &quot;Action&quot;: &quot;sts:AssumeRole&quot;,</span>
<span class="s2">            &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">            &quot;Principal&quot;: {</span>
<span class="s2">            &quot;Service&quot;: [</span>
<span class="s2">                &quot;emr.aliyuncs.com&quot;, </span>
<span class="s2">                &quot;ecs.aliyuncs.com&quot;</span>
<span class="s2">            ]</span>
<span class="s2">            }</span>
<span class="s2">        }</span>
<span class="s2">        ],</span>
<span class="s2">        &quot;Version&quot;: &quot;1&quot;</span>
<span class="s2">    }</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;this is a role test.&quot;</span><span class="p">,</span>
    <span class="n">force</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">default_cluster</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;defaultCluster&quot;</span><span class="p">,</span>
    <span class="n">emr_ver</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;emrVersion&quot;</span><span class="p">],</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="n">default_main_versions</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">],</span>
    <span class="n">host_group</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;hostGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;master_group&quot;</span><span class="p">,</span>
            <span class="s2">&quot;hostGroupType&quot;</span><span class="p">:</span> <span class="s2">&quot;MASTER&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nodeCount&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskType&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskCapacity&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
            <span class="s2">&quot;diskCount&quot;</span><span class="p">:</span> <span class="s2">&quot;1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sysDiskType&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;sysDiskCapacity&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;hostGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;core_group&quot;</span><span class="p">,</span>
            <span class="s2">&quot;hostGroupType&quot;</span><span class="p">:</span> <span class="s2">&quot;CORE&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nodeCount&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskType&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskCapacity&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
            <span class="s2">&quot;diskCount&quot;</span><span class="p">:</span> <span class="s2">&quot;4&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sysDiskType&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;sysDiskCapacity&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;hostGroupName&quot;</span><span class="p">:</span> <span class="s2">&quot;task_group&quot;</span><span class="p">,</span>
            <span class="s2">&quot;hostGroupType&quot;</span><span class="p">:</span> <span class="s2">&quot;TASK&quot;</span><span class="p">,</span>
            <span class="s2">&quot;nodeCount&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskType&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;diskCapacity&quot;</span><span class="p">:</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">data_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
            <span class="s2">&quot;diskCount&quot;</span><span class="p">:</span> <span class="s2">&quot;4&quot;</span><span class="p">,</span>
            <span class="s2">&quot;sysDiskType&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
            <span class="s2">&quot;sysDiskCapacity&quot;</span><span class="p">:</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">system_disk</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;min&quot;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">160</span> <span class="k">else</span> <span class="mi">160</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">high_availability_enable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;zone_id&quot;</span><span class="p">],</span>
    <span class="n">security_group_id</span><span class="o">=</span><span class="n">default_security_group</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;security_group_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;security_group_id&quot;</span><span class="p">],</span>
    <span class="n">is_open_public_ip</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">vswitch_id</span><span class="o">=</span><span class="n">vswitch</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">if</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vswitch_id&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="k">else</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;vswitch_id&quot;</span><span class="p">],</span>
    <span class="n">user_defined_emr_ecs_role</span><span class="o">=</span><span class="n">default_role</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">ssh_enable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">master_pwd</span><span class="o">=</span><span class="s2">&quot;ABCtest1234!&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EMR Cluster Type, e.g. HADOOP, KAFKA, DRUID, GATEWAY etc. You can find all valid EMR cluster type in emr web console. Supported ‘GATEWAY’ available in 1.61.0+.</p></li>
<li><p><strong>deposit_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cluster deposit type, HALF_MANAGED or FULL_MANAGED.</p></li>
<li><p><strong>eas_enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – High security cluster (true) or not. Default value is false.</p></li>
<li><p><strong>emr_ver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EMR Version, e.g. EMR-3.22.0. You can find the all valid EMR Version in emr web console.</p></li>
<li><p><strong>high_availability_enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – High Available for HDFS and YARN. If this is set true, MASTER group must have two nodes.</p></li>
<li><p><strong>host_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups of Host, You can specify MASTER as a group, CORE as a group (just like the above example).</p></li>
<li><p><strong>key_pair_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Ssh key pair.</p></li>
<li><p><strong>master_pwd</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master ssh password.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – bootstrap action name.</p></li>
<li><p><strong>option_software_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optional software list.</p></li>
<li><p><strong>related_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This specify the related cluster id, if this cluster is a Gateway.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Security Group ID for Cluster, you can also specify this key for each host group.</p></li>
<li><p><strong>ssh_enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this is set true, we can ssh into cluster. Default value is false.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>use_local_metadb</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Use local metadb. Default is false.</p></li>
<li><p><strong>user_defined_emr_ecs_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alicloud EMR uses roles to perform actions on your behalf when provisioning cluster resources, running applications, dynamically scaling resources. EMR uses the following roles when interacting with other Alicloud services. Default value is AliyunEmrEcsDefaultRole.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Global vswitch id, you can also specify it in host group.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Zone ID, e.g. cn-huhehaote-a</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bootstrap_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - bootstrap action args, e.g. “–a=b”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - bootstrap action name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - bootstrap action path, e.g. “oss://bucket/path”.</p></li>
</ul>
<p>The <strong>host_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auto_renew</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Auto renew for prepaid, true of false. Default is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">charge_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,local_disk,cloud_essd.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuDriver</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - host group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - host group type, supported value: MASTER, CORE or TASK, supported ‘GATEWAY’ available in 1.61.0+.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceList</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instance list for cluster scale down. This value follows the json format, e.g. [“instance_id1”,”instance_id2”]. escape character for ” is “.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Host Ecs instance type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Host number in this group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - If charge type is PrePaid, this should be specified, unit is month. Supported value: 1、2、3、4、5、6、7、8、9、12、24、36.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,cloud_essd.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.charge_type">
<code class="sig-name descname">charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.cluster_type">
<code class="sig-name descname">cluster_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.cluster_type" title="Permalink to this definition">¶</a></dt>
<dd><p>EMR Cluster Type, e.g. HADOOP, KAFKA, DRUID, GATEWAY etc. You can find all valid EMR cluster type in emr web console. Supported ‘GATEWAY’ available in 1.61.0+.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.deposit_type">
<code class="sig-name descname">deposit_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.deposit_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster deposit type, HALF_MANAGED or FULL_MANAGED.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.eas_enable">
<code class="sig-name descname">eas_enable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.eas_enable" title="Permalink to this definition">¶</a></dt>
<dd><p>High security cluster (true) or not. Default value is false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.emr_ver">
<code class="sig-name descname">emr_ver</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.emr_ver" title="Permalink to this definition">¶</a></dt>
<dd><p>EMR Version, e.g. EMR-3.22.0. You can find the all valid EMR Version in emr web console.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.high_availability_enable">
<code class="sig-name descname">high_availability_enable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.high_availability_enable" title="Permalink to this definition">¶</a></dt>
<dd><p>High Available for HDFS and YARN. If this is set true, MASTER group must have two nodes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.host_groups">
<code class="sig-name descname">host_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.host_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups of Host, You can specify MASTER as a group, CORE as a group (just like the above example).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auto_renew</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Auto renew for prepaid, true of false. Default is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">charge_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Data disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Data disk count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Data disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,local_disk,cloud_essd.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuDriver</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - host group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - host group type, supported value: MASTER, CORE or TASK, supported ‘GATEWAY’ available in 1.61.0+.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceList</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Instance list for cluster scale down. This value follows the json format, e.g. [“instance_id1”,”instance_id2”]. escape character for ” is “.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Host Ecs instance type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Host number in this group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - If charge type is PrePaid, this should be specified, unit is month. Supported value: 1、2、3、4、5、6、7、8、9、12、24、36.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,cloud_essd.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.key_pair_name">
<code class="sig-name descname">key_pair_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.key_pair_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Ssh key pair.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.master_pwd">
<code class="sig-name descname">master_pwd</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.master_pwd" title="Permalink to this definition">¶</a></dt>
<dd><p>Master ssh password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>bootstrap action name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.option_software_lists">
<code class="sig-name descname">option_software_lists</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.option_software_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional software list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.related_cluster_id">
<code class="sig-name descname">related_cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.related_cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>This specify the related cluster id, if this cluster is a Gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Security Group ID for Cluster, you can also specify this key for each host group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.ssh_enable">
<code class="sig-name descname">ssh_enable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.ssh_enable" title="Permalink to this definition">¶</a></dt>
<dd><p>If this is set true, we can ssh into cluster. Default value is false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.use_local_metadb">
<code class="sig-name descname">use_local_metadb</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.use_local_metadb" title="Permalink to this definition">¶</a></dt>
<dd><p>Use local metadb. Default is false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.user_defined_emr_ecs_role">
<code class="sig-name descname">user_defined_emr_ecs_role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.user_defined_emr_ecs_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Alicloud EMR uses roles to perform actions on your behalf when provisioning cluster resources, running applications, dynamically scaling resources. EMR uses the following roles when interacting with other Alicloud services. Default value is AliyunEmrEcsDefaultRole.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Global vswitch id, you can also specify it in host group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.Cluster.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Zone ID, e.g. cn-huhehaote-a</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.emr.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deposit_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eas_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">emr_ver</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">high_availability_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_open_public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_pair_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_pwd</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">option_software_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">related_cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_local_metadb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_defined_emr_ecs_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EMR Cluster Type, e.g. HADOOP, KAFKA, DRUID, GATEWAY etc. You can find all valid EMR cluster type in emr web console. Supported ‘GATEWAY’ available in 1.61.0+.</p></li>
<li><p><strong>deposit_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cluster deposit type, HALF_MANAGED or FULL_MANAGED.</p></li>
<li><p><strong>eas_enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – High security cluster (true) or not. Default value is false.</p></li>
<li><p><strong>emr_ver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EMR Version, e.g. EMR-3.22.0. You can find the all valid EMR Version in emr web console.</p></li>
<li><p><strong>high_availability_enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – High Available for HDFS and YARN. If this is set true, MASTER group must have two nodes.</p></li>
<li><p><strong>host_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Groups of Host, You can specify MASTER as a group, CORE as a group (just like the above example).</p></li>
<li><p><strong>key_pair_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Ssh key pair.</p></li>
<li><p><strong>master_pwd</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Master ssh password.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – bootstrap action name.</p></li>
<li><p><strong>option_software_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optional software list.</p></li>
<li><p><strong>related_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This specify the related cluster id, if this cluster is a Gateway.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Security Group ID for Cluster, you can also specify this key for each host group.</p></li>
<li><p><strong>ssh_enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this is set true, we can ssh into cluster. Default value is false.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>use_local_metadb</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Use local metadb. Default is false.</p></li>
<li><p><strong>user_defined_emr_ecs_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alicloud EMR uses roles to perform actions on your behalf when provisioning cluster resources, running applications, dynamically scaling resources. EMR uses the following roles when interacting with other Alicloud services. Default value is AliyunEmrEcsDefaultRole.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Global vswitch id, you can also specify it in host group.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Zone ID, e.g. cn-huhehaote-a</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bootstrap_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - bootstrap action args, e.g. “–a=b”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - bootstrap action name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - bootstrap action path, e.g. “oss://bucket/path”.</p></li>
</ul>
<p>The <strong>host_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auto_renew</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Auto renew for prepaid, true of false. Default is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">charge_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,local_disk,cloud_essd.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuDriver</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - host group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - host group type, supported value: MASTER, CORE or TASK, supported ‘GATEWAY’ available in 1.61.0+.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceList</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instance list for cluster scale down. This value follows the json format, e.g. [“instance_id1”,”instance_id2”]. escape character for ” is “.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Host Ecs instance type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Host number in this group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - If charge type is PrePaid, this should be specified, unit is month. Supported value: 1、2、3、4、5、6、7、8、9、12、24、36.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,cloud_essd.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.emr.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.emr.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.emr.GetDiskTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">GetDiskTypesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.GetDiskTypesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDiskTypes.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetDiskTypesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetDiskTypesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetDiskTypesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetDiskTypesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of data disk and system disk type IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetDiskTypesResult.types">
<code class="sig-name descname">types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetDiskTypesResult.types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of emr instance types. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.emr.GetInstanceTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">GetInstanceTypesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_local_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_node_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.GetInstanceTypesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceTypes.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetInstanceTypesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetInstanceTypesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetInstanceTypesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetInstanceTypesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of emr instance types IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetInstanceTypesResult.types">
<code class="sig-name descname">types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetInstanceTypesResult.types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of emr instance types. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetInstanceTypesResult.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetInstanceTypesResult.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The available zone id in Alibaba Cloud account</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.emr.GetMainVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">GetMainVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">emr_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">main_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.GetMainVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMainVersions.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetMainVersionsResult.emr_version">
<code class="sig-name descname">emr_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetMainVersionsResult.emr_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the emr cluster instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetMainVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetMainVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetMainVersionsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetMainVersionsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of emr instance types IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.emr.GetMainVersionsResult.main_versions">
<code class="sig-name descname">main_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetMainVersionsResult.main_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of versions of the emr cluster instance. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.emr.get_disk_types">
<code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">get_disk_types</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.get_disk_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">emr.getDiskTypes</span></code> data source provides a collection of data disk and 
system disk types available in Alibaba Cloud account when create a emr cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_disk_types</span><span class="p">(</span><span class="n">cluster_type</span><span class="o">=</span><span class="s2">&quot;HADOOP&quot;</span><span class="p">,</span>
    <span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;DataDisk&quot;</span><span class="p">,</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="s2">&quot;ecs.g5.xlarge&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;cn-huhehaote-a&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;dataDiskType&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_type</strong> (<em>str</em>) – The cluster type of the emr cluster instance. Possible values: <code class="docutils literal notranslate"><span class="pre">HADOOP</span></code>, <code class="docutils literal notranslate"><span class="pre">KAFKA</span></code>, <code class="docutils literal notranslate"><span class="pre">ZOOKEEPER</span></code>, <code class="docutils literal notranslate"><span class="pre">DRUID</span></code>.</p></li>
<li><p><strong>destination_resource</strong> (<em>str</em>) – The destination resource of emr cluster instance</p></li>
<li><p><strong>instance_charge_type</strong> (<em>str</em>) – Filter the results by charge type. Valid values: <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> and <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>str</em>) – The ecs instance type of create emr cluster instance.</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The Zone to create emr cluster instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.emr.get_instance_types">
<code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">get_instance_types</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_resource</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_local_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">support_node_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.get_instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">emr.getInstanceTypes</span></code> data source provides a collection of ecs
instance types available in Alibaba Cloud account when create a emr cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.59.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_instance_types</span><span class="p">(</span><span class="n">cluster_type</span><span class="o">=</span><span class="s2">&quot;HADOOP&quot;</span><span class="p">,</span>
    <span class="n">destination_resource</span><span class="o">=</span><span class="s2">&quot;InstanceType&quot;</span><span class="p">,</span>
    <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="s2">&quot;ecs.g5.2xlarge&quot;</span><span class="p">,</span>
    <span class="n">support_local_storage</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">support_node_types</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;MASTER&quot;</span><span class="p">,</span>
        <span class="s2">&quot;CORE&quot;</span><span class="p">,</span>
    <span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstInstanceType&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">.</span><span class="n">types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_type</strong> (<em>str</em>) – The cluster type of the emr cluster instance. Possible values: <code class="docutils literal notranslate"><span class="pre">HADOOP</span></code>, <code class="docutils literal notranslate"><span class="pre">KAFKA</span></code>, <code class="docutils literal notranslate"><span class="pre">ZOOKEEPER</span></code>, <code class="docutils literal notranslate"><span class="pre">DRUID</span></code>.</p></li>
<li><p><strong>destination_resource</strong> (<em>str</em>) – The destination resource of emr cluster instance</p></li>
<li><p><strong>instance_charge_type</strong> (<em>str</em>) – Filter the results by charge type. Valid values: <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> and <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>str</em>) – Filter the specific ecs instance type to create emr cluster.</p></li>
<li><p><strong>support_local_storage</strong> (<em>bool</em>) – Whether the current storage disk is local or not.</p></li>
<li><p><strong>support_node_types</strong> (<em>list</em>) – The specific supported node type list.
Possible values may be any one or combination of these: [“MASTER”, “CORE”, “TASK”, “GATEWAY”]</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The supported resources of specific zoneId.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.emr.get_main_versions">
<code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">get_main_versions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">emr_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.get_main_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">emr.getMainVersions</span></code> data source provides a collection of emr 
main versions available in Alibaba Cloud account when create a emr cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.59.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">get_main_versions</span><span class="p">(</span><span class="n">cluster_types</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;HADOOP&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ZOOKEEPER&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">emr_version</span><span class="o">=</span><span class="s2">&quot;EMR-3.22.0&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstMainVersion&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;emrVersion&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;thisClusterTypes&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">.</span><span class="n">main_versions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;clusterTypes&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_types</strong> (<em>list</em>) – The supported clusterType of this emr version.
Possible values may be any one or combination of these: [“HADOOP”, “DRUID”, “KAFKA”, “ZOOKEEPER”, “FLINK”, “CLICKHOUSE”]</p></li>
<li><p><strong>emr_version</strong> (<em>str</em>) – The version of the emr cluster instance. Possible values: <code class="docutils literal notranslate"><span class="pre">EMR-4.0.0</span></code>, <code class="docutils literal notranslate"><span class="pre">EMR-3.23.0</span></code>, <code class="docutils literal notranslate"><span class="pre">EMR-3.22.0</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
