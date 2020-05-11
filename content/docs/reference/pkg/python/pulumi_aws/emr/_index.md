---
title: Module emr
title_tag: Module emr | Package pulumi_aws | Python SDK
linktitle: emr
notitle: true
---

<div class="section" id="emr">
<h1>emr<a class="headerlink" href="#emr" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.emr"></span><dl class="py class">
<dt id="pulumi_aws.emr.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.emr.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscaling_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ami_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_root_volume_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ec2_attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_job_flow_alive_when_no_steps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kerberos_attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scale_down_behavior</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">step_concurrency_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visible_to_all_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic MapReduce Cluster, a web service that makes it easy to
process large amounts of data efficiently. See <a class="reference external" href="https://aws.amazon.com/documentation/elastic-mapreduce/">Amazon Elastic MapReduce Documentation</a>
for more information.</p>
<p>To configure <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Groups</a> for <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-task">task nodes</a>, see the <cite>``emr.InstanceGroup`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html">https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html</a>&gt;`_.</p>
<blockquote>
<div><p>Support for <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-fleets">Instance Fleets</a> will be made available in an upcoming release.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">cluster</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;cluster&quot;</span><span class="p">,</span>
    <span class="n">additional_info</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;instanceAwsClientConfiguration&quot;: {</span>
<span class="s2">    &quot;proxyPort&quot;: 8099,</span>
<span class="s2">    &quot;proxyHost&quot;: &quot;myproxy.example.com&quot;</span>
<span class="s2">  }</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">applications</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;Spark&quot;</span><span class="p">],</span>
    <span class="n">bootstrap_actions</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;args&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;instance.isMaster=true&quot;</span><span class="p">,</span>
            <span class="s2">&quot;echo running on master node&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;runif&quot;</span><span class="p">,</span>
        <span class="s2">&quot;path&quot;</span><span class="p">:</span> <span class="s2">&quot;s3://elasticmapreduce/bootstrap-actions/run-if&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">configurations_json</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;  [</span>
<span class="s2">    {</span>
<span class="s2">      &quot;Classification&quot;: &quot;hadoop-env&quot;,</span>
<span class="s2">      &quot;Configurations&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">          &quot;Classification&quot;: &quot;export&quot;,</span>
<span class="s2">          &quot;Properties&quot;: {</span>
<span class="s2">            &quot;JAVA_HOME&quot;: &quot;/usr/lib/jvm/java-1.8.0&quot;</span>
<span class="s2">          }</span>
<span class="s2">        }</span>
<span class="s2">      ],</span>
<span class="s2">      &quot;Properties&quot;: </span><span class="si">{}</span><span class="s2"></span>
<span class="s2">    },</span>
<span class="s2">    {</span>
<span class="s2">      &quot;Classification&quot;: &quot;spark-env&quot;,</span>
<span class="s2">      &quot;Configurations&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">          &quot;Classification&quot;: &quot;export&quot;,</span>
<span class="s2">          &quot;Properties&quot;: {</span>
<span class="s2">            &quot;JAVA_HOME&quot;: &quot;/usr/lib/jvm/java-1.8.0&quot;</span>
<span class="s2">          }</span>
<span class="s2">        }</span>
<span class="s2">      ],</span>
<span class="s2">      &quot;Properties&quot;: </span><span class="si">{}</span><span class="s2"></span>
<span class="s2">    }</span>
<span class="s2">  ]</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">core_instance_group</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;autoscalingPolicy&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">&quot;Constraints&quot;: {</span>
<span class="s2">  &quot;MinCapacity&quot;: 1,</span>
<span class="s2">  &quot;MaxCapacity&quot;: 2</span>
<span class="s2">},</span>
<span class="s2">&quot;Rules&quot;: [</span>
<span class="s2">  {</span>
<span class="s2">    &quot;Name&quot;: &quot;ScaleOutMemoryPercentage&quot;,</span>
<span class="s2">    &quot;Description&quot;: &quot;Scale out if YARNMemoryAvailablePercentage is less than 15&quot;,</span>
<span class="s2">    &quot;Action&quot;: {</span>
<span class="s2">      &quot;SimpleScalingPolicyConfiguration&quot;: {</span>
<span class="s2">        &quot;AdjustmentType&quot;: &quot;CHANGE_IN_CAPACITY&quot;,</span>
<span class="s2">        &quot;ScalingAdjustment&quot;: 1,</span>
<span class="s2">        &quot;CoolDown&quot;: 300</span>
<span class="s2">      }</span>
<span class="s2">    },</span>
<span class="s2">    &quot;Trigger&quot;: {</span>
<span class="s2">      &quot;CloudWatchAlarmDefinition&quot;: {</span>
<span class="s2">        &quot;ComparisonOperator&quot;: &quot;LESS_THAN&quot;,</span>
<span class="s2">        &quot;EvaluationPeriods&quot;: 1,</span>
<span class="s2">        &quot;MetricName&quot;: &quot;YARNMemoryAvailablePercentage&quot;,</span>
<span class="s2">        &quot;Namespace&quot;: &quot;AWS/ElasticMapReduce&quot;,</span>
<span class="s2">        &quot;Period&quot;: 300,</span>
<span class="s2">        &quot;Statistic&quot;: &quot;AVERAGE&quot;,</span>
<span class="s2">        &quot;Threshold&quot;: 15.0,</span>
<span class="s2">        &quot;Unit&quot;: &quot;PERCENT&quot;</span>
<span class="s2">      }</span>
<span class="s2">    }</span>
<span class="s2">  }</span>
<span class="s2">]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;bidPrice&quot;</span><span class="p">:</span> <span class="s2">&quot;0.30&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ebsConfig&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;size&quot;</span><span class="p">:</span> <span class="s2">&quot;40&quot;</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;gp2&quot;</span><span class="p">,</span>
            <span class="s2">&quot;volumesPerInstance&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="p">}],</span>
        <span class="s2">&quot;instanceCount&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="s2">&quot;c4.large&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">ebs_root_volume_size</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
    <span class="n">ec2_attributes</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;emrManagedMasterSecurityGroup&quot;</span><span class="p">:</span> <span class="n">aws_security_group</span><span class="p">[</span><span class="s2">&quot;sg&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="s2">&quot;emrManagedSlaveSecurityGroup&quot;</span><span class="p">:</span> <span class="n">aws_security_group</span><span class="p">[</span><span class="s2">&quot;sg&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="s2">&quot;instanceProfile&quot;</span><span class="p">:</span> <span class="n">aws_iam_instance_profile</span><span class="p">[</span><span class="s2">&quot;emr_profile&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
        <span class="s2">&quot;subnetId&quot;</span><span class="p">:</span> <span class="n">aws_subnet</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="p">},</span>
    <span class="n">keep_job_flow_alive_when_no_steps</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">master_instance_group</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="s2">&quot;m4.large&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">release_label</span><span class="o">=</span><span class="s2">&quot;emr-4.6.0&quot;</span><span class="p">,</span>
    <span class="n">service_role</span><span class="o">=</span><span class="n">aws_iam_role</span><span class="p">[</span><span class="s2">&quot;iam_emr_service_role&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;env&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
        <span class="s2">&quot;role&quot;</span><span class="p">:</span> <span class="s2">&quot;rolename&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">termination_protection</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">lifecycle</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;ignoreChanges&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;stepConcurrencyLevel&quot;</span><span class="p">,</span>
            <span class="s2">&quot;steps&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">},</span>
    <span class="n">steps</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;actionOnFailure&quot;</span><span class="p">:</span> <span class="s2">&quot;TERMINATE_CLUSTER&quot;</span><span class="p">,</span>
        <span class="s2">&quot;hadoopJarStep&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;args&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;state-pusher-script&quot;</span><span class="p">],</span>
            <span class="s2">&quot;jar&quot;</span><span class="p">:</span> <span class="s2">&quot;command-runner.jar&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Setup Hadoop Debugging&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="c1"># Map public IP on launch must be enabled for public (Internet accessible) subnets</span>
<span class="n">example_subnet</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Subnet</span><span class="p">(</span><span class="s2">&quot;exampleSubnet&quot;</span><span class="p">,</span> <span class="n">map_public_ip_on_launch</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">example_cluster</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;exampleCluster&quot;</span><span class="p">,</span>
    <span class="n">core_instance_group</span><span class="o">=</span><span class="p">{},</span>
    <span class="n">ec2_attributes</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;subnetId&quot;</span><span class="p">:</span> <span class="n">example_subnet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">master_instance_group</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;instanceCount&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">release_label</span><span class="o">=</span><span class="s2">&quot;emr-5.24.1&quot;</span><span class="p">,</span>
    <span class="n">termination_protection</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<p><strong>NOTE:</strong> This configuration demonstrates a minimal configuration needed to
boot an example EMR Cluster. It is not meant to display best practices. Please
use at your own risk.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">main_vpc</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Vpc</span><span class="p">(</span><span class="s2">&quot;mainVpc&quot;</span><span class="p">,</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;168.31.0.0/16&quot;</span><span class="p">,</span>
    <span class="n">enable_dns_hostnames</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;emr_test&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">main_subnet</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Subnet</span><span class="p">(</span><span class="s2">&quot;mainSubnet&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">main_vpc</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;168.31.0.0/20&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;emr_test&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="c1"># IAM role for EMR Service</span>
<span class="n">iam_emr_service_role</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;iamEmrServiceRole&quot;</span><span class="p">,</span> <span class="n">assume_role_policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;Version&quot;: &quot;2008-10-17&quot;,</span>
<span class="s2">  &quot;Statement&quot;: [</span>
<span class="s2">    {</span>
<span class="s2">      &quot;Sid&quot;: &quot;&quot;,</span>
<span class="s2">      &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">      &quot;Principal&quot;: {</span>
<span class="s2">        &quot;Service&quot;: &quot;elasticmapreduce.amazonaws.com&quot;</span>
<span class="s2">      },</span>
<span class="s2">      &quot;Action&quot;: &quot;sts:AssumeRole&quot;</span>
<span class="s2">    }</span>
<span class="s2">  ]</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="c1"># IAM Role for EC2 Instance Profile</span>
<span class="n">iam_emr_profile_role</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;iamEmrProfileRole&quot;</span><span class="p">,</span> <span class="n">assume_role_policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;Version&quot;: &quot;2008-10-17&quot;,</span>
<span class="s2">  &quot;Statement&quot;: [</span>
<span class="s2">    {</span>
<span class="s2">      &quot;Sid&quot;: &quot;&quot;,</span>
<span class="s2">      &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">      &quot;Principal&quot;: {</span>
<span class="s2">        &quot;Service&quot;: &quot;ec2.amazonaws.com&quot;</span>
<span class="s2">      },</span>
<span class="s2">      &quot;Action&quot;: &quot;sts:AssumeRole&quot;</span>
<span class="s2">    }</span>
<span class="s2">  ]</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">emr_profile</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">InstanceProfile</span><span class="p">(</span><span class="s2">&quot;emrProfile&quot;</span><span class="p">,</span> <span class="n">roles</span><span class="o">=</span><span class="p">[</span><span class="n">iam_emr_profile_role</span><span class="o">.</span><span class="n">name</span><span class="p">])</span>
<span class="n">cluster</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;cluster&quot;</span><span class="p">,</span>
    <span class="n">release_label</span><span class="o">=</span><span class="s2">&quot;emr-4.6.0&quot;</span><span class="p">,</span>
    <span class="n">applications</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;Spark&quot;</span><span class="p">],</span>
    <span class="n">ec2_attributes</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;subnetId&quot;</span><span class="p">:</span> <span class="n">main_subnet</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="s2">&quot;emrManagedMasterSecurityGroup&quot;</span><span class="p">:</span> <span class="n">aws_security_group</span><span class="p">[</span><span class="s2">&quot;allow_all&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="s2">&quot;emrManagedSlaveSecurityGroup&quot;</span><span class="p">:</span> <span class="n">aws_security_group</span><span class="p">[</span><span class="s2">&quot;allow_all&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="s2">&quot;instanceProfile&quot;</span><span class="p">:</span> <span class="n">emr_profile</span><span class="o">.</span><span class="n">arn</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">master_instance_type</span><span class="o">=</span><span class="s2">&quot;m5.xlarge&quot;</span><span class="p">,</span>
    <span class="n">core_instance_type</span><span class="o">=</span><span class="s2">&quot;m5.xlarge&quot;</span><span class="p">,</span>
    <span class="n">core_instance_count</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;role&quot;</span><span class="p">:</span> <span class="s2">&quot;rolename&quot;</span><span class="p">,</span>
        <span class="s2">&quot;dns_zone&quot;</span><span class="p">:</span> <span class="s2">&quot;env_zone&quot;</span><span class="p">,</span>
        <span class="s2">&quot;env&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;name-env&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">bootstrap_action</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;path&quot;</span><span class="p">:</span> <span class="s2">&quot;s3://elasticmapreduce/bootstrap-actions/run-if&quot;</span><span class="p">,</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;runif&quot;</span><span class="p">,</span>
        <span class="s2">&quot;args&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;instance.isMaster=true&quot;</span><span class="p">,</span>
            <span class="s2">&quot;echo running on master node&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">configurations_json</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;  [</span>
<span class="s2">    {</span>
<span class="s2">      &quot;Classification&quot;: &quot;hadoop-env&quot;,</span>
<span class="s2">      &quot;Configurations&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">          &quot;Classification&quot;: &quot;export&quot;,</span>
<span class="s2">          &quot;Properties&quot;: {</span>
<span class="s2">            &quot;JAVA_HOME&quot;: &quot;/usr/lib/jvm/java-1.8.0&quot;</span>
<span class="s2">          }</span>
<span class="s2">        }</span>
<span class="s2">      ],</span>
<span class="s2">      &quot;Properties&quot;: </span><span class="si">{}</span><span class="s2"></span>
<span class="s2">    },</span>
<span class="s2">    {</span>
<span class="s2">      &quot;Classification&quot;: &quot;spark-env&quot;,</span>
<span class="s2">      &quot;Configurations&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">          &quot;Classification&quot;: &quot;export&quot;,</span>
<span class="s2">          &quot;Properties&quot;: {</span>
<span class="s2">            &quot;JAVA_HOME&quot;: &quot;/usr/lib/jvm/java-1.8.0&quot;</span>
<span class="s2">          }</span>
<span class="s2">        }</span>
<span class="s2">      ],</span>
<span class="s2">      &quot;Properties&quot;: </span><span class="si">{}</span><span class="s2"></span>
<span class="s2">    }</span>
<span class="s2">  ]</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">service_role</span><span class="o">=</span><span class="n">iam_emr_service_role</span><span class="o">.</span><span class="n">arn</span><span class="p">)</span>
<span class="n">allow_access</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="s2">&quot;allowAccess&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Allow inbound traffic&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">main_vpc</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">ingress</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;fromPort&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
        <span class="s2">&quot;toPort&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
        <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;-1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;cidrBlocks&quot;</span><span class="p">:</span> <span class="n">main_vpc</span><span class="o">.</span><span class="n">cidr_block</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">egress</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;fromPort&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
        <span class="s2">&quot;toPort&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
        <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;-1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;cidrBlocks&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;0.0.0.0/0&quot;</span><span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;emr_test&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">gw</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">InternetGateway</span><span class="p">(</span><span class="s2">&quot;gw&quot;</span><span class="p">,</span> <span class="n">vpc_id</span><span class="o">=</span><span class="n">main_vpc</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">route_table</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">RouteTable</span><span class="p">(</span><span class="s2">&quot;routeTable&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">main_vpc</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">route</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;cidrBlock&quot;</span><span class="p">:</span> <span class="s2">&quot;0.0.0.0/0&quot;</span><span class="p">,</span>
        <span class="s2">&quot;gatewayId&quot;</span><span class="p">:</span> <span class="n">gw</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">}])</span>
<span class="n">main_route_table_association</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">MainRouteTableAssociation</span><span class="p">(</span><span class="s2">&quot;mainRouteTableAssociation&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">main_vpc</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">route_table_id</span><span class="o">=</span><span class="n">route_table</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="c1">###</span>
<span class="n">iam_emr_service_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicy</span><span class="p">(</span><span class="s2">&quot;iamEmrServicePolicy&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">iam_emr_service_role</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">    &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">    &quot;Statement&quot;: [{</span>
<span class="s2">        &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">        &quot;Resource&quot;: &quot;*&quot;,</span>
<span class="s2">        &quot;Action&quot;: [</span>
<span class="s2">            &quot;ec2:AuthorizeSecurityGroupEgress&quot;,</span>
<span class="s2">            &quot;ec2:AuthorizeSecurityGroupIngress&quot;,</span>
<span class="s2">            &quot;ec2:CancelSpotInstanceRequests&quot;,</span>
<span class="s2">            &quot;ec2:CreateNetworkInterface&quot;,</span>
<span class="s2">            &quot;ec2:CreateSecurityGroup&quot;,</span>
<span class="s2">            &quot;ec2:CreateTags&quot;,</span>
<span class="s2">            &quot;ec2:DeleteNetworkInterface&quot;,</span>
<span class="s2">            &quot;ec2:DeleteSecurityGroup&quot;,</span>
<span class="s2">            &quot;ec2:DeleteTags&quot;,</span>
<span class="s2">            &quot;ec2:DescribeAvailabilityZones&quot;,</span>
<span class="s2">            &quot;ec2:DescribeAccountAttributes&quot;,</span>
<span class="s2">            &quot;ec2:DescribeDhcpOptions&quot;,</span>
<span class="s2">            &quot;ec2:DescribeInstanceStatus&quot;,</span>
<span class="s2">            &quot;ec2:DescribeInstances&quot;,</span>
<span class="s2">            &quot;ec2:DescribeKeyPairs&quot;,</span>
<span class="s2">            &quot;ec2:DescribeNetworkAcls&quot;,</span>
<span class="s2">            &quot;ec2:DescribeNetworkInterfaces&quot;,</span>
<span class="s2">            &quot;ec2:DescribePrefixLists&quot;,</span>
<span class="s2">            &quot;ec2:DescribeRouteTables&quot;,</span>
<span class="s2">            &quot;ec2:DescribeSecurityGroups&quot;,</span>
<span class="s2">            &quot;ec2:DescribeSpotInstanceRequests&quot;,</span>
<span class="s2">            &quot;ec2:DescribeSpotPriceHistory&quot;,</span>
<span class="s2">            &quot;ec2:DescribeSubnets&quot;,</span>
<span class="s2">            &quot;ec2:DescribeVpcAttribute&quot;,</span>
<span class="s2">            &quot;ec2:DescribeVpcEndpoints&quot;,</span>
<span class="s2">            &quot;ec2:DescribeVpcEndpointServices&quot;,</span>
<span class="s2">            &quot;ec2:DescribeVpcs&quot;,</span>
<span class="s2">            &quot;ec2:DetachNetworkInterface&quot;,</span>
<span class="s2">            &quot;ec2:ModifyImageAttribute&quot;,</span>
<span class="s2">            &quot;ec2:ModifyInstanceAttribute&quot;,</span>
<span class="s2">            &quot;ec2:RequestSpotInstances&quot;,</span>
<span class="s2">            &quot;ec2:RevokeSecurityGroupEgress&quot;,</span>
<span class="s2">            &quot;ec2:RunInstances&quot;,</span>
<span class="s2">            &quot;ec2:TerminateInstances&quot;,</span>
<span class="s2">            &quot;ec2:DeleteVolume&quot;,</span>
<span class="s2">            &quot;ec2:DescribeVolumeStatus&quot;,</span>
<span class="s2">            &quot;ec2:DescribeVolumes&quot;,</span>
<span class="s2">            &quot;ec2:DetachVolume&quot;,</span>
<span class="s2">            &quot;iam:GetRole&quot;,</span>
<span class="s2">            &quot;iam:GetRolePolicy&quot;,</span>
<span class="s2">            &quot;iam:ListInstanceProfiles&quot;,</span>
<span class="s2">            &quot;iam:ListRolePolicies&quot;,</span>
<span class="s2">            &quot;iam:PassRole&quot;,</span>
<span class="s2">            &quot;s3:CreateBucket&quot;,</span>
<span class="s2">            &quot;s3:Get*&quot;,</span>
<span class="s2">            &quot;s3:List*&quot;,</span>
<span class="s2">            &quot;sdb:BatchPutAttributes&quot;,</span>
<span class="s2">            &quot;sdb:Select&quot;,</span>
<span class="s2">            &quot;sqs:CreateQueue&quot;,</span>
<span class="s2">            &quot;sqs:Delete*&quot;,</span>
<span class="s2">            &quot;sqs:GetQueue*&quot;,</span>
<span class="s2">            &quot;sqs:PurgeQueue&quot;,</span>
<span class="s2">            &quot;sqs:ReceiveMessage&quot;</span>
<span class="s2">        ]</span>
<span class="s2">    }]</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">iam_emr_profile_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicy</span><span class="p">(</span><span class="s2">&quot;iamEmrProfilePolicy&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">iam_emr_profile_role</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">    &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">    &quot;Statement&quot;: [{</span>
<span class="s2">        &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">        &quot;Resource&quot;: &quot;*&quot;,</span>
<span class="s2">        &quot;Action&quot;: [</span>
<span class="s2">            &quot;cloudwatch:*&quot;,</span>
<span class="s2">            &quot;dynamodb:*&quot;,</span>
<span class="s2">            &quot;ec2:Describe*&quot;,</span>
<span class="s2">            &quot;elasticmapreduce:Describe*&quot;,</span>
<span class="s2">            &quot;elasticmapreduce:ListBootstrapActions&quot;,</span>
<span class="s2">            &quot;elasticmapreduce:ListClusters&quot;,</span>
<span class="s2">            &quot;elasticmapreduce:ListInstanceGroups&quot;,</span>
<span class="s2">            &quot;elasticmapreduce:ListInstances&quot;,</span>
<span class="s2">            &quot;elasticmapreduce:ListSteps&quot;,</span>
<span class="s2">            &quot;kinesis:CreateStream&quot;,</span>
<span class="s2">            &quot;kinesis:DeleteStream&quot;,</span>
<span class="s2">            &quot;kinesis:DescribeStream&quot;,</span>
<span class="s2">            &quot;kinesis:GetRecords&quot;,</span>
<span class="s2">            &quot;kinesis:GetShardIterator&quot;,</span>
<span class="s2">            &quot;kinesis:MergeShards&quot;,</span>
<span class="s2">            &quot;kinesis:PutRecord&quot;,</span>
<span class="s2">            &quot;kinesis:SplitShard&quot;,</span>
<span class="s2">            &quot;rds:Describe*&quot;,</span>
<span class="s2">            &quot;s3:*&quot;,</span>
<span class="s2">            &quot;sdb:*&quot;,</span>
<span class="s2">            &quot;sns:*&quot;,</span>
<span class="s2">            &quot;sqs:*&quot;</span>
<span class="s2">        ]</span>
<span class="s2">    }]</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_info</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.</p></li>
<li><p><strong>applications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of applications for the cluster. Valid values are: <code class="docutils literal notranslate"><span class="pre">Flink</span></code>, <code class="docutils literal notranslate"><span class="pre">Hadoop</span></code>, <code class="docutils literal notranslate"><span class="pre">Hive</span></code>, <code class="docutils literal notranslate"><span class="pre">Mahout</span></code>, <code class="docutils literal notranslate"><span class="pre">Pig</span></code>, <code class="docutils literal notranslate"><span class="pre">Spark</span></code>, and <code class="docutils literal notranslate"><span class="pre">JupyterHub</span></code> (as of EMR 5.14.0). Case insensitive</p></li>
<li><p><strong>autoscaling_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.</p></li>
<li><p><strong>bootstrap_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ordered list of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below.</p></li>
<li><p><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – List of configurations supplied for the EMR cluster you are creating</p></li>
<li><p><strong>configurations_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for supplying list of configurations for the EMR cluster.</p></li>
<li><p><strong>core_instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_count</span></code> argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster’s master node and use the remainder of the nodes (<code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code>-1) as core nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p></li>
<li><p><strong>core_instance_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core">core node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code> argument, <code class="docutils literal notranslate"><span class="pre">core_instance_type</span></code> argument, or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p></li>
<li><p><strong>core_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the slave nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p></li>
<li><p><strong>custom_ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.</p></li>
<li><p><strong>ebs_root_volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.</p></li>
<li><p><strong>ec2_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Attributes for the EC2 instances running the job flow. Defined below</p></li>
<li><p><strong>instance_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block, <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block and <cite>``emr.InstanceGroup`</cite> resource(s) &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html">https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html</a>&gt;`_ instead. A list of <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> objects for each instance group in the cluster. Exactly one of <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> and <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> must be specified. If <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> is set, then it must contain a configuration block for at least the <code class="docutils literal notranslate"><span class="pre">MASTER</span></code> instance group type (as well as any additional instance groups). Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration blocks are set. Defined below</p></li>
<li><p><strong>keep_job_flow_alive_when_no_steps</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Switch on/off run cluster with no steps or when all steps are complete (default is on)</p></li>
<li><p><strong>kerberos_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kerberos configuration for the cluster. Defined below</p></li>
<li><p><strong>log_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created</p></li>
<li><p><strong>master_instance_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master">master node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> argument or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p>
</p></li>
<li><p><strong>master_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the master node. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the step.</p></li>
<li><p><strong>release_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The release label for the Amazon EMR release</p></li>
<li><p><strong>scale_down_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an <code class="docutils literal notranslate"><span class="pre">instance</span> <span class="pre">group</span></code> is resized.</p></li>
<li><p><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 4.8.0 or greater</p></li>
<li><p><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role that will be assumed by the Amazon EMR service to access AWS resources</p></li>
<li><p><strong>step_concurrency_level</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 5.28.0 or greater. (default is 1)</p></li>
<li><p><strong>steps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize <cite>``ignoreChanges`</cite> &lt;<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges">https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges</a>&gt;`_ if other steps are being managed outside of this provider.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – list of tags to apply to the EMR Cluster</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Switch on/off termination protection (default is <code class="docutils literal notranslate"><span class="pre">false</span></code>, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>visible_to_all_users</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>bootstrap_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of command line arguments passed to the JAR file’s main function when executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the step.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Location of the script to run during a bootstrap action. Can be either a location in Amazon S3 or on a local file system</p></li>
</ul>
<p>The <strong>core_instance_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of I/O operations per second (IOPS) that the volume supports</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The volume size, in gibibytes (GiB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type. Valid options are <code class="docutils literal notranslate"><span class="pre">gp2</span></code>, <code class="docutils literal notranslate"><span class="pre">io1</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">st1</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">EBS Volume Types</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource’s <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> to be configured. Public (Internet accessible) instances must be created in VPC subnets that have <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/subnet.html#map_public_ip_on_launch">map public IP on launch</a> enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the <code class="docutils literal notranslate"><span class="pre">termination_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> configuration applied before destroying this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the step.</p></li>
</ul>
<p>The <strong>ec2_attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalMasterSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String containing a comma separated list of additional Amazon EC2 security group IDs for the master node</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalSlaveSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String containing a comma separated list of additional Amazon EC2 security group IDs for the slave nodes as a comma separated string</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedMasterSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the Amazon EC2 EMR-Managed security group for the master node</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedSlaveSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the Amazon EC2 EMR-Managed security group for the slave nodes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instance Profile for EC2 instances of the cluster assume this role</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon EC2 key pair that can be used to ssh to the master node as the user called <code class="docutils literal notranslate"><span class="pre">hadoop</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccessSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the Amazon EC2 service-access security group - required when the cluster runs on a private subnet</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - VPC subnet id where you want the job flow to launch. Cannot specify the <code class="docutils literal notranslate"><span class="pre">cc1.4xlarge</span></code> instance type for nodes of a job flow launched in a Amazon VPC</p></li>
</ul>
<p>The <strong>instance_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of I/O operations per second (IOPS) that the volume supports</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The volume size, in gibibytes (GiB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type. Valid options are <code class="docutils literal notranslate"><span class="pre">gp2</span></code>, <code class="docutils literal notranslate"><span class="pre">io1</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">st1</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">EBS Volume Types</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource’s <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> to be configured. Public (Internet accessible) instances must be created in VPC subnets that have <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/subnet.html#map_public_ip_on_launch">map public IP on launch</a> enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the <code class="docutils literal notranslate"><span class="pre">termination_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> configuration applied before destroying this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role of the instance group in the cluster. Valid values are: <code class="docutils literal notranslate"><span class="pre">MASTER</span></code>, <code class="docutils literal notranslate"><span class="pre">CORE</span></code>, and <code class="docutils literal notranslate"><span class="pre">TASK</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the step.</p></li>
</ul>
<p>The <strong>kerberos_attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Active Directory password for <code class="docutils literal notranslate"><span class="pre">ad_domain_join_user</span></code>. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinUser</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustPrincipalPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kdcAdminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Kerberos realm to which all nodes in a cluster belong. For example, <code class="docutils literal notranslate"><span class="pre">EC2.INTERNAL</span></code></p></li>
</ul>
<p>The <strong>master_instance_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of I/O operations per second (IOPS) that the volume supports</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The volume size, in gibibytes (GiB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type. Valid options are <code class="docutils literal notranslate"><span class="pre">gp2</span></code>, <code class="docutils literal notranslate"><span class="pre">io1</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">st1</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">EBS Volume Types</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource’s <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> to be configured. Public (Internet accessible) instances must be created in VPC subnets that have <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/subnet.html#map_public_ip_on_launch">map public IP on launch</a> enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the <code class="docutils literal notranslate"><span class="pre">termination_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> configuration applied before destroying this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the step.</p></li>
</ul>
<p>The <strong>steps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to take if the step fails. Valid values: <code class="docutils literal notranslate"><span class="pre">TERMINATE_JOB_FLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">TERMINATE_CLUSTER</span></code>, <code class="docutils literal notranslate"><span class="pre">CANCEL_AND_WAIT</span></code>, and <code class="docutils literal notranslate"><span class="pre">CONTINUE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hadoopJarStep</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The JAR file used for the step. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of command line arguments passed to the JAR file’s main function when executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jar</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to a JAR file run during the step.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Key-Value map of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the step.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.additional_info">
<code class="sig-name descname">additional_info</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.additional_info" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.applications">
<code class="sig-name descname">applications</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.applications" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of applications for the cluster. Valid values are: <code class="docutils literal notranslate"><span class="pre">Flink</span></code>, <code class="docutils literal notranslate"><span class="pre">Hadoop</span></code>, <code class="docutils literal notranslate"><span class="pre">Hive</span></code>, <code class="docutils literal notranslate"><span class="pre">Mahout</span></code>, <code class="docutils literal notranslate"><span class="pre">Pig</span></code>, <code class="docutils literal notranslate"><span class="pre">Spark</span></code>, and <code class="docutils literal notranslate"><span class="pre">JupyterHub</span></code> (as of EMR 5.14.0). Case insensitive</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.autoscaling_role">
<code class="sig-name descname">autoscaling_role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.autoscaling_role" title="Permalink to this definition">¶</a></dt>
<dd><p>An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.bootstrap_actions">
<code class="sig-name descname">bootstrap_actions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.bootstrap_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>Ordered list of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of command line arguments passed to the JAR file’s main function when executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the step.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Location of the script to run during a bootstrap action. Can be either a location in Amazon S3 or on a local file system</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.configurations">
<code class="sig-name descname">configurations</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of configurations supplied for the EMR cluster you are creating</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.configurations_json">
<code class="sig-name descname">configurations_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.configurations_json" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON string for supplying list of configurations for the EMR cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.core_instance_count">
<code class="sig-name descname">core_instance_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.core_instance_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_count</span></code> argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster’s master node and use the remainder of the nodes (<code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code>-1) as core nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.core_instance_group">
<code class="sig-name descname">core_instance_group</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.core_instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core">core node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code> argument, <code class="docutils literal notranslate"><span class="pre">core_instance_type</span></code> argument, or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of I/O operations per second (IOPS) that the volume supports</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The volume size, in gibibytes (GiB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The volume type. Valid options are <code class="docutils literal notranslate"><span class="pre">gp2</span></code>, <code class="docutils literal notranslate"><span class="pre">io1</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">st1</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">EBS Volume Types</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource’s <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> to be configured. Public (Internet accessible) instances must be created in VPC subnets that have <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/subnet.html#map_public_ip_on_launch">map public IP on launch</a> enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the <code class="docutils literal notranslate"><span class="pre">termination_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> configuration applied before destroying this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the step.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.core_instance_type">
<code class="sig-name descname">core_instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.core_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the slave nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.custom_ami_id">
<code class="sig-name descname">custom_ami_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.custom_ami_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.ebs_root_volume_size">
<code class="sig-name descname">ebs_root_volume_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.ebs_root_volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.ec2_attributes">
<code class="sig-name descname">ec2_attributes</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.ec2_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Attributes for the EC2 instances running the job flow. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalMasterSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String containing a comma separated list of additional Amazon EC2 security group IDs for the master node</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalSlaveSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String containing a comma separated list of additional Amazon EC2 security group IDs for the slave nodes as a comma separated string</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedMasterSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier of the Amazon EC2 EMR-Managed security group for the master node</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedSlaveSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier of the Amazon EC2 EMR-Managed security group for the slave nodes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Instance Profile for EC2 instances of the cluster assume this role</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon EC2 key pair that can be used to ssh to the master node as the user called <code class="docutils literal notranslate"><span class="pre">hadoop</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccessSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier of the Amazon EC2 service-access security group - required when the cluster runs on a private subnet</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - VPC subnet id where you want the job flow to launch. Cannot specify the <code class="docutils literal notranslate"><span class="pre">cc1.4xlarge</span></code> instance type for nodes of a job flow launched in a Amazon VPC</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.instance_groups">
<code class="sig-name descname">instance_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.instance_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block, <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block and <cite>``emr.InstanceGroup`</cite> resource(s) &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html">https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html</a>&gt;`_ instead. A list of <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> objects for each instance group in the cluster. Exactly one of <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> and <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> must be specified. If <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> is set, then it must contain a configuration block for at least the <code class="docutils literal notranslate"><span class="pre">MASTER</span></code> instance group type (as well as any additional instance groups). Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration blocks are set. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of I/O operations per second (IOPS) that the volume supports</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The volume size, in gibibytes (GiB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The volume type. Valid options are <code class="docutils literal notranslate"><span class="pre">gp2</span></code>, <code class="docutils literal notranslate"><span class="pre">io1</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">st1</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">EBS Volume Types</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource’s <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> to be configured. Public (Internet accessible) instances must be created in VPC subnets that have <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/subnet.html#map_public_ip_on_launch">map public IP on launch</a> enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the <code class="docutils literal notranslate"><span class="pre">termination_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> configuration applied before destroying this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The role of the instance group in the cluster. Valid values are: <code class="docutils literal notranslate"><span class="pre">MASTER</span></code>, <code class="docutils literal notranslate"><span class="pre">CORE</span></code>, and <code class="docutils literal notranslate"><span class="pre">TASK</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the step.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.keep_job_flow_alive_when_no_steps">
<code class="sig-name descname">keep_job_flow_alive_when_no_steps</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.keep_job_flow_alive_when_no_steps" title="Permalink to this definition">¶</a></dt>
<dd><p>Switch on/off run cluster with no steps or when all steps are complete (default is on)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.kerberos_attributes">
<code class="sig-name descname">kerberos_attributes</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.kerberos_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Kerberos configuration for the cluster. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Active Directory password for <code class="docutils literal notranslate"><span class="pre">ad_domain_join_user</span></code>. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinUser</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustPrincipalPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kdcAdminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Kerberos realm to which all nodes in a cluster belong. For example, <code class="docutils literal notranslate"><span class="pre">EC2.INTERNAL</span></code></p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.log_uri">
<code class="sig-name descname">log_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.log_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.master_instance_group">
<code class="sig-name descname">master_instance_group</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.master_instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master">master node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> argument or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of I/O operations per second (IOPS) that the volume supports</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The volume size, in gibibytes (GiB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The volume type. Valid options are <code class="docutils literal notranslate"><span class="pre">gp2</span></code>, <code class="docutils literal notranslate"><span class="pre">io1</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">st1</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">EBS Volume Types</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource’s <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> to be configured. Public (Internet accessible) instances must be created in VPC subnets that have <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/subnet.html#map_public_ip_on_launch">map public IP on launch</a> enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the <code class="docutils literal notranslate"><span class="pre">termination_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> configuration applied before destroying this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the step.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.master_instance_type">
<code class="sig-name descname">master_instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.master_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the master node. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.master_public_dns">
<code class="sig-name descname">master_public_dns</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.master_public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The public DNS name of the master EC2 instance.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">core_instance_group.0.id</span></code> - Core node type Instance Group ID, if using Instance Group for this node type.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the step.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.release_label">
<code class="sig-name descname">release_label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.release_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The release label for the Amazon EMR release</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.scale_down_behavior">
<code class="sig-name descname">scale_down_behavior</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.scale_down_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an <code class="docutils literal notranslate"><span class="pre">instance</span> <span class="pre">group</span></code> is resized.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.security_configuration">
<code class="sig-name descname">security_configuration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.security_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 4.8.0 or greater</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.service_role">
<code class="sig-name descname">service_role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role that will be assumed by the Amazon EMR service to access AWS resources</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.step_concurrency_level">
<code class="sig-name descname">step_concurrency_level</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.step_concurrency_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 5.28.0 or greater. (default is 1)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.steps">
<code class="sig-name descname">steps</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.steps" title="Permalink to this definition">¶</a></dt>
<dd><p>List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize <cite>``ignoreChanges`</cite> &lt;<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges">https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges</a>&gt;`_ if other steps are being managed outside of this provider.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action to take if the step fails. Valid values: <code class="docutils literal notranslate"><span class="pre">TERMINATE_JOB_FLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">TERMINATE_CLUSTER</span></code>, <code class="docutils literal notranslate"><span class="pre">CANCEL_AND_WAIT</span></code>, and <code class="docutils literal notranslate"><span class="pre">CONTINUE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hadoopJarStep</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The JAR file used for the step. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of command line arguments passed to the JAR file’s main function when executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jar</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Path to a JAR file run during the step.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainClass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Key-Value map of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the step.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>list of tags to apply to the EMR Cluster</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.termination_protection">
<code class="sig-name descname">termination_protection</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Switch on/off termination protection (default is <code class="docutils literal notranslate"><span class="pre">false</span></code>, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.Cluster.visible_to_all_users">
<code class="sig-name descname">visible_to_all_users</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.visible_to_all_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default <code class="docutils literal notranslate"><span class="pre">true</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.emr.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscaling_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_ami_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_root_volume_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ec2_attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_job_flow_alive_when_no_steps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kerberos_attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_public_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scale_down_behavior</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">step_concurrency_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steps</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visible_to_all_users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_info</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.</p></li>
<li><p><strong>applications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of applications for the cluster. Valid values are: <code class="docutils literal notranslate"><span class="pre">Flink</span></code>, <code class="docutils literal notranslate"><span class="pre">Hadoop</span></code>, <code class="docutils literal notranslate"><span class="pre">Hive</span></code>, <code class="docutils literal notranslate"><span class="pre">Mahout</span></code>, <code class="docutils literal notranslate"><span class="pre">Pig</span></code>, <code class="docutils literal notranslate"><span class="pre">Spark</span></code>, and <code class="docutils literal notranslate"><span class="pre">JupyterHub</span></code> (as of EMR 5.14.0). Case insensitive</p></li>
<li><p><strong>autoscaling_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.</p></li>
<li><p><strong>bootstrap_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ordered list of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below.</p></li>
<li><p><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – List of configurations supplied for the EMR cluster you are creating</p></li>
<li><p><strong>configurations_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for supplying list of configurations for the EMR cluster.</p></li>
<li><p><strong>core_instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_count</span></code> argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster’s master node and use the remainder of the nodes (<code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code>-1) as core nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p></li>
<li><p><strong>core_instance_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core">core node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code> argument, <code class="docutils literal notranslate"><span class="pre">core_instance_type</span></code> argument, or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p>
</p></li>
<li><p><strong>core_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the slave nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p></li>
<li><p><strong>custom_ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.</p></li>
<li><p><strong>ebs_root_volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.</p></li>
<li><p><strong>ec2_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Attributes for the EC2 instances running the job flow. Defined below</p></li>
<li><p><strong>instance_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block, <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block and <cite>``emr.InstanceGroup`</cite> resource(s) &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html">https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html</a>&gt;`_ instead. A list of <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> objects for each instance group in the cluster. Exactly one of <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> and <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> must be specified. If <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> is set, then it must contain a configuration block for at least the <code class="docutils literal notranslate"><span class="pre">MASTER</span></code> instance group type (as well as any additional instance groups). Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration blocks are set. Defined below</p></li>
<li><p><strong>keep_job_flow_alive_when_no_steps</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Switch on/off run cluster with no steps or when all steps are complete (default is on)</p></li>
<li><p><strong>kerberos_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kerberos configuration for the cluster. Defined below</p></li>
<li><p><strong>log_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created</p></li>
<li><p><strong>master_instance_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master">master node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> argument or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p>
</p></li>
<li><p><strong>master_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the master node. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p></li>
<li><p><strong>master_public_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public DNS name of the master EC2 instance.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `core_instance_group.0.id` - Core node type Instance Group ID, if using Instance Group for this node type.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the step.</p></li>
<li><p><strong>release_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The release label for the Amazon EMR release</p></li>
<li><p><strong>scale_down_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an <code class="docutils literal notranslate"><span class="pre">instance</span> <span class="pre">group</span></code> is resized.</p></li>
<li><p><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 4.8.0 or greater</p></li>
<li><p><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role that will be assumed by the Amazon EMR service to access AWS resources</p></li>
<li><p><strong>step_concurrency_level</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 5.28.0 or greater. (default is 1)</p></li>
<li><p><strong>steps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize <cite>``ignoreChanges`</cite> &lt;<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges">https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges</a>&gt;`_ if other steps are being managed outside of this provider.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – list of tags to apply to the EMR Cluster</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Switch on/off termination protection (default is <code class="docutils literal notranslate"><span class="pre">false</span></code>, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>visible_to_all_users</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>bootstrap_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of command line arguments passed to the JAR file’s main function when executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the step.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Location of the script to run during a bootstrap action. Can be either a location in Amazon S3 or on a local file system</p></li>
</ul>
<p>The <strong>core_instance_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of I/O operations per second (IOPS) that the volume supports</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The volume size, in gibibytes (GiB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type. Valid options are <code class="docutils literal notranslate"><span class="pre">gp2</span></code>, <code class="docutils literal notranslate"><span class="pre">io1</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">st1</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">EBS Volume Types</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource’s <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> to be configured. Public (Internet accessible) instances must be created in VPC subnets that have <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/subnet.html#map_public_ip_on_launch">map public IP on launch</a> enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the <code class="docutils literal notranslate"><span class="pre">termination_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> configuration applied before destroying this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the step.</p></li>
</ul>
<p>The <strong>ec2_attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalMasterSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String containing a comma separated list of additional Amazon EC2 security group IDs for the master node</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalSlaveSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String containing a comma separated list of additional Amazon EC2 security group IDs for the slave nodes as a comma separated string</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedMasterSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the Amazon EC2 EMR-Managed security group for the master node</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedSlaveSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the Amazon EC2 EMR-Managed security group for the slave nodes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instance Profile for EC2 instances of the cluster assume this role</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon EC2 key pair that can be used to ssh to the master node as the user called <code class="docutils literal notranslate"><span class="pre">hadoop</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccessSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the Amazon EC2 service-access security group - required when the cluster runs on a private subnet</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - VPC subnet id where you want the job flow to launch. Cannot specify the <code class="docutils literal notranslate"><span class="pre">cc1.4xlarge</span></code> instance type for nodes of a job flow launched in a Amazon VPC</p></li>
</ul>
<p>The <strong>instance_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of I/O operations per second (IOPS) that the volume supports</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The volume size, in gibibytes (GiB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type. Valid options are <code class="docutils literal notranslate"><span class="pre">gp2</span></code>, <code class="docutils literal notranslate"><span class="pre">io1</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">st1</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">EBS Volume Types</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource’s <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> to be configured. Public (Internet accessible) instances must be created in VPC subnets that have <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/subnet.html#map_public_ip_on_launch">map public IP on launch</a> enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the <code class="docutils literal notranslate"><span class="pre">termination_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> configuration applied before destroying this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The role of the instance group in the cluster. Valid values are: <code class="docutils literal notranslate"><span class="pre">MASTER</span></code>, <code class="docutils literal notranslate"><span class="pre">CORE</span></code>, and <code class="docutils literal notranslate"><span class="pre">TASK</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the step.</p></li>
</ul>
<p>The <strong>kerberos_attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Active Directory password for <code class="docutils literal notranslate"><span class="pre">ad_domain_join_user</span></code>. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinUser</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustPrincipalPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kdcAdminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Kerberos realm to which all nodes in a cluster belong. For example, <code class="docutils literal notranslate"><span class="pre">EC2.INTERNAL</span></code></p></li>
</ul>
<p>The <strong>master_instance_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of I/O operations per second (IOPS) that the volume supports</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The volume size, in gibibytes (GiB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type. Valid options are <code class="docutils literal notranslate"><span class="pre">gp2</span></code>, <code class="docutils literal notranslate"><span class="pre">io1</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">st1</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">EBS Volume Types</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource’s <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> to be configured. Public (Internet accessible) instances must be created in VPC subnets that have <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/subnet.html#map_public_ip_on_launch">map public IP on launch</a> enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the <code class="docutils literal notranslate"><span class="pre">termination_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> configuration applied before destroying this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the step.</p></li>
</ul>
<p>The <strong>steps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action to take if the step fails. Valid values: <code class="docutils literal notranslate"><span class="pre">TERMINATE_JOB_FLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">TERMINATE_CLUSTER</span></code>, <code class="docutils literal notranslate"><span class="pre">CANCEL_AND_WAIT</span></code>, and <code class="docutils literal notranslate"><span class="pre">CONTINUE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hadoopJarStep</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The JAR file used for the step. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of command line arguments passed to the JAR file’s main function when executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jar</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to a JAR file run during the step.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Key-Value map of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the step.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.emr.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.InstanceGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.emr.</code><code class="sig-name descname">InstanceGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscaling_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bid_price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic MapReduce Cluster Instance Group configuration.
See <a class="reference external" href="https://aws.amazon.com/documentation/emr/">Amazon Elastic MapReduce Documentation</a> for more information.</p>
<blockquote>
<div><p><strong>NOTE:</strong> At this time, Instance Groups cannot be destroyed through the API nor
web interface. Instance Groups are destroyed when the EMR Cluster is destroyed.
this provider will resize any Instance Group to zero when destroying the resource.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">task</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">InstanceGroup</span><span class="p">(</span><span class="s2">&quot;task&quot;</span><span class="p">,</span>
    <span class="n">cluster_id</span><span class="o">=</span><span class="n">aws_emr_cluster</span><span class="p">[</span><span class="s2">&quot;tf-test-cluster&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">instance_count</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="s2">&quot;m5.xlarge&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscaling_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p>
</p></li>
<li><p><strong>bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, the bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>configurations_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for supplying list of configurations specific to the EMR instance group. Note that this can only be changed when using EMR release 5.21 or later.</p></li>
<li><p><strong>ebs_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ebs_config</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.</p></li>
<li><p><strong>instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – target number of instances for the instance group. defaults to 0.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly name given to the instance group. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of I/O operations per second (IOPS) that the volume supports.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type. Valid options are ‘gp2’, ‘io1’ and ‘standard’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of EBS Volumes to attach per instance.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.emr.InstanceGroup.autoscaling_policy">
<code class="sig-name descname">autoscaling_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.autoscaling_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.InstanceGroup.bid_price">
<code class="sig-name descname">bid_price</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.bid_price" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.InstanceGroup.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.InstanceGroup.configurations_json">
<code class="sig-name descname">configurations_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.configurations_json" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON string for supplying list of configurations specific to the EMR instance group. Note that this can only be changed when using EMR release 5.21 or later.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.InstanceGroup.ebs_configs">
<code class="sig-name descname">ebs_configs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.ebs_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">ebs_config</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of I/O operations per second (IOPS) that the volume supports.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The volume type. Valid options are ‘gp2’, ‘io1’ and ‘standard’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of EBS Volumes to attach per instance.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.InstanceGroup.ebs_optimized">
<code class="sig-name descname">ebs_optimized</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.InstanceGroup.instance_count">
<code class="sig-name descname">instance_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.instance_count" title="Permalink to this definition">¶</a></dt>
<dd><p>target number of instances for the instance group. defaults to 0.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.InstanceGroup.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.InstanceGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human friendly name given to the instance group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.emr.InstanceGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscaling_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bid_price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configurations_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ebs_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">running_instance_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscaling_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p>
</p></li>
<li><p><strong>bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, the bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>configurations_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for supplying list of configurations specific to the EMR instance group. Note that this can only be changed when using EMR release 5.21 or later.</p></li>
<li><p><strong>ebs_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ebs_config</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.</p></li>
<li><p><strong>instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – target number of instances for the instance group. defaults to 0.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly name given to the instance group. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of I/O operations per second (IOPS) that the volume supports.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type. Valid options are ‘gp2’, ‘io1’ and ‘standard’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of EBS Volumes to attach per instance.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.emr.InstanceGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.InstanceGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.SecurityConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.emr.</code><code class="sig-name descname">SecurityConfiguration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage AWS EMR Security Configurations</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">emr</span><span class="o">.</span><span class="n">SecurityConfiguration</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="n">configuration</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;EncryptionConfiguration&quot;: {</span>
<span class="s2">    &quot;AtRestEncryptionConfiguration&quot;: {</span>
<span class="s2">      &quot;S3EncryptionConfiguration&quot;: {</span>
<span class="s2">        &quot;EncryptionMode&quot;: &quot;SSE-S3&quot;</span>
<span class="s2">      },</span>
<span class="s2">      &quot;LocalDiskEncryptionConfiguration&quot;: {</span>
<span class="s2">        &quot;EncryptionKeyProviderType&quot;: &quot;AwsKms&quot;,</span>
<span class="s2">        &quot;AwsKmsKey&quot;: &quot;arn:aws:kms:us-west-2:187416307283:alias/tf_emr_test_key&quot;</span>
<span class="s2">      }</span>
<span class="s2">    },</span>
<span class="s2">    &quot;EnableInTransitEncryption&quot;: false,</span>
<span class="s2">    &quot;EnableAtRestEncryption&quot;: true</span>
<span class="s2">  }</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON formatted Security Configuration</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the EMR Security Configuration. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.configuration">
<code class="sig-name descname">configuration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON formatted Security Configuration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.creation_date">
<code class="sig-name descname">creation_date</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Date the Security Configuration was created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the EMR Security Configuration. By default generated by this provider.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.emr.SecurityConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_date</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON formatted Security Configuration</p></li>
<li><p><strong>creation_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Date the Security Configuration was created</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the EMR Security Configuration. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.emr.SecurityConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.SecurityConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
