<div class="section" id="module-pulumi_aws.eks">
<span id="eks"></span><h1>eks<a class="headerlink" href="#module-pulumi_aws.eks" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.eks.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.eks.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>enabled_cluster_log_types=None</em>, <em>name=None</em>, <em>role_arn=None</em>, <em>version=None</em>, <em>vpc_config=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EKS Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enabled_cluster_log_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the desired control plane logging to enable. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Control Plane Logging</a></li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cluster.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.</li>
<li><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC Considerations</a> and <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster Security Group Considerations</a> in the Amazon EKS User Guide. Configuration detailed below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.certificate_authority">
<code class="descname">certificate_authority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.certificate_authority" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing <code class="docutils literal notranslate"><span class="pre">certificate-authority-data</span></code> for your cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.enabled_cluster_log_types">
<code class="descname">enabled_cluster_log_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.enabled_cluster_log_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the desired control plane logging to enable. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html">Amazon EKS Control Plane Logging</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint for your Kubernetes API server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.platform_version">
<code class="descname">platform_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.platform_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform version for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Desired Kubernetes master version. If you do not specify a value, the latest available version at resource creation is used and no upgrades will occur except those automatically triggered by EKS. The value must be configured and increased to upgrade the version when desired. Downgrades are not supported by EKS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.Cluster.vpc_config">
<code class="descname">vpc_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.Cluster.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument for the VPC associated with your cluster. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html">Cluster VPC Considerations</a> and <a class="reference external" href="https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html">Cluster Security Group Considerations</a> in the Amazon EKS User Guide. Configuration detailed below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.eks.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.eks.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.eks.GetClusterAuthResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.eks.</code><code class="descname">GetClusterAuthResult</code><span class="sig-paren">(</span><em>name=None</em>, <em>token=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.GetClusterAuthResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusterAuth.</p>
<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterAuthResult.token">
<code class="descname">token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterAuthResult.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token to use to authenticate with the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterAuthResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterAuthResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.eks.GetClusterResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.eks.</code><code class="descname">GetClusterResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>certificate_authority=None</em>, <em>created_at=None</em>, <em>endpoint=None</em>, <em>name=None</em>, <em>platform_version=None</em>, <em>role_arn=None</em>, <em>version=None</em>, <em>vpc_config=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.certificate_authority">
<code class="descname">certificate_authority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.certificate_authority" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing <code class="docutils literal notranslate"><span class="pre">certificate-authority-data</span></code> for your cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The Unix epoch time stamp in seconds for when the cluster was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint for your Kubernetes API server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.platform_version">
<code class="descname">platform_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.platform_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform version for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kubernetes server version for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.vpc_config">
<code class="descname">vpc_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested attribute containing VPC configuration for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.eks.GetClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.eks.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.eks.get_cluster">
<code class="descclassname">pulumi_aws.eks.</code><code class="descname">get_cluster</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about an EKS Cluster.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.eks.get_cluster_auth">
<code class="descclassname">pulumi_aws.eks.</code><code class="descname">get_cluster_auth</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.eks.get_cluster_auth" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an authentication token to communicate with an EKS cluster.</p>
<p>Uses IAM credentials from the AWS provider to generate a temporary token that is compatible with
<a class="reference external" href="https://github.com/kubernetes-sigs/aws-iam-authenticator">AWS IAM Authenticator</a> authentication.
This can be used to authenticate to an EKS cluster or to a cluster that has the AWS IAM Authenticator
server configured.</p>
</dd></dl>

</div>
