---
title: Module aws
title_tag: Module aws | Package pulumi_signalfx | Python SDK
linktitle: aws
notitle: true
---

<div class="section" id="aws">
<h1>aws<a class="headerlink" href="#aws" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-signalfx/issues">pulumi/pulumi-signalfx repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/issues">terraform-providers/terraform-provider-signalfx repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_signalfx.aws"></span><dl class="py class">
<dt id="pulumi_signalfx.aws.ExternalIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.aws.</code><code class="sig-name descname">ExternalIntegration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx AWS CloudWatch integrations using Role ARNs. For help with this integration see <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#connect-to-aws">Connect to AWS CloudWatch</a>.</p>
<blockquote>
<div><p><strong>NOTE</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider.</p>
<p><strong>WARNING</strong> This resource implements a part of a workflow. You must use it with <code class="docutils literal notranslate"><span class="pre">aws.Integration</span></code>. Check with SignalFx support for your realm’s AWS account id.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">aws_myteam_extern</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">aws</span><span class="o">.</span><span class="n">ExternalIntegration</span><span class="p">(</span><span class="s2">&quot;awsMyteamExtern&quot;</span><span class="p">)</span>
<span class="n">signalfx_assume_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">get_policy_document</span><span class="p">(</span><span class="n">statement</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;actions&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;sts:AssumeRole&quot;</span><span class="p">],</span>
    <span class="s2">&quot;principals&quot;</span><span class="p">:</span> <span class="p">[{</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
        <span class="s2">&quot;identifiers&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">aws_myteam_extern</span><span class="o">.</span><span class="n">signalfx_aws_account</span><span class="p">],</span>
    <span class="p">}],</span>
    <span class="s2">&quot;condition&quot;</span><span class="p">:</span> <span class="p">[{</span>
        <span class="s2">&quot;test&quot;</span><span class="p">:</span> <span class="s2">&quot;StringEquals&quot;</span><span class="p">,</span>
        <span class="s2">&quot;variable&quot;</span><span class="p">:</span> <span class="s2">&quot;sts:ExternalId&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">aws_myteam_extern</span><span class="o">.</span><span class="n">external_id</span><span class="p">],</span>
    <span class="p">}],</span>
<span class="p">}])</span>
<span class="n">aws_sfx_role</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;awsSfxRole&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;signalfx integration to read out data and send it to signalfxs aws account&quot;</span><span class="p">,</span>
    <span class="n">assume_role_policy</span><span class="o">=</span><span class="n">signalfx_assume_policy</span><span class="o">.</span><span class="n">json</span><span class="p">)</span>
<span class="n">aws_read_permissions</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Policy</span><span class="p">(</span><span class="s2">&quot;awsReadPermissions&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;farts&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">        &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">        &quot;Statement&quot;: [</span>
<span class="s2">                {</span>
<span class="s2">                        &quot;Action&quot;: [</span>
<span class="s2">                                &quot;dynamodb:ListTables&quot;,</span>
<span class="s2">                    &quot;dynamodb:DescribeTable&quot;,</span>
<span class="s2">                    &quot;dynamodb:ListTagsOfResource&quot;,</span>
<span class="s2">                    &quot;ec2:DescribeInstances&quot;,</span>
<span class="s2">                    &quot;ec2:DescribeInstanceStatus&quot;,</span>
<span class="s2">                    &quot;ec2:DescribeVolumes&quot;,</span>
<span class="s2">                    &quot;ec2:DescribeReservedInstances&quot;,</span>
<span class="s2">                    &quot;ec2:DescribeReservedInstancesModifications&quot;,</span>
<span class="s2">                    &quot;ec2:DescribeTags&quot;,</span>
<span class="s2">                    &quot;organizations:DescribeOrganization&quot;,</span>
<span class="s2">                    &quot;cloudwatch:ListMetrics&quot;,</span>
<span class="s2">                    &quot;cloudwatch:GetMetricData&quot;,</span>
<span class="s2">                    &quot;cloudwatch:GetMetricStatistics&quot;,</span>
<span class="s2">                    &quot;cloudwatch:DescribeAlarms&quot;,</span>
<span class="s2">                    &quot;sqs:ListQueues&quot;,</span>
<span class="s2">                    &quot;sqs:GetQueueAttributes&quot;,</span>
<span class="s2">                    &quot;sqs:ListQueueTags&quot;,</span>
<span class="s2">                    &quot;elasticmapreduce:ListClusters&quot;,</span>
<span class="s2">                    &quot;elasticmapreduce:DescribeCluster&quot;,</span>
<span class="s2">                    &quot;kinesis:ListShards&quot;,</span>
<span class="s2">                    &quot;kinesis:ListStreams&quot;,</span>
<span class="s2">                    &quot;kinesis:DescribeStream&quot;,</span>
<span class="s2">                    &quot;kinesis:ListTagsForStream&quot;,</span>
<span class="s2">                    &quot;rds:DescribeDBInstances&quot;,</span>
<span class="s2">                    &quot;rds:ListTagsForResource&quot;,</span>
<span class="s2">                    &quot;elasticloadbalancing:DescribeLoadBalancers&quot;,</span>
<span class="s2">                    &quot;elasticloadbalancing:DescribeTags&quot;,</span>
<span class="s2">                    &quot;elasticache:describeCacheClusters&quot;,</span>
<span class="s2">                    &quot;redshift:DescribeClusters&quot;,</span>
<span class="s2">                    &quot;lambda:GetAlias&quot;,</span>
<span class="s2">                    &quot;lambda:ListFunctions&quot;,</span>
<span class="s2">                    &quot;lambda:ListTags&quot;,</span>
<span class="s2">                    &quot;autoscaling:DescribeAutoScalingGroups&quot;,</span>
<span class="s2">                    &quot;s3:ListAllMyBuckets&quot;,</span>
<span class="s2">                    &quot;s3:ListBucket&quot;,</span>
<span class="s2">                    &quot;s3:GetBucketLocation&quot;,</span>
<span class="s2">                    &quot;s3:GetBucketTagging&quot;,</span>
<span class="s2">                    &quot;ecs:ListServices&quot;,</span>
<span class="s2">                    &quot;ecs:ListTasks&quot;,</span>
<span class="s2">                    &quot;ecs:DescribeTasks&quot;,</span>
<span class="s2">                    &quot;ecs:DescribeServices&quot;,</span>
<span class="s2">                    &quot;ecs:ListClusters&quot;,</span>
<span class="s2">                    &quot;ecs:DescribeClusters&quot;,</span>
<span class="s2">                    &quot;ecs:ListTaskDefinitions&quot;,</span>
<span class="s2">                    &quot;ecs:ListTagsForResource&quot;,</span>
<span class="s2">                    &quot;apigateway:GET&quot;,</span>
<span class="s2">                    &quot;cloudfront:ListDistributions&quot;,</span>
<span class="s2">                    &quot;cloudfront:ListTagsForResource&quot;,</span>
<span class="s2">                    &quot;tag:GetResources&quot;,</span>
<span class="s2">                    &quot;es:ListDomainNames&quot;,</span>
<span class="s2">                    &quot;es:DescribeElasticsearchDomain&quot;</span>
<span class="s2">                        ],</span>
<span class="s2">                        &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">                        &quot;Resource&quot;: &quot;*&quot;</span>
<span class="s2">                }</span>
<span class="s2">        ]</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">sfx_read_attach</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicyAttachment</span><span class="p">(</span><span class="s2">&quot;sfx-read-attach&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">aws_sfx_role</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">policy_arn</span><span class="o">=</span><span class="n">aws_read_permissions</span><span class="o">.</span><span class="n">arn</span><span class="p">)</span>
<span class="n">aws_myteam</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">aws</span><span class="o">.</span><span class="n">Integration</span><span class="p">(</span><span class="s2">&quot;awsMyteam&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">integration_id</span><span class="o">=</span><span class="n">aws_myteam_extern</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">external_id</span><span class="o">=</span><span class="n">aws_myteam_extern</span><span class="o">.</span><span class="n">external_id</span><span class="p">,</span>
    <span class="n">role_arn</span><span class="o">=</span><span class="n">aws_sfx_role</span><span class="o">.</span><span class="n">arn</span><span class="p">,</span>
    <span class="n">regions</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">],</span>
    <span class="n">poll_rate</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
    <span class="n">import_cloud_watch</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">enable_aws_usage</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this integration</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_signalfx.aws.ExternalIntegration.external_id">
<code class="sig-name descname">external_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The external ID to use with your IAM role and with <code class="docutils literal notranslate"><span class="pre">aws.Integration</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.ExternalIntegration.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.ExternalIntegration.signalfx_aws_account">
<code class="sig-name descname">signalfx_aws_account</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.signalfx_aws_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Account ARN to use with your policies/roles, provided by SignalFx.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.aws.ExternalIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signalfx_aws_account</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ExternalIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external ID to use with your IAM role and with <code class="docutils literal notranslate"><span class="pre">aws.Integration</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this integration</p></li>
<li><p><strong>signalfx_aws_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Account ARN to use with your policies/roles, provided by SignalFx.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.aws.ExternalIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.aws.ExternalIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.aws.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.aws.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_cloudwatch_namespaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_namespace_sync_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_aws_usage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">import_cloud_watch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_sync_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">poll_rate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_get_metric_data_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx AWS CloudWatch integrations. For help with this integration see <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#monitor-amazon-web-services">Monitoring Amazon Web Services</a>.</p>
<blockquote>
<div><p><strong>NOTE</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider.</p>
<p><strong>WARNING</strong> This resource implements a part of a workflow. You must use it with one of either <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="c1"># This resource returns an account id in `external_id`…</span>
<span class="n">aws_myteam_external</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">aws</span><span class="o">.</span><span class="n">ExternalIntegration</span><span class="p">(</span><span class="s2">&quot;awsMyteamExternal&quot;</span><span class="p">)</span>
<span class="c1"># Make yourself an AWS IAM role here, use `signalfx_aws_external_integration.aws_myteam_external.external_id`</span>
<span class="n">aws_sfx_role</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;awsSfxRole&quot;</span><span class="p">)</span>
<span class="c1"># Stuff here that uses the external and account ID</span>
<span class="n">aws_myteam</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">aws</span><span class="o">.</span><span class="n">Integration</span><span class="p">(</span><span class="s2">&quot;awsMyteam&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">integration_id</span><span class="o">=</span><span class="n">aws_myteam_external</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">external_id</span><span class="o">=</span><span class="n">aws_myteam_external</span><span class="o">.</span><span class="n">external_id</span><span class="p">,</span>
    <span class="n">role_arn</span><span class="o">=</span><span class="n">aws_sfx_role</span><span class="o">.</span><span class="n">arn</span><span class="p">,</span>
    <span class="n">regions</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">],</span>
    <span class="n">poll_rate</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
    <span class="n">import_cloud_watch</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">enable_aws_usage</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">custom_namespace_sync_rule</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;defaultAction&quot;</span><span class="p">:</span> <span class="s2">&quot;Exclude&quot;</span><span class="p">,</span>
        <span class="s2">&quot;filterAction&quot;</span><span class="p">:</span> <span class="s2">&quot;Include&quot;</span><span class="p">,</span>
        <span class="s2">&quot;filterSource&quot;</span><span class="p">:</span> <span class="s2">&quot;filter(&#39;code&#39;, &#39;200&#39;)&quot;</span><span class="p">,</span>
        <span class="s2">&quot;namespace&quot;</span><span class="p">:</span> <span class="s2">&quot;fart&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">namespace_sync_rule</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;defaultAction&quot;</span><span class="p">:</span> <span class="s2">&quot;Exclude&quot;</span><span class="p">,</span>
        <span class="s2">&quot;filterAction&quot;</span><span class="p">:</span> <span class="s2">&quot;Include&quot;</span><span class="p">,</span>
        <span class="s2">&quot;filterSource&quot;</span><span class="p">:</span> <span class="s2">&quot;filter(&#39;code&#39;, &#39;200&#39;)&quot;</span><span class="p">,</span>
        <span class="s2">&quot;namespace&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS/EC2&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<blockquote>
<div><p><strong>NOTE</strong> You can use the data source “.getAwsServices” to specify all services.</p>
</div></blockquote>
<p>Fields that expect an AWS service/namespace will work with one of: “AWS/ApiGateway” “AWS/AppStream” “AWS/AutoScaling” “AWS/Billing” “AWS/CloudFront” “AWS/CloudSearch” “AWS/Events” “AWS/Logs” “AWS/Connect” “AWS/DMS” “AWS/DX” “AWS/DynamoDB” “AWS/EC2” “AWS/EC2Spot” “AWS/ECS” “AWS/ElasticBeanstalk” “AWS/EBS” “AWS/EFS” “AWS/ELB” “AWS/ApplicationELB” “AWS/NetworkELB” “AWS/ElasticTranscoder” “AWS/ElastiCache” “AWS/ES” “AWS/ElasticMapReduce” “AWS/GameLift” “AWS/Inspector” “AWS/IoT” “AWS/KMS” “AWS/KinesisAnalytics” “AWS/Firehose” “AWS/Kinesis” “AWS/KinesisVideo” “AWS/Lambda” “AWS/Lex” “AWS/ML” “AWS/OpsWorks” “AWS/Polly” “AWS/Redshift” “AWS/RDS” “AWS/Route53” “AWS/SageMaker” “AWS/DDoSProtection” “AWS/SES” “AWS/SNS” “AWS/SQS” “AWS/S3” “AWS/SWF” “AWS/States” “AWS/StorageGateway” “AWS/Translate” “AWS/NATGateway” “AWS/VPN” “WAF” “AWS/WorkSpaces”.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_cloudwatch_namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.</p></li>
<li><p><strong>custom_namespace_sync_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">custom_cloudwatch_namespaces</span></code> property.</p></li>
<li><p><strong>enable_aws_usage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, SignalFx imports the metrics.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">external_id</span></code> property from one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code></p></li>
<li><p><strong>import_cloud_watch</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.</p></li>
<li><p><strong>integration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code>.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you specify <code class="docutils literal notranslate"><span class="pre">auth_method</span> <span class="pre">=</span> <span class="pre">&quot;SecurityToken&quot;</span></code> in your request to create an AWS integration object, use this property to specify the key.</p></li>
<li><p><strong>namespace_sync_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">services</span></code> property. If you don’t specify either property, SignalFx syncs all data in all AWS namespaces.</p></li>
<li><p><strong>poll_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS regions that SignalFx should monitor.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role ARN that you add to an existing AWS integration object. <strong>Note</strong>: Ensure you use the <code class="docutils literal notranslate"><span class="pre">arn</span></code> property of your role, not the id!</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with <code class="docutils literal notranslate"><span class="pre">namespace_sync_rule</span></code>.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used with <code class="docutils literal notranslate"><span class="pre">signalfx_aws_token_integration</span></code>. Use this property to specify the token.</p></li>
<li><p><strong>use_get_metric_data_method</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable the use of Amazon’s <code class="docutils literal notranslate"><span class="pre">GetMetricData</span></code> for collecting metrics. Note that this requires the inclusion of the <code class="docutils literal notranslate"><span class="pre">&quot;cloudwatch:GetMetricData&quot;</span></code> permission.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_namespace_sync_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
<p>The <strong>namespace_sync_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.custom_cloudwatch_namespaces">
<code class="sig-name descname">custom_cloudwatch_namespaces</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.custom_cloudwatch_namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.custom_namespace_sync_rules">
<code class="sig-name descname">custom_namespace_sync_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.custom_namespace_sync_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">custom_cloudwatch_namespaces</span></code> property.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.enable_aws_usage">
<code class="sig-name descname">enable_aws_usage</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.enable_aws_usage" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, SignalFx imports the metrics.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the integration is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.external_id">
<code class="sig-name descname">external_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">external_id</span></code> property from one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.import_cloud_watch">
<code class="sig-name descname">import_cloud_watch</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.import_cloud_watch" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.integration_id">
<code class="sig-name descname">integration_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.integration_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.key">
<code class="sig-name descname">key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.key" title="Permalink to this definition">¶</a></dt>
<dd><p>If you specify <code class="docutils literal notranslate"><span class="pre">auth_method</span> <span class="pre">=</span> <span class="pre">&quot;SecurityToken&quot;</span></code> in your request to create an AWS integration object, use this property to specify the key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.namespace_sync_rules">
<code class="sig-name descname">namespace_sync_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.namespace_sync_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">services</span></code> property. If you don’t specify either property, SignalFx syncs all data in all AWS namespaces.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.poll_rate">
<code class="sig-name descname">poll_rate</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.poll_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.regions">
<code class="sig-name descname">regions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of AWS regions that SignalFx should monitor.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Role ARN that you add to an existing AWS integration object. <strong>Note</strong>: Ensure you use the <code class="docutils literal notranslate"><span class="pre">arn</span></code> property of your role, not the id!</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.services">
<code class="sig-name descname">services</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.services" title="Permalink to this definition">¶</a></dt>
<dd><p>List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with <code class="docutils literal notranslate"><span class="pre">namespace_sync_rule</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.token">
<code class="sig-name descname">token</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.token" title="Permalink to this definition">¶</a></dt>
<dd><p>Used with <code class="docutils literal notranslate"><span class="pre">signalfx_aws_token_integration</span></code>. Use this property to specify the token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.Integration.use_get_metric_data_method">
<code class="sig-name descname">use_get_metric_data_method</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.use_get_metric_data_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable the use of Amazon’s <code class="docutils literal notranslate"><span class="pre">GetMetricData</span></code> for collecting metrics. Note that this requires the inclusion of the <code class="docutils literal notranslate"><span class="pre">&quot;cloudwatch:GetMetricData&quot;</span></code> permission.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.aws.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_cloudwatch_namespaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_namespace_sync_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_aws_usage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">import_cloud_watch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_sync_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">poll_rate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_get_metric_data_method</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_cloudwatch_namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.</p></li>
<li><p><strong>custom_namespace_sync_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">custom_cloudwatch_namespaces</span></code> property.</p></li>
<li><p><strong>enable_aws_usage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, SignalFx imports the metrics.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">external_id</span></code> property from one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code></p></li>
<li><p><strong>import_cloud_watch</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.</p></li>
<li><p><strong>integration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code>.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you specify <code class="docutils literal notranslate"><span class="pre">auth_method</span> <span class="pre">=</span> <span class="pre">&quot;SecurityToken&quot;</span></code> in your request to create an AWS integration object, use this property to specify the key.</p></li>
<li><p><strong>namespace_sync_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">services</span></code> property. If you don’t specify either property, SignalFx syncs all data in all AWS namespaces.</p></li>
<li><p><strong>poll_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS regions that SignalFx should monitor.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role ARN that you add to an existing AWS integration object. <strong>Note</strong>: Ensure you use the <code class="docutils literal notranslate"><span class="pre">arn</span></code> property of your role, not the id!</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with <code class="docutils literal notranslate"><span class="pre">namespace_sync_rule</span></code>.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used with <code class="docutils literal notranslate"><span class="pre">signalfx_aws_token_integration</span></code>. Use this property to specify the token.</p></li>
<li><p><strong>use_get_metric_data_method</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable the use of Amazon’s <code class="docutils literal notranslate"><span class="pre">GetMetricData</span></code> for collecting metrics. Note that this requires the inclusion of the <code class="docutils literal notranslate"><span class="pre">&quot;cloudwatch:GetMetricData&quot;</span></code> permission.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_namespace_sync_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
<p>The <strong>namespace_sync_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.aws.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.aws.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.aws.TokenIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.aws.</code><code class="sig-name descname">TokenIntegration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx AWS CloudWatch integrations using security tokens. For help with this integration see <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#connect-to-aws">Connect to AWS CloudWatch</a>.</p>
<blockquote>
<div><p><strong>NOTE</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider.</p>
<p><strong>WARNING</strong> This resource implements a part of a workflow. You must use it with <code class="docutils literal notranslate"><span class="pre">aws.Integration</span></code>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">aws_myteam_token</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">aws</span><span class="o">.</span><span class="n">TokenIntegration</span><span class="p">(</span><span class="s2">&quot;awsMyteamToken&quot;</span><span class="p">)</span>
<span class="c1"># Make yourself an AWS IAM role here</span>
<span class="n">aws_sfx_role</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;awsSfxRole&quot;</span><span class="p">)</span>
<span class="c1"># Stuff here that uses the external and account ID</span>
<span class="n">aws_myteam</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">aws</span><span class="o">.</span><span class="n">Integration</span><span class="p">(</span><span class="s2">&quot;awsMyteam&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">integration_id</span><span class="o">=</span><span class="n">aws_myteam_token</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">token</span><span class="o">=</span><span class="s2">&quot;put_your_token_here&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;put_your_key_here&quot;</span><span class="p">,</span>
    <span class="n">regions</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">],</span>
    <span class="n">poll_rate</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
    <span class="n">import_cloud_watch</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">enable_aws_usage</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">custom_namespace_sync_rule</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;defaultAction&quot;</span><span class="p">:</span> <span class="s2">&quot;Exclude&quot;</span><span class="p">,</span>
        <span class="s2">&quot;filterAction&quot;</span><span class="p">:</span> <span class="s2">&quot;Include&quot;</span><span class="p">,</span>
        <span class="s2">&quot;filterSource&quot;</span><span class="p">:</span> <span class="s2">&quot;filter(&#39;code&#39;, &#39;200&#39;)&quot;</span><span class="p">,</span>
        <span class="s2">&quot;namespace&quot;</span><span class="p">:</span> <span class="s2">&quot;fart&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">namespace_sync_rule</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;defaultAction&quot;</span><span class="p">:</span> <span class="s2">&quot;Exclude&quot;</span><span class="p">,</span>
        <span class="s2">&quot;filterAction&quot;</span><span class="p">:</span> <span class="s2">&quot;Include&quot;</span><span class="p">,</span>
        <span class="s2">&quot;filterSource&quot;</span><span class="p">:</span> <span class="s2">&quot;filter(&#39;code&#39;, &#39;200&#39;)&quot;</span><span class="p">,</span>
        <span class="s2">&quot;namespace&quot;</span><span class="p">:</span> <span class="s2">&quot;AWS/EC2&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this integration</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_signalfx.aws.TokenIntegration.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.TokenIntegration.signalfx_aws_account">
<code class="sig-name descname">signalfx_aws_account</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.signalfx_aws_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Account ARN to use with your policies/roles, provided by SignalFx.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_signalfx.aws.TokenIntegration.token_id">
<code class="sig-name descname">token_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.token_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The SignalFx-generated AWS token to use with an AWS integration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.aws.TokenIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signalfx_aws_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TokenIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this integration</p></li>
<li><p><strong>signalfx_aws_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Account ARN to use with your policies/roles, provided by SignalFx.</p></li>
<li><p><strong>token_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SignalFx-generated AWS token to use with an AWS integration.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.aws.TokenIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.aws.TokenIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
