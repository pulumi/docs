---
title: Module eks
---

<div class="section" id="eks">
<h1>eks<a class="headerlink" href="#eks" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.eks"></span><dl class="class">
<dt id="pulumi_aws.eks.AwaitableGetClusterAuthResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">AwaitableGetClusterAuthResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.AwaitableGetClusterAuthResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.eks.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">certificate_authority=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">enabled_cluster_log_types=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_version=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">vpc_config=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.eks.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled_cluster_log_types=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">vpc_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EKS Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled_cluster_log_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the desired control plane logging to enable. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Control Plane Logging</a></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cluster.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.</p></li>
<li><p><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC Considerations</a> and <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster Security Group Considerations</a> in the Amazon EKS User Guide. Configuration detailed below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/eks_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/eks_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.certificate_authority">
<code class="sig-name descname">certificate_authority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.certificate_authority" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing <code class="docutils literal notranslate"><span class="pre">certificate-authority-data</span></code> for your cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.enabled_cluster_log_types">
<code class="sig-name descname">enabled_cluster_log_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.enabled_cluster_log_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the desired control plane logging to enable. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Control Plane Logging</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint for your Kubernetes API server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.platform_version">
<code class="sig-name descname">platform_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.platform_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform version for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the EKS cluster. One of <code class="docutils literal notranslate"><span class="pre">CREATING</span></code>, <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.vpc_config">
<code class="sig-name descname">vpc_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC Considerations</a> and <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster Security Group Considerations</a> in the Amazon EKS User Guide. Configuration detailed below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.eks.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">certificate_authority=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">enabled_cluster_log_types=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_version=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">vpc_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the cluster.
:param pulumi.Input[dict] certificate_authority: Nested attribute containing <code class="docutils literal notranslate"><span class="pre">certificate-authority-data</span></code> for your cluster.
:param pulumi.Input[list] enabled_cluster_log_types: A list of the desired control plane logging to enable. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Control Plane Logging</a>
:param pulumi.Input[str] endpoint: The endpoint for your Kubernetes API server.
:param pulumi.Input[str] name: Name of the cluster.
:param pulumi.Input[str] platform_version: The platform version for the cluster.
:param pulumi.Input[str] role_arn: The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
:param pulumi.Input[str] status: The status of the EKS cluster. One of <code class="docutils literal notranslate"><span class="pre">CREATING</span></code>, <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>. 
:param pulumi.Input[str] version: Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.
:param pulumi.Input[dict] vpc_config: Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC Considerations</a> and <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster Security Group Considerations</a> in the Amazon EKS User Guide. Configuration detailed below.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/eks_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/eks_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.eks.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.eks.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.eks.GetClusterAuthResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">GetClusterAuthResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.GetClusterAuthResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusterAuth.</p>
<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterAuthResult.token">
<code class="sig-name descname">token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterAuthResult.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token to use to authenticate with the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterAuthResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterAuthResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.eks.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">certificate_authority=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">enabled_cluster_log_types=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_version=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">vpc_config=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.certificate_authority">
<code class="sig-name descname">certificate_authority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.certificate_authority" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing <code class="docutils literal notranslate"><span class="pre">certificate-authority-data</span></code> for your cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The Unix epoch time stamp in seconds for when the cluster was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.enabled_cluster_log_types">
<code class="sig-name descname">enabled_cluster_log_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.enabled_cluster_log_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The enabled control plane logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint for your Kubernetes API server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.platform_version">
<code class="sig-name descname">platform_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.platform_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform version for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the EKS cluster. One of <code class="docutils literal notranslate"><span class="pre">CREATING</span></code>, <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kubernetes server version for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.vpc_config">
<code class="sig-name descname">vpc_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing VPC configuration for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.eks.get_cluster">
<code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about an EKS Cluster.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/eks_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/eks_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.eks.get_cluster_auth">
<code class="sig-prename descclassname">pulumi_aws.eks.</code><code class="sig-name descname">get_cluster_auth</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.get_cluster_auth" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an authentication token to communicate with an EKS cluster.</p>
<p>Uses IAM credentials from the AWS provider to generate a temporary token that is compatible with
<a class="reference external" href="https://github.com/kubernetes-sigs/aws-iam-authenticator">AWS IAM Authenticator</a> authentication.
This can be used to authenticate to an EKS cluster or to a cluster that has the AWS IAM Authenticator
server configured.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/eks_cluster_auth.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/eks_cluster_auth.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
