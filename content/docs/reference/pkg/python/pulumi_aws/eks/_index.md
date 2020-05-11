---
title: Module eks
title_tag: Module eks | Package pulumi_aws | Python SDK
linktitle: eks
notitle: true
---

<div class="section" id="eks">
<h1>eks<a class="headerlink" href="#eks" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.eks"></span><dl class="py class">
<dt id="pulumi_aws.eks.AwaitableGetClusterAuthResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">AwaitableGetClusterAuthResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.AwaitableGetClusterAuthResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.eks.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_authority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_cluster_log_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.eks.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_cluster_log_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EKS Cluster.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">assume_role_policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">  &quot;Statement&quot;: [</span>
<span class="s2">    {</span>
<span class="s2">      &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">      &quot;Principal&quot;: {</span>
<span class="s2">        &quot;Service&quot;: &quot;eks.amazonaws.com&quot;</span>
<span class="s2">      },</span>
<span class="s2">      &quot;Action&quot;: &quot;sts:AssumeRole&quot;</span>
<span class="s2">    }</span>
<span class="s2">  ]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">example__amazon_eks_cluster_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicyAttachment</span><span class="p">(</span><span class="s2">&quot;example-AmazonEKSClusterPolicy&quot;</span><span class="p">,</span>
    <span class="n">policy_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws:iam::aws:policy/AmazonEKSClusterPolicy&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example__amazon_eks_service_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicyAttachment</span><span class="p">(</span><span class="s2">&quot;example-AmazonEKSServicePolicy&quot;</span><span class="p">,</span>
    <span class="n">policy_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws:iam::aws:policy/AmazonEKSServicePolicy&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">cluster_name</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;clusterName&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">cluster_name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">cluster_name</span> <span class="o">=</span> <span class="s2">&quot;example&quot;</span>
<span class="n">example_cluster</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">eks</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;exampleCluster&quot;</span><span class="p">,</span> <span class="n">enabled_cluster_log_types</span><span class="o">=</span><span class="p">[</span>
    <span class="s2">&quot;api&quot;</span><span class="p">,</span>
    <span class="s2">&quot;audit&quot;</span><span class="p">,</span>
<span class="p">])</span>
<span class="n">example_log_group</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">cloudwatch</span><span class="o">.</span><span class="n">LogGroup</span><span class="p">(</span><span class="s2">&quot;exampleLogGroup&quot;</span><span class="p">,</span> <span class="n">retention_in_days</span><span class="o">=</span><span class="mi">7</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled_cluster_log_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the desired control plane logging to enable. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Control Plane Logging</a></p></li>
<li><p><strong>encryption_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with encryption configuration for the cluster. Only available on Kubernetes 1.13 and above clusters created after March 6, 2020. Detailed below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cluster.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Ensure the resource configuration includes explicit dependencies on the IAM Role permissions by adding <cite>``dependsOn`</cite> &lt;<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson">https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson</a>&gt;`_ if using the <cite>``iam.RolePolicy`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_role_policy.html">https://www.terraform.io/docs/providers/aws/r/iam_role_policy.html</a>&gt;`_ or <cite>``iam.RolePolicyAttachment`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html</a>&gt;`_, otherwise EKS cannot delete EKS managed EC2 infrastructure such as Security Groups on EKS Cluster deletion.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value map of resource tags.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.</p></li>
<li><p><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC Considerations</a> and <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster Security Group Considerations</a> in the Amazon EKS User Guide. Configuration detailed below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>encryption_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block with provider for encryption. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the Key Management Service (KMS) customer master key (CMK). The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html">Allowing Users in Other Accounts to Use a CMK in the AWS Key Management Service Developer Guide</a>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of strings with resources to be encrypted. Valid values: <code class="docutils literal notranslate"><span class="pre">secrets</span></code></p></li>
</ul>
<p>The <strong>vpc_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecurityGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The cluster security group that was created by Amazon EKS for the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpointPrivateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether or not the Amazon EKS private API server endpoint is enabled. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpointPublicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether or not the Amazon EKS public API server endpoint is enabled. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccessCidrs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of CIDR blocks. Indicates which CIDR blocks can access the Amazon EKS public API server endpoint when enabled. EKS defaults this to a list with <code class="docutils literal notranslate"><span class="pre">0.0.0.0/0</span></code>. This provider will only perform drift detection of its value when present in a configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of security group IDs for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of subnet IDs. Must be in at least two different availability zones. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The VPC associated with your cluster.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.certificate_authority">
<code class="sig-name descname">certificate_authority</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.certificate_authority" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing <code class="docutils literal notranslate"><span class="pre">certificate-authority-data</span></code> for your cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The base64 encoded certificate data required to communicate with your cluster. Add this to the <code class="docutils literal notranslate"><span class="pre">certificate-authority-data</span></code> section of the <code class="docutils literal notranslate"><span class="pre">kubeconfig</span></code> file for your cluster.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.enabled_cluster_log_types">
<code class="sig-name descname">enabled_cluster_log_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.enabled_cluster_log_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the desired control plane logging to enable. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Control Plane Logging</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.encryption_config">
<code class="sig-name descname">encryption_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.encryption_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with encryption configuration for the cluster. Only available on Kubernetes 1.13 and above clusters created after March 6, 2020. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block with provider for encryption. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of the Key Management Service (KMS) customer master key (CMK). The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html">Allowing Users in Other Accounts to Use a CMK in the AWS Key Management Service Developer Guide</a>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of strings with resources to be encrypted. Valid values: <code class="docutils literal notranslate"><span class="pre">secrets</span></code></p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.endpoint">
<code class="sig-name descname">endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint for your Kubernetes API server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.identities">
<code class="sig-name descname">identities</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.identities" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing identity provider information for your cluster. Only available on Kubernetes version 1.13 and 1.14 clusters created or upgraded on or after September 3, 2019.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">oidcs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Nested attribute containing <a class="reference external" href="https://openid.net/connect/">OpenID Connect</a> identity provider information for the cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Issuer URL for the OpenID Connect identity provider.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.platform_version">
<code class="sig-name descname">platform_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.platform_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform version for the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Ensure the resource configuration includes explicit dependencies on the IAM Role permissions by adding <cite>``dependsOn`</cite> &lt;<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson">https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson</a>&gt;`_ if using the <cite>``iam.RolePolicy`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_role_policy.html">https://www.terraform.io/docs/providers/aws/r/iam_role_policy.html</a>&gt;`_ or <cite>``iam.RolePolicyAttachment`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html</a>&gt;`_, otherwise EKS cannot delete EKS managed EC2 infrastructure such as Security Groups on EKS Cluster deletion.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the EKS cluster. One of <code class="docutils literal notranslate"><span class="pre">CREATING</span></code>, <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value map of resource tags.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.Cluster.vpc_config">
<code class="sig-name descname">vpc_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC Considerations</a> and <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster Security Group Considerations</a> in the Amazon EKS User Guide. Configuration detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecurityGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The cluster security group that was created by Amazon EKS for the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpointPrivateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether or not the Amazon EKS private API server endpoint is enabled. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpointPublicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether or not the Amazon EKS public API server endpoint is enabled. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccessCidrs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of CIDR blocks. Indicates which CIDR blocks can access the Amazon EKS public API server endpoint when enabled. EKS defaults this to a list with <code class="docutils literal notranslate"><span class="pre">0.0.0.0/0</span></code>. This provider will only perform drift detection of its value when present in a configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of security group IDs for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of subnet IDs. Must be in at least two different availability zones. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The VPC associated with your cluster.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.eks.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_authority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_cluster_log_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the cluster.</p></li>
<li><p><strong>certificate_authority</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested attribute containing <code class="docutils literal notranslate"><span class="pre">certificate-authority-data</span></code> for your cluster.</p></li>
<li><p><strong>enabled_cluster_log_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of the desired control plane logging to enable. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Control Plane Logging</a></p>
</p></li>
<li><p><strong>encryption_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with encryption configuration for the cluster. Only available on Kubernetes 1.13 and above clusters created after March 6, 2020. Detailed below.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint for your Kubernetes API server.</p></li>
<li><p><strong>identities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Nested attribute containing identity provider information for your cluster. Only available on Kubernetes version 1.13 and 1.14 clusters created or upgraded on or after September 3, 2019.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cluster.</p></li>
<li><p><strong>platform_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The platform version for the cluster.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Ensure the resource configuration includes explicit dependencies on the IAM Role permissions by adding <cite>``dependsOn`</cite> &lt;<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson">https://www.pulumi.com/docs/intro/concepts/programming-model/#dependson</a>&gt;`_ if using the <cite>``iam.RolePolicy`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_role_policy.html">https://www.terraform.io/docs/providers/aws/r/iam_role_policy.html</a>&gt;`_ or <cite>``iam.RolePolicyAttachment`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html">https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html</a>&gt;`_, otherwise EKS cannot delete EKS managed EC2 infrastructure such as Security Groups on EKS Cluster deletion.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the EKS cluster. One of <code class="docutils literal notranslate"><span class="pre">CREATING</span></code>, <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value map of resource tags.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.</p></li>
<li><p><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC Considerations</a> and <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster Security Group Considerations</a> in the Amazon EKS User Guide. Configuration detailed below.</p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificate_authority</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The base64 encoded certificate data required to communicate with your cluster. Add this to the <code class="docutils literal notranslate"><span class="pre">certificate-authority-data</span></code> section of the <code class="docutils literal notranslate"><span class="pre">kubeconfig</span></code> file for your cluster.</p></li>
</ul>
<p>The <strong>encryption_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block with provider for encryption. Detailed below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the Key Management Service (KMS) customer master key (CMK). The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html">Allowing Users in Other Accounts to Use a CMK in the AWS Key Management Service Developer Guide</a>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of strings with resources to be encrypted. Valid values: <code class="docutils literal notranslate"><span class="pre">secrets</span></code></p></li>
</ul>
<p>The <strong>identities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">oidcs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Nested attribute containing <a class="reference external" href="https://openid.net/connect/">OpenID Connect</a> identity provider information for the cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer URL for the OpenID Connect identity provider.</p></li>
</ul>
</li>
</ul>
<p>The <strong>vpc_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecurityGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The cluster security group that was created by Amazon EKS for the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpointPrivateAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether or not the Amazon EKS private API server endpoint is enabled. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpointPublicAccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether or not the Amazon EKS public API server endpoint is enabled. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicAccessCidrs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of CIDR blocks. Indicates which CIDR blocks can access the Amazon EKS public API server endpoint when enabled. EKS defaults this to a list with <code class="docutils literal notranslate"><span class="pre">0.0.0.0/0</span></code>. This provider will only perform drift detection of its value when present in a configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of security group IDs for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of subnet IDs. Must be in at least two different availability zones. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The VPC associated with your cluster.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.eks.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.eks.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.eks.FargateProfile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">FargateProfile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fargate_profile_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_execution_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selectors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.FargateProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EKS Fargate Profile.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">eks</span><span class="o">.</span><span class="n">FargateProfile</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">aws_eks_cluster</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">pod_execution_role_arn</span><span class="o">=</span><span class="n">aws_iam_role</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="n">subnet_ids</span><span class="o">=</span><span class="p">[</span><span class="n">__item</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">aws_subnet</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">]],</span>
    <span class="n">selector</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;namespace&quot;</span><span class="p">:</span> <span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">assume_role_policy</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span>
    <span class="s2">&quot;Statement&quot;</span><span class="p">:</span> <span class="p">[{</span>
        <span class="s2">&quot;Action&quot;</span><span class="p">:</span> <span class="s2">&quot;sts:AssumeRole&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Effect&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Principal&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;Service&quot;</span><span class="p">:</span> <span class="s2">&quot;eks-fargate-pods.amazonaws.com&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">}],</span>
    <span class="s2">&quot;Version&quot;</span><span class="p">:</span> <span class="s2">&quot;2012-10-17&quot;</span><span class="p">,</span>
<span class="p">}))</span>
<span class="n">example__amazon_eks_fargate_pod_execution_role_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicyAttachment</span><span class="p">(</span><span class="s2">&quot;example-AmazonEKSFargatePodExecutionRolePolicy&quot;</span><span class="p">,</span>
    <span class="n">policy_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws:iam::aws:policy/AmazonEKSFargatePodExecutionRolePolicy&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the EKS Cluster.</p></li>
<li><p><strong>fargate_profile_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the EKS Fargate Profile.</p></li>
<li><p><strong>pod_execution_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Fargate Profile.</p></li>
<li><p><strong>selectors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) for selecting Kubernetes Pods to execute with this EKS Fargate Profile. Detailed below.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifiers of private EC2 Subnets to associate with the EKS Fargate Profile. These subnets must have the following resource tag: <code class="docutils literal notranslate"><span class="pre">kubernetes.io/cluster/CLUSTER_NAME</span></code> (where <code class="docutils literal notranslate"><span class="pre">CLUSTER_NAME</span></code> is replaced with the name of the EKS Cluster).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value map of resource tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>selectors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Key-value map of Kubernetes labels for selection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Kubernetes namespace for selection.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.eks.FargateProfile.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the EKS Fargate Profile.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.FargateProfile.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the EKS Cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.FargateProfile.fargate_profile_name">
<code class="sig-name descname">fargate_profile_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.fargate_profile_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the EKS Fargate Profile.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.FargateProfile.pod_execution_role_arn">
<code class="sig-name descname">pod_execution_role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.pod_execution_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Fargate Profile.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.FargateProfile.selectors">
<code class="sig-name descname">selectors</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.selectors" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block(s) for selecting Kubernetes Pods to execute with this EKS Fargate Profile. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Key-value map of Kubernetes labels for selection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Kubernetes namespace for selection.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.FargateProfile.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the EKS Fargate Profile.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.FargateProfile.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifiers of private EC2 Subnets to associate with the EKS Fargate Profile. These subnets must have the following resource tag: <code class="docutils literal notranslate"><span class="pre">kubernetes.io/cluster/CLUSTER_NAME</span></code> (where <code class="docutils literal notranslate"><span class="pre">CLUSTER_NAME</span></code> is replaced with the name of the EKS Cluster).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.FargateProfile.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value map of resource tags.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.eks.FargateProfile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fargate_profile_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_execution_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selectors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FargateProfile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the EKS Fargate Profile.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the EKS Cluster.</p></li>
<li><p><strong>fargate_profile_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the EKS Fargate Profile.</p></li>
<li><p><strong>pod_execution_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Fargate Profile.</p></li>
<li><p><strong>selectors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Configuration block(s) for selecting Kubernetes Pods to execute with this EKS Fargate Profile. Detailed below.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the EKS Fargate Profile.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifiers of private EC2 Subnets to associate with the EKS Fargate Profile. These subnets must have the following resource tag: <code class="docutils literal notranslate"><span class="pre">kubernetes.io/cluster/CLUSTER_NAME</span></code> (where <code class="docutils literal notranslate"><span class="pre">CLUSTER_NAME</span></code> is replaced with the name of the EKS Cluster).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value map of resource tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>selectors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Key-value map of Kubernetes labels for selection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Kubernetes namespace for selection.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.eks.FargateProfile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.eks.FargateProfile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.FargateProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.eks.GetClusterAuthResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">GetClusterAuthResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.GetClusterAuthResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusterAuth.</p>
<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterAuthResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterAuthResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterAuthResult.token">
<code class="sig-name descname">token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterAuthResult.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token to use to authenticate with the cluster.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.eks.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_authority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_cluster_log_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.certificate_authority">
<code class="sig-name descname">certificate_authority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.certificate_authority" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing <code class="docutils literal notranslate"><span class="pre">certificate-authority-data</span></code> for your cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The Unix epoch time stamp in seconds for when the cluster was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.enabled_cluster_log_types">
<code class="sig-name descname">enabled_cluster_log_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.enabled_cluster_log_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The enabled control plane logs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint for your Kubernetes API server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.identities">
<code class="sig-name descname">identities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.identities" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing identity provider information for your cluster. Only available on Kubernetes version 1.13 and 1.14 clusters created or upgraded on or after September 3, 2019. For an example using this information to enable IAM Roles for Service Accounts, see the <cite>``eks.Cluster`</cite> resource documentation &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/eks_cluster.html">https://www.terraform.io/docs/providers/aws/r/eks_cluster.html</a>&gt;`_.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.platform_version">
<code class="sig-name descname">platform_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.platform_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform version for the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the EKS cluster. One of <code class="docutils literal notranslate"><span class="pre">CREATING</span></code>, <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value map of resource tags.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kubernetes server version for the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.GetClusterResult.vpc_config">
<code class="sig-name descname">vpc_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested list containing VPC configuration for the cluster.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.eks.NodeGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">NodeGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ami_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remote_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.NodeGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EKS Node Group, which can provision and optionally update an Auto Scaling Group of Kubernetes worker nodes compatible with EKS. Additional documentation about this functionality can be found in the <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html">EKS User Guide</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">eks</span><span class="o">.</span><span class="n">NodeGroup</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">aws_eks_cluster</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">node_role_arn</span><span class="o">=</span><span class="n">aws_iam_role</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="n">subnet_ids</span><span class="o">=</span><span class="p">[</span><span class="n">__item</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">aws_subnet</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">]],</span>
    <span class="n">scaling_config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;desiredSize&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="s2">&quot;maxSize&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="s2">&quot;minSize&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">assume_role_policy</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span>
    <span class="s2">&quot;Statement&quot;</span><span class="p">:</span> <span class="p">[{</span>
        <span class="s2">&quot;Action&quot;</span><span class="p">:</span> <span class="s2">&quot;sts:AssumeRole&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Effect&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Principal&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;Service&quot;</span><span class="p">:</span> <span class="s2">&quot;ec2.amazonaws.com&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">}],</span>
    <span class="s2">&quot;Version&quot;</span><span class="p">:</span> <span class="s2">&quot;2012-10-17&quot;</span><span class="p">,</span>
<span class="p">}))</span>
<span class="n">example__amazon_eks_worker_node_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicyAttachment</span><span class="p">(</span><span class="s2">&quot;example-AmazonEKSWorkerNodePolicy&quot;</span><span class="p">,</span>
    <span class="n">policy_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example__amazon_ekscni_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicyAttachment</span><span class="p">(</span><span class="s2">&quot;example-AmazonEKSCNIPolicy&quot;</span><span class="p">,</span>
    <span class="n">policy_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example__amazon_ec2_container_registry_read_only</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicyAttachment</span><span class="p">(</span><span class="s2">&quot;example-AmazonEC2ContainerRegistryReadOnly&quot;</span><span class="p">,</span>
    <span class="n">policy_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ami_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of Amazon Machine Image (AMI) associated with the EKS Node Group. Defaults to <code class="docutils literal notranslate"><span class="pre">AL2_x86_64</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">AL2_x86_64</span></code>, <code class="docutils literal notranslate"><span class="pre">AL2_x86_64_GPU</span></code>. This provider will only perform drift detection if a configuration value is provided.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the EKS Cluster.</p></li>
<li><p><strong>disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Disk size in GiB for worker nodes. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>. This provider will only perform drift detection if a configuration value is provided.</p></li>
<li><p><strong>instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set of instance types associated with the EKS Node Group. Defaults to <code class="docutils literal notranslate"><span class="pre">[&quot;t3.medium&quot;]</span></code>. This provider will only perform drift detection if a configuration value is provided. Currently, the EKS API only accepts a single value in the set.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.</p></li>
<li><p><strong>node_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the EKS Node Group.</p></li>
<li><p><strong>node_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.</p></li>
<li><p><strong>release_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.</p></li>
<li><p><strong>remote_access</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with remote access settings. Detailed below.</p></li>
<li><p><strong>scaling_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with scaling settings. Detailed below.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: <code class="docutils literal notranslate"><span class="pre">kubernetes.io/cluster/CLUSTER_NAME</span></code> (where <code class="docutils literal notranslate"><span class="pre">CLUSTER_NAME</span></code> is replaced with the name of the EKS Cluster).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kubernetes version. Defaults to EKS Cluster Kubernetes version. This provider will only perform drift detection if a configuration value is provided.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>remote_access</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ec2SshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - EC2 Key Pair name that provides access for SSH communication with the worker nodes in the EKS Node Group. If you specify this configuration, but do not specify <code class="docutils literal notranslate"><span class="pre">source_security_group_ids</span></code> when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Set of EC2 Security Group IDs to allow SSH access (port 22) from on the worker nodes. If you specify <code class="docutils literal notranslate"><span class="pre">ec2_ssh_key</span></code>, but do not specify this configuration when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).</p></li>
</ul>
<p>The <strong>scaling_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">desiredSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Desired number of worker nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of worker nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Minimum number of worker nodes.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.ami_type">
<code class="sig-name descname">ami_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.ami_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of Amazon Machine Image (AMI) associated with the EKS Node Group. Defaults to <code class="docutils literal notranslate"><span class="pre">AL2_x86_64</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">AL2_x86_64</span></code>, <code class="docutils literal notranslate"><span class="pre">AL2_x86_64_GPU</span></code>. This provider will only perform drift detection if a configuration value is provided.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the EKS Node Group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the EKS Cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.disk_size">
<code class="sig-name descname">disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Disk size in GiB for worker nodes. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>. This provider will only perform drift detection if a configuration value is provided.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.instance_types">
<code class="sig-name descname">instance_types</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of instance types associated with the EKS Node Group. Defaults to <code class="docutils literal notranslate"><span class="pre">[&quot;t3.medium&quot;]</span></code>. This provider will only perform drift detection if a configuration value is provided. Currently, the EKS API only accepts a single value in the set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.node_group_name">
<code class="sig-name descname">node_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.node_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the EKS Node Group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.node_role_arn">
<code class="sig-name descname">node_role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.node_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.release_version">
<code class="sig-name descname">release_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.release_version" title="Permalink to this definition">¶</a></dt>
<dd><p>AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.remote_access">
<code class="sig-name descname">remote_access</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.remote_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with remote access settings. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ec2SshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - EC2 Key Pair name that provides access for SSH communication with the worker nodes in the EKS Node Group. If you specify this configuration, but do not specify <code class="docutils literal notranslate"><span class="pre">source_security_group_ids</span></code> when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set of EC2 Security Group IDs to allow SSH access (port 22) from on the worker nodes. If you specify <code class="docutils literal notranslate"><span class="pre">ec2_ssh_key</span></code>, but do not specify this configuration when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.resources">
<code class="sig-name descname">resources</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>List of objects containing information about underlying resources.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of objects containing information about AutoScaling Groups.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the AutoScaling Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteAccessSecurityGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifier of the remote access EC2 Security Group.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.scaling_config">
<code class="sig-name descname">scaling_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.scaling_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with scaling settings. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">desiredSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Desired number of worker nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum number of worker nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Minimum number of worker nodes.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the EKS Node Group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: <code class="docutils literal notranslate"><span class="pre">kubernetes.io/cluster/CLUSTER_NAME</span></code> (where <code class="docutils literal notranslate"><span class="pre">CLUSTER_NAME</span></code> is replaced with the name of the EKS Cluster).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.eks.NodeGroup.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Kubernetes version. Defaults to EKS Cluster Kubernetes version. This provider will only perform drift detection if a configuration value is provided.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.eks.NodeGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ami_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remote_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodeGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ami_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of Amazon Machine Image (AMI) associated with the EKS Node Group. Defaults to <code class="docutils literal notranslate"><span class="pre">AL2_x86_64</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">AL2_x86_64</span></code>, <code class="docutils literal notranslate"><span class="pre">AL2_x86_64_GPU</span></code>. This provider will only perform drift detection if a configuration value is provided.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the EKS Node Group.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the EKS Cluster.</p></li>
<li><p><strong>disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Disk size in GiB for worker nodes. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>. This provider will only perform drift detection if a configuration value is provided.</p></li>
<li><p><strong>instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set of instance types associated with the EKS Node Group. Defaults to <code class="docutils literal notranslate"><span class="pre">[&quot;t3.medium&quot;]</span></code>. This provider will only perform drift detection if a configuration value is provided. Currently, the EKS API only accepts a single value in the set.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.</p></li>
<li><p><strong>node_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the EKS Node Group.</p></li>
<li><p><strong>node_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.</p></li>
<li><p><strong>release_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.</p></li>
<li><p><strong>remote_access</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with remote access settings. Detailed below.</p></li>
<li><p><strong>resources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of objects containing information about underlying resources.</p></li>
<li><p><strong>scaling_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block with scaling settings. Detailed below.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the EKS Node Group.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: <code class="docutils literal notranslate"><span class="pre">kubernetes.io/cluster/CLUSTER_NAME</span></code> (where <code class="docutils literal notranslate"><span class="pre">CLUSTER_NAME</span></code> is replaced with the name of the EKS Cluster).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kubernetes version. Defaults to EKS Cluster Kubernetes version. This provider will only perform drift detection if a configuration value is provided.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>remote_access</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ec2SshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - EC2 Key Pair name that provides access for SSH communication with the worker nodes in the EKS Node Group. If you specify this configuration, but do not specify <code class="docutils literal notranslate"><span class="pre">source_security_group_ids</span></code> when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Set of EC2 Security Group IDs to allow SSH access (port 22) from on the worker nodes. If you specify <code class="docutils literal notranslate"><span class="pre">ec2_ssh_key</span></code>, but do not specify this configuration when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).</p></li>
</ul>
<p>The <strong>resources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of objects containing information about AutoScaling Groups.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the AutoScaling Group.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteAccessSecurityGroupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifier of the remote access EC2 Security Group.</p></li>
</ul>
<p>The <strong>scaling_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">desiredSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Desired number of worker nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of worker nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Minimum number of worker nodes.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.eks.NodeGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.eks.NodeGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.NodeGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.eks.get_cluster">
<code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about an EKS Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the cluster</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – Key-value map of resource tags.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.eks.get_cluster_auth">
<code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">get_cluster_auth</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.get_cluster_auth" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an authentication token to communicate with an EKS cluster.</p>
<p>Uses IAM credentials from the AWS provider to generate a temporary token that is compatible with
<a class="reference external" href="https://github.com/kubernetes-sigs/aws-iam-authenticator">AWS IAM Authenticator</a> authentication.
This can be used to authenticate to an EKS cluster or to a cluster that has the AWS IAM Authenticator
server configured.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the cluster</p>
</dd>
</dl>
</dd></dl>

</div>
